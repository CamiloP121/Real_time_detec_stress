import mediapipe as mp
import cv2
import numpy as np
from modules.utils import tqdm_bar

def Equ_Hist(image: np.ndarray):
    '''
    Backlight image check function
    ----------------------------------------------------------------
    Args:
    - image: image to check
    Returns:
    - Image original if image is not backlighted
    - Image with Histogram equalization if image is backlighted
    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    max = np.max(hist)
    h_t = np.var(hist[50:200])/max

    if h_t < 3:
        ycrcb_img = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        # equalize the histogram of the Y channel
        ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
        # convert back to RGB color-space from YCrCb
        img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YUV2BGR)
    else: img = image

    return img

def One_Face(Result,h,w):
    ''' 
    Function to have a single face
    If there are more than two detections, it selects the two that are closest to the camera
    ----------------------------------------------------------------
    Args:
    - Result: object with result MediaPipe
    - h: height of the image
    - w: width of the image
    '''
    Vec_A = []
    for detection in Result.detections:
        we = int(detection.location_data.relative_bounding_box.width * w)
        hg = int(detection.location_data.relative_bounding_box.height * h)
        Vec_A.append(we*hg)

    Index = Vec_A.index(max(Vec_A))
    return [Result.detections[Index]]

def Norm_Bounding(detection:object):
    '''
    Function to verify that the Bounding box does not exceed the limits of the image.
    In case with points out of the image will remplace with 1.0    
    ----------------------------------------------------------------
    Args: 
    - detection: object with results of MediaPipe
    Returns:
    - detection: object with results of MediaPipe
    '''

    # Verificar x
    if (detection.location_data.relative_bounding_box.xmin + detection.location_data.relative_bounding_box.width 
        > 1.0): 
        Dif = detection.location_data.relative_bounding_box.xmin + detection.location_data.relative_bounding_box.width - 1
        detection.location_data.relative_bounding_box.width = detection.location_data.relative_bounding_box.width - Dif
    # Verificar y
    if (detection.location_data.relative_bounding_box.ymin + detection.location_data.relative_bounding_box.height
        > 1.0): 
        Dif = detection.location_data.relative_bounding_box.ymin + detection.location_data.relative_bounding_box.height - 1
        detection.location_data.relative_bounding_box.height = detection.location_data.relative_bounding_box.height - Dif
    
    return detection


def Not_Detection(I_Before,I_Temp):
    '''
    Verify that the image prior to the undetected image is substantially equivalent to overlap the information.
    --------------------------------
    Args: 
    - I_Before: Image before not detect face
    - I_Temp: Image actual
    Returns:
    - True if the is substantially equivalent
    - False if the is no substantially equivalent
    '''
    dif = cv2.subtract(I_Temp,I_Before)
    gray = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
    # Imagen binaria
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # Caso 1 simulitud
    if np.sum(bw)/(bw.size) < 5: 
        ban = True
        # print('Equivalente')
    # Caso 2: Descarte total
    else: ban = False
    '''imas = np.hstack((I_Temp,I_Before))
    cv2.imshow('Compara',imas)
    cv2.imshow('binary', bw)
    cv2.waitKey(1000)'''
    return ban

def Detected_face(Frames:list, height:int, width:int):
    '''
    Face detection by MediaPipe
    ----------------------------------------------------------------
    Args:
    - Frame (list): list of frames to be detected
    '''
    I_Before, Result_Before = [], []
    Vec_Image, Vec_Results, Vec_Image_dw = [], [], []
    cont = 0

    # Declare face detection model
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    # Detention threshold -> 70%
    with mp_face_detection.FaceDetection(
            min_detection_confidence=0.7) as face_detection:
        for image in Frames:
            # Backlight check
            I = image.copy()
            image = Equ_Hist(I)
            # Conversion a RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Image actual
            I_Temp = image.copy()
            # Image drawring
            I_draw = I.copy()
            # Detection
            Result = face_detection.process(rgb)
            # Case not detection face
            if Result.detections is None and len(I_Before) != 0:
                Ban = Not_Detection(I_Before,I_Temp)
                if Ban:
                    mp_drawing.draw_detection(I_draw, Result_Before)

                    Vec_Results.append(Result_Before)
                    Vec_Image.append(I_Before)
                    Vec_Image_dw.append(I_draw)
            # Case find face in image
            elif Result.detections is not None:
                if len(Result.detections) > 1:
                    # Only one face
                    Results = One_Face(Result,height,width)
                else:
                    Results = Result.detections

                for detection in Results:
                    detection =  Norm_Bounding(detection)

                    mp_drawing.draw_detection(I_draw, detection)

                    Vec_Results.append(detection)
                    Vec_Image.append(image)
                    Vec_Image_dw.append(I_draw)
                
                
                I_Before = image ; Result_Before = detection
            
            cont += 1
            if cont == 8: 
                print(len(Vec_Image), len(Vec_Image_dw), len(Vec_Image))
                return Vec_Image, Vec_Image_dw, Vec_Image
            '''
            cv2.imshow('Deteccion mediapipe', np.hstack((I,I_draw)))
            if cv2.waitKey(10) & 0xFF == ord('q'): 
                break
            '''
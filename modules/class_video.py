import cv2
import datetime

class Video:
    '''
    Create a video class
    ----------------------------------------------------------------
    Contains:
    - Capture the video
    - Information about the video
    '''
    def __init__(self, path:str, name:str):
        self.path = path
        self.capture = cv2.VideoCapture(path) # Load video capture
        self.name = name
        self.FPS = self.capture.get(cv2.CAP_PROP_FPS)
        self.frames = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.shape_HW = [self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT), self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)]
        self.video_time = datetime.timedelta(seconds=int(self.frames/self.FPS))
        print('---> Success: Crate video object', self.name)

    # Video's information
    def get_info(self):
        print('INFORMATION ABOUT THE VIDEO'.center(40))
        print(f'--> Name: {self.name}')
        print(f'---> Number of frames: {self.frames}')
        print(f'---> Frame rate: {self.FPS}')
        print(f'---> Shape:')
        print(f'-----> Heigth: {self.shape_HW[0]}')
        print(f'-----> Width: {self.shape_HW[1]}')
        print(f'---> Duration of the video: {self.video_time}')

        
import os
from tqdm import tqdm
from modules.class_video import Video

def open_video_path(path:str, Select:int, info:bool=False):
    '''
    Browse video and select "Linea base" or "Inducción Estres"
    ----------------------------------------------------------------
    Args:
    - path (str): path to open video
    - Select (int): 
        0 = "Linea base"
        1 = "Inducción Estres
    - Info (bool): print video's information 

    Returns:
    Video object
    '''

    # Check if path exists
    if not os.path.exists(path):
        raise Exception('Could not find folder video')
    
    # Select step of video
    if Select == 0: 
        name = f"{path.split('/')[-1]}_Etapa1.mp4"
    elif Select == 1: 
        name = f"{path.split('/')[-1]}_Etapa2.mp4"
    else: raise Exception('Error selecting video, please try again with 0 or 1')

    video_path = f'{path}/{name}'
    print(video_path)
    
    # Check if video exists
    if not os.path.exists(video_path):
        raise Exception('Could not find video')
    
    try:
        video_render =Video(path=video_path, name=name.split('.')[0])
    except Exception as e:
        print(e)
        raise Exception('Could not open the video')
    
    if info:
        video_render.get_info()
    
    return video_render
        

def render_video(Video:object, window:int):
    '''
    Function to render video in window
    ----------------------------------------------------------------
    Args:
    - Video (object): video object
    - Window (int): max quility frames in window
    Returns:
    - Frames in window
    '''


    Frames = []
    pbar = tqdm(total=window, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            desc="Loading video of the window", ncols=70, ascii=True)

    while Video.capture.isOpened():
        ret, frame = Video.capture.read()
            #frame = Equ_Hist(frame)
        Frames.append(frame)
        pbar.update(1)
        # print('Progress: ', len(Frames),'/',window, end='\r')
        if len(Frames) == window or ret == False:break 
    pbar.close()
    return Frames
    



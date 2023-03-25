'''
Pipeline open - process - extract metrics from videos
25/03/2023
'''

from modules.aux_open import *
from modules.aux_face import *

# Open video as class
video_render = open_video_path(path='Base de datos/pb_02', Select=1)
# Video in window of one minute
window = int(60 * video_render.FPS)
num_windows = round(video_render.video_time.seconds / 60)
print(f'Extract windows: {0} / {num_windows}')
for i in range(num_windows):
    # Render window
    frames = render_video(Video=video_render, window=window)
    if len(frames) == 0:
        raise Exception('Could not extract video in the window')
    print(f'Window: {i+1} / {num_windows}')
    cont_general = 0
    while  cont_general < len(frames)-1:
        (Vec_Image, Vec_Image_dw, Vec_Image, cont) = Detected_face(Frames=frames[cont_general:], 
                                                    height=video_render.shape_HW[0], width=video_render.shape_HW[1])
        cont_general += cont
        print('Star procesing video: ',cont_general,'/',len(frames), end='\r')
    # Modulo de extracción

    # Detect face in window video
    if i == 3: break


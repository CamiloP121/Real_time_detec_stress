
from tqdm import tqdm
import numpy as np
import cv2

def tqdm_bar(text, time):
    pbar = tqdm(total=time, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            desc=text, ncols=70, ascii=True)
    
    return pbar

def plot(title:str, images:list, images_2:list=None, how:bool=False):
    if not how: 
        for I in images:
            cv2.imshow(title, I)
            if cv2.waitKey(10) & 0xFF == ord('q'):  break
    else: 
        for I1,I2 in zip(images, images_2):
            I = np.hstack((I1,I2))
            cv2.imshow(title, I)
            if cv2.waitKey(10) & 0xFF == ord('q'):  break
    
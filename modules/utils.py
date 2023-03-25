
from tqdm import tqdm

def tqdm_bar(text, time):
    pbar = tqdm(total=time, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            desc=text, ncols=70, ascii=True)
    
    return pbar
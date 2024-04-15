from moviepy.editor import VideoFileClip
import cv2
import numpy as np
import time
from scipy.io import savemat
import rethinkdb as r
frames = []
cap = cv2.VideoCapture('/home/ke/Desktop/database/testing/Data605Project/Python Codes/Rickroll.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
'''for i in range(length):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    y=np.array(frame)
    print(i/length)'''
rethink = r.RethinkDB()
#rethink.connect('localhost', 28015).repl()
#print(loaded_arrays[1].ndim)
# Write the array to disk
#print(frames[12].ndim)
#newarray = np.stack(frames)
#print(newarray.shape)
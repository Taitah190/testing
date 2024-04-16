from moviepy.editor import VideoFileClip
import cv2
import numpy as np
import time
from scipy.io import savemat
import rethinkdb as r
import json
import pandas as pd
rethink = r.RethinkDB()
rethink.connect('localhost', 28015).repl()
frames = []
'''cap = cv2.VideoCapture('/home/ke/Desktop/database/testing/Data605Project/Python Codes/Rickroll.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
for i in range(100):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    frame = frame.tolist()
    #y=np.array(frame)
    frames.append(frame)
    print(i/length)'''
#rethink.db("test").table_create("array").run()
#print(frame.ndim)

#new = frames
'''jsondata = json.dumps(frames)
with open("/home/ke/Desktop/database/testing/Data605Project/Python Codes/test2.json", "w") as json_file:
    json_file.write(jsondata)'''
# Serialize the list to JSON
#rethink.db("ke-B660M-AORUS-PRO-AX-DDR4").table
#rethink.connect('localhost', 28015).repl()
#print(loaded_arrays[1].ndim)
# Write the array to disk
#print(frames[12].ndim)
#newarray = np.stack(frames)
#print(newarray.shape)

###Line of Submission###
im = cv2.imread("/home/ke/Desktop/database/testing/Data605Project/Python Codes/earth.jpg")
#print(im[1][1])
im = im.astype(str)
data = {'array_3d': im}
red = im[:, :, 0:1]
#red = red.tolist()
green = im[:, :, 1:2]
blue = im[:, :, 2:3]
print(red[1:10])
#rethink.db('Project').table_create('NewArray').run()
#rethink.db('Project').table('Array').insert({'red':red}).run()

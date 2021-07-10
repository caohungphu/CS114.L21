import os
import cv2
import numpy as np
from sys import argv
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

def preprocessingImage(img):
  # Chuyển màu từ BGR sang RGB
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  # Làm mượt ảnh bằng GaussianBlur
  img = cv2.GaussianBlur(img, (5, 5), 0)
  # Chuyển ảnh về kích thước 224 x 224 để phù hợp với model ở phía dưới
  img = cv2.resize(img, (224, 224))
  # Scale ảnh về cho các pixel dao động từ 0 -> 1
  img = img / 255
  # Trả về ảnh (224, 224, 3)
  return img
    
try:
    path_model = argv[1]
    path_video = argv[2]
    
    model = load_model(path_model)
    
    width = 640
    height = 400
    video = cv2.VideoCapture(path_video)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, height)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, width)
    
    if (video.isOpened() == False): 
        print("Error opening videos")
   
    color = None
    text_output = 'Predict: {:.2f} -> {}: {:.2f}%'
    result = None
        
    while(video.isOpened()):
        video.set(cv2.CAP_PROP_FPS,1) 
        ret, frame = video.read()
        frame = cv2.resize(frame, (width, height))
        frame = cv2.putText(frame, result, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        
        img_process = preprocessingImage(frame).reshape(1,224,224,3)
        predict = model.predict(img_process)[0][0]
        
        if predict < 0.5:
            color = (0, 255, 0)
            result = text_output.format(predict, "NONFIRE", ((0.5 - predict) / 0.5) * 100)
        else:
            color = (0, 0, 255)
            result = text_output.format(predict, "FIRE", predict * 100)
        if ret == True:
            cv2.imshow('detectVideo', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else: 
            break

    video.release()
    cv2.destroyAllWindows()
except:
    print("Error! Usage: python detectVideo.py ./model/a.h5 ./video/a.mp4")
    
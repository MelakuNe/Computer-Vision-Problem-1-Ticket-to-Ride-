"""
"""
import cv2 as cv
    
path = '/train/all.jpg'
image = cv.imread(path)
centers, n_trains, scores = predict_image(image)
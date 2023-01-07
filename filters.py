import cv2
import numpy
import matplotlib.pyplot as plot

def blur(frame):
    #applying a bilateral filter 
    #params are the frame, diam of pixel neighborhood, sigma space and border type
    frame = cv2.bilateralFilter(frame, 20, 115, 35)    
    return frame

def heatmap(frame):
    heatmap = cv2.applyColorMap(frame, cv2.COLORMAP_BONE) #grayscale conversion
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET) #heatmap applied to b/w frame
    return heatmap

def shades(frame):
    return None
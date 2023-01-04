import cv2
import numpy
#import matplotlib

def blur(frame):
    #applying a bilateral filter 
    #params are the frame, diam of pixel neighborhood, sigma space and border type
    frame = cv2.bilateralFilter(frame, 20, 115, 35)    
    return frame

#def heatmap(frame):
 #   colormap = matplotlib.get_cmap('inferno')
  #  heatmap = (colormap(frame) * 2**16).astype(numpy.uint16)[:,:,:3]
   # heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)
    #return heatmap
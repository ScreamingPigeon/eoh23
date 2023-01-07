# import the opencv library
import cv2
from filters import blur, heatmap
# define a video capture object
vid = cv2.VideoCapture(0)
mode = 'heatmap'
while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # Display the resulting frame
    if mode =='def':
        cv2.imshow('frame', frame)
    elif mode == 'blur':
        cv2.imshow('frame', blur(frame))
    elif mode == 'heatmap':
        cv2.imshow('frame', heatmap(frame))


    # the 'q' button is set as the quit button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



vid.release()
cv2.destroyAllWindows()
# import the opencv library
import cv2
from filters import blur
# define a video capture object
vid = cv2.VideoCapture(0)
mode = 'def'
while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    #create conditionals that apply filters
    if cv2.waitKey(1) & 0xFF == ord('0'):
        #apply filter 0
        mode ='def'
    elif cv2.waitKey(1) & 0xFF == ord('1'):
        #apply filter 1
        mode ='blur'



    # Display the resulting frame
    if mode =='def':
        cv2.imshow('frame', frame)
    elif mode == 'blur':
        cv2.imshow('frame', blur(frame))


    # the 'q' button is set as the quit button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



vid.release()
cv2.destroyAllWindows()
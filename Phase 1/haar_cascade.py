import cv2

# loaded the video file
cap = cv2.VideoCapture('vid1.mp4')
# loaded the XML file
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# this will go under while loop while video is playing and mark the human detected
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)

    # Display the resulting frame
    for (x,y,w,h) in humans:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    # for showing the video file
    cv2.imshow('frame',frame)

    # when we press q the video file will stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# at final the video loaded is released
cap.release()
cv2.destroyAllWindows()

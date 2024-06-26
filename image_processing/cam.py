import cv2
import numpy as np
from ultralytics import YOLO

#Capture video stream
webcam = cv2.VideoCapture(0)

CONFIDENCE_THRESHOLD = 0.8

yolo_model = YOLO("yolov8n.pt")

while(1):
    
    #Read video and store as image frames
    _, imageFrame = webcam.read()
    '''
    #Convert frame from RGB to HSV
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    

    #Define mask for the colors
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    kernel = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=green_mask)

    blue_mask = cv2.dilate(blue_mask, kernel)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=blue_mask)

    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + y, w + h), (0, 0, 255), 2)
            cv2.putText(imageFrame, "Red Color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + y, w + h), (0, 255, 0), 2)
            cv2.putText(imageFrame, "Green Color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + y, w + h), (255, 0, 0), 2)
            cv2.putText(imageFrame, "Blue Color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
    '''
    detections = yolo_model(imageFrame)[0]

    for data in detections.boxes.data.tolist():
        
        confidence = data[4]
        '''
        if float(confidence) < CONFIDENCE_THRESHOLD:
            continue
        '''
        xmin, ymin, xmax, ymax, confidence_score, class_id = int(data[0]), int(data[1]), int(data[2]), int(data[3]), float(data[4]), int(data[5])

        cv2.rectangle(imageFrame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(imageFrame, f"{detections.names[class_id]} {int(confidence_score*100)}%", (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

        print(f'({(xmax+xmin)/2}, {(ymax+ymin)/2})')

    cv2.imshow("Color Detection - RGB", imageFrame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        print("Closed!")
        break

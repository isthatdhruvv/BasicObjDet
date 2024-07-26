from ultralytics import YOLO
import cv2
model = YOLO('../Yolo-weights/yolov8l.pt')
resultrs = model("Images/1.jpg",show=True)
cv2.waitKey(0)
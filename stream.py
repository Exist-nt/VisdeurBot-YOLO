import cv2
import time
from ultralytics import YOLO

model = YOLO("visdeurbot-yolo.pt")
cap = cv2.VideoCapture("<https://visdeurbel.videostreams.nl/hls/visdeurbel/index.m3u8>")
timestamp = time.strftime("%Y%m%d-%H%M%S")

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:
		break
	
	results = model(frame)
	for resx in results:
		boxes = resx.boxes
		if boxes is not None and len(boxes) > 0:
			annotated_frame = resx.plot()
			cv2.imwrite("detection-"+timestamp+".png", annotated_frame)
cap.release()
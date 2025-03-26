from ultralytics import YOLO

model = YOLO('yolov8n.pt')

result = model(source = 0, show = True, conf = 0.4, save = False)


from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.val(data="coco128.yaml")

print("\nEvaluation Results")
print("------------------")
print(f"mAP50:     {results.box.map50:.3f}")
print(f"mAP50-95:  {results.box.map:.3f}")
print(f"Precision: {results.box.mp:.3f}")
print(f"Recall:    {results.box.mr:.3f}")
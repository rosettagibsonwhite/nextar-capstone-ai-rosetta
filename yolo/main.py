from ultralytics import YOLO
from pathlib import Path
import csv

model = YOLO("yolov8n.pt")

image_folder = Path("images")
results_folder = Path("results")

results_folder.mkdir(exist_ok=True)

image_files = list(image_folder.glob("*.jpg"))

print(f"Found {len(image_files)} images.\n")

detection_data = []

for image_path in image_files:

    print(f"Processing: {image_path.name}")

    results = model(image_path, conf=0.5)

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            detection_data.append([
                image_path.name,
                class_name,
                round(confidence, 2)
            ])

        output_path = results_folder / f"detected_{image_path.name}"
        result.save(filename=str(output_path))

with open("results_summary.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Image",
        "Object",
        "Confidence"
    ])

    writer.writerows(detection_data)

print("\nAll images processed!")
print("Annotated images saved in the 'results' folder.")
print("Detection summary saved as 'results_summary.csv'.")
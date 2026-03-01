import os
from collections import Counter

# Path to your NEW processed labels
LABEL_DIR = "data/processed/labels/train"

# The names we established in road_hazards.yaml
class_names = {
    "1": "Pothole_Minor", 
    "2": "Pothole_Major",
    "4": "Crack_Longitudinal",
    "5": "Crack_Transverse", 
    "6": "Crack_Alligator"
}

counts = Counter()

if not os.path.exists(LABEL_DIR):
    print(f"Error: Could not find {LABEL_DIR}")
else:
    for file in os.listdir(LABEL_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(LABEL_DIR, file), 'r') as f:
                for line in f:
                    class_id = line.split()[0]
                    counts[class_id] += 1

    print("\n--- VisionRoad Dataset Summary ---")
    for id, name in sorted(class_names.items()):
        print(f"{name} (ID {id}): {counts.get(id, 0)} instances")
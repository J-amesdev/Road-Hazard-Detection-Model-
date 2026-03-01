import os

# Configuration - Update these paths if your folders are named differently
RAW_LABEL_DIR = "data/raw/RDD2022/train/labels"
PROCESSED_LABEL_DIR = "data/processed/labels/train"
os.makedirs(PROCESSED_LABEL_DIR, exist_ok=True)

# Mapping RDD2022 IDs 
# RDD: 0=Long, 1=Trans, 2=Alligator, 3=Pothole
mapping = {
    0: 4,  # Crack_Longitudinal
    1: 5,  # Crack_Transverse
    2: 6,  # Crack_Alligator
    3: 1   # Pothole (Default to Minor)
}
`
def process_labels():
    for filename in os.listdir(RAW_LABEL_DIR):
        if not filename.endswith(".txt"): continue
        
        with open(os.path.join(RAW_LABEL_DIR, filename), 'r') as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            parts = line.split()
            old_id = int(parts[0])
            
            if old_id in mapping:
                # Apply size heuristic for Pothole Depth (Major vs Minor)
                if old_id == 3:
                    width, height = float(parts[3]), float(parts[4])
                    area = width * height
                    # If the pothole takes up more than 3% of the image, call it Major
                    parts[0] = str(2) if area > 0.03 else str(1)
                else:
                    parts[0] = str(mapping[old_id])
                
                new_lines.append(" ".join(parts))
        
        if new_lines:
            with open(os.path.join(PROCESSED_LABEL_DIR, filename), 'w') as f:
                f.write("\n".join(new_lines))

print("Processing VisionRoad labels...")
process_labels()
print("Done! Cleaned labels are in data/processed/labels/train")
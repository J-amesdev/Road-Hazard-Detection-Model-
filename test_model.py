from ultralytics import YOLO
import cv2

model = YOLO(r'C:\Users\Lenovo\OneDrive\Desktop\Road_Hazard_YOLO\runs\detect\VisionRoad_Initial3\weights\best.pt')

# TREATMENT: Reduce input size to 320 for extreme speed if 640 is too slow
results = model.predict(
    source=r"C:\Users\Lenovo\Downloads\test.mov",
    stream=True,     # Stops the 'bottleneck' effect
    conf=0.25,       # Lowering this helps detect hazards earlier (farther away)
    imgsz=640,       # Ensure this matches your training size
    device=0         # GTX 1650
)

for r in results:
    # TREATMENT: plot() with 'labels=False' can save a few ms of CPU time
    frame = r.plot(labels=True, conf=True) 
    
    cv2.imshow("VisionRoad Real-Time Validation", frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
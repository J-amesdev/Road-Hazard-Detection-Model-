from ultralytics import YOLO

def main():
    # Start fresh since no checkpoint was found
    model = YOLO('yolov8n.pt')

    model.train(
        data='road_hazards.yaml',
        epochs=50,
        imgsz=640,
        batch=8,          
        workers=2,        # Crucial to prevent WinError 1455
        name='VisionRoad_Initial',
        device=0
    )

if __name__ == '__main__':
    main()
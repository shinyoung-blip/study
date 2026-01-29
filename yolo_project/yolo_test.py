from ultralytics import YOLO
import cv2

# 1. 모델 불러오기 (Hugging Face에서 받은 YOLO 가중치 경로)
model = YOLO('demo-bin-picking/demo-bin-picking/yolo11/train_obj_s/detection/obj_s/yolo11-detection-obj_s.pt') 

# 2. 이미지 추론
results = model('test_imgs/test_imgs/IMG_20251007_165718.jpg')

# 3. 결과 화면에 표시 및 저장
for r in results:
    im_array = r.plot() # 박스가 그려진 이미지
    cv2.imwrite('yolo_result_2d.jpg', im_array)
    print("성공! yolo_result_2d.jpg 파일이 생성되었습니다.")


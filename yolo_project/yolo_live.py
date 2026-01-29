import cv2
from ultralytics import YOLO

# 1. 모델 로드
# 기존: model = YOLO('yolo11n.pt')
# 변경: demo 폴더 안에 있는 전용 모델 경로를 넣습니다. (파일명은 다를 수 있으니 확인 필수!)
model_path = '/Users/shinyoung/HCCEPose/yolo_project/demo-bin-picking/demo-bin-picking/yolo11/train_obj_s/detection/obj_s/yolo11-detection-obj_s.pt'
# 위에서 찾은 모델 경로를 인자로 YOLO() 괄호 안에 넣어주기
model = YOLO(model_path)
# 2. 카메라 설정 (Iriun이 연결되었다면 0 또는 1 또는 2)
# 0이 맥북 카메라면 1이 Iriun일 확률이 높습니다.
cap = cv2.VideoCapture(1)

print("실시간 YOLO 창을 엽니다... (종료하려면 창을 클릭하고 'q' 키를 누르세요)")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("카메라를 찾을 수 없습니다. 인덱스(0, 1, 2)를 확인하세요.")
        break

    # YOLO 실시간 추론 (추론 결과 시각화)
    results = model.predict(frame, conf=0.5, show=True)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

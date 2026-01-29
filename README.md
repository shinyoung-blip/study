### yolo 설치 및 실행 가이드
1. 내 컴퓨터(로컬) 가상환경 세팅
```
# 1. 폴더 이동
cd ~/HCCEPose/yolo_project

# 비어있는 맥 폴더가 도커의 입력 데이터들을 지워버릴 수 있으므로, 맥 폴더에 미리 입력 데이터를 다운받아 놓기
# demo-bin-picking은 모델이 입력 데이터를 해석하기 위한 설정이 들어있는 폴더이기 때문에 중요함. (객체 ID, 이름, 원본 설계도 )
huggingface-cli download SEU-WYL/HccePose --include "demo-bin-picking/*" --local-dir . --repo-type dataset

# 2. 가상환경 생성 (이걸 해야 venv 폴더가 생깁니다!)
python3 -m venv venv

# 3. 가상환경 활성화
source venv/bin/activate

# 4. 필수 라이브러리 설치(이미 설치가 되어있다면, 패스해도 됨)
pip install "numpy<2.0" torch torchvision ultralytics opencv-python huggingface_hub bop-toolkit-lib pycocotools ruamel.yaml
```
2. 실행
- A. 도커 사용
```
docker-compose up --build
```

- B. 로컬에서 직접 실행
```
source venv/bin/activate
python yolo_live.py
```

3. 결과 이미지
<p align="center">
  <img src="https://github.com/user-attachments/assets/1af5e2a0-7506-4eb9-bf7f-925a719e0a51" width="45%">
  <img src="https://github.com/user-attachments/assets/8377fc22-0c6b-4fd0-af73-96771e3fe054" width="45%">
</p>

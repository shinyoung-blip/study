# 가제보 이그니션 환경설정 
### 가제보 모델 경로 환경 변수 추가
```
export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/gcamp_ros2_ws/src
```
> 기존에 설정된 IGN_GAZEBO_RESOURCE_PATH 값에 ~/gcamp_ros2_ws/src 경로 추가해서 다시 환경 변수 저장  
> 이그니션은 패키지 안의 파일을 찾을 때, IGN_GAZEBO_RESOURCE_PATH 라는 환경 변수 참조. 이를 터미널에 알려줘야 함.

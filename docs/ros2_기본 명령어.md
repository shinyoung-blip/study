# 기본 명령어
### ros2 run
```
ros2 run <패키지 이름> <실행 파일 이름>
```
> 특정 패키지 안에 있는 실팽 파일을 실행할 때 사용
>> 예) ros2 run teleop_twist_keyboard teleop_twixt_keyboard
### ros2 launch
```
ros2 launch <패키지 이름> <launch 파일명>
```
> 여러 노드나 실행 환경을 한 번에 실행하고 싶을 때 launch 파일 사용
***
### 패키지 만들기
```
ros2 pkg create --build-type ament_python my_package --dependencies rclpy
```
> --build-type ament_python: Python 패키지 생성 시 사용  
> --dependencies: 사용할 ROS 2 패키지를 명시 (예: rclpy)

### 패키지 빌드 및 적용
```
cd ~/ros2_ws colcon build --symlink-install
source ~/ros2_ws/insatll/setup.bash
```
### 설치 확인
```
ros2 pkg list
ros2 pkg list | grep my_package
```

### 특정 패키지만 빌드하기
```
colcon build --symlink-install --packages-select my_package
```
> 패키지 빌드하고 나서, 무조건 적용하는 source 코드 넣어줘야 함.

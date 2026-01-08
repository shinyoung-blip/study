# 로봇을 움직이고 싶을 때 
## ros2controlcli 패키지 설치되어 있지 않을 때
```
sudo apt update
sudo apt install ros-$ROS_DISTRO-ros2-control ros-$ROS_DISTRO-ros2-controllers
```

## 환경 설정(source) 확인
```
# ROS2 기본 경로 설정
source /opt/ros/$ROS_DISTRO/setup.bash

# 본인의 워크스페이스 설정 (빌드했을 경우)
source ~/ros2_ws/install/setup.bash
```

## 하드웨어 인터페이스 목록 확인
```
ros2 control list_hardware_interfaces
```
> 실행했을 때 아무것도 나오지 않는다면, 현재 실행 중인 Controller Manager 노드가 없기 때문.  
> 하드웨어 제어하는 런치 파일 실행 중인지 확인

## parameters들이 로드되었는지 확인
```
ros2 param list /controller_manager
```
> ros2_control은 컨트롤러가 어떤 타입인지 미리 파라미터로 알고 있어야 함.
>> 예시) joint_state_broadcaster/JointStateBroadcaster

## 컨트롤러 상태 확인
```
ros2 control list_controllers
```
> joint_state_broadcaster [joint_state_broadcaster/JointStateBroadcaster] active 출력되면 성공

## 로드 가능한 컨트롤러 타입 확인하기
```
ros2 control list_controller_types
```
> 인터페이스가 확인되었으니, 관절들을 움직이게 할 컨트롤러 올릴 차례. 어떤 컨트롤러들이 로드되어 있는지 확인 가능

## 관절 상태 데이터 확인
```
ros2 topic echo /joint_states
```
> 각도 데이터 실시간으로 받아볼 수 있음

## 컨트롤러 활성화 
```
# 1. 관절 상태 브로드캐스터 로드 및 시작
ros2 control load_controller --set-state active joint_state_broadcaster

# 2. 컨트롤러 로드
ros2 control load_controller --set-state active joint_trajectory_controller
```

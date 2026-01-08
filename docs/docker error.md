# 📦 1. 볼륨 마운트(Volume Mount)의 핵심 원리
> 도커 컨테이너는 기본적으로 **'휘발성'**입니다. 컨테이너 내부에서 파일을 수정하거나 삭제해도, 컨테이너를 지우고 다시 만들면 모든 변경 사항이 사라집니다. 이를 해결하고 호스트의 코드를 컨테이너에서 실행하기 위해 볼륨 마운트를 사용합니다.

## 문제 상황: 파일 불일치 및 미인식

> 맥의 ~/Desktop/ros2_ws 폴더에는 코드가 있지만, 도커 내부의 /home/mousey/ros2_ws 폴더는 비어있거나 구버전 파일만 남아있어 src 패키지를 인식하지 못하는 문제가 발생했습니다.

## 해결 원리: 바인드 마운트(Bind Mount)

> 호스트의 특정 디렉토리를 컨테이너의 특정 디렉토리에 '덮어쓰기' 방식으로 연결합니다. 이렇게 하면 맥에서 VS Code로 파일을 저장하는 즉시 도커 내부 파일도 동시에 업데이트됩니다.

# 🛠️ 2. 핵심 문법 및 상세 해결책

## ① docker-compose.yml 볼륨 설정

> 문법: - [호스트 경로]:[컨테이너 경로]  

> 예시:
```
services:
  ros:
    volumes:
      - .:/home/mousey/ros2_ws  # 점(.)은 현재 docker-compose.yml이 있는 위치를 의미
```
> 호스트 경로(.): 맥의 ros2_ws 폴더 전체를 의미합니다.   
> 컨테이너 경로: 도커 내부의 작업 공간인 /home/mousey/ros2_ws를 의미합니다.  
> 결과: 맥의 src 폴더가 도커의 src 폴더로 실시간 동기화되어, colcon build 시 패키지를 정상적으로 찾을 수 있게 됩니다.

## ② --force-recreate 옵션의 기술적 이유

> 단순히 docker-compose up을 하면 도커는 "이미 컨테이너가 있네?" 하고 기존의 연결(마운트) 정보를 재사용하려 합니다.

> 명령어: 
```docker-compose up -d --force-recreate  ```

> 해결책의 의미:

>> 기존 컨테이너를 강제로 삭제합니다.  
>> docker-compose.yml의 새로운 volumes 설정을 읽어옵니다.  
>>새로운 마운트 지점을 설정하여 컨테이너를 처음부터 다시 생성합니다.

# 📂 3. 절대 경로 수정 (경로 문법의 차이)
> 볼륨 마운트로 파일은 연결되었지만, 가제보가 로봇의 외형(Mesh)을 찾지 못했던 것은 경로 표현 방식 때문입니다.

## ROS 2 vs Gazebo 경로 문법

> ROS 2 (package://): ROS 패키지 이름을 기준으로 경로를 찾습니다. (joint_state_publisher 등이 사용)  
> Gazebo (/home/mousey/...): 시뮬레이터 시스템이 직접 파일 시스템을 뒤져야 하므로 절대 경로를 선호합니다.

### 정확한 수정 예시 (gp250_macro.xacro)
```
<mesh filename="package://motoman_description/meshes/visual/base_link.dae"/>

<mesh filename="/home/mousey/ros2_ws/src/motoman_description/meshes/gp250/visual/base_link.dae"/>
```
> 핵심: 볼륨 마운트를 통해 맥의 파일이 도커의 /home/mousey/ros2_ws에 위치하게 되었으므로, 가제보에게 이 도커 내부의 주소를 명확히 알려주어야 로봇이 투명하게 보이지 않고 정상 출력됩니다.

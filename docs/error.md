# 에러 해결
### 실제 파일 어디에 있는지 확인
```
find ~/gcamp_ros2_ws/src -name "base_link.dae"
```

### 파일명 수정
```
# gp215 폴더를 gp250으로 이름 변경
mv ~/gcamp_ros2_ws/src/motoman_description/meshes/gp215 ~/gcamp_ros2_ws/src/motoman_description/meshes/gp250
```
### 런치 파일 실행 과정 속에서 문제
```
ubuntu@47aaa605749d:~/gcamp_ros2_ws$ ros2 launch motoman_gazebo motoman_gazebo.launch.py
에러 발생 -> <urdf-string>/../../motoman_description/...

* 상대 경로 방식으로 인해 생긴 문제 *
해결방안 : vim에서 :%s/..\/..\/motoman_description/package:\/\/motoman_description/g 로 바꿔주기 (절대경로로)
```

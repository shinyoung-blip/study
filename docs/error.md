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

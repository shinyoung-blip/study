#  ros2 package, build

### package.xml
> 패키지 설정 파일
>> 패키지 이름, 저작자, 라이선스, 의존성 패키지, 빌드 툴 등 패키지 정보를 XML 형식으로 기술하는 파일
```
<?xml>: 문서 문법 정의
<package> </package>: ROS 패키지 설정 부분. format="3"은 패키지 설정 파일 버전이 3이라는 뜻.
<name>: 패키지 이름
<version>: 패키지 버전
<description>: 패키지 설명
<maintainer>: 패키지 관리자의 이름과 메일주소
<license>
<url>: 패키지를 설명하는 웹 페이지/소스코드 저장소 등의 주소 기재
<author>: 패키지 개발에 차여한 개발자의 이름과 메일주소
<buildtool_depend>: 빌드 툴 의존성 정의 -> 패키지 빌드 시 사용하는 도구 선언
<build_depend>: 패키지 빌드 시 필요한 의존 패키지 이름
<exec_depend>: 패키지 실행 시 필요한 의존 패키지 이름
<test_depend>: 패키지 테스트 시 필요한 의존 패키지 이름
<export>: 위에 없는 태그명을 여기에 다 씀. <build_type>,<rviz>,<rqt_gui>,<deprecated> 등
// <build_type>은 이 패키지가 어떤 방식, 규칙으로 빌드할지를 정리한 건지를 정의
```

### CMakeLists.txt
> 빌드 설정 파일
>> ROS2의 빌드 시스템인 ament_cmake 사용 -> CMakeLists.txt에 빌드 환경을 기술해 사용
```
cmake_minimum_required(운영체제에 설치된 cmake의 최소 요구 버전)
project(파일 이름)
if()
  set(언어 사용시 기준이 되는 버전)
endif()
if()
  add_compile_options(컴파일 시 옵션)
endif()
find_package(ament 빌드를 할 때 요구되므로 먼저 설치할 패키지)
rosidl_generate_interfaces(추가할 자신만의 인터페이스 파일)
include_directories(빌드 옵션: 헤더파일 폴더 지정)
add_executable(빌드 옵션: 빌드할 때 참조할 코드와 실행파일 이름 지정)
ament_target_dependencies(빌드에 앞서 우선적으로 생성할 의존성 있는 인터페이스)
install(설치 옵션)
```

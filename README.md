# 1stProject - autoplus

1. AUTOMIS에 입력된 반납차량 정보를 가져와 DB에 구성
=> app_name = "input"

2. 반납현황 정리
=> app_name = "monitoring"

3. 반납일정 관리

4. 원상회복 관리

5. DB데이터를 AUTOPLUS DB로 반출

<파일 설명>
1stProject_Git => Git에 올리는 파일들

1stProject_Git>>READMI.md : 주요 사항을 정리
1stProject_Git>>Progress.md : 진행 사항을 정리

1stProject_Git>>manage.py : 파이참 프로그램을 관리하는 python file => 수정없음



1stProject_Git>>config => 프로젝트의 큰 틀을 결정

1stProject_Git>>config>>setting.py : 셋팅 (DB, URL, templates 등)
1stProject_Git>>config>>urls.py : 전체 url을 통괄
1stProject_Git>>config>>asset_storage.py : 파일 저장 관리



1stProject_Git>>input => 첫번째 app (반납데이터 input하여 DB에 설정하는 기능)
1stProject_Git>>monitoring => 두번째 app (반납현황 관리 기능)
1stProject_Git>>?? => 세번째 app (반납현황 관리 기능, 미설정)
1stProject_Git>>?? => 네번째 app (반납현황 관리 기능, 미설정)
1stProject_Git>>?? => 다섯번째 app (반납현황 관리 기능, 미설정)

<각 app의 주요 파일>
models.py : DB의 테이블을 구성
views.py : model과 template를 컨트롤
urls.py : template 활용할 주소를 컨트롤




<추가 기능>
1. list page의 paging 기능
2. 네비게이션바 정리

1. 장고 설치
$ pip install django==2.1
(pymysql 사용을 위해 2.1버전으로 다운로)

2. 프로젝스 시작(설정)
$ django-admin startproject config .

3. DB 설치
  <SQL lite 활용>
  $ python manage.py migrate


  - admin 사용자 추가 -
  $ python manage.py createsuperuser
  ID : admin
  PW : abcd1234


  <AWS에 DB 셋팅하여 활용>
  1) AWS RDB에 DB 생성 => [db name = predata]
  2) DB 모듈 추가
     $ pip install pymysql
  3) setting에 import pymysql & DB 설정 변경
  4) 데이터 베이스 재설정
     $ python manage.py migrate
  5) 관리자 계정 생성
     $ python manage.py createsuperuser
     ID : admin
     PW : abcd1234



4. Static 파일 서버 설정 <AWS S3>
  1) staic 파일 설정 모듈 설치
    $ pip install boto3  => AWS S3 접속 모듈
    $ pip install django-storages

  2) AWS S3(스토리지) 서버만들기 (autoplus-storage)
  3) IAM 사용자 추가 및 권한 설
    - 엑세스 유형 => 프로그래밍 방식 엑세스
    - 그룹생성 -> autoplus_gorup -> AmazonS3FullAccess 선택
    - 엑세스 키 다운도드

  4) setting 설정

  5) 파일스토르지 설정 [config/asset_storage.py]

5. Static 파일 모으기 실행
$ python manage.py collectstatic

---------------------
6. Account App 만들기 (app_name = Account)
  생략 (로그인, 로그아웃, 회원가입)
---------------------

7. App 만들기 (input)
$ python manage.py startapp input
=> setting 추가

8. input/models.py 설정 => 엑셀 저장하는 DB
9. DB 반영
$ python manage.py makemigrations input
$ python manage.py migrate input

10. Admin에 데이터 관리 등록

11. input/views.py 만들기

12. urls 연결
 1) config/urls.py
 2) input/urls.py

13. 관리자 페이지 만들기 [input/admin.py]

14. 템플릿 만들기
[input/templates/file_list.html]
[input/templates/upload.html]

15. 레이아웃 템플렛 만들기
[templates/layout.html]
===============================

16. App 만들기 (monitoring)
$ python manage.py startapp monitoring
=> setting 추가

17. monitoring/views.만들

18. urls 연결
 1) config/urls.py
 2) monitoring/urls.py

19. 템플릿 만들기
[monitoring/templates/ban_board.html]
=> 작성요청(*****)

20. 업로드 엑셀 끌어와서 데이터 베이스로 입력
 1) 반납 엑셀데이터 저장 테이블 => [monitoring/models.py]
   $ python manage.py migrations monitoring
   $ python manage.py mograte monitoring

 2) 엑셀 데이터를 불러와서 테이블에 저장 => [monitoring/views.py]

   $ pip install openpyxl
   $ pip install pandas
   $ pip install xlrd

 3) 반납 현황 로직 및 화면 구성 => [monitoring/views2.py]
   3-1) 대량반납 현황 게시판
       [monitoring/models.py] => 게시판 모델 추가

       $ python manage.py makemigrations monitoring
       $ python manage.py migrate monitoring
       admin 등록

       [monitoring/views2.py] => 리스트뷰, 추가뷰, 수정뷰, 삭제뷰 추가

       [monitoring/urls.py] => 추가

       [monitoring/templates/massboard_list.html]
       [monitoring/templates/massboard_create.html]
       [monitoring/templates/massboard_update.html]
       [monitoring/templates/massboard_confirm_delete.html]


   3-2) 차량상세 뷰 => [monitoring/templates/data_detail.html]

 4) 검색 기능 구현
   4-1) url 설정 
      path('data/', search_list, name='search')
   4-2) view 설정
   4-3) template 설정 [monitoring/templates/data_list.html]

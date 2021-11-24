# 🏆Final pjt

### SSAFY 최종 프로젝트 (팀명: MOVIE_IS_AWESOME)



## 프로젝트 목표

> **Django REST API와 Vue.js를 활용한 영화 추천 및 커뮤니티 사이트 제작**
>
> 1. 한 학기 동안 사용한 모든 것을 활용해서 제작할 것
>
> 2. Backend와 Frontend의 역할 분담을 하지만, 
>
>    팀원 모두가 프로젝트 전체를 이해할 수 있도록 협업을 위주로 할 것
>
> 3. 의견을 수시로 나누면서 팀원과 프로젝트 진행 상황을 공유할 것



## **"SSINEMA"**

> SSAFY + CINEMA



## **개발 기간**

- 2021.11.16 ~ 2021.11.26



## 결과물 Preview

- 로그인 & 회원가입



- 메인 페이지



- 메인 페이지 - 조회 & 검색



- 영화 상세 페이지 - 평점 & 포토카드 추가



- 영화 상세 페이지 - 리뷰 & 댓글

  

- 프로필 페이지



- 관리자 페이지



- 로그아웃



## 개발 환경

### 1. 개발 스택

- Python
- Django
- HTML
- CSS
- JavaScript
- Vue.js



### 2. 설치

- python

```
python -m venv venv
source venv/Scripts/activate
python manage.py migrate
python manage.py runserver
```

- vue

```
npm i
npm run serve
```



## GIT의 흐름

#### 개발 진행 중에 GIT 사용 흐름



##### 주의사항

1. 반드시 git pull origin develop 을 해서 변경사항이 있는지 확인한다.
2. 반드시 branch 를 만들어서 작업을 진행한다.
3. merge conflict 가 발생하지 않도록 진행하는 부분을 동시에 진행하지 않는다.
3. git의 main branch는 devleop으로 default 해두었습니다. (master는 배포를 위한 공간)



##### GIT의 흐름 (예시)

1. git pull origin develop

2. git checkout -b feature/FE_login 또는 git checkout -b feature/BE_movieApi

    (작업을 시작하고, 완료가 된다면)
    
3. git add .

4. git commit -m "FE_login(만든 기능) complete"

5. git push origin feature/FE_login(만든 기능) (develop 또는 master 가 아님을 주의)

    (gitlab 으로 이동해서)

6. gitlab에서 create merge

    (delete source 체크되어있는지 확인)
    
    (merge 방향이 맞는지 확인 ( ex) feature/FE_login into develop) )
    
7. git checkout develop 

    (develop 브랜치로 이동하면, 아직 반영이 안되어있음을 알 수 있음)

8. git pull origin develop (pull 해주면 반영 완료)

9. git branch -D feature/FE_login (사용한 branch 는 삭제)



------

------



## Design Thinking

#### 1. Target

OTT 서비스 이용자 수의 증가에 따라서, 해당 서비스를 이용하기 전에

최적의 콘텐츠를 추천받고 싶은 사용자를 위한  WEB 어플리케이션 제작



#### 2. Why

국내에 도입되는 OTT 서비스가 많아짐에 따라, 각 OTT가 지닌 콘텐츠들도 다릅니다.

그래서 자신이 좋아하는 장르, 혹은 영화사 등의 정보를 미리 파악할 수 있도록 하면

추후 해당 OTT 서비스를 고르고 이용하기 편해진다고 생각했습니다.



#### 3. How

1. 가입 후, 메인페이지에서 업데이트되는 DB를 기반으로 불러오는 영화 목록에서,

   본인이 재미있게 본 영화를 발견하면 별점과 코멘트를 작성할 수 있습니다. 

   별점을 7점 이상 부여 시, 찜한 목록에 들어가서 해당 장르를 기반으로 한 알고리즘을 통해 

   메인페이지에서 제공되는 추천 영화 목록이 변경되어 나타납니다.

2. 계절에 따라, 날씨에 따른 알고리즘 설계를 통해 제공되는 추천 영화 목록이 변경됩니다.

   이를 통해, 사용자가 다양한 영화의 정보를 파악할 수 있습니다.

3. 기본적으로 평점높은 영화, 개봉된 (혹은 개봉 예정인) 영화, 인기있는 영화를 DB 업데이트를 통해

   매번 다른 영화 목록을 제공하고 있습니다.

   

## ERD





## Back end

### 0. 구조

- final_pjt_back-(프로젝트)
- account-(계정 앱)
- article-(커뮤니티 앱)
- movie-(서비스 관련 앱)
  - category-(영화 서비스 제공을 위한 앱)
- dummy(data/DataSet)-(영화데이터 추출 및 입력을 위한 실험 앱)





## Front end

### 0. 구조

- Login-(로그인 기능)
- Signup-(회원가입 기능)
- Home-(메인 페이지)
  - Movie List-(알고리즘 기반 영화 목록 제공)
  - Movie Review-(영화 선택 시, 리뷰 작성 기능)
- Search-(영화 검색 서비스)
  - Search Movie List-(검색 관련 영화 목록 제공)
- My Profile-(영화데이터 추출 및 입력을 위한 실험 앱)
  - Other User Profile
- Community
  - Article
  - Comment


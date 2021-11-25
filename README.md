# 🏆Final pjt

### SSAFY 최종 프로젝트 (팀명: SSINEMA)

- **이동철** - Frontend (팀장)
- **이유현** - Backend



## 프로젝트 목표

> **Django REST API와 Vue.js를 활용한 영화 추천 및 커뮤니티 사이트 제작**

- 한 학기 동안 사용한 모든 것을 활용해서 제작할 것

- Backend와 Frontend의 역할 분담을 하지만, 

  팀원 모두가 프로젝트 전체를 이해할 수 있도록 협업을 위주로 할 것

- 의견을 수시로 나누면서 팀원과 프로젝트 진행 상황을 공유할 것



## **"SSINEMA"**

> SSAFY + CINEMA



## **개발 기간**

- 2021.11.16 ~ 2021.11.26



## 결과물 Preview

- 로그인 & 회원가입



- 메인 페이지



- 메인 페이지 - 영화 검색  & 조회



- 영화 상세 페이지 - Youtube & Star Point & Review



- 게시판 페이지 - CRUD & Liked



- 프로필 페이지



- 다른 유저의 프로필 페이지 - Follow



- 로그아웃



- 관리자 페이지



## 개발 환경

### 1. 개발 스택

- Python
- Django
- HTML
- CSS
- JavaScript
- Vue.js
- Vuex



### 2. 설치

- python

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
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

![ERD](README.assets/ERD.png)

- 주 모델: 영화, 게시글, 유저
- 모델 관계
  - 영화ㅡ리뷰 (1:N)
  - 영화ㅡ장르 (M:N)
  - 게시글ㅡ유저 (M:N)
  - 게시글ㅡ댓글 (1:N)
  - 유저ㅡ팔로우 (M:N)
  - 유저ㅡ리뷰 (M:N)
- 유저 영화 리뷰 별점 (추천 알고리즘)
  - 유저에게 영화를 추천하는 알고리즘을 짜기 위해 생성한 관계
  - 유저가 평점을 준 영화의 장르 정보들을 통해서 유저에게 영화를 추천



## Back end

#### 0. 구조

- final_pjt_back-(프로젝트)
- accounts-(계정 앱)
- articles-(커뮤니티 앱)
- movies-(서비스 관련 앱)
  - category-(영화 서비스 제공을 위한 앱)
- dummy(data / DataSet)-(영화데이터 추출 및 입력을 위한 실험 앱)



#### 1. final_pjt_back



#### 2. accounts



#### 3. articles



#### 4.movies



#### 5. dummy







## Front end

#### 0. 구조

- Login-(로그인 기능)
- Signup-(회원가입 기능)
- Home-(메인 페이지)
  - Movie List-(알고리즘 기반 영화 목록 제공)
    - Movie Detail / Review-(영화 정보 상세 페이지 정보 제공, 리뷰 작성 기능)
- Search-(영화 검색 서비스)
  - Search Movie List-(검색 관련 영화 목록 제공)
- My Profile-(개인의 정보를 볼 수 있는 서비스)
  - Follow-(유저 간 팔로우 기능)
  - Created Article / Comment-(작성한 글과 댓글 목록)
  - Liked Movies-(별점 기반 유저가 좋아하는 영화 목록)
  - Delete Account-(회원탈퇴 기능)
- Other User Profile-(다른 유저의 프로필에 접근)
- Community
  - Article / Comment-(CRUD 기능 제공)
    - Article Search-(제목, username을 기반으로 Article 검색 기능)
    - Like-(유저 간 게시글 좋아요 기능)



#### 1. Login Page

> 구현한 기능

- user id와 password 입력을 통해 로그인 method를 구현

> 개선점

- 기본적인 CSS를 줬지만 브라우저 창에 따른 크기 조절을 완벽히 주지는 못했다.
  - 브라우저 창 크기에 따른 media css 적용 필요
- 상황에 따른 모달 창 메세지 분기 처리 필요
  - 아이디 입력하세요 / 비밀번호를 입력하세요 / 아이디와 비밀번호를 확인하세요



#### 2. Singup Page

> 구현한 기능

- user id와 password 그리고 password confirmation 입력을 통해 회원가입 method를 구현

> 개선점

- 기본적인 CSS를 줬지만 브라우저 창에 따른 크기 조절을 완벽히 주지는 못했다.
  - 브라우저 창 크기에 따른 media css 적용 필요
- 상황에 따른 모달 창 메세지 분기 처리 필요
  - 아이디 입력하세요 / 비밀번호를 입력하세요 / 아이디와 비밀번호를 확인하세요
- 회원가입 후, 바로 로그인 되도록 하면 좋을 듯 하다.



#### 3. Home Page

> 구현한 기능

- 알고리즘 기반 Movie List를 Carousel 형태로 제공
  - Hover를 통한 포스터 확대해서 보는 기능 구현
  - 다양한 기준으로 영화 정보를 가져오는 기능 구현
    - User의 별점 기반, 비슷한 장르 랜덤 추천
    - 계절, 날씨에 따른 오늘의 추천 영화 랜덤 추천
    - 평점, 개봉 날짜, 스테디 셀러 등의 기준으로 영화 랜점 추천
- 해당 영화 상세 페이지 모달 / Youtube API를 이용한 영상제공 / 리뷰 기능 구현
  - DB에 접근하여 영화의 상세 데이터들을 제공
  - Youtube API를 이용해 영화의 trailer 제공
  - 별점 기반 알고리즘과 연동된 리뷰 기능 구현 
  - 본인의 리뷰일 경우, 삭제 기능 구현
  - 리뷰를 작성한 유저의 ID 클릭 시, 해당 유저의 프로필에 접근 기능 구현

> 개선점

- Hover의 기능이 자연스럽지 못하다.
  - 카드 전체가 Position으로 띄어서 확대된다면 자연스럽게 보일 듯 하다.
- Youtubue API를 이용해 영상 데이터를 가져오는 과정에서 문제가 발생한다.
  - 의도치 않은 곳에서도 여러번 요청이 돼서, 사용 횟수 급속 증가 및 트래픽에서 발생한다고 판단했다.
  - 원인을 파악해서, 이 부분에 대한 코드 수정이 필요할 것 같다.
- 영화 Detail을 Modal로 열었을 때, 창 크기에 따라 포스터가 모달 영영을 벗어난다.
  - 브라우저 창 크기에 따른 media css 적용 필요



#### 4. Search Page

> 구현한 기능

- Login 한 경우에, NavBar에서 검색할 수 있는 기능 구현
- 검색한 영화 타이틀을 기반으로 Movie List를 Carousel 형태로 제공
  - Movie List의 영화를 선택 시, Home에서 연결한 것와 같이 해당 영화 상세 페이지 Modal로 제공
  - 없는 영화일 경우, 없는 페이지를 보여주도록 v-if / v-else로 설계

> 개선점

- Vuex를 이용해서 로직을 구성했는데, Consol.log로 데이터 입력 순서를 가정하고 실행했지만 생각했던 순서대로 실행이 되지 않았다. 아마도 이 순서가 다른것을 보고 생각하면, 영화 데이터를 받는 시간보다 영화를 받아오는 컴포넌트의 접근이 더 빠른 것 같다. 그래서 Component 이동 후 데이터가 들어옴과 동시에 새로고침이 발생해서, 새로고침을 하면 데이터가 사라지게 되면서 보여줄 영화가 없어지게 된다고 생각했다.
  - 이를 해결하지 못해서, vuex persistedstate를 이용해서 새로고침이 일어나도 데이터가 저장되므로 그대로 원하는 결과를 보여주도록 방지했다.
  - Vuex의 흐름을 다시 생각하고 코드를 수정해야겠다.



#### 5. My Profile Page

> 구현한 기능

- 팔로우 / 팔로잉 숫자 표현
- 별점 기반으로 찜한 영화 목록 제공
- 작성한 커뮤니티 게시글과 댓글 표현 및 Pagination 구현을 통해 정리
- 회원 탈퇴 기능 구현

> 개선점

- 페이지가 단조롭다는 생각이 든다.
  - 구현에 어려움이 있어서 제외한 프로필 이미지, 내 주변 영화관 위치 찾기 지도를 넣어봐야겠다.
  - CSS를 더 생각해서 깔끔한 페이지를 구현해봐야겠다.



#### 6. Other User Profile Page

> 구현한 기능

- Follow / Unfollow 기능 구현

- 해당 유저가 별점 기반으로 찜한 영화 목록 제공
- 작성한 커뮤니티 게시글 표현 및 Pagination 구현을 통해 정리

> 개선점

- 페이지가 단조롭다는 생각이 든다.
  - Follow한 유저가 게시글을 작성하면 알림 혹은 다른 Component에 보여주는 등의 기획도 좋을 것 같다.
  - CSS를 더 생각해서 깔끔한 페이지를 구현해봐야겠다.



#### 7. Community Page

> 구현한 기능

- CRUD에 충실한 게시글, 댓글 기능 구현
- 게시글의 제목, 유저의 이름으로 게시글을 검색할 수 있는 서비스 구현
- 조회 수 기반 Best Top 게시글을 볼 수 있도록 표현
- 게시글 상세 페이지를 Modal로 표현
  - 게시글 좋아요 기능 구현
  - 게시글 작성자의 프로필로 접근 기능 구현
  - 댓글 기능 구현 및 Pagination 구현을 통해 정리

> 개선점

- 페이지가 단조롭다는 생각이 든다.
  - 구현에 어려움이 있어서 제외한 게시글 카테고리 분류, 게시글 이미 첨부 등을 추가해봐야겠다.
  - CSS를 더 생각해서 깔끔한 페이지를 구현해봐야겠다.



------



## 최종 리뷰

#### 1. Vue에 관한 공부가 필요

- Vuex도 사용하고 기본적인 Vue의 Life Cycle를 이용한 설계도 사용했지만, 아직도 Vue에 대한 이해가 부족했던 것 같습니다. Console를 이용해 오류를 찾으려 했지만 해결하지 못하고 오류를 감춰버리거나, 해당 기능 구현을 포기하는 상황도 맞이했습니다. 또한 같은 값을 가르키는 변수를 여러번 사용해서 코드의 깔끔함도 부족하다. Vuex를 통해 처리하는 방법, Vue의 Life Cycle, 코드 정리를 연습하고, 다음 프로젝트 전에는 Vue에 대한 세세한 공부가 필요해보인다.
- 이미지 첨부, 지도맵 활용을 해내지 못했다. 순수한 자바스크립트 혹은 장고로만 개발했을 때는 해당 기능들을 잘 사용했지만, Vue를 이용해서 변환을 하려했는데 실패했다.

# MOVIE_IS_AWESOME

Final pjt

주의사항
1. 반드시 git pull origin develop 을 해서 변경사항이 있는지 확인한다.
2. 반드시 branch 를 만들어서 작업을 진행한다.
3. merge conflict 가 발생하지 않도록 진행하는 부분을 동시에 진행하지 않는다.

GIT의 흐름 (예시)
1. git pull origin develop
2. git checkout -b feature/FE_login
  (작업이 완료되면)
3. git add .
4. git commit -m "FE_login complete"
5. git push origin feature/FE_login (develop 또는 master 가 아님을 주의)
  (gitlab 으로 이동해서)
6. create merge
  (delete source 체크되어있는지 확인)
  (merge 방향이 맞는지 확인 ( ex) feature/FE_login into develop) )
7. git checkout develop (반영이 안된 것을 확인 할 수 있음)
8. git pull origin develop (pull 해서 반영시켜주자)
9. git branch -D feature/FE_login (사용한 branch 는 삭제)
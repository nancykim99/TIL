# GIT
## git 동작
1. `git init` : 로컬 저장소 설정 (초기화). git의 버전 관리를 시작할 디렉토리에서 진행
2. `git add <파일명>` : 변경사항이 있는 파일을 staging area에 추가
3. `git commit -m <커밋 이름>` : taging area에 있는 파일들을 저장소에 기록 → 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
4. `git status` : 로컬 저장소의 파일 상태 확인
5. `git log` : commit 목록 확인
   1. `git log --oneline` : commit 목록 한 줄로 보기
6. `git status` : 현재 로컬 저장소의 파일 상태 보기
7. `git config --global user.email "메일주소"` : commit 작성자 author 정보 이메일 설정
8. `git config --global user.name "유저네임"` : commit 작성자 author 정보 유저 네임 설정
9. `git config --global -l` : git global 설정 정보 보기
10. `git commit --amend` : commit 메시지 수정
    1.  수정 전, i를 통해 Vim 창에서 수정
    2.  수정 후, :wq를 통해 Vim 창 닫기
11. `git remote add origin remote_repo_url` : 로컬 저장소에 원격 저장소 추가
    1.  `origin` : 추가하는 원격 저장소 별칭
    2.  `remote_repo_url` : 추가하는 원격 저장소 주소
12. `git push origin master` : 원격 저장소에 commit 목록을 업로드
13. `git pull origin master` : 원격 저장소의 변경사항만을 받아옴 (업데이트)
14. `git clone remote_repo_url` : 원격 저장소 전체를 복제 (다운로드)
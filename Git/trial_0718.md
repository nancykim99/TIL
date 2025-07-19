### github push/pull 연습 실습

    1. 조장은 홈 디렉토리에 word-relay 폴더 생성
    2. 조장은 Github에 word-relay 원격 저장소 생성 및 로컬 저장소와 연결
    3. 조장은 로컬 저장소에 README.md 와 .gitignore 파일을 생성하고 push
    4. 조장은 원격 저장소의 collaborator로 조원을 초대하기
    5. 조원들은 해당 레포 clone 하기
    ---
    6. 조장과 조원은 add, commit, push, pull을 이용해서 끝말잇기 진행한다.
    7. 자신이 끝말잇기 작성 후 push, push 완료 후 완료한 사실 팀원에게 공유 (끝말잇기는 README.md 에 작성한다.)
    8. 전체 6바퀴 돌면 상황 종료
    9. 전체 6바퀴가 돈 이후에도 연습을 한다면, 순서를 뺏거나 데이터를 섞어서 conflict 을 유발하면서 여러가지 실험을 하는 것도 추천!

```Bash
cd ~
mkdir word-relay
cd word-relay
touch README.md
touch .gitignore
git add README.md
git commit -m '끝말잇기'
git remote add origin remote_repo_url
git push origin master
---
git pull origin master
git add README.md
git commit -m '~'
git push origin master
```

#### Git Status, Log, Add, Commit 연습하기

>1. myFolder 라는 디렉토리를 만들고, Git 초 기화를 진행하세요.
>2. myFolder 디렉토리로 이동 후, test.py 파 일을 만드세요
>3. test.py을 staging area 로 추가하세요.
>4. first commit 이라는 커밋명으로 커밋을 추가하세요.
>5. InnerFolder 디렉토리를 생성하고, 해당 디렉토리 내부에 test2.py 와 test3.py, test4. py 파일을 생성하세요.
>6. InnerFolder 안의 test2.py 를 staging area로 추가한 뒤 second commit 이라 는 커밋을 추가하세요.
>7. InnerFolder 안에서 커밋에 추가되지 않은 나머지 파일을 third commit 으로 커밋을 추가하세요.
>위 과정을 실행한 후
>git status => nothing to commit,
>working tree clean 문구가 나타나야 함
>git log => third commit -> second
>commit-> first commit 이 위에서부터 순 서대로 나타나야 함

```Bash
mkdir myFolders
cd myFolder
git init
touch test.py
git add test.py
git commit -m "first commit"
mkdir InnerFolder
cd InnerFolder
touch test2.py test3.py test4.py
git add test2.py
git commit -m "second commit"
git add test3.py
git add test4.py
git commit-m "third commit"
git status
git log
```
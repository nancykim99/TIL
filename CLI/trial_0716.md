
CLI 연습하기
> 1. 홈 디렉토리로 이동하기
> 2. Practice 디렉토리 생성하기
> 3. Practice 안에 Practice_Folder 디렉토 리 생성하기
> 4. Practice 디렉토리 안의 디렉토리 및 파일출력하기
> 5. Practice 디렉토리에서 practice_file.txt생성하기
> 6. practice_file.txt copy-practice_fille.txt 로 복사하기
> 7. copy_practice_file.txt =Practice_Folder로 위치를 변경하고, 이 때 이름을 moved_practice_file.txt로 변경하기
> 8. Practice 디렉토리의 practice_file.txt파일 삭제하기
> 9. Practice_Folder 디렉토리 삭제하기
> 10. Practice 디렉토리 삭제하기

``` Bash
cd ~
mkdir Practice
cd Practice
mkdir Practice_Folder
ls 
touch practice_file.txt
cp practice_file.txt copy_practice.txt
mv copy_practice_file.txt <moving directory>
cd ..
rm practice_file.txt
rm -r Practice_Folder
cd ..
rm -r Practice
```
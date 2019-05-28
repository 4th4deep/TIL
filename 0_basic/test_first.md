# 190527 기초 설치 및 사용법 학습

## markdown 작성하기

### 제목 작성

제목은, Semantic 하게 작성한다.

### 나열(리스트) 작성하기

#### 순서가 있는 리스트

1. WeMakeO 앱을 받는다.
2. 회원가입한다.
   * 카카오
   * 페북
   * 네이버
3. W카페를 찾는다.
4. 커피를 주문한다.
5. 알림이 오면 픽업하러 간다.

#### 순서가 없는 리스트

* 파이썬 설치하기
  * 3.7
  * 3.6
* 타이포라 설치하기
* Git 설치하기

### 일반 문단 작성하기

오늘 점심은 무엇일까요. 

오늘 점심은 탄수화물 폭탄입니다.

### 코드 블럭 작성하기

터미널에서 `python -e` 라고 입력하면, **코드가 실행**됩니다.

```python
def index():
	return 'hi'

def create():
    save()
```





## CLI - terminal 명령어 학습

```sh
$ touch a.txt  # a.txt 를 생성한다.
$ mkdir test  # test 폴더/디렉토리를 생성한다. MaKe DIRectory
$ cd test  # test 디렉토리로 이동한다. Change Directory
$ cd ..  # 한단계 위의 디렉토리로 이동한다.
$ cd -  # 뒤로 가기
$ cd ~  # home 으로 이동한다.
$ rm a.txt  # a.txt 를 삭제한다.
$ rm -r test/  # test/ 디렉토리를 삭제한다.
$ ls  # LiSt 현재 디렉토리 안의 파일/디렉토리 목록을 표시한다.
$ pwd  # 현재 내가 위치한 디렉토리를 표시한다. Present Working Directory
```



## git 기초 명령

```sh
$ git init  # pwd 에서 git 으로 버젼관리 시작! (.git/ 를 만든다.)
$ git remote add origin <remote url>  # 드라이브 등록

## 여기까지는 한번만! ## 

$ git add .  # 내 위치(.) 를 전체 등록 (사진 찍을 준비)

$ git commit -m 'MESSAGE'  # 사진 찰칵 + 메시지

## 계속 반복! add & commit ##

$ git push origin master  # 드라이브 백업
```

```sh
# 반드시 확인!!
$ pwd
/c/Users/student/TIL  # TIL 에 있는걸 확인하자!!

# 수업 중간 중간
$ git add .
$ git commit -m '남길 메시지'
# 적절한 타이밍에!

# 집에가기 전에
$ git push origin master
```



## 좌석표 작성

### `bit.do/4th4deep`





## Python 기초

``




















# python_begin

## 파이썬 설치 mac os X, VSCode

<br>[python.org](http://python.org) 사이트에서 다운로드 → VSCode의 Python extension 설치

<br>터미널에서 which python3 를 입력하면 python3가 위치한 경로가 나옴. 해당 경로를 vscode의 setting.json 마지막줄에 추가해준다. setting.json은 아래 사진과 같이 들어가서 나오는 화면의 우측 상단의 아이콘을 클릭하면 볼수있다.

![](https://github.com/sebaek42/python_begin/blob/master/img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-07-29%20%EC%98%A4%EC%A0%84%2010.21.41.png?raw=true)

`"python.pythonPath": "/Library/Frameworks/Python.framework/Versions/3.8/bin/python3"`

<br>이걸 json파일의 마지막 줄에 추가해주면된다. (추가하기 전 윗줄에 ','제대로 써줬나 확인해보자)

<br>인터프리터를 선택하라고하면 아까설치한 버전으로 선택해주면 설정 끝.

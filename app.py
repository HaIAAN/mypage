#빈화면에서 가상환경 적용부터 해야함
#상단 뉴터미널, 터미널창에서  -m venv venv 명령실행
#폴더에 venv(가상환경) 생성확인후 우측하단 3.8.6 클릭하여 상단에 venv 적용
#기존터미널 끄고 다시 뉴터미널 실행시 파일위치에 venv뜨는거 확인


from flask import Flask,render_template
app = Flask(__name__)

#플라스크, 뒤에 render_template 입력(사용하겠다)
#하단으로 다시이동


@app.route('/')
def home():
   return 'This is Home!'
#복붙해서 아래에 붙이기

@app.route('/mypage')
def mypage():
   return render_template('index.html')

#host주소뒤에 /mypage입력 (창구역할)
#def 뒤에도 마찬가지로 변경적용
#새폴더 templates 안에 새파일 index.html 
#인덱스파일 끌어와주는 기능 - 플라스크의 렌더 템플릿사용
#상단으로 이동 
#플라스크뒤에 렌더템플릿 사용 명령적용하고 
#내려와서 return뒤에 렌더템플릿('인데스html')불러올 파일


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)


#플라스크를 가지고프론트엔드에서 백엔드로
# 데이터를 전송하고, 데이터베이스에 넣고, 내려받기가능
#4주차 1강~4강 

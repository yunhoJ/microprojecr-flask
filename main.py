from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# mysql과 연결 
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@db/main' # mysql에 유저네임 :페스워드 @호스트(docker서비스명)/db이름
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
CORS(app)
# db 모델 구성 알키미 패키지를 이용해 모델처럼 구성한다 
db=SQLAlchemy(app)

class Shop():
    id=db.Column(db.Integer,primary_key=True,autoincrement=False) # 장고의 db와 싱크를 맞춰야함 
    shop_name=db.Column(db.String(200))
    shop_address=db.Column(db.String(200))

class Order(): # boss 데이터베이스는 order date와 deliverFinish를 가지고 있을 필요가 없음
    id=db.Column(db.Integer,primary_key=True,autoincrement=False) # 장고의 db와 싱크를 맞춰야함 
    shop=db.Column(db.Integer)
    address=db.Column(db.String(200))


@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')

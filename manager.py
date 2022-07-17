#쉘 스크립트로 마이 그레이션 할때 도와주는 코드 
from main import app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

migrate=Migrate(app,db)

manager=Manager(app)
manager.add_command('db',MigrateCommand) #db이후 어떤 명령어 올지 

if __name__=='__main__':
    manager.run()
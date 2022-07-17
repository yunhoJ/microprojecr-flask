FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app    
#워킹디렉토리가 같아도 분리되어있어 독립컨테이너에서 설정함
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app 
# 현재 디렉토리에 있는 모든 파일을 app에 복사 

# CMD python manage.py runserver 0.0.0.0:8000 - 장고
CMD python main.py
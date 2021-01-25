FROM python:3

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

ADD    ./djangosample   /app/djangosample/
ADD    ./usertasksapi   /app/usertasksapi/
ADD    ./manage.py      /app/

  
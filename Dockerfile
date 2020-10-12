FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY ./src/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./src/ .

EXPOSE 8000

CMD ["python" , "manage.py" , "runserver" , "--noreload" , "0.0.0.0:8000"]

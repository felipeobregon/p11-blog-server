FROM python:3.7.4-slim-buster

WORKDIR /app

COPY . . 

RUN pip3 install -r requirements.txt

#CMD ["gunicorn", "main:app"]

CMD ["python", "main.py"]
FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app1.py .

ENV FLASK_APP=app1

EXPOSE 5005
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5005"]

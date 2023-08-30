FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
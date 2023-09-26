FROM python:3.7.4-slim-buster

COPY . /modelZ

WORKDIR /model

RUN pip install -r requirements.txt

CMD ["python", "model.py"]
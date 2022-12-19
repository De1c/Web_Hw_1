FROM python:3.9.12

LABEL Yehor Serdiuk

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
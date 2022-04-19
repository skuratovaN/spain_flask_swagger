FROM python:3.9.11

RUN mkdir /app
COPY /app /app
WORKDIR /app

RUN pip install flask
RUN pip install bs4
RUN pip install connexion

CMD ["python", "app.py"]
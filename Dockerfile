FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install poetry && poetry install
RUN export FLASK_APP=app.py
EXPOSE 5001

ENTRYPOINT ["poetry", "run", "python3", "app.py"]

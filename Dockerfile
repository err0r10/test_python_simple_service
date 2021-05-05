FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN export FLASK_APP=app.py
EXPOSE 5000
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

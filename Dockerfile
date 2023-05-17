FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY . .
WORKDIR .

# https://github.com/python-poetry/poetry/issues/6489
RUN pip3 install --use-pep517 psycopg2-binary

RUN pip3 install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install
RUN export FLASK_APP=app.py
RUN ["chmod", "+x", "./script.sh"]

EXPOSE 5001
CMD ["./script.sh"]

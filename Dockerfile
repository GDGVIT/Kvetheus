# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip3 install pipenv
CMD ["pipenv", "install"]

COPY . .

CMD [ "python3", "-m" , "app.py"]

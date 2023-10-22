FROM python:3.10
WORKDIR /usr/src/app
COPY ./app ./
CMD [ "python", "./prediction.py" ]
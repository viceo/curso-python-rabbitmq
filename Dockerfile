FROM python:alpine
WORKDIR /usr/src/app
COPY . .

RUN apk update
RUN apk add nodejs
RUN apk add npm
RUN npm install -g nodemon
RUN pip install pika

CMD [ "nodemon","./consumer/consumer.py"]
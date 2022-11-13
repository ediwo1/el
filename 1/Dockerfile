FROM python:3.8.15-alpine3.16

RUN apk update
RUN apk add docker docker-cli docker-compose openrc
RUN addgroup root docker
RUN rc-update add docker boot
 
# Create app directory
WORKDIR /app

# Install app dependencies
COPY 1/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY 1/* ./

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]


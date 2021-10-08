
## Installation
Create workdir:
```sh
mkdir telegram-plug-bot
```
Create .env file:
```sh
API_TOKEN=1234:12345
MESSAGE_TEXT=My message
LOG_LEVEL=ERROR
```
Run docker container:
```sh
docker run -d --env-file .env --name telegram-plug-bot artempal/telegram-plug-bot
```

## About
Base image - **python:3.9-alpine**

Powered by **aiogram**. 

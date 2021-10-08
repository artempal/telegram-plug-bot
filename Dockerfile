FROM python:3.9-alpine
RUN pip install --user aiogram
WORKDIR /usr/src/app/
COPY bot.py /usr/src/app/
CMD ["python", "bot.py"]

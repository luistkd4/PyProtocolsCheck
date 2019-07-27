FROM python:3.5.7-jessie
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["API-ProtocolTest.py"]
EXPOSE 5000

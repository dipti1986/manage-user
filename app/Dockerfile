FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3.5 curl
RUN mkdir app
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "main.py"]

# https://docs.docker.com/language/python/build-images/
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# docker build --tag python-docker .
# docker run -d -p 5000:5000 <image>
# https://docs.docker.com/config/containers/container-networking/
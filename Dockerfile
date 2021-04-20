# https://docs.docker.com/language/python/build-images/
FROM python:3.8-slim-buster

WORKDIR /srv

COPY . .
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y iputils-ping
# CMD ["python3", "/test_python.py"] -- week 1 command 

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"] -- command from https://docs.docker.com/language/python/build-images/

CMD ["python3", "api.py"]
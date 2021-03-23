# https://docs.docker.com/language/python/build-images/
FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
# CMD ["python3", "/test_python.py"] -- week 1 command 

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"] -- command from https://docs.docker.com/language/python/build-images/

CMD ["python3", "/api.py"]

# note: add RUN apt-get update and install 

FROM python:3.7.5-slim
# CMD ["sleep", "infinity"]

COPY requirements.txt requirements.txt

COPY test_python.py .
COPY api.py .
RUN pip3 install -r requirements.txt
# CMD ["python3", "/test_python.py"]
CMD ["python3", "/api.py"]
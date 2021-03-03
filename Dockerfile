FROM python:3.7.5-slim
# CMD ["sleep", "infinity"]
COPY test_python.py .
CMD ["python3", "/test_python.py"]
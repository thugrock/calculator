FROM python:3.10
WORKDIR /src/app
COPY . /src/app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
CMD ["python3", "test_app.py"]

FROM python:3.10
WORKDIR /src
COPY . /src
RUN pip install -r ./app/requirements.txt
RUN python3 ./app/test_app.py
CMD ["python3", "./app/app.py"]

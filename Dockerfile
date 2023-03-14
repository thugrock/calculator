FROM python:3.10
WORKDIR /src/app
COPY . /src/app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python3", "app.py"]

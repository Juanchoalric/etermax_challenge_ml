FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

#RUN apt-get install python3-sqlalchemy

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY . .

RUN python app.py

EXPOSE 5000

CMD ["python", "app.py", "serve"]
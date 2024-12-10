FROM python:3.12-slim

WORKDIR /app
RUN apt update -y && apt install awscii -y

COPY . /app/
RUN pip install -r requiements.txt

CMD ["python3", "app.py"]
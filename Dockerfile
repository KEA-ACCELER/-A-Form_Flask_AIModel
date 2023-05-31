FROM python:latest

WORKDIR /app

COPY . /app

RUN pip3 install flask
RUN pip3 install flask_cors
RUN pip3 install openai

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
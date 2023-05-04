
from threading import Thread
from flask import Flask, request
import os
import subprocess
import openai
import argparse
import os



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/chatbot', methods=['POST'])
def run_script():
    body = request.get_json() 
    print(body)
    
    api_key = os.environ['OPENAI_API_KEY']

    openai.api_key = api_key
    
    
    # 모델 - GPT 3.5 Turbo 선택
    model = "gpt-3.5-turbo"

    # 메시지 설정하기
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": body["msg"]}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    print(answer)
    return answer
    # result=subprocess.run(["python3", "open_ai.py", "--query", body["msg"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    # print(result.stdout) # 표준 출력
    # return result.stdout

if __name__ == '__main__': 
    #Thread(target=run_schedule).start()
    app.run(host="0.0.0.0", port=5000)
import pya3rt
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def hello():
    apikey = "" #自分のAPIキーを設定する
    client = pya3rt.TalkClient(apikey)
    return "ようこそ TalkAIへ"

def talk_ai():
  words = input("あなた >")
  while words!="":
    response = client.talk(words)
    print("Bot >"+((response['results'])[0])['reply'])
    words = input("あなた >")

if __name__ == '__main__':
    app.run()
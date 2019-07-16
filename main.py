from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,

app = Flask(__name__)

line_bot_api = LineBotApi('7V069b8jBNfXHeQLg/2baW1qV84JytuoDk+y1wuBOwqVEJl8LeCWtxl+13NJkBDl5MSYmJC96oYq52h3FE0UiEbAjJjkgKU9cSLOr3w3wMBSazjaJhd5ssyA+4wQS5I1xIhRV1Gkj9viyPfS0WchaQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e95453e5afce1e2dd34af3807c6d417e')

@app.route("/")
def greeting():
    return "hello"

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
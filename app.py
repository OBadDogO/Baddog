from flask import Flask, request, abort

from events.basic import *
from events.service import*
from line_bot_api import *

from extensions import db, migrate
from models.user import User
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS','config.DevConfig'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zx2203300zx:MXCp7IA8FF60LFIpc4vTM13QTs7BtfFo@dpg-cjkcdqb37aks738v0kk0-a.singapore-postgres.render.com/ex2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
migrate.init_app(app, db)

@app.route("/callback", methods=['POST'])
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

    message_text = str(event.message.text).lower()

    if message_text == '@關於我們':
        about_us_event(event)

    elif message_text == '@營業據點':
        location_event(event)
    
    elif message_text == '@預約服務':
        service_category_event(event)

@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    if data.get('action') == 'service':
        service_event(event)

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """Hello! 您好，歡迎您成為 Master SPA 的好友！

我是Master SPA的小幫手 

-想預約按摩/臉部淨化護理服務都可以直接跟我互動喔~
-直接點選下方【歡迎光臨專屬您的SPA】選單功能

-期待您的光臨！"""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


if __name__ == "__main__":
    app.run()

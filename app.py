from flask import Flask, request, abort

#from events.basic import *
#from line_bot_api import *
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage
)

line_bot_api = LineBotApi('kQavKvxNS5PDFgBV/8mgLPpQZmmdToFeaneQMCvj7wZvP5xe67lxDFvnpCkDwFaAT9xGyOgR2C+HeKWjDcIPcEsiqtMAL809pC5MnwVejhqZR30540WJZlCBBvn7ce/tqMJy93FUic3JY8gFdN3PMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('248fb9d60f05e53f3fd713f2e184f598')

app = Flask(__name__)

@app.route("/callback" , methods=['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " +body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
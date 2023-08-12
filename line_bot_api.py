# pip install line-bot-sdk
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage,FlexSendMessage,TemplateSendMessage,ImageCarouselTemplate,PostbackAction,ImageCarouselColumn
)

line_bot_api = LineBotApi('kQavKvxNS5PDFgBV/8mgLPpQZmmdToFeaneQMCvj7wZvP5xe67lxDFvnpCkDwFaAT9xGyOgR2C+HeKWjDcIPcEsiqtMAL809pC5MnwVejhqZR30540WJZlCBBvn7ce/tqMJy93FUic3JY8gFdN3PMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('248fb9d60f05e53f3fd713f2e184f598')
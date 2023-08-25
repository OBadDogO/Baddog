# pip install line-bot-sdk
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage,FlexSendMessage,TemplateSendMessage,ImageCarouselTemplate,PostbackAction,ImageCarouselColumn,PostbackEvent
)

line_bot_api = LineBotApi('kQavKvxNS5PDFgBV/8mgLPpQZmmdToFeaneQMCvj7wZvP5xe67lxDFvnpCkDwFaAT9xGyOgR2C+HeKWjDcIPcEsiqtMAL809pC5MnwVejhqZR30540WJZlCBBvn7ce/tqMJy93FUic3JY8gFdN3PMAdB04t89/1O/w1cDnyilFU=')
##上面紅色字串是LINE developers (API)裡的 "Channel access token"
handler = WebhookHandler('248fb9d60f05e53f3fd713f2e184f598')
##上面是紅色字串是LINE developers 裡的"Channel secret"
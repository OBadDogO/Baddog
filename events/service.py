from line_bot_api import*
from urllib.parse import parse_qsl

services = {
    1:{
        'category':'按摩調理',
        'img_ur1':'https://icook.tw/recipes/428846',
        'title':'運動按摩(按摩與伸展)',
        'duration':'90min',
        'description':'深層肌肉緊繃酸痛',
        'price':1500,
        'post_ur1':'https://linecorp.com'
    },
    2:{
        'category':'按摩調理',
        'img_ur1':'https://icook.tw/recipes/432383',
        'title':'按摩調理(指壓/精油)',
        'duration':'90min',
        'description':'深層肌肉緊繃酸痛',
        'price':2000,
        'post_ur1':'https://linecorp.com'
    
    },
    3:{
        'category':'按摩調理',
        'img_ur1':'https://icook.tw/recipes/428846',
        'title':'按摩調理(指壓/精油)',
        'duration':'90min',
        'description':'深層肌肉緊繃酸痛',
        'price':2000,
        'post_ur1':'https://linecorp.com'
    
    },
    4:{
        'category':'臉部護理',
        'img_ur1':'https://icook.tw/recipes/428846',
        'title':'按摩調理(指壓/精油)',
        'duration':'90min',
        'description':'深層肌肉緊繃酸痛',
        'price':2000,
        'post_ur1':'https://linecorp.com'
    
    },
}

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text = "請選擇想要的服務",
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = 'https://icook.tw/recipes/428846',
                    action=PostbackAction(
                        label = '按摩調理',
                        display_text = "想了解按摩" ,
                        data='action=service&category=按摩調理'
                    )
                ),
                ImageCarouselColumn(
                    image_url = 'https://icook.tw/recipes/428846',
                    action = PostbackAction(
                        label = '臉部護理',
                        display_text = "想了解按摩" ,
                        data = 'action=service&category=臉部護理'
                    )
                )        
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])

def service_event(event):
    data = dict(parse_qsl(event.postback.data))
    bubbles = []  

    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubble = {
              "type": "bubble",
              "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "url": service['img_url']
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": service['title'],
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                  },
                  {
                    "type": "text",
                    "text": service['duration'],
                    "size": "md",
                    "weight": "bold"
                  },
                  {
                    "type": "text",
                    "text": service['description'],
                    "margin": "lg",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": f"NT$ {service['price']}",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0
                      }
                    ],
                    "margin": "xl"
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "button",
                    "style": "primary",
                    "action": {
                      "type": "postback",
                      "label": "預約",
                      "data": f"action=select_date&service_id={service_id}",
                      "displayText": f"我想預約【{service['title']} {service['duration']}】"
                    },
                    "color": "#b28530"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "了解詳情",
                      "uri": service['post_url']
                    }
                  }
                ]
              }
            }

            bubbles.append(bubble)

    flex_message = FlexSendMessage(
        alt_text = '請選擇預約項目',
        contents = {
            "type":"carousel",
            "contents": bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])
    
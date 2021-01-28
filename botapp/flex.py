from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from botapp.models import *

def jobs_progress(uid):
    contents=dict()
    contents['type']='carousel'
    bubbles=[]
    datas = Jobs.objects.filter(uid=uid)
    for data in datas:
        label = data.job_name
        percentage = data.percentage
        text = data.description
        bubble= {   "type": "bubble",
                    "size": "nano",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": label,
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": str(percentage)+"%",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                }
                                ],
                                "width": str(percentage)+"%",
                                "backgroundColor": "#0D8186",
                                "height": "6px"
                            }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        }
                        ],
                        "backgroundColor": "#27ACB2",
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": text,
                                "color": "#8C8C8C",
                                "size": "sm",
                                "wrap": True
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                    },
                    "styles": {
                        "footer": {
                        "separator": False
                        }
                    }
                }
        bubbles.append(bubble)
    contents['contents']=bubbles
    message=FlexSendMessage(alt_text='工作進度',contents=contents)
    return message
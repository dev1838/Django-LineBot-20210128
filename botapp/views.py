from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

#models.py資料表
from botapp.models import *
from botapp.flex import *
from botapp.image_processing import *

import string
import random
import os
import csv

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        #建立message list
        message=[]
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        message.append(TextSendMessage(text=str(body)))

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                # print(event.message.type)
                if event.message.type=='text':
                    mtest = event.message.text
                    if "FlexTest" in mtest:
                        message.append(flexexample())
                        line_bot_api.reply_message(event.reply_token,message)
                    else:    
                        message.append(TextSendMessage(text='文字訊息'))
                        line_bot_api.reply_message(event.reply_token,message)
                elif event.message.type=='image':
                    image_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(4))
                    image_content = line_bot_api.get_message_content(event.message.id)
                    image_name = image_name.upper()+'.png'
                    path='./static/'+image_name
                    with open(path, 'wb') as fd:
                        for chunk in image_content.iter_content():
                            fd.write(chunk)
    
                    #將原圖存為灰階、二值化圖片
                    gray,binary,contour = image_processing_1(image_name,path)

                    domain = 'b3c4322ec312.ngrok.io'

                    gray = 'https://'+domain+gray[1:]
                    binary = 'https://'+domain+binary[1:]
                    contour = 'https://'+domain+contour[1:]

                    message.append(ImageSendMessage(original_content_url=gray,preview_image_url=gray))
                    message.append(ImageSendMessage(original_content_url=binary,preview_image_url=binary))
                    message.append(ImageSendMessage(original_content_url=contour,preview_image_url=contour))

                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='location':
                    message.append(TextSendMessage(text='位置訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='video':
                    message.append(TextSendMessage(text='影片訊息'))
                    line_bot_api.reply_message(event.reply_token,message)


                elif event.message.type=='sticker':
                    message.append(TextSendMessage(text='貼圖訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='audio':
                    message.append(TextSendMessage(text='聲音訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='file':
                    message.append(TextSendMessage(text='檔案訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, FollowEvent):
                print('加入好友')
                line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, UnfollowEvent):
                print('取消好友')

            elif isinstance(event, JoinEvent):
                print('進入群組')
                line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, LeaveEvent):
                print('離開群組')
                line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, MemberJoinedEvent):
                print('有人入群')
                line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, MemberLeftEvent):
                print('有人退群')
                line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, PostbackEvent):
                print('PostbackEvent')


        return HttpResponse()
    else:
        return HttpResponseBadRequest()
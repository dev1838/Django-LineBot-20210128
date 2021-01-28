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
from botapp.superpix import *

#import speech_recognition及pydub套件
import speech_recognition as sr
from pydub import AudioSegment

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

                    domain = 'c74f160c6d3f.ngrok.io'

                    slic = SLIC(image_name,path)
                    seed = SEEDS(image_name,path)
                    lsc = LSC(image_name,path)

                    message.append(ImageSendMessage(original_content_url=slic,preview_image_url=slic))
                    message.append(ImageSendMessage(original_content_url=seed,preview_image_url=seed))
                    message.append(ImageSendMessage(original_content_url=lsc,preview_image_url=lsc))
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
                    audio_content = line_bot_api.get_message_content(event.message.id)
                    path='./static/sound.m4a'
                    with open(path, 'wb') as fd:
                        for chunk in audio_content.iter_content():
                            fd.write(chunk)

                    #進行語音轉文字處理
                    r = sr.Recognizer()
                    AudioSegment.converter = 'C:\\ffmpeg\\bin\\ffmpeg.exe'#輸入自己的ffmpeg.exe路徑
                    sound = AudioSegment.from_file_using_temporary_files(path)
                    path = os.path.splitext(path)[0]+'.wav'
                    sound.export(path, format="wav")
                    with sr.AudioFile(path) as source:
                        audio = r.record(source)
                    text = r.recognize_google(audio,language='zh-Hant')#設定要以什麼文字轉換

                    #將轉換的文字回傳給用戶
                    message.append(TextSendMessage(text=text))
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
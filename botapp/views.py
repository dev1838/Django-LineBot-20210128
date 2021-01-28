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
from botapp.flex import *

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
                #print(event.message.type)
                message=[]
                uid=event.source.user_id
                profile=line_bot_api.get_profile(uid)
                name=profile.display_name
                if event.message.type=='text':
                    mtext = event.message.text
                    if 'jobs' in mtext:
                            job = mtext.split(',')
                            Jobs.objects.create(uid=uid,
                                                name=name,
                                                job_name=job[1],
                                                percentage=job[2],
                                                description=job[3])
                            message.append(TextSendMessage(text='收到的工作內容為：'+str(job)))
                            message.append(TextSendMessage(text='建立工作內容完成'))
                            line_bot_api.reply_message(event.reply_token,message)
                    elif "工作查詢" in mtext:
                        message.append(jobs_progress(uid))
                        line_bot_api.reply_message(event.reply_token,message)
                    else:
                        message.append(TextSendMessage(text='文字訊息'))
                        line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='image':
                    message.append(TextSendMessage(text='圖片訊息'))
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
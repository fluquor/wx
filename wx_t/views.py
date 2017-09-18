# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import hashlib
from . import reply
from . import receive
# Create your views here.
    
class WeChat(View):
    
    def get(self,request):
        try:
            token='anhedonia'
            data=request.GET
            print(data)
            if len(data)==0:
                return 'No data'
            signature=data.get('signature')
            nonce = data.get('nonce')
            echostr = data.get('echostr')
            timestamp = data.get('timestamp')
            ist = [token, timestamp, nonce]
            print(ist)

            ist.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, ist)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            # if hashcode == signature:
            return HttpResponse(echostr)
            # else:
            #     return HttpResponse("")
        except (Exception):
            pass
    
    def post(self,request):
        try:
            data=request.body.decode('utf-8')
            print(data)
            # rec_msg=receive.parse_xml(data)
            recMsg = receive.parse_xml(data )
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return HttpResponse(replyMsg.send())
            else:
                print('不处理')
                return HttpResponse('Success')
        except Exception:
            return ''

        return HttpResponse("")
            

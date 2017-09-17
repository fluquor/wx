from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from . import reply
from . import receive
# Create your views here.

def handle(request):
    print(request.body)
    
    if request.methd=='GET':
        return GET(request)
    else:
        return POST(request)
    

def GET(request):
    try:
        token='anhedonia'
        data=request.GET
        if len(data)==0:
            return 'No data'
        signature=data.siganture
        nonce = data.nonce
        echostr = data.echostr
        timestamp = data.timestamp
        ist = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return "Bad"
    except (Exception):
        pass

def POST(request):
    pass
            

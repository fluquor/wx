from django.shortcuts import render
from django.http import HttpResponse
import hashlib
# Create your views here.

def handle(request):
    print(request.body)
    token='anhedonia'
    try:
        data=request.GET
        if len(data)==0:
            return 'No data'
        siganture=data.siganture
        nonce = data.nonce
        echostr = data.echostr
        ist = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return "Good"
    except Exception,Argument:
        return Argument
            

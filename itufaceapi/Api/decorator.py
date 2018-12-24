import json,requests
from  public.AesUtils import AesUtils
def JsonToDict(func):
    def inner(request,*args, **kwargs):

        data = json.loads(str(request.body, encoding='utf-8'))
        aus=AesUtils()
        if 'mobile' in data.keys():
            print('装饰器mobile----》',data['mobile'])
            encrpyts=aus.encrpyt(data['mobile'])
            print('encrpyts=====>',encrpyts)
            data['mobile']=''.join(encrpyts)
        if 'idNo' in data.keys():
            encrpyts=aus.encrpyt(data['idNo'])
            data['idNo']=''.join(encrpyts)
        request.JSON=data
        return func(request,*args,**kwargs)
    return inner



def JsonToList(func):
    def inner(request,*args, **kwargs):

        data = json.loads(str(request.body, encoding='utf-8'))
        aus=AesUtils()
        if 'mobile' in data.keys():
            print('装饰器mobile----》',data['mobile'])
            encrpyts=aus.encrpyt(data['mobile'])
            print('encrpyts=====>',encrpyts)
            data['mobile']=encrpyts
        if 'idNo' in data.keys():
            encrpyts=aus.encrpyt(data['idNo'])
            data['idNo']=encrpyts
        request.JSON=data
        return func(request,*args,**kwargs)
    return inner

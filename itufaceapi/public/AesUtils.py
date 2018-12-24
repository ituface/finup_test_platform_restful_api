
import requests
import json
class  AesUtils():
    def __init__(self):
        self.encrpyt_api='http://10.10.180.206:8090/getEncrpyt?array=' #加密
        self.decrpyt_api='http://10.10.180.206:8090/getDecrpyt?array=' #解密

    '''
    加密
    '''
    def  encrpyt(self,parameter):
        url=self.encrpyt_api+parameter
        return self.request(url)

    '''
    解密
    '''
    def  decrpyt(self,parameter):
        url=self.decrpyt_api=self.decrpyt_api+parameter
        return self.request(url)



    def request(self,request):
        data=requests.get(request).text
        return json.loads(data)


a=AesUtils()
print(a.encrpyt('17600810360'))
# print(requests.get('http://10.10.180.206:8090//getEncrpyt?array=222,2,3,').text)


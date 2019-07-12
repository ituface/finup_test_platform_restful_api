from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning,AcceptHeaderVersioning,NamespaceVersioning
from django.http import JsonResponse
from django.shortcuts import HttpResponse
import json,os
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,authentication_classes,renderer_classes
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from  public.mysql import MysqlHandle
import time
from public.AesUtils import AesUtils


from  Api.decorator import JsonToDict,JsonToList



class Test1Authentication(BaseAuthentication):
    def authenticate(self, request):
        auth=request.META.get('HTTP_AUTHORIZATION')
        #token=request.META.get('HTTP_TOKEN')
        # timeStrap=int(request.META.get('HTTP_TIMESTRAP'))
        # server_timeStrap=int(time.time())
        if auth!='YLS':
            raise exceptions.AuthenticationFailed({"error":'NOT AUTHORIZATION'})


'''
搜索进件
'''
@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToDict
def SearchResult(request):
       data=request.JSON
       status=data['status']
       sql=MysqlHandle.get_xml_sql(xml_path='select_sql',xml_tag='select',xml_id='search_result')
       sql_data=MysqlHandle.select_mysql_data(sql.format(status=status))
       count=len(sql_data)
       result = {'code': 200, 'data': sql_data}
       if count:
           strs=''
           for inner in sql_data:
               strs=strs+','+inner['mobile']
           aus=AesUtils()
           mobile_list=aus.decrpyt(strs.lstrip(','))
           for let in range(len(mobile_list)):
                sql_data[let]['mobile']=mobile_list[let]
           result['data']=sql_data
           return JsonResponse(result, status=200)


       result['code']=202
       return  JsonResponse(result, status=202)
'''
必填项
'''
@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToDict
def ProductIsRequired(request):
    data=request.JSON
    product_name=data['product_name']
    sql = MysqlHandle.get_xml_sql(xml_path='select_sql', xml_tag='select', xml_id='search_product_required')
    sql_data = MysqlHandle.select_mysql_data(sql.format(product_name=product_name))
    result_data=[]
    for inner in sql_data:
        result_data.append(inner["material_type"])
    result={'code':200,'data':result_data}
    print('必填项-----》',result)
    return JsonResponse(result,status=200)

'''
更改身份证
'''
@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToDict
def changeIdNo(request):
    '''

    :param request:mobile：str 装饰器加密 idNo：str 装饰器加密 ，customer_name：str 姓名
    :return:
    '''
    data = request.JSON
    mobile = data['mobile']
    idNo=data['idNo']
    customer_name=data['customer_name']
    result = {'code': '200', 'data': '成功了'}
    try:
        sql = MysqlHandle.get_xml_sql(xml_path='update_sql', xml_tag='update', xml_id='update_customer_idno')
        print('sql.format(idNo=idNo,mobile=mobile,customer_name=customer_name)---->',sql.format(idNo=idNo,mobile=mobile,customer_name=customer_name))
        sql_data = MysqlHandle.delete_update_insert_mysql_data(sql.format(idNo=idNo,mobile=mobile,customer_name=customer_name))
    except Exception as e:
        result['code']='400'
        result['data']=e
        return JsonResponse(result,status=400)
    return JsonResponse(result,status=200)


'''
更新魔蝎状态
'''


@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToDict
def updateMXstatus(request):
    '''

    :param request: mobile:str 装饰器加密 ，type：list 为魔蝎字段
    :return: json
    '''
    data=request.JSON
    mobile=data['mobile']
    types=list(data['type'])
    strs=''
    for i in types:
        strs = strs + ',' + '"%s"'%i
    print('strs------->',strs)
    result = {'code': '200', 'data': '成功了'}
    try:
        sql = MysqlHandle.get_xml_sql(xml_path='update_sql', xml_tag='update', xml_id='update_mx_grap')
        sql=sql.format(mobile=mobile, type=strs.lstrip(','))
        sql_data = MysqlHandle.delete_update_insert_mysql_data(sql.format(mobile=mobile, type=strs.lstrip(',')))
    except Exception as e:
        result['code'] = '400'
        result['data'] = e
        return JsonResponse(result, status=400)
    return JsonResponse(result,status=200)

'''
删除user_token ,返回lend_request_id
'''

@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToDict
def delete_token_return_lend_request_id(request):
    data=request.JSON
    sale_no=data['sale_no']
    mobile=data['mobile']
    print('data======>',mobile)

    result = {'code': '202', 'data': '没有此手机号'}
    try:
        sql1 = MysqlHandle.get_xml_sql(xml_path='select_sql', xml_tag='select', xml_id='select_lend_request_id')
        print(sql1.format(mobile=mobile))
        sql_data1 = MysqlHandle.select_mysql_data(sql1.format(mobile=mobile))
        sql2 = MysqlHandle.get_xml_sql(xml_path='delete_sql', xml_tag='delete', xml_id='delete_user_token')
        sql_data2 = MysqlHandle.delete_update_insert_mysql_data(sql2.format(sale_no=sale_no))

    except Exception as e:
        result['code'] = '400'
        result['data'] = e
        return JsonResponse(result, status=400)
    if sql_data1:
     result['code']='200'
     result['data']=sql_data1[0]
    return JsonResponse(result,status=200)



@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToDict
def mobile_enable(request):
    data=request.JSON
    result={'code':'200','data':'1'}
    mobile=data['mobile']
    try:
        sql= MysqlHandle.get_xml_sql(xml_path='select_sql', xml_tag='select', xml_id='select_mobile_enable')
        print('sql---->',sql.format(mobile=mobile))
        mysql_data=MysqlHandle.select_mysql_data(sql.format(mobile=mobile))
        dicts=mysql_data[0]
        tag=dicts['counts']
    except Exception as e :
        result['code']='400'
        result['data']=e
        return  JsonResponse(result,status=400)
    if tag:
        return JsonResponse(result,status=200)
    result['data']='%s'%tag
    return JsonResponse(result,status=200)

@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToList
def mobile_to_id_status(request):
    data=request.JSON
    mobile=data['mobile']
    mobile_str=''
    print('views 中 mobile----》',mobile)
    for i in mobile:
        mobile_str=mobile_str+'"%s"'%i+','
    sql_moblie=mobile_str.rstrip(',')
    print('sql_moblie----->',sql_moblie)
    sql=MysqlHandle.get_xml_sql(xml_path='select_sql',xml_tag='select',xml_id='select_id_status_to_piece')
    print(sql.format(mobile=sql_moblie))


    data=MysqlHandle.select_mysql_data(sql.format(mobile=sql_moblie))


    result={'code':200,'data':data}
    return JsonResponse(result,status=200)


'''
跳过人脸识别
'''

@api_view(['post'])
@authentication_classes([Test1Authentication])
@JsonToList
def update_face_id(request):
    try:
        data = request.JSON
        mobile = data['mobile'][0]
        today=date.today()
        sql=MysqlHandle.get_xml_sql(xml_path='update_sql',xml_tag='update',xml_id='update_face_id')
       # print('sql---->',sql.format(mobile=mobile))
        data=MysqlHandle.delete_update_insert_mysql_data(sql.format(mobile=mobile,date=today))
        result = {'code': 200}
    except Exception  as e:
        pass
    return JsonResponse(result,status=200)









"""itufaceapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'v1/get/SearchResult', views.SearchResult),  # 查询结果
    url(r'v1/get/searchProductRequired', views.ProductIsRequired),  # 是否为必填项
    url(r'v1/get/changeIdNo', views.changeIdNo),  # 更改身份证号姓名
    url(r'v1/get/updateMXstatus', views.updateMXstatus),  # 更新魔蝎状态
    url(r'v1/get/deleteTokenLendRequestId', views.delete_token_return_lend_request_id),  # 删除token，返回lend_request_id
    url(r'v1/get/mobileEnable', views.mobile_enable), #
    url(r'v1/get/IdAndStatus', views.mobile_to_id_status) #查找id
]

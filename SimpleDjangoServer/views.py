from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import SimpleDjangoServer.data as JSON_DATA

ModelTypeCode = JSON_DATA.ModelTypeCodeList(self=None)
ModelTypeValue = JSON_DATA.ModelTypeValue(self=None)
LatestOrderList = JSON_DATA.LatestOrder(self=None)
HotestOrderList = JSON_DATA.HotestOrder(self=None)
Social = JSON_DATA.Social(self=None)
PhoneNumber = JSON_DATA.PhoneNumber(self=None)
Payment = JSON_DATA.Payment(self=None)
ModelTypeList = JSON_DATA.ModelTypeList(self=None)
ModelNameList = JSON_DATA.ModelNameList(self=None)
OrderData = JSON_DATA.OrderData(self=None)

class IndexPage(View):
    mytemplate = 'index.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social,
        'LatestOrderList' : LatestOrderList,
        'HotestOrderList' : HotestOrderList})
    def post(self, request):
        return HttpResponse(self.unsupported)

class AboutPage(View):
    mytemplate = 'about.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social})
    def post(self, request):
        return HttpResponse(self.unsupported)
class ContactPage(View):
    mytemplate = 'contact.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social})
    def post(self, request):
        return HttpResponse(self.unsupported)
class PaymentPage(View):
    mytemplate = 'payment.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social,
        'Payment' : Payment})
    def post(self, request):
        return HttpResponse(self.unsupported)
class UserTrackingPage(View):
    mytemplate = 'usertracking.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social})
    def post(self, request):
        return HttpResponse(self.unsupported)
class TrackingPage(View):
    mytemplate = 'tracking.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social})
    def post(self, request):
        return HttpResponse(self.unsupported)
class OrderCodeTrackingPage(View):
    mytemplate = 'codetracking.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social})
    def post(self, request):
        return HttpResponse(self.unsupported)
class GetOrderPage(View):
    mytemplate = 'getorder.html'
    unsupported = 'Unsupported operation'
    def get(self, request):
        return render(request, self.mytemplate,
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'Social' : Social})
    def post(self, request):
        return HttpResponse(self.unsupported)


def OrderModelType_DATA(request):
    ModelType = request.GET.get('ModelType', None)
    return render(request, 'order_modeltype.html',
        {'ModelTypeCode' : ModelTypeCode,
        'ModelTypeValue' : ModelTypeValue,
        'ModelTypeList' : ModelTypeList[ModelType],
        'ModelType' : ModelType,
        'Social' : Social,
        'ModelNameList': ModelNameList,
        'ModelTypeName' : ModelTypeValue[ModelType],
        'OrderData' : OrderData})
def OrderModelName_DATA(request):
    ModelName = request.GET.get('ModelName', None)
    ModelType = request.GET.get('ModelType', None)
    return render(request, 'order_modelname.html',
                  {'ModelName' : ModelName,
                   'Order' : OrderData,
                   'ModelNameValue' : ModelNameList[ModelName],
                   'ModelTypeCode' : ModelTypeCode,
                    'ModelTypeValue' : ModelTypeValue,
                    'ModelTypeList' : ModelTypeList[ModelType],
                    'ModelType' : ModelType,
                    'Social' : Social,
                    'ModelNameList': ModelNameList})
def SearchOrder(request):
    SearchData = request.GET.get('q', None)
    Order = {}
    if SearchData == '' or SearchData == None:
        Order = OrderData
    else:
        for tmp in OrderData:
            if OrderData[tmp]['OrderName'].find(SearchData) != -1:
                Order[tmp] = OrderData[tmp]
    if len(Order) == 0:
        return render(request, 'nofoudorder.html', {'resualt' : SearchData,
                                                     'ModelTypeCode' : ModelTypeCode,
                                                     'ModelTypeValue' : ModelTypeValue,
                                                     'Social' : Social,
                                                     'LatestOrderList' : LatestOrderList,
                                                     'HotestOrderList' : HotestOrderList})
    else:
        return render(request, 'ordersearch.html', {'q' : Order,
                                                    'resualt' : SearchData,
                                                    'ModelTypeCode' : ModelTypeCode,
                                                    'ModelTypeValue' : ModelTypeValue,
                                                    'Social' : Social})
def UserTracking_Page(request):
    username = request.POST.get('UserName', None)
    password = request.POST.get('Password', None)
    return render(request, 'user_login.html', {'username' : username,
                                               'password' : password, 
                                                'ModelTypeCode' : ModelTypeCode,
                                                'ModelTypeValue' : ModelTypeValue,
                                                'Social' : Social})
def CodeTracking_Page(request):
    code = request.GET.get('OrderCode', None)
    return render(request, 'codetracking_in.html', {'ordercode' : code,
                                                'ModelTypeCode' : ModelTypeCode,
                                                'ModelTypeValue' : ModelTypeValue,
                                                'Social' : Social})

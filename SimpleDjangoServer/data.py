
import json, urllib.request

def GetJSONDataFromURL(self, url):
    if url == None:
        return None
    else:
        try:
            JsonData = urllib.request.urlopen(url)
            JsonGetData = json.loads(JsonData.read().decode())
            return JsonGetData
        except ValueError:
            return None

def ModelTypeCodeList(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeValue.json')
    return Data
def ModelTypeValue(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeValue.json')
    return Data
def LatestOrder(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleLatestOrder.json')
    return Data
def HotestOrder(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleHotestOrder.json')
    return Data
def Social(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleSocial.json')
    return Data
def PhoneNumber(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimplePhoneNumber.json')
    return Data
def Payment(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimplePayment.json')
    return Data
def ModelTypeList(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeList.json')
    return Data
def ModelNameList(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelNameList.json')
    return Data
def OrderData(self):
    Data = GetJSONDataFromURL(self, 'https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleOrderName_Value.json')
    return Data
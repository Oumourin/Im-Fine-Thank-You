import requests
import random
from bs4 import BeautifulSoup
import json


# 填写获取到的cookies
# my_cookies = {'.ASPXFORMSAUTHYZY': 'D51E7C6AC416A3410F5442C605F87F161D159858C1DA470FBDC28E3DA1EAF697365AE6D8DCD088F04BCC1B5DFE1F7B85FC2C8081D8546C084A70855428A9F97271F4C82F13FAADC670F94CF584CBFAB819CBE1D66FAC9A217EC182165F3D85C2B42317E95DEC1402F76425BB19EBCA47',
#            'ASP.NET_SessionId': 'yn24ltfeit3mnouenlj5mttc',
#            '__RequestVerificationToken': '4NDTDEnw06-yPQOoAcZAa7Rk3AaJi7d-G1vupcwy8NN09fA7gDvr8JEJ8X0JQ9FrkZM52VG6XOAUEnCTHCZJ6T2kCW6h_Ly541cy-0epOy41'}

# 登录页面URL
get_url = "http://39.98.190.134:81/Report/Reported"

# 登录请求URL
sign_up_url = "http://39.98.190.134:81/Account/Login"

# 申请短信验证码URL
mobile_phone_code_url = "http://39.98.190.134:81/Account/GetLoginMobileCode"

# 提交日常数据URL
post_daily_data_url = "http://39.98.190.134:81/Report"

# 打卡结果获取URL
get_checkin_result_url = "http://39.98.190.134:81/Report/Success"

#伪造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# r = requests.get(get_url, headers=headers, cookies=my_cookies)

# 获取一个随机体温值
get_random = random.randint(355, 365)
get_my_temperature = get_random / 10.0
# my_daily_data = {"IsContactFever": "False",     # 这里开始
#                  "IsSymptoms": "",
#                  "IsSuspected": "",
#                  "IsConfirmed": "",
#                  "IsContactSuspected": "False",
#                  "IsContactConfirmed": "False",
#                  "IsContactEpidemic": "",
#                  "IsContactRisk": "False",      # 这里结束，参数应该所有人都是一样的 maybe
#                  "PersonnelTypeID": "6",        # 这里开始应该会每个人有差异
#                  "HolderID": "",
#                  "Holder": "",
#                  "province1": "50",
#                  "city1": "5001",
#                  "district1": "500117",
#                  "PositionID": "9",
#                  "province2": "50",
#                  "city2": "5001",
#                  "district2": "500117",
#                  "Temperature": str(get_my_temperature),
#                  "PhysicalConditionID": "1",
#                  "iscontactfever": "false",
#                  "iscontactsuspected": "false",
#                  "iscontactconfirmed": "false",
#                  "iscontactrisk": "false",
#                  "ReturnTime1": "",
#                  "province5": "000000",
#                  "city5": "000000",
#                  "district5": "000000",
#                  "ReturnTool": "自驾",
#                  "ReturnToolRemark": "",
#                  "ReturnRemark": "",
#                  "ReturnTime2": "",
#                  "Station": "其他",
#                  "Remarks": ""
#                  }

# Json解析
with open("config.json", 'r', encoding='utf-8') as f:
    config_data = json.load(f)
my_cookies = config_data['cookies']
my_daily_data = config_data['data']
my_daily_data['Temperature'] = str(get_my_temperature)

# 获取连接
request = requests.request('GET', get_url, cookies=my_cookies, headers=headers)

# 提交数据
post = requests.request('POST', post_daily_data_url, data=my_daily_data, cookies=my_cookies)



# 获取结果
result_request = requests.request('GET', get_checkin_result_url, cookies=my_cookies, headers=headers)
soup = BeautifulSoup(result_request.content, 'lxml')
result_string = soup.find('h2').text
if result_string == '打卡成功':
    print('Im Fine Fuck You NUC')
else:
    print('Check-in failed')

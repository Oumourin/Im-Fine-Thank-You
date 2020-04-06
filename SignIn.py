import requests


# 填写获取到的cookies
my_cookies = {'.ASPXFORMSAUTHYZY': 'D51E7C6AC416A3410F5442C605F87F161D159858C1DA470FBDC28E3DA1EAF697365AE6D8DCD088F04BCC1B5DFE1F7B85FC2C8081D8546C084A70855428A9F97271F4C82F13FAADC670F94CF584CBFAB819CBE1D66FAC9A217EC182165F3D85C2B42317E95DEC1402F76425BB19EBCA47',
           'ASP.NET_SessionId': 'yn24ltfeit3mnouenlj5mttc',
           '__RequestVerificationToken': '4NDTDEnw06-yPQOoAcZAa7Rk3AaJi7d-G1vupcwy8NN09fA7gDvr8JEJ8X0JQ9FrkZM52VG6XOAUEnCTHCZJ6T2kCW6h_Ly541cy-0epOy41'}

# 登录页面URL
get_url = "http://39.98.190.134:81/Report/Reported"

# 登录请求URL
sign_up_url = "http://39.98.190.134:81/Account/Login"

# 申请短信验证码URL
mobile_phone_code_url = "http://39.98.190.134:81/Account/GetLoginMobileCode"

# 提交日常数据URL
post_daily_data_url = "http://39.98.190.134:81/Report"

# 伪造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 57.0.2987.133Safari / 537.36"
}

r = requests.get(get_url, headers=headers, cookies=my_cookies)
print(r.status_code)
print(r.text)

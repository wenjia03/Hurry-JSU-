from json import encoder
import requests , urllib.parse , json ,yagmail,os,time
#用于开源设置
name = "考生姓名"#考生姓名
CID = "身份证号"#考生身份证号
exammeeID = "考生号"#考生高考考生号（可以在潇湘高考等平台查询）
def pause():
    os.system("pause")

def sendEMSID(EMS):
    SendEmailID = "发信邮箱账号"#发信邮件账号
    SendEmailPassword = "发信邮箱密码或者授权码"#发信邮件密码
    SMTPHost = "发信SMTP服务器"#发信邮件SMTP服务器地址（这个为腾讯企业邮的地址）
    ReciveNoticeEmail = '收信邮箱地址'#收信人地址
    Sentservice = yagmail.SMTP( user=SendEmailID, password=SendEmailPassword, host=SMTPHost)
    contents = ['WatchDog已经检测到EMS状态更新',"时间：" + str(time.asctime( time.localtime(time.time()) )) + 'EMS单据号：' + str(EMS), '看门狗已经退出']
    Sentservice.send(ReciveNoticeEmail, 'EMS单据号：' + str(EMS), contents)

print("吉首大学，你办事快点！ 版本号 1.0.0 WenjiaChen")
i = 1
while True:
    print("Watchdog Running……")
    print("正在监听端口，第 " + str(i) + " 次,共计经历" + str(i* 45)+"秒")
    response = {}
    url = "http://jsuzs.jysd.com/admit/admit"
    payload='name='+ str(urllib.parse.quote(name)) +'&sfzh='+ CID +'&zkzh=' + exammeeID
    headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PHPSESSID2=3if35cn9v2j5pdfg7m71ur66s1'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.loads(response.text)
    EMS = result["ems"]
    lens = len(EMS)
    if lens > 0 :
        print(EMS)
        print("已经在吉首大学官网查询到EMS运单号信息，已经送信到邮箱")
        sendEMSID(int(EMS))
        pause()
        break
    else:
        print("未找到EMS运单号信息。")
        print('吉大招办搞快点，招生也是你们最慢同志……')
        time.sleep(45)
        i = i + 1
    
        
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import configparser

config = configparser.ConfigParser()
config.read("config.ini",encoding='UTF8')

user_agent = config.get("app","UserAgent")
cookie = config.get("app","Cookie")
user = config.get("app","User")
print(user_agent)
print(cookie)
print(user)

def sign_in1():
    url= 'https://h5.ele.me/restapi/member/v2/users/'+ user +'/sign_in/daily/prize'
    data = 'channel=app&index=1'
    header = {'User-Agent':user_agent,
              'Cookie':cookie,
              'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post(url=url,data=data,headers=header)
    print(res.text)

def hongbao():
    url1 = 'https://h5.ele.me/restapi/member/v1/users/'+ user +'/sign_in/limit/hongbao'
    data = {'channel':'app'}
    header = {'User-Agent': user_agent,
              'Cookie': cookie,
              'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post(url=url1,data=data,headers=header)
    print(datetime.datetime.now().strftime('%m-%d %H:%M:%S.%f')+res.text)

def sign_in():
    url = 'https://h5.ele.me/restapi/member/v1/users/'+ user +'/sign_in'
    data = 'channel=app&captcha_code=&captcha_hash=&source=main'
    header = {'User-Agent': user_agent,
              'Cookie': cookie,
              'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post(url=url, data=data, headers=header)
    print(res.text)
    sign_in1()

if __name__=='__main__':
    sched = BlockingScheduler()
    sched.add_job(sign_in,'cron',hour='8')
    sched.add_job(hongbao, 'cron', hour='10,14,17,20', minute='0', second='0')
    sched.start()

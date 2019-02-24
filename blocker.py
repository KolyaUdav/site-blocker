import time
from datetime import datetime as dt


host_file = 'hosts'

redirect = '127.0.0.1'

website_list = ['vk.com', 'mail.ru']


def blocker_process():
    while True:
        ymd = (dt.now().year, dt.now().month, dt.now().day)
        if dt(*ymd, 8) < dt.now() < dt(*ymd, 16):
            print('Rihanna')
            when_work()
        else:
            print('Drake')
            when_chill()
        time.sleep(5)


def when_work():
    file = open(host_file, '+r')
    content = file.read()
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect + ' ' + website + '\n')


def when_chill():
    file = open(host_file, '+r')
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
        file.truncate()


blocker_process()

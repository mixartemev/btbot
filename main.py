import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


def get_list() -> (float, list):
    d: list = requests.get('https://api-v2.bit.team/api/v2/anunt/get?type=sell').json()['data']
    d: list = list(filter(lambda e: e['coin'] == 'pzm' and e['currency'] == 'rub', d))
    d: list = sorted(d, key=lambda e: e['price_advert'])[:5]
    best = d[0]['price_advert']
    return best, d


def links() -> str:
    lst = get_list()
    link = '<h1>{} RUR</h1><br>'.format(lst[0])
    for e in lst[1]:
        link += '{} ({}-{}) <a href="https://bit.team/buy/advert/{}">{}:{}</a> {}min<br>'.format(
            e['price_advert'],
            e['limit_min'],
            e['limit_max'],
            e['advert_link_id'],
            e['user']['username'],
            e['user']['rating_user'],
            e['user']['isOnlineMin']
        )
    return link


if __name__ == '__main__':
    from_adr = 'BT Bot <{}>'.format(os.getenv('SMTP_FROM'))
    to_adr = 'BT Client <{}>'.format(os.getenv('STMP_TO'))
    message = """From: %s 
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: BT Rate

%s
""" % (from_adr, to_adr, links())
    message = message.encode("ascii", errors="ignore")
    try:
        with smtplib.SMTP(os.getenv('SMTP_HOST'), os.getenv('SMTP_PORT')) as server:
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PWD'))
            server.sendmail(from_adr, to_adr, message)
            print('Successfully sent email')
    except smtplib.SMTPException:
        print('Error: unable to send email')

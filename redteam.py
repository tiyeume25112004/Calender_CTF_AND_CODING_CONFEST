import requests
import json
import datetime

url = 'https://clist.by/get/events/'

headers = {
    'Host': 'clist.by',
    'Cookie': 'csrftoken=UBvdcQvjO9qHImwrGosGl9tqG2nD0mioJNShQUF9ULhD20G6PpPRhSVeEzYAlBAd;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'X-Csrftoken': 'UBvdcQvjO9qHImwrGosGl9tqG2nD0mioJNShQUF9ULhD20G6PpPRhSVeEzYAlBAd',
    'Referer': 'https://clist.by'
}

end_date = datetime.date.today() + datetime.timedelta(days=1)

data = {
    'start': datetime.date.today(),
    'end': end_date.strftime('%Y-%m-%d'),
    'categories': 'calendar',
    'search_query': '',
    'status': ''
}

r = requests.post(url, headers=headers, data=data)

if r.status_code == 200:
    events = json.loads(r.text)
    for repo in events:
        print(f"""
        --------------------------
        title:{repo['title']}
        url:{repo['url']}
        host:{repo['host']} 
        start:{repo['start']} 
        end:{repo['end']}
        --------------------------  """)
else:
    print('Failed to retrieve events. Status code:', r.status_code)

# import requests
# url="http://clist.by/get/events/"
# cookies={
#     "csrftoken":"UBvdcQvjO9qHImwrGosGl9tqG2nD0mioJNShQUF9ULhD20G6PpPRhSVeEzYAlBAd"
# }
# data={
#     "categories":"calendar"
# }
# headers={
#     "x-csrftoken":"UBvdcQvjO9qHImwrGosGl9tqG2nD0mioJNShQUF9ULhD20G6PpPRhSVeEzYAlBAd",
#     "Referer": url
# }
# r=requests.post(url,cookies=cookies,data=data,headers=headers)
# print(r.status_code)
import requests
import json
import datetime
from datetime import date
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

data = {
    'start': datetime.date.today(),
    'end': f'2023-{date.today().month}-{date.today().day+1}',
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
        # print(f'{repo["title"]}: {repo["host"]: {repo["start"]}: {repo["end"]}: {repo["url"]}: }')
    # Process the retrieved events as needed
    # print(events)
else:
    print('Failed to retrieve events. Status code:', r.status_code)
# Lưu ý, nó không hoàn thiện và sẽ xảy ra lỗi gần cuối tháng nên nếu ai đó muốn dùng thì tự hoàn thiện nha

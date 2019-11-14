import requests

url = 'http://localhost:12000/hello.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    with open('answer.html', 'w') as f:
        f.write(r.text)
except requests.HTTPError:
    print('Error')

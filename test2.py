import requests

url = 'https://www.google.co.jp/search'

# グーグルへ接続
req = requests.get(url, params={'q': 'パイソン'})

# アドレス取得
req.url
#[結果] 'https://www.google.co.jp/search?q=%E3%83%91%E3%82%A4%E3%82%BD%E3%83%B3'

# 検索結果取得
#print(req.text)
#[結果] <!doctype html><html itemscope="" 以下省略

path="ans.html"
with open(path, mode='w') as f:
    f.write(req.text)

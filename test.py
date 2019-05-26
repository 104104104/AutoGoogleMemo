import MeCab
import requests
import random

url = 'https://www.google.co.jp/search'

text = '''
文章のノリが完全に「銀河ヒッチハイクガイド」
- むしろあれより悪ふざけはひどいかも

NoUIの作法その1
- いつもの手順を考えること
	- 車の鍵を開けるたびに、スマホを取り出して鍵を開ける？ 馬鹿馬鹿しい、勝手に鍵が空けばそれでサイコーじゃないか

NoUIの作法その2
- テクノロジーを活用し、僕らに使いこなされるシステムを作ろう
	- メールの通知とか、全部潰してアイコンの左上の数字を消したければ、結構な「デジタル雑用」をしいられる
	- パスワード考え/パスワード覚え とか、ひどいデジタル雑用だ…
	- どうすればいいの？
		-  ラグビーで頭をぶつけすぎて病気になる… → ヘルメットにセンサーを付けてあとは勝手に情報収集してくれる
		-  タイヤの空気圧が低すぎるせいで、ガソリンが無駄になってる…
			- 政府「点検して」と呼びかけ
				- しかし効果薄…
			- Goodyearという会社が、走ってるだけで空気圧が高くなるタイヤを作った(!)
			- 旅行会社のアプリ
				- メールを向こうに送ると、勝手にGoogleカレンダーに登録してくれたりする
	- 忘れっぽい人類がやるべき雑用を、コンピュータに押し付けられるようにしたいものだ
	- 選ぶってのは、なかなかの負担になるものらしい
	- “You’ve got a mail”の時代は、コンピュータが人間に与える「雑用」は無害で可愛らしいものだったのに…


NoUIの作法その3
- ひとりひとりに合わせる
'''
tagger = MeCab.Tagger()
parse = tagger.parse(text)

words = []
lines = parse.split('\n')
import re
for line in lines:
    items = re.split('[\t,]',line)
    if len(items) >= 2 and items[1] == '助詞':
        continue
    if len(items) >= 2 and items[1] == '助動詞':
        continue
    if len(items) >= 2 and items[1] == '記号':
        continue
    words.append(items[0])

# counting
words2 = {}
for word in words:
    words2[word] = words2.get(word, 0) + 1

# sort by count
d = [(v,k) for k,v in words2.items()]
d.sort()
d.reverse()
ans_temp=[]
for count, word in d[:20]:
    ans_temp.append(word)



#if len(words)>=20:
#    words=random.sample(words, k=20)

ans=' '.join(ans_temp)

req = requests.get(url, params={'q': ans})

# アドレス取得
req.url

path="ans.html"
with open(path, mode='w') as f:
    f.write(req.text)

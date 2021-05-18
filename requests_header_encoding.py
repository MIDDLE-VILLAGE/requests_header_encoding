# ライブラリをインポートして利用可能にする
import sys
import requests

# 第一引数からURLを取得する
url = sys.argv[1]

# urlで指定したWebページを取得する
r = requests.get(url)

# エンコーディングを標準エラー出力に出力する。
print(f'encoding: {r.encoding}', file=sys.stderr)

# デコードしたレスポンスボディを標準出力に出力する
print(r.text)

# このファイルをrequests_header_encoding.pyという名前のファイル名に保存して以下のようにターミナルで実行するとHTTPヘッダーから得られたエンコーディングとデコードされたレスポンスボディが出力されます
# $ python requests_header_encoding.py https://gihyo.jp/dp

# 以下を入力すると、出力されたレスポンスボディを保存できる
# $ python requests_header_encoding.py https://gihyo.jp/dp > dp.html

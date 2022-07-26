from flask import Flask
from flask import jsonify
import asyncio
import json
import requests

app = Flask(__name__)

@app.route('/')
async def hello_world():
   base_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
   url_oc = "https://www.nseindia.com/option-chain"
   headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) '
                            'Chrome/80.0.3987.149 Safari/537.36',
              'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
   session = requests.Session()
   await request = session.get(url_oc, headers=headers, timeout=5)
   cookies = dict(request.cookies)
   await response = session.get(base_url, headers=headers, timeout=5, cookies=cookies)
   print(response.status_code)
   if response.status_code == 200:
      data = response.content
      res = json.loads(data)
      #print(type(res))
      return jsonify(result=res)
   return jsonify(result={"status_code":response.status_code})

async def main():
   app.config.update(
   PROPAGATE_EXCEPTIONS=True
   )
   await app.run(debug=True)
   app.logger.addHandler(logging.StreamHandler(sys.stdout))
   app.logger.setLevel(logging.ERROR)

if __name__== '__main__':
   asyncio.run(main())

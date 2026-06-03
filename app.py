import os
from flask import Flask, render_template, request

app = Flask(__name__)

# 🚗 這裡一定要放小米汽車的資料，否則網頁會報錯
cars = {
    "su7_standard": {
        "name": "小米 SU7 標準版",
        "price": "21.59 萬人民幣",
        "range": "700 km",
        "power": "299 馬力"
    },
    "su7_pro": {
        "name": "小米 SU7 Pro",
        "price": "24.59 萬人民幣",
        "range": "830 km",
        "power": "299 馬力"
    },
    "su7_max": {
        "name": "小米 SU7 Max",
        "price": "29.99 萬人民幣",
        "range": "800 km",
        "power": "673 馬力"
    }
}

@app.route('/')
def index():
    # 將 cars 資料傳給網頁
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

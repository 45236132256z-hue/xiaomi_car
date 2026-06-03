import os
from flask import Flask, render_template, request

app = Flask(__name__)

# 🚗 小米汽車「智駕 / 頂級 / 概念車」科技對比資料庫 (完全對應 index.html 欄位)
cars = {
    "su7_standard": {
        "name": "小米 SU7 標準版",
        "type": "智駕主力車款",
        "price": "21.59 萬人民幣",
        "acceleration": "5.28 秒",
        "top_speed": "210 km/h",
        "battery": "700 km (CLTC)",
        "smart_drive": "Xiaomi Pilot Pro",
        "hardware": "1x NVIDIA Orin-N, 11x 鏡頭, 12x 超聲波雷達",
        "navigation": "全車型基本導航、智慧泊車輔助"
    },
    "su7_max": {
        "name": "小米 SU7 Max",
        "type": "頂級性能旗艦",
        "price": "29.99 萬人民幣",
        "acceleration": "2.78 秒",
        "top_speed": "265 km/h",
        "battery": "800 km (CLTC)",
        "smart_drive": "Xiaomi Pilot Max",
        "hardware": "2x NVIDIA Orin-X, 1x 鐳射雷達, 高清鏡頭毫米波雷達",
        "navigation": "城市 NOA 領航輔助、高速領航輔助、代客泊車"
    },
    "su7_ultra_concept": {
        "name": "小米 SU7 Ultra 概念車",
        "type": "賽道巔峰概念",
        "price": "非賣品 / 賽道專用",
        "acceleration": "1.97 秒",
        "top_speed": "350+ km/h",
        "battery": "賽道高功率電池包",
        "smart_drive": "賽道級客製化智駕系統",
        "hardware": "全車極致輕量化、賽道專屬熱管理與感測器",
        "navigation": "紐北賽道專屬地圖導航、極限駕控分析"
    }
}

# 1. 首頁路由（一開始進入時，尚未選擇車款）
@app.route('/')
def index():
    return render_template('index.html', cars=cars, car1=None, car2=None)

# 2. 對比路由（按下「開始對比 Tech Radar」按鈕後觸發）
@app.route('/compare', methods=['POST'])
def compare():
    car1_id = request.form.get('car1')
    car2_id = request.form.get('car2')
    
    # 根據使用者選的 ID 撈出對應的汽車資料
    car1_data = cars.get(car1_id)
    car2_data = cars.get(car2_id)
    
    return render_template('index.html', cars=cars, car1=car1_data, car2=car2_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

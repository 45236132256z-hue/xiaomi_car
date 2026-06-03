import os
from flask import Flask, render_template, request

app = Flask(__name__)

# 🚗 修正後的完整資料庫，欄位名稱完全對應你的 HTML 表格
cars = {
    "su7_standard": {
        "name": "小米 SU7 標準版",
        "price": "21.59 萬人民幣",
        "type": "純電動轎車",
        "acceleration": "5.28 秒",
        "top_speed": "210 km/h",
        "battery": "700 km",
        "smart_drive": "Xiaomi Pilot Pro",
        "hardware": "NVIDIA Orin-N",
        "navigation": "基礎智慧導航",
        "engine": "單電機後驅 (V6 內置)",
        "horsepower": "299 匹馬力",
        "fuel_consumption": "純電驅動 (0 耗油)"
    },
    "su7_max": {
        "name": "小米 SU7 Max",
        "price": "29.99 萬人民幣",
        "type": "純電性能旗艦",
        "acceleration": "2.78 秒",
        "top_speed": "265 km/h",
        "battery": "800 km",
        "smart_drive": "Xiaomi Pilot Max",
        "hardware": "雙 NVIDIA Orin-X + 光達",
        "navigation": "城市 NOA 領航",
        "engine": "雙電機四驅 (V6s + V6)",
        "horsepower": "673 匹馬力",
        "fuel_consumption": "純電驅動 (0 耗油)"
    },
    "su7_ultra_concept": {
        "name": "小米 SU7 Ultra 概念車",
        "price": "非賣品 / 賽道專用",
        "type": "賽道巔峰概念車",
        "acceleration": "1.97 秒",
        "top_speed": "350+ km/h",
        "battery": "賽道高功率電池",
        "smart_drive": "賽道級智駕系統",
        "hardware": "全車賽道感測器",
        "navigation": "紐北專屬地圖",
        "engine": "三電機四驅 (2x V8s + 1x V6s)",
        "horsepower": "1548 匹馬力",
        "fuel_consumption": "純電賽道配置 (0 耗油)"
    }
}

@app.route('/')
def index():
    return render_template('index.html', cars=cars, car1=None, car2=None)

@app.route('/compare', methods=['POST'])
def compare():
    car1_id = request.form.get('car1')
    car2_id = request.form.get('car2')
    
    car1_data = cars.get(car1_id)
    car2_data = cars.get(car2_id)
    
    return render_template('index.html', cars=cars, car1=car1_data, car2=car2_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

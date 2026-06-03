import os

if __name__ == '__main__':
    # 讓程式自動讀取雲端環境指定的 Port，若在本機則預設為 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
import os
from flask import Flask, render_template, request # 確保有匯入

app = Flask(__name__)

# ====== 這裡放你原本寫好的所有網頁路由與邏輯 (例如之前的對比功能) ======
@app.route('/')
def index():
    return render_template('index.html')

# =============================================================

# 最底下保持我們剛剛改好的這段動態 PORT 設定
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

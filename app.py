import os
from flask import Flask, render_template, request

app = Flask(__name__)

# ====== 這裡放你原本寫好的所有網頁路由與邏輯 ======
@app.route('/')
def index():
    return render_template('index.html')
# =============================================================

# 最底下保持這段動態 PORT 設定即可
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
@app.route('/')
def index():
    return render_template('index.html')
# =============================================================

# 最底下保持這段動態 PORT 設定即可
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

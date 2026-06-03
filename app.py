import os

if __name__ == '__main__':
    # 讓程式自動讀取雲端環境指定的 Port，若在本機則預設為 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

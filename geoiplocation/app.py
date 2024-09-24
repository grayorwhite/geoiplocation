from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 기본 페이지 제공
@app.route('/')
def index():
    return render_template('index.html')

# 위치 정보 수신
@app.route('/location', methods=['POST'])
def location():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']
    print(f"Received location: Latitude = {latitude}, Longitude = {longitude}")
    
    # 필요한 작업 (예: DB 저장, 로그 기록) 수행 가능
    return jsonify({"status": "Location received"})

if __name__ == "__main__":
    app.run(debug=True)

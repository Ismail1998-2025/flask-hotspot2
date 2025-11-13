from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/auth', methods=['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "admin" and password == "1234":
        return jsonify({"status": "success", "message": "تم تسجيل الدخول بنجاح ✅"})
    else:
        return jsonify({"status": "error", "message": "بيانات غير صحيحة ❌"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

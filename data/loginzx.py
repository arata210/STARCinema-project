from flask import Flask, request, jsonify
import redis
import random

app = Flask(__name__)
redis_client = redis.StrictRedis(host='192.168.88.130', port=6379, password='123456', db=0)


@app.route('/send_verification_code', methods=['POST'])
def send_verification_code():
    # 从请求中获取手机号
    phone = request.form.get('phone')

    if not phone:
        return jsonify({'error': 'Phone number is required'}), 400

    # 生成随机验证码
    verification_code = str(random.randint(1000, 9999))

    # 存储验证码到 Redis Hash
    redis_client.hset('user_verification_codes', phone, verification_code)

    return jsonify({'message': 'Verification code sent successfully'})


@app.route('/verify_code', methods=['POST'])
def verify_code():
    # 从请求中获取手机号和用户输入的验证码
    phone = request.form.get('phone')
    user_input_code = request.form.get('code')

    if not phone or not user_input_code:
        return jsonify({'error': 'Phone number and verification code are required'}), 400

    # 从 Redis Hash 中获取存储的验证码
    stored_code = redis_client.hget('user_verification_codes', phone)

    if stored_code and user_input_code == stored_code.decode('utf-8'):
        return jsonify({'message': 'Verification code is correct'})
    else:
        return jsonify({'error': 'Invalid verification code'}), 400


if __name__ == '__main__':
    app.run(debug=True)

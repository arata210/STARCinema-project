from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取 POST 请求中的表单数据
        input_text = request.form.get('input_text')
        return f'You entered: {input_text}'
    else:
        return render_template('loginzx.html')


if __name__ == '__main__':
    app.run(debug=True)

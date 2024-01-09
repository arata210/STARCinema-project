from flask import Flask, render_template
from create_coupon import Get_all_info
from film import findAll
from film_info import find_film
from douban_rating_nums import douban_rating_num

app = Flask(__name__)


@app.route('/')
def index():
    # 示例数据
    a = find_film()[2]
    b = douban_rating_num(a[0])
    print(a)
    return render_template("index.html", data=a, data2=b)


if __name__ == '__main__':
    app.run(debug=True)

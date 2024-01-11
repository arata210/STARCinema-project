from flask import Flask, render_template, request

# from create_coupon import Get_all_info
from index_page import find_films_info, update_films_rating_num, find_films_intro, make_html_li
from info_page import find_film_info_byid, find_film_intro_byid
from session_page import find_film_session_byMovieId, find_film_cover_byid, make_html_li_2
from order_page import find_film_session_byOrderId, find_order_byid, find_pay_amount_byid

# 设置静态元素存放路径和名字
app = Flask(__name__, static_url_path='/static', static_folder='static')


# 启动前更新电影评分
# update_films_rating_num()


@app.route('/')
def index():
    """
    星光影院(STARCinema)首页
    :return: html格式的电影数据
    功能扩充：电影状态 - 1 上映中
                - -1 结束放映
                - 0 即将上映
    """
    # 获取电影基本信息
    films_info = find_films_info()
    # 获取电影图片信息
    films_cover = find_films_intro()
    # 双重循环 制作显示的信息
    film_index = str()
    for i in range(len(films_info)):
        for j in range(len(films_cover)):
            if films_info[i][0] == films_cover[j]['movie_id']:
                film_index = film_index + (
                    make_html_li(films_cover[j]['movie_cover'], films_info[i][0], films_info[i][1], films_info[i][5],
                                 films_info[i][-2], films_info[i][-1]))
    # 发送数据
    return render_template("index.html", data=film_index)


@app.route('/info.html', methods=['GET'])
def info():
    """
    单个电影信息页
    :return: 电影数据
    """
    # 接收movie_id
    the_movie_id = request.args.get('movie_id')
    # 获取MySQL数据
    film_info = find_film_info_byid(the_movie_id)[0]
    title = film_info[1]
    release = film_info[2]
    country = film_info[3]
    movie_length = film_info[4]
    director = film_info[5]
    genre = film_info[6]
    actor = film_info[7]
    rating_num = film_info[8]
    # 获取MongoDB数据
    film_intro = find_film_intro_byid(the_movie_id)
    movie_intro = film_intro['movie_intro']
    movie_cover = film_intro['movie_cover']
    # 发送数据
    return render_template('info.html', title=title, release=release, country=country,
                           movie_length=movie_length, director=director, genre=genre,
                           actor=actor, rating_num=rating_num, movie_intro=movie_intro,
                           movie_cover=movie_cover, movie_id=the_movie_id)


@app.route('/session.html', methods=['GET'])
def session():
    the_movie_id = request.args.get('movie_id')
    cover = find_film_cover_byid(the_movie_id)
    film_info = find_film_info_byid(the_movie_id)[0]
    title = film_info[1]
    rating = film_info[-1]
    film_sessions = find_film_session_byMovieId(the_movie_id)
    sessions = str()
    if len(film_sessions) == 0:
        return render_template('session.html', sessions='<li><div class="s-middle"><p>暂无排片</p></div></li>',
                               cover=cover, title=title, rating=rating)
    for i in range(len(film_sessions)):
        sessions = sessions + (make_html_li_2(film_sessions[i]['start_time'], film_sessions[i]['finish_time'],
                                              film_sessions[i]['language'], film_sessions[i]['type'],
                                              film_sessions[i]['hall'], film_sessions[i]['price'],
                                              str(film_sessions[i]['_id']), str(film_sessions[i]['movie_id'])))

    return render_template('session.html', sessions=sessions, cover=cover, title=title, rating=rating)


@app.route('/login.html', methods=['GET'])
def login():
    data = '1'
    return render_template('login.html', data=data)


@app.route('/ticket.html', methods=['GET'])
def ticket():
    data = '1'
    the_movie_id = request.args.get('movie_id')
    the_session = request.args.get('session')
    the_phone = request.args.get('phone')

    film_info = find_film_info_byid(the_movie_id)[0]

    return render_template('ticket.html', data=data)


@app.route('/order.html', methods=['GET'])
def order():
    the_order_id = request.args.get('order_id')
    order_info = find_order_byid(the_order_id)[0]
    phone = order_info[1][: 3] + '*' * 4 + order_info[1][-4:]
    actual_price = f"{order_info[3]}"
    count = order_info[4]
    seat_1 = order_info[5][0]
    seat_2 = order_info[5][1]
    pay_time = order_info[6].strftime("%Y-%m-%d %H:%M:%S")
    payment = order_info[7]
    code = order_info[8]
    pay_info = find_pay_amount_byid(the_order_id)[0]
    coupon = f"{pay_info[1]}"
    parameter = f"{pay_info[2]}"
    session_id = order_info[2]
    sessions = find_film_session_byOrderId(session_id)
    date = sessions['date']
    start_time = sessions['start_time']
    language = sessions['language']
    movie_type = sessions['type']
    price = sessions['price']
    finish_time = sessions['finish_time']
    hall = sessions['hall']
    movie_id = sessions['movie_id']
    cover = find_film_cover_byid(movie_id)
    title = find_film_info_byid(movie_id)[0][1]

    return render_template('order.html', the_order_id=the_order_id, date=date, start_time=start_time, language=language,
                           movie_type=movie_type, price=price,
                           finish_time=finish_time, hall=hall, cover=cover, title=title, phone=phone, actual_price=actual_price,
                           seat_1=seat_1,
                           seat_2=seat_2, pay_time=pay_time, payment=payment, code=code, coupon=coupon,
                           parameter=parameter, count=count)


if __name__ == '__main__':
    app.run(debug=True)

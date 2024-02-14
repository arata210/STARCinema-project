多源数据库项目大作业——星光影城（Readme暂未完全写完）

使用Python+Flask与MySQL、MongoDB、Redis等多源数据库的电影院在线购票网站系统

配置
Windows 10系统：
Python 3.11
Mysql 8.0
Pycharm（可选）
Linux系统：
CentOS 7 64 位（VMware Workstation Pro与Xshell）
MongoDB最新版
Redis最新版
Python：
flask、pymongo、redis、mysql-connector、beautifulsoup4、requests

功能
影院排片
影片信息
上映日程
用户手机登录
获取验证码
自动选座生产订单
订单详情
订单查询
爬取豆瓣评分
周边地理位置
网页框架自动化生成

使用
MySQL中导入film.sql，MongoDB中导入CinemaDB.films.json、CinemaDB.session35725869.json，Redis优惠券信息需要提前运行单独运行ticket_page.py的create_coupon方法。
Pycharm运行flask_test.py即可。




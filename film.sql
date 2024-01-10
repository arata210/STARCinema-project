-- 清空数据库
drop database cinema;

-- 创建cinema数据库
CREATE DATABASE cinema
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 使用数据库
use cinema;

-- 创建电影表 film
CREATE TABLE film (
    movie_id CHAR(10) PRIMARY KEY, -- 电影id
    title VARCHAR(255), -- 标题
    release_date CHAR(10), -- 上映时间
    country VARCHAR(255), -- 国家/地区
    length INT, -- 时长
    director VARCHAR(255), -- 导演
    genre VARCHAR(100), -- 类型
    actor VARCHAR(255), -- 主要演员
    rating_num CHAR(10) -- 评分
);

-- 初始化电影表
INSERT INTO film (movie_id, title, release_date, country, length, director, genre, actor, rating_num)
VALUES 
('35725869', '年会不能停！', '2023-12-29', '中国大陆', 117, '董润年', '剧情 / 喜剧', '大鹏 / 白客 / 庄达菲 / 王迅', '8.2'),
('35074609', '金手指', '2023-12-30', '中国香港 / 中国大陆', 125, '庄文强', '剧情 / 犯罪', '梁朝伟 / 刘德华 / 蔡卓妍 / 任达华', '6.4'),
('35927496', '潜行', '2023-12-29', '中国大陆 / 中国香港', 114, '关智耀', '剧情 / 动作 / 犯罪', '刘德华 / 林家栋 / 彭于晏 / 刘雅瑟', '5.9'),
('35768712', '一闪一闪亮星星', '2023-12-30', '中国大陆', 107, '陈小明 / 章攀', '爱情 / 奇幻', '屈楚萧 / 张佳宁 / 傅菁 / 蒋昀霖', '6.1'),
('35312439', '回西藏', '2024-01-11', '中国大陆', 109, '陈国星 / 拉华加', '剧情', '宋洋 / 金巴 / 陶海 / 索朗旺姆', '暂无评分');

-- 创建过渡表 amount（订单和优惠两张表的过渡）
CREATE TABLE amount (
    order_id CHAR(20) NOT NULL, -- 订单id
    actual_price DECIMAL(6,2) NOT NULL, -- 实际支付金额
    PRIMARY KEY (order_id, actual_price)
);

-- 创建订单表 ticket_order
CREATE TABLE ticket_order (
    order_id CHAR(20) NOT NULL, -- 订单id
    uid CHAR(10), -- 用户id
    session_id CHAR(20), -- 场次id
    actual_price DECIMAL(6,2), -- 实际支付金额
    count INT, -- 数量
    seat CHAR(20), -- 座位
    datetime DATETIME, -- 支付时间
    payment CHAR(20), -- 支付方式
    PRIMARY KEY (order_id)
);

-- 创建用户表 user
CREATE TABLE user (
    uid CHAR(10) NOT NULL, -- 用户id
    pid CHAR(15), -- 参数id
    name VARCHAR(20), -- 用户名
    phone CHAR(11), -- 用户手机号
    type CHAR(6), -- 用户类型
    balance DECIMAL(6,2), -- 用户余额
    status BOOL, -- 用户状态
    PRIMARY KEY (uid)
);

-- 创建参数表 parameter
CREATE TABLE parameter (
    pid CHAR(15) NOT NULL, -- 参数id
    pname CHAR(20), -- 参数名
    pvalue FLOAT(10), -- 折扣数
    PRIMARY KEY (pid)
);

-- 创建金额记录表 pay_amount
CREATE TABLE pay_amount (
    original_price DECIMAL(6,2), -- 原始价格
    coupon_amount DECIMAL(6,2), -- 优惠券价格
    parameter_amount DECIMAL(6,2), -- 影城卡价格
    total_discount_amount DECIMAL(6,2), -- 总优惠价
    actual_price DECIMAL(6,2) NOT NULL, -- 实际支付金额
    order_id CHAR(20), -- 订单id
    PRIMARY KEY (actual_price)
);

-- 创建外键约束
ALTER TABLE amount ADD CONSTRAINT FK_order_1 FOREIGN KEY (order_id)
      REFERENCES ticket_order (order_id);

ALTER TABLE amount ADD CONSTRAINT FK_price_2 FOREIGN KEY (actual_price)
      REFERENCES pay_amount (actual_price);

ALTER TABLE ticket_order ADD CONSTRAINT FK_have FOREIGN KEY (uid)
      REFERENCES user (uid);

ALTER TABLE user ADD CONSTRAINT FK_benefit FOREIGN KEY (pid)
      REFERENCES parameter(pid);

-- 初始化参数表 parameter
INSERT INTO parameter (pid, pname, pvalue)
VALUES
  ('P001', '月费卡', -5),
  ('P002', '储值卡', 0.8);

-- 初始化用户表 user
INSERT INTO user (uid, pid, name, phone, type, balance, status)
VALUES
    ('1001', NULL, '小明', '13812345678', '普通会员', 0, true),
    ('1002', 'P001', '小红', '13987654321', 'VIP会员', 0, true),
    ('1003', 'P002', '小王', '18788886666', 'VIP会员', 176, true);

-- 初始化订单表 ticket_order
INSERT INTO ticket_order (order_id, uid, actual_price, session_id, count, seat, datetime, payment)
VALUES
('S0123', '1001', 29, '35725869001', 1, 'A1', '2024-01-05 19:45:00', '支付宝'),
('S0124', '1002', 25, '35725869001', 1, 'B3', '2024-01-06 15:30:00', '微信'),
('S0125', '1003', 24, '35725869001', 1, 'C2', '2024-01-07 16:00:00', '储值卡');

-- 初始化金额记录表 pay_amount
INSERT INTO pay_amount (original_price, coupon_amount, parameter_amount, total_discount_amount, actual_price, order_id)
VALUES
   (30.00, 1.00, 0.00, 1.00, 29.00, 'S0123'),
   (30.00, 0.00, 5.00, 5.00, 25.00, 'S0124'),
   (30.00, 0.00, 6.00, 6.00, 24.00, 'S0125');

-- 初始化过渡表 amount
INSERT INTO amount (order_id, actual_price)
VALUES
    ('S0123', 29.00),
    ('S0124', 25.00),
    ('S0125', 24.00);

-- 查询用户表
SELECT * FROM user;

-- 查询电影表
SELECT * FROM film;

-- 查询订单和金额记录表的并集
SELECT
    a.order_id AS 订单号,
    a.session_id AS 场次ID,
    a.count AS 购买数量,
    a.seat AS 座位号,
    a.uid AS 用户ID,
    a.actual_price AS 实际支付,
    a.datetime AS 购买时间,
    a.payment AS 支付方式,
    b.original_price AS 原价,
    b.coupon_amount AS 优惠券,
    b.parameter_amount AS 影城卡,
    b.total_discount_amount AS 总优惠
FROM ticket_order AS a
JOIN pay_amount AS b ON a.order_id = b.order_id;

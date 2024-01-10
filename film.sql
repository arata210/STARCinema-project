-- ������ݿ�
drop database cinema;

-- ����cinema���ݿ�
CREATE DATABASE cinema
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- ʹ�����ݿ�
use cinema;

-- ������Ӱ�� film
CREATE TABLE film (
    movie_id CHAR(10) PRIMARY KEY, -- ��Ӱid
    title VARCHAR(255), -- ����
    release_date CHAR(10), -- ��ӳʱ��
    country VARCHAR(255), -- ����/����
    length INT, -- ʱ��
    director VARCHAR(255), -- ����
    genre VARCHAR(100), -- ����
    actor VARCHAR(255), -- ��Ҫ��Ա
    rating_num CHAR(10) -- ����
);

-- ��ʼ����Ӱ��
INSERT INTO film (movie_id, title, release_date, country, length, director, genre, actor, rating_num)
VALUES 
('35725869', '��᲻��ͣ��', '2023-12-29', '�й���½', 117, '������', '���� / ϲ��', '���� / �׿� / ׯ��� / ��Ѹ', '8.2'),
('35074609', '����ָ', '2023-12-30', '�й���� / �й���½', 125, 'ׯ��ǿ', '���� / ����', '����ΰ / ���»� / ��׿�� / �δﻪ', '6.4'),
('35927496', 'Ǳ��', '2023-12-29', '�й���½ / �й����', 114, '����ҫ', '���� / ���� / ����', '���»� / �ּҶ� / ������ / ����ɪ', '5.9'),
('35768712', 'һ��һ��������', '2023-12-30', '�й���½', 107, '��С�� / ����', '���� / ���', '������ / �ż��� / ��ݼ / ������', '6.1'),
('35312439', '������', '2024-01-11', '�й���½', 109, '�¹��� / ������', '����', '���� / ��� / �պ� / ������ķ', '��������');

-- �������ɱ� amount���������Ż����ű�Ĺ��ɣ�
CREATE TABLE amount (
    order_id CHAR(20) NOT NULL, -- ����id
    actual_price DECIMAL(6,2) NOT NULL, -- ʵ��֧�����
    PRIMARY KEY (order_id, actual_price)
);

-- ���������� ticket_order
CREATE TABLE ticket_order (
    order_id CHAR(20) NOT NULL, -- ����id
    uid CHAR(10), -- �û�id
    session_id CHAR(20), -- ����id
    actual_price DECIMAL(6,2), -- ʵ��֧�����
    count INT, -- ����
    seat CHAR(20), -- ��λ
    datetime DATETIME, -- ֧��ʱ��
    payment CHAR(20), -- ֧����ʽ
    PRIMARY KEY (order_id)
);

-- �����û��� user
CREATE TABLE user (
    uid CHAR(10) NOT NULL, -- �û�id
    pid CHAR(15), -- ����id
    name VARCHAR(20), -- �û���
    phone CHAR(11), -- �û��ֻ���
    type CHAR(6), -- �û�����
    balance DECIMAL(6,2), -- �û����
    status BOOL, -- �û�״̬
    PRIMARY KEY (uid)
);

-- ���������� parameter
CREATE TABLE parameter (
    pid CHAR(15) NOT NULL, -- ����id
    pname CHAR(20), -- ������
    pvalue FLOAT(10), -- �ۿ���
    PRIMARY KEY (pid)
);

-- ��������¼�� pay_amount
CREATE TABLE pay_amount (
    original_price DECIMAL(6,2), -- ԭʼ�۸�
    coupon_amount DECIMAL(6,2), -- �Ż�ȯ�۸�
    parameter_amount DECIMAL(6,2), -- Ӱ�ǿ��۸�
    total_discount_amount DECIMAL(6,2), -- ���Żݼ�
    actual_price DECIMAL(6,2) NOT NULL, -- ʵ��֧�����
    order_id CHAR(20), -- ����id
    PRIMARY KEY (actual_price)
);

-- �������Լ��
ALTER TABLE amount ADD CONSTRAINT FK_order_1 FOREIGN KEY (order_id)
      REFERENCES ticket_order (order_id);

ALTER TABLE amount ADD CONSTRAINT FK_price_2 FOREIGN KEY (actual_price)
      REFERENCES pay_amount (actual_price);

ALTER TABLE ticket_order ADD CONSTRAINT FK_have FOREIGN KEY (uid)
      REFERENCES user (uid);

ALTER TABLE user ADD CONSTRAINT FK_benefit FOREIGN KEY (pid)
      REFERENCES parameter(pid);

-- ��ʼ�������� parameter
INSERT INTO parameter (pid, pname, pvalue)
VALUES
  ('P001', '�·ѿ�', -5),
  ('P002', '��ֵ��', 0.8);

-- ��ʼ���û��� user
INSERT INTO user (uid, pid, name, phone, type, balance, status)
VALUES
    ('1001', NULL, 'С��', '13812345678', '��ͨ��Ա', 0, true),
    ('1002', 'P001', 'С��', '13987654321', 'VIP��Ա', 0, true),
    ('1003', 'P002', 'С��', '18788886666', 'VIP��Ա', 176, true);

-- ��ʼ�������� ticket_order
INSERT INTO ticket_order (order_id, uid, actual_price, session_id, count, seat, datetime, payment)
VALUES
('S0123', '1001', 29, '35725869001', 1, 'A1', '2024-01-05 19:45:00', '֧����'),
('S0124', '1002', 25, '35725869001', 1, 'B3', '2024-01-06 15:30:00', '΢��'),
('S0125', '1003', 24, '35725869001', 1, 'C2', '2024-01-07 16:00:00', '��ֵ��');

-- ��ʼ������¼�� pay_amount
INSERT INTO pay_amount (original_price, coupon_amount, parameter_amount, total_discount_amount, actual_price, order_id)
VALUES
   (30.00, 1.00, 0.00, 1.00, 29.00, 'S0123'),
   (30.00, 0.00, 5.00, 5.00, 25.00, 'S0124'),
   (30.00, 0.00, 6.00, 6.00, 24.00, 'S0125');

-- ��ʼ�����ɱ� amount
INSERT INTO amount (order_id, actual_price)
VALUES
    ('S0123', 29.00),
    ('S0124', 25.00),
    ('S0125', 24.00);

-- ��ѯ�û���
SELECT * FROM user;

-- ��ѯ��Ӱ��
SELECT * FROM film;

-- ��ѯ�����ͽ���¼��Ĳ���
SELECT
    a.order_id AS ������,
    a.session_id AS ����ID,
    a.count AS ��������,
    a.seat AS ��λ��,
    a.uid AS �û�ID,
    a.actual_price AS ʵ��֧��,
    a.datetime AS ����ʱ��,
    a.payment AS ֧����ʽ,
    b.original_price AS ԭ��,
    b.coupon_amount AS �Ż�ȯ,
    b.parameter_amount AS Ӱ�ǿ�,
    b.total_discount_amount AS ���Ż�
FROM ticket_order AS a
JOIN pay_amount AS b ON a.order_id = b.order_id;

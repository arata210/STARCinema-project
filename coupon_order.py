import json
from datetime import datetime

from connect_dbs import RedisConn

coupon = RedisConn()


def Check_number():
    return len(coupon.conn.smembers('film:coupons'))


def Get_info(coupons_id):
    coupons_info = eval(coupon.conn.hget('film:coupons_info', coupons_id))
    return coupons_info


def Last_order_id():
    if not coupon.conn.exists('film:order_id'):
        # 如果键不存在，则添加一个初始元素
        coupon.conn.zadd('film:order_id', {'S0000': 0})
    # 执行 zrange 操作
    return coupon.conn.zcard('film:order_id') - 1


def Order(order_id, userid, coupon_set):
    new_order = dict()
    new_order[order_id] = {
        "userid": userid,
        "coupons": list(coupon_set),
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "payment": "在线支付"
    }
    coupon.conn.hset('film:order_info', order_id, json.dumps(new_order, ensure_ascii=False))


def Change_state(coupon_id, coupon_state):
    coupons_info = Get_info(coupon_id)
    coupons_info['state'] = coupon_state
    coupon.conn.hset('film:coupons_info', coupon_id, json.dumps(coupons_info, ensure_ascii=False))


def coupon_order_id():
    # 获取最后id+1位
    last_id = Last_order_id() + 1
    print(last_id)
    # 订单ID以S开头
    order_id = 'S' + str(last_id).zfill(4)
    print(order_id)
    # 加入数据库
    coupon.conn.zadd('film:order_id', {order_id: last_id})
    return order_id


def coupon_order(userid, coupon_set):
    # 获取订单ID，接收传入的用户ID和优惠券集
    Order(coupon_order_id(), userid, coupon_set)


def buy_coupons(number, userid):
    coupon_set = set()
    # 不能超额购买，超额默认购买余存全部
    if Check_number() - number < 0:
        number = Check_number()
    if Check_number() - number < 0:
        print(userid, ':库存不足')
    else:
        # 获取指定数量优惠券，更改优惠券状态为1，并生成订单
        print(userid, "实际购买", number, "张")
        for x in range(number):
            coupon_set.add(coupon.conn.spop('film:coupons'))
        if coupon_set:
            coupon_order(userid, coupon_set)

        for coupon_id in coupon_set:
            Change_state(coupon_id, 1)
            # print(new_dict)

            print(f"{userid}:{coupon_id}，{Get_info(coupon_id)['name']}至【优惠券】兑换")

    # except Exception as e:
    #     print(userid, ':优惠券售空')


buy_coupons(1, "001")

import json
from datetime import datetime

from connect_dbs import RedisConn
from create_coupon_id import coupon_id_creator

coupon = RedisConn()


def couponGenerator(name=None, discount=1, count=10, exp=7):
    for x in range(count):
        new_coupon = dict()
        # Mf校验码+唯一id
        new_id = "Mf" + coupon_id_creator(x)
        # 创建字典, 优惠券名, 折扣, 状态,开始时间预留, 有效期预留
        new_coupon[new_id] = {
            "name": name,
            "discount": discount,
            # state = 0 未启用
            "state": 0,
            "start": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "exp": exp,
        }
        coupon.conn.sadd('film:coupons', new_id)
        coupon.conn.hset('film:coupons_info', new_id, json.dumps(new_coupon[new_id], ensure_ascii=False))


# 生成各种类型的优惠券
couponGenerator("1元立减券", -1, 5, 7)
couponGenerator("95折折扣券", 0.95, 10, 7)
couponGenerator("7折折扣券", 0.7, 4, 7)
couponGenerator("10元立减券", -10, 1, 7)


def Get_all_info():
    hash_dict = coupon.conn.hgetall('film:coupons_info')
    result = {key: json.loads(value) for key, value in hash_dict.items()}
    return result
# 清空数据
# coupon.conn.delete('film:coupons')
# coupon.conn.delete('film:coupons_info')

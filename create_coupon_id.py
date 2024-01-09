import random
import uuid


# 创建唯一兑换ID
def coupon_id_creator(number):
    # 0-25随机数
    c = random.randint(0, 25)
    # uuid4算法
    d = uuid.uuid4()
    # 随机数转为随机大小写·字母+16进制4位ID+uuid4第一段
    unique_id = f"{chr(ord(random.choice(['A', 'a'])) + c)}{hex(number+128)[2:].zfill(4)}{str(d).split('-')[0]}"
    # print(unique_id, end='|')
    return unique_id


def coupon_id(number):
    a = list()
    for x in range(256, 256+number):
        a.append('Mc' + coupon_id_creator(x))
    return a

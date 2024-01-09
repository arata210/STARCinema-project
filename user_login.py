import random

from connect_dbs import RedisConn

login = RedisConn()


def Login_code(userid):
    code = str(random.randint(0, 9999)).zfill(4)
    login.conn.setex('film:login:userid' + userid, 60, code)
    return code


def Login_code_check(userid, input_code):
    code = login.conn.get('film:login:userid' + userid)
    if code == input_code:
        login.conn.delete('film:login:userid' + userid)
        return True
    else:
        return False


login_code = Login_code('')
print(login_code)

if Login_code_check('', input()):
    print('Login success')
else:
    print('Login code error')

import json

from connect_dbs import MongoDBConn

film_conn = MongoDBConn()

# 创建 MongoDB 连接对象，获取电影集合
cinemaDB = film_conn.client["CinemaDB"]["films"]


def addFilm(movie_id, move_name, movie_cover, movie_intro):
    new_id = film_conn.find_last_id("films")
    try:
        cinemaDB.insert_one({"_id": new_id,
                         "movie_id": movie_id,
                         "move_name": move_name,
                         "movie_cover": movie_cover,
                         "movie_intro": movie_intro})
        return "插入成功！"
    except Exception as e:
        return f"t'r插入失败，发生错误：{e}"


# 调用 addFilm 方法
# addFilm("30270746", "寒单", "https://img1.doubanio.com/view/photo/l/public/p2901699719.webp", """“炸寒单”是台东特有的元宵文化习俗。正月十五，夜晚的街头锣鼓喧天，炮炸寒单爷现场挤满了人潮，肉身寒单阿义（郑人硕 饰）站在神轿上，威风凛凛地接受信徒丢上鞭炮轰炸。忽然间，成堆的炸药被引爆，震耳欲聋，尖叫声不断……""")

# try:
#     cinemaDB.insert_many([
#         {
#             "_id": 1,
#             "movie_id": "35725869",
#             "movie_name": "年会不能停！",
#             "movie_cover": "https://gw.alicdn.com/bao/uploaded/i4/O1CN01PtD4AL21zF9OAswzQ_!!6000000007055-0-alipicbeacon.jpg",
#             "movie_intro": "国民级喜剧人年底大聚会，真实还原打工人精神状态！钳工胡建林 (大鹏 饰)在集团裁员之际阴差阳错被调入总部，裹挟在“错调”事件中的人事经理马杰 (白客 饰) "
#                            "为保饭碗被迫为其隐瞒四处周旋。从“工厂”到“大厂”，从“蓝领”变“金领”，胡建林因与大厂环境格格不入而笑料百出，也像一面“职场照妖镜”照出职场众生相......胡建林为何能在裁员之际一路升职加薪制霸大厂？马杰又能否在“错调”事件中全身而退？这场离谱的“错调”背后又隐藏着什么惊天大瓜……"
#         },
#         {
#             "_id": 2,
#             "movie_id": "35927496",
#             "movie_name": "潜行",
#             "movie_cover": "https://gw.alicdn.com/bao/uploaded/i3/O1CN014yiVPx1gteNzAvvHJ_!!6000000004200-0-alipicbeacon.jpg",
#             "movie_intro": "刘德华时隔16年再演大反派，单挑三代警察！4吨毒品秘密抵达香港后人间蒸发，幕后黑手竟是看上去人畜无害的律师林阵安（刘德华 饰）。借助暗网直播贩毒，一边杀人一边利用法律脱罪，无恶不作的林阵安不知道自己已悄悄被警察和仇家锁定。最好的兄弟、最爱的妻子先后遭遇变故，穷途末路的他彻底疯狂，想要让全世界付出代价……"
#         },
#         {
#             "_id": 3,
#             "movie_id": "35074609",
#             "movie_name": "金手指",
#             "movie_cover": "https://gw.alicdn.com/bao/uploaded/i4/O1CN013yvvHG1ar0PR2n547_!!6000000003382-0-alipicbeacon.jpg",
#             "movie_intro": "用100元的投入换来百亿奢靡人生！看穷小子不择手段颠覆规则将财富和权势玩弄于股掌之中！梁朝伟刘德华二十年后再合体，极致演绎跨年档最受期待的 "
#                            "“暴富”大片！改自真实案件揭秘金融资本内幕！看《金手指》，一览上流社会令人瞠目结舌的狂妄生活！上市公司嘉文集团在短短几年间从默默无名到风生水起，再到没落清盘，市值蒸发超过一百亿。幕后老板程一言(梁朝伟饰)也从万众瞩目的股民偶像变成人人喊打的过街老鼠。高级调查主任刘启源(刘德华饰)长达十五年锲而不舍地搜证和跨境调查，消耗超过两亿诉讼费，竟发现局中有局案中有案，牵涉数条人命并波及香港整个上流社会，究竟谁在幕后?谁能逃脱?谁会出局?"
#         },
#         {
#             "_id": 4,
#             "movie_id": "35768712",
#             "movie_name": "一闪一闪亮星星",
#             "movie_cover": "https://gw.alicdn.com/bao/uploaded/i4/O1CN013yvvHG1ar0PR2n547_!!6000000003382-0-alipicbeacon.jpg",
#             "movie_intro": "现象级爆款剧集同名电影《一闪一闪亮星星》，原班人马再续纯爱故事，令无数观众翘首以盼的纯爱时空再启，奔赴甜虐暗恋！张万森（屈楚萧 饰）计划在高考后向暗恋已久的女生林北星（张佳宁 "
#                            "饰） "
#                            "表白，突如其来的演唱会事故却让一切变成了一场无可挽回的悲剧，没想到的是，痛苦无助的张万森竟意外重启了这个夏天，再次回到悲剧发生前的林北星身边，而重启夏天的秘密，仿佛没有想象中那么简单……这一次，拼尽全力的张万森能否成功守护林北星，让所有刻骨铭心的遗憾都得以圆满? 星河流转中的某个瞬间，青春里的那场绵绵大雪，能不能落在相爱的两人身上？"
#         },
#         {
#             "_id": 5,
#             "movie_id": "35312439",
#             "movie_name": "回西藏",
#             "movie_cover": "https://gw.alicdn.com/bao/uploaded/i3/O1CN01bUbIod21bQZ7jxKLX_!!6000000007003-0-alipicbeacon.jpg",
#             "movie_intro": "秦奋与梁笑笑，老狐狸与比目鱼，爱情故事万千，取其一对展开。两人结婚十年，梁笑笑找到心之所向，开始四海为家。一别之后，两地相悬。以为是三四月，又谁知五六七八九十年。好友老范，见其思念难解，忧其岁月蹉跎，故赠予一仿生智能人，模样若笑笑，伴其左右。岁月时而静好，时而吵闹，时而苦中有笑，智能人也日渐有了曾经佳人的味道。本是良辰美景，故事突发变故，又一笑笑开锁入门，一笑笑莞尔一笑，一笑笑笑里藏刀，一切如梦如幻，如真似假。秦奋射出的箭，如今正中自己的靶心。谁去谁留？且在跨年揭晓。"
#         }
#     ])
#     print("插入成功")
# except Exception as e:
#     print("插入失败")


# print((cinemaDB.findById("006")))
#
# print(cinemaDB.delById("006"))
#

# print(cinemaDB.updateFilm("006", "zxcvbnm"))
# print(cinemaDB.findAll())
#
# print(cinemaDB.filmName("005"))
# print(cinemaDB.addSession("005", "English", "2024-01-10", "12:00",125, 1,"2D",58))
# print(cinemaDB.findSession("005"))
# print(cinemaDB.findSessionById("005", 1))


def findAll():
    return list(cinemaDB.find())
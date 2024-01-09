import requests
from bs4 import BeautifulSoup


def douban_rating_num(movie_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.get('https://movie.douban.com/subject/' + movie_id, headers=headers)
    html_content = response.text

    # 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找class为"rating_nums"的标签
    rating_num = soup.find('div', {'class': 'rating_self'}).find('strong', {'class': 'll rating_num'}).text.strip()
    # 提取评分内容
    if len(rating_num) == 0:
        rating_num = '暂无'

    return rating_num

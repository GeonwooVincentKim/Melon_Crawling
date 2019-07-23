from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def melon_hi():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_element = requests.get("https://www.melon.com/chart/index.htm", headers=headers)
    html = get_element.text
    bsObj = BeautifulSoup(html, "html.parser")
    charts = bsObj.findAll("div", {"class": "ellipsis rank01"})
    artists = bsObj.findAll("span", {"class": "checkEllipsis"})

    for i in range(len(charts)):
        chart = charts[i].text.strip()
        artist = artists[i].text.strip()
        print("{0:3d}위 {1} - {2}".format(i+1, chart, artist))

    file = open('melonTop100.txt', 'w', -1, 'UTF-8')
    for i in range(len(charts)):
        chart = charts[i].text.strip()
        artist = artists[i].text.strip()
        data = "{0:3d}위 {1} - {2}".format(i+1, chart, artist)
        file.write(data + '\n')

    print("파일 쓰기 완료 !")
    file.close()


if __name__ == "__main__":
    melon_hi()

# def song(a):
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#     get_melon = requests.get("https://www.melon.com/chart/index.htm", headers=headers)
#     html = get_melon.text
#     bsObj = BeautifulSoup(html, "html.parser")
#     singers_name = bsObj.findAll("span", {"class": "checkEllipsis"})
#     charts_name = bsObj.findAll("div", {"class": "ellipsis rank01"})
#
#     tk = list()
#     for i in range(len(singers_name)):
#         singer_chart = singers_name[i].text.strip()
#         chart_name = charts_name[i].text.strip()
#         if a in singer_chart:
#             tk.append("{0:3d}위 {1} - {2}".format(i + 1, chart_name, singer_chart))
#         else:
#             pass
#
#     if len(tk) > 0:
#         print("입력하신 {}에 대한 내용을 뽑아왔어요".format(a))
#         print(tk)
#     else:
#         print('해당 가수가 없습니다. 다른 가수를 찾아보세요')


# if __name__ == "__main__":
#     RANK = 100
#     header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
#     req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
#     html = req.text
#     parse = BeautifulSoup(html, 'html.parser')
#
#     titles = parse.find_all("div", {"class": "ellipsis rank01"})
#     songs = parse.find_all("div", {"class": "ellipsis rank02"})
#
#     title = []
#     song = []
#
#     for t in titles:
#         title.append(t.find('a').text)
#
#     for s in songs:
#         song.append(s.find('span', {"class": "checkEllipsis"}).text)
#
#     for i in range(RANK):
#         print('%3d위: %s - %s' % (i + 1, title[i], song[i]))
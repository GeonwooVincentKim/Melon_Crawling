from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def melon_name():
    a = input("원하는 가수 또는 노래 제목을 입력하세요")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_melon = requests.get("https://www.melon.com/chart/index.htm", headers=headers)
    html = get_melon.text
    bsObj = BeautifulSoup(html, "html.parser")
    singers_name = bsObj.findAll("span", {"class": "checkEllipsis"})
    charts_name = bsObj.findAll("div", {"class": "ellipsis rank01"})
    result = []

    print("입력하신 {}에 대한 내용을 뽑아왔어요".format(a))
    singer_chart = []
    # chart_name = []
    for i in range(len(singers_name)):
        # if a in singer_chart:
        singer_chart = singers_name[i].text.strip()
        chart_name = charts_name[i].text.strip()

        if a in singer_chart or a in chart_name:
            result += ["{0:3d}위 {1} - {2}".format(i + 1, chart_name, singer_chart)]
            # print("{0:3d}위 {1} - {2}".format(i + 1, chart_name, singer_chart))
    if len(result) > 0:
        for r in result:
            print(r)

    else:
        print("앗! " + a + "에 데이터가 없다네요.. 다시 한 번 찾아보시겠어요?")

        # if a in singer_chart or a in chart_name:
        #     print("{0:3d}위 {1} - {2}".format(i + 1, chart_name, singer_chart))
        # if len(singer_chart):
        # if a not in singer_chart or a not in chart_name:
        #     print("ERROR")
        #     break

        # singer_chart.append(singers_name)
        # chart_name.append(charts_name)

        # if len(singer_chart) > 0:
        #     print(a + " 의 차트 여부입니다.")
        #     for i in range(0, len(singer_chart) - 1):
        #         print(singer_chart[i] + " - " + chart_name[i])
        # elif len(singer_chart) is 0:
        #     print(a + " 는 차트 안에 없습니다.")
        # elif a not in singer_chart or a not in chart_name:
        #     print("ERROR")

        # else:
        #     print("앗 데이터가 없다네요..다시 한 번 찾아보세요")
        #     break

    file = open("find_name_result.txt", 'w', -1, 'UTF-8')
    for i in result:
        file.write(i + "\n")
    # for i in range(len(singers_name)):
    #     singer_chart = singers_name[i].text.strip()
    #     chart_name = charts_name[i].text.strip()
    #     # if len(singer_chart):
    #     if a in singer_chart or a in chart_name:
    #         data = "{0:3d}위 {1} - {2}".format(i + 1, chart_name, singer_chart)
    #         file.write(data + "\n")
        # else:
        #     print("저장이 안됐어요ㅠㅠ")
        #     break
    if len(result) > 0:
        print("파일 쓰기가 모두 완료되었습니다.")
        file.close()

    else:
        print("입력하신 "+a+"에 대한 데이터가 없어서 저장할 수가 없어요ㅠㅠ")


if __name__ == "__main__":
    melon_name()



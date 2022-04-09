import requests
from tkinter import *
import matplotlib.pyplot as plt


def get_data():
    base_url = "https://coronavirus-tracker-api.herokuapp.com/v2/locations?timelines=1"
    country_code = city_info.get()

    if country_code == "":
        put_city.config(text="country:not find country")
    else:
        base_url += ("&country_code=" + country_code)
        # print(base_url)
        response = requests.get(base_url)
        global info
        info = response.json()
        # print(info)
        put_city.config(text="country:" + info["locations"][0]["country"])
        put_confirmed.config(text="confirmed:" +
                             str(info["locations"][0]["latest"]["confirmed"]))
        put_deaths.config(text="deaths:" +
                          str(info["locations"][0]["latest"]["deaths"]))
        put_updated.config(
            text="last updated:" +
            info["locations"][0]["last_updated"].split('T')[0] + "," +
            info["locations"][0]["last_updated"].split('T')[1][:-1])


def show_figure():
    timelines = info["locations"][0]["timelines"]["confirmed"]["timeline"]
    timelines_key_list = list(timelines.keys())
    timelines_val_list = list(timelines.values())
    month = []
    month_confirmed = []
    # print(timelines_key_list)
    for i in range(len(timelines_key_list)):
        timelines_key_list[i] = timelines_key_list[i].split("T")[0]
        # print(timelines_key_list[i].split("-")[2])
        if timelines_key_list[i].split("-")[2] == "01":
            # print(timelines_key_list[i])
            month.append(timelines_key_list[i][:-3])
            month_confirmed.append(timelines_val_list[i])

    # plt.figure(figsize=(15, 10), dpi=100, linewidth=2)
    plt.plot(month, month_confirmed, label="confirmed")
    plt.xticks(rotation=90)
    # plt.hexbin(timelines.keys().split('T')[0], timelines.values(), label="confirmed")
    plt.title("Python Line chart example")
    # # plt.xticks(fontsize=20)
    # # plt.yticks(fontsize=20)
    # # 標示x軸(labelpad代表與圖片的距離)
    # plt.xlabel("date", fontsize=30, labelpad=15)
    # # 標示y軸(labelpad代表與圖片的距離)
    # plt.ylabel("number", fontsize=30, labelpad=20)
    # # 顯示出線條標記位置
    # plt.legend(loc="best", fontsize=20)
    plt.show()


# https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=TW
# temp = {
#     "latest": {
#         "confirmed": 16313,
#         "deaths": 846,
#         "recovered": 0
#     },
#     "locations": [{
#         "id": 245,
#         "country": "Taiwan*",
#         "country_code": "TW",
#         "country_population": 22894384,
#         "province": "",
#         "last_updated": "2021-10-14T06:31:03.756047Z",
#         "coordinates": {
#             "latitude": "23.7",
#             "longitude": "121.0"
#         },
#         "latest": {
#             "confirmed": 16313,
#             "deaths": 846,
#             "recovered": 0
#         }
#     }]
# }

windows = Tk()
windows.title("My Weather")

put_city = Label(windows, text="country:")
put_city.pack()

put_confirmed = Label(windows, text="confirmed:")
put_confirmed.pack()

put_deaths = Label(windows, text="deaths:")
put_deaths.pack()

put_updated = Label(windows, text="last updated:")
put_updated.pack()

city_info = Entry(windows)
city_info.pack()

btn = Button(windows, text='get data', command=get_data)
btn.pack()

btn_figure = Button(windows, text='show figure', command=show_figure)
btn_figure.pack()

windows.mainloop()

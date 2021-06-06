import datetime

my_birthday = input("請輸入今年的生日日期(格式月/日/年): ")

next = datetime.datetime.strptime(my_birthday, '%m/%d/%Y').date()

now = datetime.date.today()

diff = next - now

print(diff)
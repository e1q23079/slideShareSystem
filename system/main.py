import datetime
import time

setHour = 00
setMinute = 00
print("自動更新プログラムを実行しています．")
while True:
    dt_now = datetime.datetime.now()
    hour = dt_now.hour
    minute = dt_now.minute
    time.sleep(1)
    if(hour==setHour and minute==setMinute):
        print("システムを更新しました．")
        f = open('archive.js','w')
        f.write("var archieves = ['test'];")
        f.close()
        break
        
import speedtest
import datetime
import csv
import time

s = speedtest.Speedtest()

d = datetime.datetime.now().strftime("%d-%m-%y")

try:
    with open(f'Saidas/monitor_{d}.csv', mode='w') as speedcsv:
        csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'download', 'upload'])
        csv_writer.writeheader()
        while True:
            time_now = datetime.datetime.now().strftime("%D %H:%M")
            download = round((round(s.download()) / 1048576), 2)
            upload = round((round(s.upload()) / 1048576), 2)
            csv_writer.writerow({
                'time': time_now,
                'download': download,
                "upload": upload
            })
            print('monitor checked at {}, to exit monitor press CTRL+C'.format(time_now))
            time.sleep(60)
except KeyboardInterrupt as e:
    print('\nend monitoring, check ./Saidas')
    exit()
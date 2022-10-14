import requests
import json
import psycopg2
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

#날짜 리스트 만들기
def date_range(startdate, enddate) :
    start_date = datetime.strptime(startdate, '%Y%m%d')
    end_date = datetime.strptime(enddate, '%Y%m%d')
            
    dates = []

    while start_date.strftime('%Y%m%d') != end_date.strftime('%Y%m%d'):
        dates.append(start_date.strftime('%Y%m%d'))
        start_date += timedelta(days=1)

    return dates

dt_list = date_range("20210101", "20220101")

#open api 호출
total_data = []
for i in dt_list :
    seoul_api_key = os.environ.get('seoul_api_key')
    url = f'http://openapi.seoul.go.kr:8088/{seoul_api_key}/json/CardSubwayStatsNew/1/1000/'+ i

    raw_data = requests.get(url)
    parsed_data = json.loads(raw_data.text)
    subway_data = parsed_data['CardSubwayStatsNew']['row']
    total_data.append(subway_data)

# #postgre와 연결해서 db연결
conn = psycopg2.connect(
    host="arjuna.db.elephantsql.com",
    database="kpodyujx",
    user="kpodyujx",
    password="eYCCvsQlP4_M3mb1dIZonEqSdIQ2pS7C")

cur = conn.cursor()


#db에 저장
cur.execute("DROP TABLE IF EXISTS subwayride")
cur.execute(""" CREATE TABLE subwayride(
                    date DATE, 
                    line VARCHAR(20),
                    station VARCHAR(20),
                    ride_num INTEGER,
                    alight_num INTEGER
                    );
            """)

for row in total_data : 
    for i in range(len(row)) : 
        temp = {}
        temp_list = []
        temp.update(
            {
                'date' : row[i]['USE_DT'],
                'line' : row[i]['LINE_NUM'],
                'station' : row[i]['SUB_STA_NM'],
                'ride_num' : row[i]['RIDE_PASGR_NUM'],
                'alight_num' : row[i]['ALIGHT_PASGR_NUM']
            }
                    )
        temp_list.append(list(temp.values()))

        for j in temp_list :
            cur.execute("INSERT INTO subwayride(date, line, station, ride_num, alight_num) VALUES (%s, %s, %s, %s, %s)", j)

conn.commit()
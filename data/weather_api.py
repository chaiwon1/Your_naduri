import requests
import json
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

weather_key = os.environ.get('weather_key')
startDate = '20210101'
endDate =  '20211231'
location = 108

#open api 호출
url = f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={weather_key}&pageNo=1&numOfRows=999&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt={startDate}&endDt={endDate}&stnIds={location}'

raw_data = requests.get(url)
parsed_data = json.loads(raw_data.text)
weather_data = parsed_data['response']['body']['items']['item']

#postgre와 연결
conn = psycopg2.connect(
                            host = os.environ.get('host'),
                            database = os.environ.get('database'),
                            user = os.environ.get('user'),
                            password = os.environ.get('password')
                        )

cur = conn.cursor()

#db에 저장
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute(""" CREATE TABLE weather(
                                        DATE DATE NOT NULL PRIMARY KEY, 
                                        avgTa FLOAT,
                                        minTa FLOAT,
                                        maxTa FLOAT,
                                        sumSsHr FLOAT,
                                        avgWs FLOAT,
                                        sumRn FLOAT,
                                        avgRhm FLOAT
                                    );
            """)

# DATE 날짜
# avgTa 평균기온
# minTa 최저기온
# maxTa 최고기온
# sumSsHr 합계일조시간
# avgWs 평균풍속
# sumRn 일강수량
# avgRhm 평균상대습도

for row in weather_data : 
    temp = {}
    temp_list = []
    temp.update(
        {
            'DATE' : row['tm'],
            'avgTa' : row['avgTa'],
            'minTa' : row['minTa'],
            'maxTa' : row['maxTa'],
            'sumSsHr' : row['sumSsHr'],
            'avgWs' : row['avgWs'],
            'sumRn' : row['sumRn'],
            'avgRhm' : row['avgRhm']
        }
    )
    for i in temp:
        if temp[i] == '':
            temp[i] = '0'

    temp_list.append(list(temp.values()))

    for j in temp_list :
        cur.execute("INSERT INTO weather (DATE, avgTa, minTa, maxTa, sumSsHr, avgWs, sumRn, avgRhm) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", j)

conn.commit()
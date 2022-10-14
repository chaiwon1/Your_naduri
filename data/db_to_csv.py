import psycopg2
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

#postgre에 들어가 있는 weather 테이블은 csv로 만들기
conn = psycopg2.connect(
                            host = os.environ.get('host'),
                            database = os.environ.get('database'),
                            user = os.environ.get('user'),
                            password = os.environ.get('password')
                        )

cur = conn.cursor()

weather_query = "COPY (SELECT * FROM weather) To STDOUT With CSV DELIMITER ','"
with open("weather.csv", "w") as file:
        cur.copy_expert(weather_query, file)


#subway 데이터는 너무 커서 pandas로 정리해서 합계만 csv파일 만들어주기(colab에서 진행)
df = pd.read_csv('/data/subway.csv', encoding='euc-kr')

df_total = pd.DataFrame({'DATE':[], 'RIDE':[], 'ALIGHT':[]})

def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2021-01-01", "2021-12-31")

ride = []

for i in dates :
  ride_num = df[(df['날짜']==i)&(df['구분']=='승차')]['합 계'].sum()
  ride.append(ride_num)

alight = []

for i in dates :
  alight_num = df[(df['날짜']==i)&(df['구분']=='하차')]['합 계'].sum()
  alight.append(alight_num)

df_total['DATE'] = dates
df_total['RIDE'] = ride
df_total['ALIGHT'] = alight

df_total.to_csv("/data/subway_data.csv")
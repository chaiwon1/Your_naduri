from flask import Blueprint, render_template, request
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

home_bp = Blueprint('home', __name__)
@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET' :
        return render_template('home.html')
    
    if request.method == 'POST' :
        try : 
            date = request.form['날짜']
            weather_date = int(date.replace('-','').strip())

            key = os.environ.get('key')
            
            startDate = weather_date - 10000
            endDate =  startDate
            location = 108

            url = f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={key}&pageNo=1&numOfRows=999&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt={startDate}&endDt={endDate}&stnIds={location}'

            raw_data = requests.get(url)
            parsed_data = json.loads(raw_data.text)
            weather_data = parsed_data['response']['body']['items']['item']
        
            return render_template('home_api.html', weather_data=weather_data, date=date), 200
        
        except :
            return render_template("404.html")
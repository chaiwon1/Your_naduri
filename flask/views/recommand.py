from flask import Blueprint, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

recommand_bp = Blueprint('recommand', __name__)

@recommand_bp.route('/recommand', methods=['GET', 'POST'])
def recommand():
    if request.method == 'GET' :
        return render_template('recommand_home.html')

    if request.method == 'POST' :
        try :
            ncreds = {

                    "client_id": os.environ.get('client_id'),
                    "client_secret" : os.environ.get('client_secret')

                 }
            nheaders = {
                            "X-Naver-Client-Id" : ncreds.get('client_id'),
                            "X-Naver-Client-Secret" : ncreds.get('client_secret')
                        }

            naver_local_url = "https://openapi.naver.com/v1/search/local.json?"

            location = request.form['지역']

            recommands = []
            query = location + " " + " 맛집"
            params = "sort=comment" + "&query=" + query + "&display=" + '20'
                
            res = requests.get(naver_local_url + params, headers=nheaders)
            result_list = res.json().get('items')

            for i in range(0,5):
                recommands.append(result_list[i])

            return render_template('recommand.html', recommand=recommands, location=location)

        except :
            return render_template("404.html")
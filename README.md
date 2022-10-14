<h1>프로젝트 개요</h1>
<a href="https://your-naduri.herokuapp.com/">사이트 바로가기</a>

<a href="https://www.figma.com/file/3QKPYNiUVwQoEj0nd30Edo/Your_naduri?node-id=0%3A1">홈페이지 구성보기</a>

[Your_naduri_ppt.pptx](https://github.com/chaiwon1/Your_naduri/files/9778929/Your_naduri_ppt.pptx)


<h3>🎯프로젝트 목적</h3>
  <ul>
    <li>CSV파일과 API로 로드한 데이터를 Postgres에 적재, 추출하는 프로세스를 진행한다.</li>
    <li>Open API를 호출하고 Python 파일에서 데이터를 파싱한다.</li>
    <li>Rest API를 설계하고 Flask와 Heroku를 통해 웹구축과 배포를 시행한다.</li>
  </ul>

<h3>🤫프로젝트 배경</h3>
  <ul>
   코로나가 끝나가고 있는 지금, 서울 나들이를 계획하고 있는 나들이객들을 위해 API를 이용해 
   지난해 같은 시기 기상 변수를 반환하고, 그를 기반으로  지하철 예상 이용객수를 예측, 
   목적지 주변의 맛집을 안내하는 웹서비스를 제공하여 나들이객들의 보다 즐거운 나들이 계획을 돕고자 한다.  
  </ul>

<h3>🛴서비스 기능</h3>
  <ul>
    <li>나들이날의 예상 기상 변수 반환(기상청 API)</li>
    <li>예상 기상 변수를 기반으로 RandomForest모델을 기반으로 해당 날의 지하철 예상 승객수 반환(서울시 공공API)</li>
    <li>목적지 주변 5개의 맛집 추천(네이버 API)</li>
  </ul>

<br>
<br>

<h1>사용 기술 스택</h1>
<br>

<table>
	<th>skill</th>
	<th>version</th>
	<tr>
	    <td>개발환경</td>
	    <td>MacOS M1</td>
	</tr>
	<tr>
	    <td>IDE</td>
	    <td>VSCode</td>
	</tr>
  	<tr>
	    <td>개발 Framework</td>
	    <td>Flask 2.1.2</td>
	</tr>
  	<tr>
	    <td>프로그래밍 언어</td>
	    <td>Python 3.8</td>
	</tr>
  	<tr>
	    <td>DataBase</td>
	    <td>psycopg2-binary 2.9.3</td>
	</tr>
  	<tr>
	    <td>배포환경</td>
	    <td>Heroku</td>
	</tr>
    </table>
    
<br>
<br>

<h1>워크플로우</h1>

![그림1](https://user-images.githubusercontent.com/95471902/195664840-addbecf0-3f2e-42a6-a5d2-3e7337721687.png)

<br>
<br>

<h1>개선점 및 회고</h1>
<h4>1. ML 모델의 성능</h4>
  <ul>
    <li>DB 활용과 API 설계가 목적이었기 때문에 ML 모델의 성능을 크게 신경쓰지 않아, 성능이 많이 떨어졌다.</li>
    <li>따라서, 좀 더 실효성 있는 컬럼들을 추가한 ML 모델을 만들고 서빙해보고 싶다.</li>
  </ul>

<h4>2. 데이터 파이프라인</h4>
  <ul>
    <li>다양한 API를 일정한 주기에 따라 수집하고 그 때마다 ML 모델의 컬럼들을 업데이트하여 보다 스트리밍한 데이터 파이프라인을 구축하고 싶다.</li>
    <li>추후 Airflow를 더 공부하여 실행에 옮겨보도록 하겠다.</li>
  </ul>

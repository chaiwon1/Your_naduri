import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

import pickle

#데이터 불러오기
df_sub = pd.read_csv('csv/subway_data.csv')
df_weather = pd.read_csv('csv/weather.csv')

#df_sub에서 RIDE 컬러만 사용하기로
df_sub.drop('ALIGHT', axis=1, inplace=True)

#여기서 합쳐주고 index를 DATE로, 강수량은 큰 영향도가 없어 삭제
df_total = pd.merge(df_weather, df_sub, how='outer', on='DATE').set_index('DATE')
df_total.drop('sumRn', axis=1, inplace=True)

#target 설정 + 학습, 테스트 데이터셋 나누기
target = 'RIDE'
y_train = df_total[target]
X_train = df_total.drop(target, axis=1, inplace=False)

#정규화
scaler = MinMaxScaler()
X_train[:] = scaler.fit_transform(X_train[:])

#모델 학습용 함수
model = RandomForestRegressor(n_estimators=500)
model.fit(X_train, y_train)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# #성능 확인용 함수
# def evaluate_regr(y,pred):
#     mae_val = mean_absolute_error(y,pred)
#     mse_val = mean_squared_error(y, pred)
#     rmse_val = mean_squared_error(y, pred)**0.5
#     r2 = r2_score(y, pred)
#     print('MAE: {0:.5f}, MSE: {1:.5F}, RMSE: {2:.5F}, R2: {3:.5F}'.format(mae_val, mse_val, rmse_val, r2))

# def get_model_predict(model, X_train, X_test, y_train, y_test):
#     model.fit(X_train, y_train)
#     pred = model.predict(X_test)
#     print('###',model.__class__.__name__,'###')
#     evaluate_regr(y_test, pred)   

# get_model_predict(model, X_train.values, X_test.values, y_train.values, y_test.values)

## 새로운 데이터 한 샘플을 선택해 학습한 모델을 통해 예측해 봅니다
# input_data = [[-4.2, -9.8, 1.6, 6.5, 2.0, 0.0, 64.0]]
# y_pred = model.predict(input_data)

# print(f'{input_data[0][0]} 이러한 날씨변수를 가지는 날의 지하철 예상 승객수는 ${int(y_pred)}명 입니다.')

#pickle로 저장
with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)
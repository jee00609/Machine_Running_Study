import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn import linear_model

#1. 데이터들 불러오기.
csv = pd.read_csv("./Airbnb.csv")
label = csv["price"] #컴퓨터는 최종적으로 집값을 예측을 해야하니 price로 해야겠지?
data = csv[["crim","dust","reservation","distance","like","review"]]

#코드를 여러줄 쓰고 싶으면 역슬래시 쓴다.
train_data,valid_data,train_label,valid_label \
    = train_test_split(data,label)

#2.학습시키기
#2.1.학습 알고리즘 정하기
#/*SVM: support vector machine*/
clf = linear_model.LinearRegression()  #학습알고리즘정할땐 train_data,train_label이거 안넣고 학습시킬때만 넣음
# LinearRegression()이란

#지도학습은 2가지로 분류할수있는데 1. 분류 : 나눠떨어지는 값을 예측  2.회귀 : 연속적인 값을 예측   //지금은 회귀.

#2.2.학습시키기
clf.fit(train_data,train_label)

#3. 예측시키기--하나의 리스트를 질문하는데 이때 열개를 질문하고 싶으면 [] 를 여러개 작성
# result=clf.predict([
#     [3.2,1.2,6.75,2.1],
#     [2.1,4.3,2.32,0.2]
# ])
result= clf.predict(valid_data)
score=metrics.mean_squared_error\
          (result,valid_label)**(1/2)  #루트를 씌우는것이다.
# mean_squared_error말고도 다른 것들도 많다.

print(score)  #score출력했을때 1에 가까울수록 연관성이 높은거고 0에 가까울수록 연관성이 떨어지는거

#지도학습은 1. 미지의 데이터를 예측 , 2.어떤 것들 간에 연관성을 증명

#학습용 검증용

import pickle
with open("Airbnb.pkl","wb") as pkl:
    pickle.dump(clf,pkl)
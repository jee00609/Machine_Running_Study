#Feature Enginerring
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

#1. 데이터들 불러오기.
csv = pd.read_csv("./iris.csv")
label = csv["variety"]
data = csv[["sepal.length","sepal.width","petal.length","petal.width"]]

#학습용 평가용 변수 넣기
#코드를 여러줄 쓰고 싶으면 역슬래시 쓴다.
train_data,valid_data,train_label,valid_label = train_test_split(data,label)

#2.학습시키기
#2.1.학습 알고리즘 정하기
#/*SVM: support vector machine*/
clf = svm.SVC(gamma="auto")

#2.2.학습시키기
clf.fit(data,label)

#3. 예측시키기--하나의 리스트를 질문하는데 이때 열개를 질문하고 싶으면 [] 를 여러개 작성
# result=clf.predict([
#     [3.2,1.2,6.75,2.1],
#     [2.1,4.3,2.32,0.2]
# ])
result= clf.predict(valid_data)
score=metrics.accuracy_score(result,valid_label)

print(score)
print(result)

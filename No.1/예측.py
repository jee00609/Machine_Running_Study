import pickle
with open("AirBNB.pkl","rb") as pkl:
    clf=pickle.load(pkl)

    result=clf.predict([[0.4,1.2,4.32,5.3,42.1,453]])

    print(result)
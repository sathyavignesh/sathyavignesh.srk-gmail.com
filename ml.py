import urllib
import requests 
import time
import serial    


ser1 = serial.Serial('/dev/ttyS0',9600)


API_ENDPOINT = "http://healthiot.life/add.php"


def ml():
    print("Machine Learning Evaluate")
    import pandas as pd
    dataset=pd.read_csv("health.csv")
    x=dataset.iloc[:,0:4].values
    y=dataset.iloc[:,4].values
    from sklearn.model_selection import train_test_split 
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=0)
    from sklearn.linear_model import LogisticRegression
    mymodel=LogisticRegression()
    mymodel.fit(x_train,y_train)
    a = mymodel.predict([[hb,hm,gsr,tmp]])
    
    if a[0]==1:
        print("please consult your doctor")
    else:
        print("health condition good")

while True:
    s = ser1.readline()
    hb,hm,gsr,tmp,dm = s.decode().split(",")
    hb = int(hb)
    hm = int(hm)
    gsr = int(gsr)
    tmp = int(tmp)
    
    data = {'hb':hb,'hm':hm,'tmp':tmp,'gsr':gsr}
    r = requests.post(url = API_ENDPOINT, data = data)
    print(data)
    time.sleep(20)
    ml()

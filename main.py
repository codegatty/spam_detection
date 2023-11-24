from flask import Flask,request
import pickle
from text_transformer import  text_transformer
from test import tfidf,model
import nltk

app = Flask(__name__)


@app.route("/",methods=['POST'])
def hello_world():
    json_data=request.get_json()
    print(json_data)
    return "<p>This is flask rest api</p>"

@app.route("/hello",methods=['GET'])
def func():
    return "<p>hi bro</p>"

@app.route("/detect_spam",methods=['POST'])
def detect_spam():
    nltk.download('stopwords')
    msg=request.get_json();
    msg=dict(msg)
    res={};
    for i in msg:
        print(msg[i])
        processed_msg=text_transformer(msg[i])
        vector=tfidf.transform([processed_msg])
        result=model.predict(vector)[0]
        if result==1:
            res[i]="spam"
        else:
            res[i]="ham"

    return res

    # processed_msg=text_transformer(msg)
    # vector=tfidf.transform([processed_msg])
    # result=model.predict(vector)[0]
    # if result==1:
    #     return msg+" "+"spam"
    # else:
    #     return msg+" "+"ham"
 

if __name__=="__main__":
    
    #app.run(debug=True) 
    app.run(debug=False,host="0.0.0.0")
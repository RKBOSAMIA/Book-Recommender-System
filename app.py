from flask import Flask, render_template, request
import json

app = Flask(__name__)
with open('/Users/rushikeshbosamia/Google Drive/Assignments/256/Assignment-2/Recommed-App/results.json','r') as inputfile:
    data = json.load(inputfile)

user_id = []
for user in data.keys():
    user_id.append(user)

@app.route('/',methods=['GET','POST'])
def GetUsers():
    return render_template('index.html',result=user_id)

@app.route('/results',methods=['GET','POST'])
def Results():
    curr_user = request.form['user_id']
    result = data[curr_user]
    return render_template('results.html',result = [result,curr_user])

if __name__ == "__main__":
    app.run()
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success_with_post/<name>')
def success_with_post(name):
   return 'welcome with post %s' % name

@app.route('/success_with_get/<name>')
def success_with_get(name):
   return 'welcome with get %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success_with_post',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success_with_get',name = user))

app.run(debug = True)
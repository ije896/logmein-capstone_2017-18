from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('jinja2-conditional-test.html', marks = score)


app.run(debug = True)
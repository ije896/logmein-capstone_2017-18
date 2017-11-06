from flask import Flask, redirect, url_for
app = Flask(__name__)

# basics
# following tutorialspoint

@app.route('/')
def null_page():
    return 'Null page'

@app.route('/hello')
def hello_world():
    return 'hello world'


# variables
# https://www.tutorialspoint.com/flask/flask_variable_rules.htm

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

#
# https://www.tutorialspoint.com/flask/flask_url_building.htm

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


"""
# can't get add url rule working
# https://www.tutorialspoint.com/flask/flask_routing.htm
def blanko():
    return 'test successful'
app.add_url_rule('/', 'blank', blanko)
"""



app.debug = True
app.run()
app.run(debug = True)

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
#     app.run(debug = True)


#the routes - where the visitor can go into

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if title != str or author != str:
            return redirect(url_for('error'))
        else:
            return redirect(url_for('search'))

    return render_template('home.html')

# @app.route('/home')
# def search():
#     return render_template('search.html')


# @app.route('/error')
# def error():
#     return render_template('error.html')
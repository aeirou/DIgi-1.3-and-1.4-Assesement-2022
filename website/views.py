#the routes - where the visitor can go into

from flask import Blueprint, render_template, redirect, request, url_for, flash

views = Blueprint('views', __name__) #Blueprint is not an actual application - needs to be registered
lend = Blueprint('lend', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if title != str or author != str:
            return redirect(url_for('error'))
        else:
            return redirect(url_for('search'))

    return render_template('home.html')

@views.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year_pub = request.form.get('year_pub')
        isbn = request.form.get('isbn')

        if len(isbn) < 17:
            flash('Please try again.', category='error') #flash is a message that pops up when an error occours
        elif len(isbn) > 17:
            flash('Please try again', category='error')
        else:
            return
    return render_template('lend.html')
  
# @app.route('/home')
# def search():
#     return render_template('search.html')


# @app.route('/error')
# def error():
#     return render_template('error.html')

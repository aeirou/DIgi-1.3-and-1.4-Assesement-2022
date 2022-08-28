from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#@app.route('/')
#@app.route('/<name>')
#def home():
#    return render_template('home.html')

#@app.route('/shortenurl/')
#def shortenurl():
#    return render_template('shortenurl.html')

@app.route('/home')
def search():
    return render_template('search.html')


@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if title != str or author != str:
            return redirect(url_for('error'))#firgure out redirect...
        else:
            return redirect(url_for('search'))

    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
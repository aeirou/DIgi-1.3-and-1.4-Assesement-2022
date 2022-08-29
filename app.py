from flask import Flask, render_template, request, redirect, url_for
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


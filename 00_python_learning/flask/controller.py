from flask import Flask, render_template, request, redirect, url_for, abort
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method=='GET':
        return redirect(url_for('home'))
    urls = {}
    urls[request.form['code']] = {'url': request.form['url']}
    with open('urls.json', 'w') as url_file:
        json.dump(urls, url_file)
    return render_template('your_url.html', code=request.form['code'])


@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
    return abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
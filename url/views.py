from flask import render_template, flash, redirect, request
from url import app, db
from url.models import URLMap

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#makes url and stores it, then redirect to success/fail page
@app.route('/make', methods=['POST'])
def make():
    url = URLMap(longURL=request.form['longURL'], shortURL=request.form['shortURL'])
    db.session.add(url)
    db.session.commit()
    return redirect('/success')

@app.route('/success')
def success():
    urls = URLMap.query.all()
    recent = db.session.query(URLMap).order_by(URLMap.id.desc()).first()
    return render_template('success.html', urls=urls, recent=recent)

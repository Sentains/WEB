from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', title="Заготовка")

@app.route('/training/<prof>')
def training_of_fly(prof):
    params = {'prof': prof, 'title': 'Тренинг'}
    return render_template('training_of_fly.html', **params)

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')

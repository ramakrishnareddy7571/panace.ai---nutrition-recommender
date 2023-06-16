from collections import UserString
from flask import Flask

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


app.register(UserString, url_prefix='/user')
app.register(UserString, url_prefix='/food')


SECRET_KEY = '3df785ec-879e-4d71-8bb2-d4615d7748b0'

app.use('https://www.nutritionix.com/api/{SECRET_KEY}')

app.run()

if __name__ == '__main__':
    app.run(host='172.20.0.1', port=105)
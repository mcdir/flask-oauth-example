from app import app

app.config['SECRET_KEY'] = 'top secret!'

app.config['SERVER_NAME'] = '2.dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '870858516259504',
        'secret': '9c1c609012328d497b60e91dc5b84844'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

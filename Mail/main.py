from flask import Flask
from flask_mail import Message, Mail

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='syeuty@gmail.com',
    MAIL_PASSWORD='kyera12589'
)
mail = Mail(app)


@app.route('/')
def sendError():
    try:
        print('에러발생')
        msg = Message('Internal Error 500', sender='Tellin', recipients=['syeuty@naver.com'])
        msg.body = '에러발생'
        mail.send(msg)
    except Exception as e:
        print(e)
    finally:
        return '성공'


if __name__ == '__main__':
    app.run(debug=True)

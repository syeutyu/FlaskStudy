from flask import Flask
import logging.handlers
app = Flask(__name__)

if not app.debug:
    # 파일로 로그를 남길시 파일이 너무 커지면 자동으로 새로운 파일을 생성한뒤 다시 로그를 저장하는 RotatingFileHandler
    handler = logging.handlers.RotatingFileHandler('log.txt', mode='a', maxBytes=10485760, backupCount=5,encoding='utf-8', delay=False)
    app.logger.addHandler(handler)
    app.logger.info('logger start')

@app.route("/")
def logger():
    app.logger.debug("Error를 파일로 저장합니다")
    return '콘솔확인좀'

if __name__ == '__main__':
    app.debug = True
    app.run()

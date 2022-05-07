import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    # mysql 配置
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME') or "root"
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD') or "summer123"
    MYSQL_HOST = os.getenv('MYSQL_HOST') or "127.0.0.1"
    MYSQL_PORT = int(os.getenv('MYSQL_PORT') or 3306)
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE') or "FlaskEnd"
    # mysql 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ 开发配置 """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


config = {
    'development': DevelopmentConfig

}

from decouple import config

class Config:
    SECRET_KEY = 'pruebaproyecto'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web_facilito'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('MAIL_USERNAME', default='pythonflask@gmail.com')
    MAIL_PASSWORD = config('MAIL_PASSWORD', default='google123')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web_facilito_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}

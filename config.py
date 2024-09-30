from decouple import config

class Config:
     SECRET_KEY = config('SECRET_KEY')
     SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
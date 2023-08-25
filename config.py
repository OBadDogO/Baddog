import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://zx2203300zx:MXCp7IA8FF60LFIpc4vTM13QTs7BtfFo@dpg-cjkcdqb37aks738v0kk0-a.singapore-postgres.render.com/ex2'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
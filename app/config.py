class Config:
    DB_HOST = 'localhost'


class DevelopmentConfig(Config):
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'model-api'
    DEBUG = True


class ProductionConfig(Config):
    pass


config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

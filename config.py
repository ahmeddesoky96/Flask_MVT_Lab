class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///db.sqlite"
    
class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI= "postgresql://postgres:123@localhost:5432/posts"
    # SQLALCHEMY_DATABASE_URI= "sqlite:///db.sqlite"


project_config= {
    "dev": DevelopmentConfig,
    "prd":ProductionConfig
}

from flask import Flask
from blog_mvt.config import project_config
from blog_mvt.models import db,Post
import os

def create_app(config_name):
    app = Flask(__name__)
    app_config = project_config[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"]=app_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(app_config)
    db.init_app(app)


    ### views
    # from blog_mvt.posts.views import listPost,createPost
    # app.add_url_rule("/posts", view_func=listPost)
    # app.add_url_rule("/posts/addpost",methods=["GET", "POST"], view_func=createPost)
    from blog_mvt.posts.bluePrintPosts import postBlueprint
    app.register_blueprint(postBlueprint)
    return app


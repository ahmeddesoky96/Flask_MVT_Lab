from blog_mvt import create_app
import os

app = create_app('prd')

if __name__=='__main__':
    app.run()
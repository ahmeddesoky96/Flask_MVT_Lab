from blog_mvt.models import Post,db
from blog_mvt.posts.bluePrintPosts import postBlueprint
from flask import render_template,redirect,request,url_for



#######main page#######

def firstPage():
    
    return render_template("main.html")


#######3 view all posts########
@postBlueprint.route("",endpoint='postList')
def listPost():
    posts=Post.getAllPost()
    return render_template("posts/listPostHtml.html",posts=posts)


######### create post ######
@postBlueprint.route("/addpost", methods=["GET", "POST"], endpoint="postAdd")
def createPost():
    if request.method == "POST":
        
        post = Post(
            title=request.form["title"],
            body=request.form["body"],
            image=request.form["image"],
            
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.postList"))
    return render_template("posts/addPostHtml.html")

####### display post########
@postBlueprint.route("/<int:id>", endpoint="postDisplay")
def displayPost(id):
    post = Post.getSpecificPost(id)
    return render_template("posts/displayPost.html", myPost=post )


##### delete post ##########
@postBlueprint.route("/<int:id>/delete", endpoint="postDelete")
def deletePost(id):
    post = Post.getSpecificPost(id)
    post.deletePost()
    return redirect(url_for('posts.postList'))


##### update post ######
@postBlueprint.route("/<int:id>/edit", methods=["GET", "POST"], endpoint="postUpdate")
def updatePost(id):
    post = Post.getSpecificPost(id)
    if request.method=="POST":
        post.title=request.form["title"]
        post.body=request.form["body"]
        post.image = request.form["image"]
        
        db.session.commit()
        return redirect(url_for('posts.postList'))
    return render_template("posts/updatePostHtml.html",setPost=post)
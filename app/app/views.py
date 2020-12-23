from app import app

from flask import render_template,request,redirect, jsonify ,make_response
from datetime import datetime




@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")



@app.route("/")
def index():
    print("selam")
    return render_template("/public/index.html")


@app.route("/about")
def about():
    date=datetime.utcnow()
   
    return render_template("/public/about.html",date=date)
@app.route("/sign-up", methods=["GET","POST"])
def sign_up() :
    if request.method=="POST":
        req=request.form
        username=req["username"]
        email=req["email"]
        password=req["password"]
        print (f"Username:{username}, email: {email}, password:{password}")
        

        return redirect (request.url)
     
    return render_template("public/sign_up.html")
@app.route("/profile/<username>")
def profile(username):
    user=username
    date=datetime.utcnow()
    return render_template("public/profile.html",user=user,date=date)

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()
    print (req)
    res=make_response(jsonify(req),200)

    return res


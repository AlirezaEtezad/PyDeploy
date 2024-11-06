from flask import Flask, render_template, request


app = Flask("Personal Website")

@app.route("/", methods=["GET"])
def my_root():
    global media
    media = ["image", "music", "movie"]
   # return "<p> Hello Flasksssss </p>"
    return render_template("index.html", name="Ali", x=10, media=media)


@app.route("/me", methods=["GET"])
def my_inforamtion():
    my_info = {"firstname": "Alireza", "email": "hello"}
    return my_info



@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "GET"
    elif request.method == "POST":
        return "POST"
    

@app.route("/download", methods=["GET"])
def download():
   # media = ["image", "music", "movie"]
    return render_template("download.html", media="media")

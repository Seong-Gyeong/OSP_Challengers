from flask import Flask, render_template, request
from database import DBhandler
import sys

application = Flask(__name__)

DB = DBhandler()

@application.route("/")
def hello():
    return render_template("home.html")

@application.route("/showRestaurantList")
def view_list():
    return render_template("/showRestaurantList.html")


@application.route("/addRestaurant")
def reg_restaurant():
    return render_template("addRestaurant.html")

@application.route("/showRecommendation")
def view_recomm_list():
    return render_template("showRecommendation.html")

@application.route("/showAboutUs")
def view_info():
    return render_template("showAboutUs.html")

@application.route("/addBestMenu", methods=['POST'])
def reg_bestmenu():
    data=request.form
    print(list(data.values()))
    return render_template("addBestMenu.html", data=data)


@application.route("/showBestMenu")
def view_bestmenu():
    return render_template("showBestMenu.html")

@application.route("/showBestMenu", methods=['POST'])
def reg_bestmenu_submit():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    print(list(data.values()))
    
    if DB.insert_menu(data['menu__name'], data, image_file.filename):
        return render_template("showBestMenu.html", data=data, image_path="/static/image/"+image_file.filename) 
    else:
        return "menu name already exist!"

@application.route("/addReview")
def reg_review():
    return render_template("addReview.html")

@application.route("/showReview")
def view_review():
    return render_template("showReview.html")

@application.route("/showReview", methods=['POST']) 
def reg_review_submit():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    print(list(data.values()))
    
    if DB.insert_review(data['review__reviewer'], data, image_file.filename):
        return render_template("showReview.html", data=data, image_path="/static/image/"+image_file.filename) 

@application.route("/result", methods=['POST']) 
def reg_restaurant_submit():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    print(list(data.values()))
    
    if DB.insert_restaurant(data['restaurant_name'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="/static/image/"+image_file.filename) 
    else:
        return "Restaurant name already exist!"
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
    

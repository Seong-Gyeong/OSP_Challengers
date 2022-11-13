from flask import Flask, render_template, request
import sys
application = Flask(__name__)


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

@application.route("/addBestMenu")
def reg_bestmenu():
    return render_template("addBestMenu.html")


@application.route("/showBestMenu")
def view_bestmenu():
    return render_template("showBestMenu.html")

@application.route("/showBestMenu", methods=['POST'])
def reg_bestmenu_submit():
    data2=request.form
    print(list(data2.values()))
    return render_template("showBestMenu.html", data2=data2)

@application.route("/addReview")
def reg_review():
    return render_template("addReview.html")

@application.route("/showReview")
def view_review():
    return render_template("showReview.html")

@application.route("/showReview", methods=['POST']) 
def reg_review_submit():
    data3=request.form
    print(list(data3.values()))
    return render_template("showReview.html", data3=data3)

@application.route("/result", methods=['POST']) 
def reg_restaurant_submit():
    #image_file=request.files["file"]
    #image_file.save("static/image/{}".format(image_file.filename))]
    data=request.form
    print(list(data.values()))
    return render_template("result.html", data=data)

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)

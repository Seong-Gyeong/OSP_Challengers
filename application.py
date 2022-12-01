from flask import Flask, render_template, request, redirect, url_for
from database import DBhandler
import sys, math

application = Flask(__name__)

DB = DBhandler()

@application.route("/")
def hello():
    return render_template("homeView.html")

@application.route("/addRestaurant")
def reg_restaurant():
    return render_template("addRestaurant.html")

@application.route("/showRestaurantList")
def view_list():
    return render_template("showRestaurantList.html")

@application.route("/showRestaurantDetail")
def view_res_detail():
    return render_template("showRestaurantDetail.html")

@application.route("/showRecommendation")
def view_recomm_list():
    return render_template("showRecommendation.html")

@application.route("/showAboutUs")
def view_info():
    return render_template("showAboutUs.html")

@application.route("/addBestMenuFirst", methods=['POST'])
def reg_bestmenu():
    data=request.form
    print(list(data.values()))
    return render_template("addBestMenuFirst.html", data=data)

#@application.route("/addBestMenu", methods=['POST'])
#def reg_bestmenus():
#    data=request.form
#    print(list(data.values()))
#    return render_template("addBestMenu.html", data=data)

@application.route("/showBestMenu")
def view_bestmenu():
    return render_template("showBestMenu.html")

@application.route("/addBestMenuResult")
def reg_finish():
    return render_template("addBestMenuResult.html")

@application.route("/addBestMenuResult", methods=['POST'])
def reg_bestmenu_submit():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    print(list(data.values()))
    
    if DB.insert_menu(data['menu_name'], data, image_file.filename):
        return render_template("addBestMenuResult.html", data=data, img_path="/static/image/"+image_file.filename) 
    else:
        return "menu name already exist!"

@application.route("/addReviewResult")
def reg_review_result():
    return render_template("addReviewResult.html")

@application.route("/addReviewResult", methods=['POST'])
def reg_review_submit():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    print(list(data.values()))
    
    if DB.insert_review(data['review_reviewer'], data, image_file.filename):
        return render_template("addReviewResult.html", data=data, img_path="/static/image/"+image_file.filename) 
    
    
@application.route("/add_reviews/<res_name>/")
def add_reviews(res_name):
    res_data = DB.get_restaurant_byname(str(res_name))
        
    return render_template(
        "addReview.html",
        data=res_data
        )

#@application.route("/addReview")
#def reg_review():
#    return render_template("addReview.html")
    
    
#@application.route("/addReview")
#def reg_review():
#    return render_template("addReview.html")

#@application.route("/showReview", methods=['POST']) 
#def reg_review_submit():
#    image_file=request.files["file"]
#    image_file.save("static/image/{}".format(image_file.filename))
#    data=request.form
#    print(list(data.values()))
    
#    if DB.insert_review(data['review_reviewer'], data, image_file.filename):
#        return render_template("showReview.html", data=data, image_path="/static/image/"+image_file.filename) 

@application.route("/result", methods=['POST']) 
def reg_restaurant_submit():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    print(list(data.values()))
    print(data)
    
    if DB.insert_restaurant(data['restaurant_name'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="/static/image/"+image_file.filename) 
    else:
        return "Restaurant name already exist!"
    

@application.route("/showAllRestaurantList")
def list_all_restaurants():
    page = request.args.get("page", 0, type=int)
    category = request.args.get("category", "전체")
    limit = 6
    
    start_idx=limit*page
    end_idx=limit*(page+1)
    
    if category=="전체":
        data = DB.get_restaurants()
    else:
        data = DB.get_restaurants_bycategory(category)
    
 #   data = DB.get_restaurants() #read the table
    tot_count = len(data)
    print("category",category,tot_count)
    if tot_count<=limit:
        data = dict(list(data.items())[:tot_count])
    else:
        data = dict(list(data.items())[start_idx:end_idx])
    data = dict(sorted(data.items(), key=lambda x: x[1]['name'], reverse=False))
    print(data)
    
    page_count = len(data)
    print(tot_count,page_count)
    return render_template(
        "showAllRestaurantList.html",
        datas=data.items(),
        total=tot_count,
        limit=limit,
        page=page,
        page_count=math.ceil(tot_count/6),
        category=category)

@application.route("/view_detail/<name>/")
def view_restaurant_detail(name):
    data = DB.get_restaurant_byname(str(name))
    avg_rate = DB.get_avgrate_byname(str(name))
    
    print("####data:",data)
    return render_template("showRestaurantDetail.html", data=data, avg_rate=avg_rate)

@application.route("/list_foods/<res_name>/")
def view_foods(res_name):
    
    data = DB.get_food_byname(str(res_name))
    tot_count = len(data)
    page_count = len(data)
    
    return render_template(
        "showBestMenu.html",
        datas=data,
        total=tot_count)

@application.route("/list_reviews/<res_name>/")
def view_reviews(res_name):
    res_data = DB.get_restaurant_byname(str(res_name))
    data = DB.get_review_byname(str(res_name))
    
    avg_rate = DB.get_avgrate_byname(str(res_name))
    tot_count = len(data)
    page_count = len(data)
    
    return render_template(
        "showReview.html",
        data=res_data,
        datas=data,
        total=tot_count,
        avg_rate=avg_rate)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)     
    
############################addBestMenu 동적라우팅######################
    
@application.route("/add_menus/<res_name>/")
def add_menus(res_name):
    data = DB.get_restaurant_byname(str(res_name))
    
    return render_template(
        "addBestMenu.html",
        data=data)

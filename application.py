from flask import Flask, render_template, request, flash, redirect, url_for, session
from database import DBhandler
import hashlib
import sys, math

application = Flask(__name__)
application.config["SECRET_KEY"] = "anything-you-want"

DB = DBhandler()

@application.route("/")
def hello():
    return render_template("homeView.html")

@application.route("/signup")
def signup():
    return render_template("signup.html")

@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for('hello'))

@application.route("/signup_post", methods=['POST'])
def register_user():
    data=request.form
    pw=request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    
    if DB.insert_user(data,pw_hash):
        return render_template("login.html")
    else:
        flash("user id already exist!")
        return render_template("signup.html")

@application.route("/login_confirm", methods=['POST'])
def login_user():
    id_=request.form['id']
    pw=request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()

    if DB.find_user(id_,pw_hash):
        session['id']=id_
        return redirect(url_for('hello'))
    else:
        flash("Wrong ID or PW!")
        return render_template("login.html")    
      
@application.route("/addRestaurant")
def reg_restaurant():
    return render_template("addRestaurant.html")

@application.route("/submit_restaurant_post", methods=['POST'])
def reg_restaurant_submit_post():
    global idx
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    #data['img_path']=image_file.filename
    if DB.insert_restaurant(data['name'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="static/image/"+image_file.filename)
    #그 외의 상황 구현 중...
    #else:
        #flash("No image!")
        #return redirect(url_for('addRestaurant'))

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
        flash("Restaurant name already exist!")
        return redirect(url_for('reg_restaurant'))
        #return "Restaurant name already exist!"
    

@application.route("/showAllRestaurantList")
def list_all_restaurants():
    page = request.args.get("page", 0, type=int)
    category = request.args.get("category", "전체")
    limit = 6
    
    start_idx=limit*page
    end_idx=limit*(page+1)
    
    list_idx=range(start_idx, end_idx)
    print(list_idx[2])
    
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
    menu_data = DB.get_food_byname(str(name))
    data = DB.get_restaurant_byname(str(name))
    
    avg_rate = DB.get_avgrate_byname(str(name))
    menu_count = len(menu_data)
    
    print("####data:",data)
    return render_template("showRestaurantDetail.html", menu_data=menu_data, data=data, avg_rate=avg_rate, total=menu_count)

@application.route("/list_foods/<res_name>/")
def view_foods(res_name):
    res_data= DB.get_restaurant_byname(str(res_name))
    data = DB.get_food_byname(str(res_name))
    tot_count = len(data)
    page_count = len(data)
    
    return render_template(
        "showBestMenu.html",
        res_data=res_data,
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
    
@application.route("/add_menus/<res_name>/")
def add_menus(res_name):
    res_data = DB.get_restaurant_byname(str(res_name))
    
    return render_template(
        "addBestMenu.html",
        data=res_data
        )

@application.route("/showRecommendationList/<hashtag>/")
def list_hashtag_restaurants(hashtag):
    page = request.args.get("page", 0, type=int)
    hashtag = request.args.get("hashtag", hashtag)
    limit = 6
    
    start_idx=limit*page
    end_idx=limit*(page+1)
    
    data = DB.get_restaurants_byhash(str(hashtag))

    tot_count = len(data)
    print("hashtag",hashtag,tot_count)

    
    page_count = len(data)
    print(tot_count,page_count)
    return render_template(
        "showRecommendationList.html",
        datas=data,
        total=tot_count,
        limit=limit,
        page=page,
        page_count=math.ceil(tot_count/6),
        hashtag=hashtag)

###############################################################


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)     
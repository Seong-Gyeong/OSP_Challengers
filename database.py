import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
            
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
            
    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        
        for res in restaurants.each():
            value = res.val()
            
            if value['name'] == name:
                return False
        return True 
    
    def menu_duplicate_check(self, name):
        menu_name = self.db.child("menu").get()
        for men in menu_name.each():
            if men.key() == name:
                return False
        return True 
        
    def insert_restaurant(self, name, data, img_path):
        restaurant_info ={
            "name": name,
            "addr": data['restaurant_address'],
            "tel": data['restaurant_contact'],
            "parking": data['restaurant_parking'],
            "open_time": data['restaurant_open_time'],
            "close_time": data['restaurant_close_time'],
            "price_range": data['restaurant_price_range'],
            "site": data['restaurant_homepage'],
            "category": data['restaurant_category'],
            "hashtag": data['hashtag'],
            "introduce": data['restaurant_introduce'],
            "img_path": img_path
        }   
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").push(restaurant_info)
            print(data,img_path)
            return True
        else:
            return False      
        
    def get_restaurants(self):
        restaurants = self.db.child("restaurant").get().val()
        return restaurants
    
    def get_reviews(self):
        reviews = self.db.child("review").get()
        rates=[]
        for rev in reviews.each():
            value = rev.val()
            rates.append(float(value['rating']))
                            
        return float(sum(rates)/len(rates))
        
    def get_avgrate_byname(self,name):
        reviews = self.db.child("review").get()
        rates=[]
        
        for rev in reviews.each():
            value = rev.val()
            if value['res_name'] == name:
                rates.append(float(value['rating']))
                
        if len(rates)==0:
            return 0
        else:
            return float(sum(rates)/len(rates))
        
        reviews = self.db.child("review").get().val()
        return reviews
    
    def get_restaurant_byname(self, name):
        restaurants = self.db.child("restaurant").get()
        target_value=""
        for res in restaurants.each():
            value = res.val()
            
            if value['name'] == name:
                target_value=value
        return target_value
    
    
    def get_food_byname(self, name):
        menus = self.db.child("menu").get()
        target_value=[]
        for men in menus.each():
            value = men.val()
            
            if value['res_name'] == name:
                target_value.append(value)
                
        return target_value

    def get_avgrate_byname(self,name):
        reviews = self.db.child("review").get()
        rates=[]
        for rev in reviews.each():
            value = rev.val()
            if value['res_name'] == name:
                rates.append(float(value['rating']))
                
        if len(rates)==0:
            return 0
        else:
            return float(sum(rates)/len(rates))
    
    def get_review_byname(self, name):
        reviews = self.db.child("review").get()
        target_value=[]
        for rev in reviews.each():
            value = rev.val()
            
            if value['res_name'] == name:
                target_value.append(value)
                
        return target_value
    
    def get_restaurants_bycategory(self, cate):
        restaurants = self.db.child("restaurant").get()
        target_value=[]
        for res in restaurants.each():
            value = res.val()
            
            if value['category'] == cate:
                target_value.append(value)
        print("######target_value",target_value)
        new_dict={}
        for k,v in enumerate(target_value):
            new_dict[k]=v
        
        return new_dict
    
    def get_restaurants_byhash(self, hashtag):
        restaurants = self.db.child("restaurant").get()
        target_value=[]
        for res in restaurants.each():
            value = res.val()
            
            if value['hashtag'] == hashtag:
                target_value.append(value)
                
        return target_value
    

    def insert_menu(self, name, data, img_path):    
        menu_info ={
            "res_name": data['restaurant_name'],
            "menu_name": data['menu_name'],
            "menu_price": data['menu_price'],
            "menu_vegan": data['menu_vegan'],
            "menu_allergy": data['menu_allergy'],
            "menu_introduce": data['menu_introduce'],
            "img_path": img_path
        }   
        self.db.child("menu").child(name).set(menu_info)
        print(data,img_path)
        return True
            
        if self.menu_duplicate_check(name):
            self.db.child("menu").child(name).set(menu_info)
            print(data,img_path)
            return True
        else:
            return False         
        
    def insert_review(self, name, data, img_path):
        review_info ={
            "res_name": data['res_name'],
            "nickname": data['review_reviewer'],
            "rating": data['rating'],
            "comment": data['review_content'],
            "img_path": img_path 
        }   
        self.db.child("review").child(name).set(review_info)
        print(data,img_path)
        return True

    def user_duplicate_check(self, id_string):
        users = self.db.child("user").get()
        
        print("users###",users.val())
        if str(users.val()) == "None": # first registration
            return True
        else:
            for res in users.each():
                value = res.val()
                
                if value['id'] == id_string:
                    return False
            return True    
        
    def insert_user(self, data, pw):
        user_info ={
        "id": data['id'],
        "pw": pw,
        "nickname": data['nickname']
        }
        if self.user_duplicate_check(str(data['id'])):
            self.db.child("user").push(user_info)
            print(data)
            return True
        else:
            return False

    def find_user(self, id_, pw_):
        users = self.db.child("user").get()
        target_value=[]
        for res in users.each():
            value = res.val()
        
        if value['id'] == id_ and value['pw'] == pw_:
            return True    
        return False

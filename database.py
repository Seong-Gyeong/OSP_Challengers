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
            if res.key() == name:
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
            "addr": data['restaurant_address'],
            "tel": data['restaurant_contact'],
            "open_time": data['restaurant_open_time'],
            "close_time": data['restaurant_close_time'],
            "site": data['restaurant_homepage'],
            "img_path": img_path 
        }   
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,img_path)
            return True
        else:
            return False      
        
    def insert_menu(self, name, data, img_path):
        menu_info ={
            "menu_name": data['menu__name'],
            "menu_price": data['menu__price'],
            "menu_allergy": data['menu__allergy'],
            "menu_introduce": data['menu__introduce'],
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
            "nickname": data['review__reviewer'],
            "rating": data['review__rating'],
            "comment": data['review_content'],
            "img_path": img_path 
        }   
        self.db.child("review").child(name).set(review_info)
        print(data,img_path)
        return True
class Restaurant:
    all_restaurants = []  

    def _init_(self, name):
        self.name = name
        self.reviews = []  
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def customers(self):
        reviewing_customers = []
        for review in self.reviews:
            customer = review.get_customer()
            if customer not in reviewing_customers:
                reviewing_customers.append(customer)
        return reviewing_customers

    def add_review(self, review):
        self.reviews.append(review)

    def average_star_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_rating = sum(review.get_rating() for review in self.reviews)
        return total_rating / len(self.reviews)
    
    @classmethod
    def all(cls):
        return cls.all_restaurants
    
    
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")
restaurant3 = Restaurant("Restaurant C")

for restaurant in Restaurant.all_restaurants:
    print(restaurant.get_name())
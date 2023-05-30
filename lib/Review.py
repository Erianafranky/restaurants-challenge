class Review:
    all_reviews = []  
    def _init_(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews

# Sample review instances
review1 = Review("amos kipkorir", "Restaurant A", 4)
review2 = Review("wangechi florence", "Restaurant B", 5)
review3 = Review("dorothy ariana", "Restaurant C", 3)


for review in Review.all():
    print(f"Review by: {review.get_customer()}")
    print(f"Restaurant: {review.get_restaurant()}")
    print(f"Rating: {review.get_rating()}")
    print()
        
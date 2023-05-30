class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

    @classmethod
    def review_all(cls):
        return cls.all_reviews

    def rating(self):
        return self.rating

    
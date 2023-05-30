class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.all_restaurants.append(self)

    @classmethod
    def all_restaurant(cls):
        return cls.all_restaurants

    def add_review(self, review):
        self.reviews.append(review)

    
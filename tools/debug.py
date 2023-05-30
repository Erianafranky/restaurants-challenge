#!/usr/bin/env python3
import ipdb;
class Customer:
    instances = []

    def __init__(self, given_name="amos", family_name="kipkorir"):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = {}
        Customer.instances.append(self)

    def get_given_name(self):
        return self.given_name

    def set_given_name(self, new_given_name):
        self.given_name = new_given_name

    def get_family_name(self):
        return self.family_name

    def set_family_name(self, new_family_name):
        self.family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.instances

    def _repr_(self):
        return f"Customer(given_name='{self.given_name}', family_name='{self.family_name}')"

    def restaurants(self):
        return list(self.reviews.keys())

    def add_review(self, restaurant, rating):
        if restaurant not in self.reviews:
            self.reviews[restaurant] = []
        self.reviews[restaurant].append(int(rating))

    def num_reviews(self):
        return sum(len(reviews) for reviews in self.reviews.values())

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.instances:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = [customer for customer in cls.instances if customer.given_name == name]
        return matching_customers


def main():
    #create test instances
    customer1 = Customer("Amos", "kipkorir")
    customer2 = Customer("kinuthia", "geofrey")
    customer3 = Customer("florence", "wangechi")
    customer4 = Customer("Ariana", "Dorothy")


    print(customer1.get_given_name())
    print(customer1.get_family_name())
    print(customer1.full_name())
    print(customer2.full_name())
    print(customer3.full_name())
    print(customer4.full_name())



    print(Customer.all())

    print(Customer.find_by_name("Amos kipkorir").full_name())
    print([c.full_name() for c in Customer.find_all_by_given_name("Amos")])

main()

if __name__ == '__main__':









# DO NOT REMOVE THIS
    ipdb.set_trace()

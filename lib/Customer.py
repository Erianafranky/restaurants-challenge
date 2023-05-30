
#from Review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all_customers.append(self)

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def customer_all(cls):
        return cls.all_customers

    
from Review import Review
class Customer(Review):
    customers = []
    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)
    
    def get_given_name(self):
        return self._given_name
    def set_given_name(self,given_name):
        self._given_name = given_name
    given_name = property(get_given_name,set_given_name)

    def get_family_name(self):
        return self._family_name
    def set_family_name(self,family_name):
        self._family_name = family_name
    family_name = property(get_family_name,set_family_name)

    def full_name(self):
        name = f"{self.given_name} {self.family_name}"
        print(name)
        return name
    @classmethod
    def all(cls):
        return cls.customers
    def restaurants(self):
        reviews_list = super().all_reviews
        restaurant_list = []
        for review in reviews_list:
            if review['Customer'] == self.full_name():
                restaurant_list.append(review['Restaurant'])
        return restaurant_list
    def add_review(self,restaurant,rating):
        new_review = {'Customer':{self.full_name()},'Restaurant':{restaurant},'Rating':{rating}}
        super().all_reviews.append(new_review)
        
class Review:
    all_reviews = []
    def __init__(self,customer,restaurant,rating):
        self._customer = customer
        self.restaurant = restaurant
        self._rating = rating
        view = {'Customer':{customer},'Restaurant':{restaurant},'Rating':{rating}}
        Review.all_reviews.append(view)

    def rating(self):
        return self._rating
    @classmethod
    def reviews(cls):
        return cls.all_reviews
    def customer(self):
        return self._customer
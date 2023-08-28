class Customer:
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
class DVD:
    def __init__(self, id, title, description, image, vote_average):
        self.id = id
        self.title = title
        self.description = description
        self.image = image
        self.vote_average = vote_average

    def get_dvd_details(self):
        return str(self)

    def __repr__(self): 
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Image: {self.image} \n"

class Tour:
    def __init__(self, id, name, description, image, price, city, date):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.city = city
        self.date = date
    
    def get_tour_details(self):
        return str(self)

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Image: {self.image}, Price: {self.price}, City: {self.city}, Date: {self.date}\n"

class Order:
    def __init__(self, id, status, firstname, surname, email, phone, date, tours, total_cost):
        self.id = id
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.date = date
        self.tours = tours
        self.total_cost = total_cost
    
    def get_tour_details(self):
        return str(self)

    def __repr__(self):
        return f"ID: {self.id}, Status: {self.status}, First Name: {self.firstname}, Surname: {self.surname}, Email: {self.email}, Phone: {self.phone}, Date: {self.date}, Tours: {self.tours}, Total Cost: {self.total_cost}\n"
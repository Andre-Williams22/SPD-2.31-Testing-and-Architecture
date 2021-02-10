# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

class Person:
    def __init__(self, my_age):
        self.age = my_age
        self.LEGAL_DRINKING_AGE = 18

    def enter_night_club(self, my_age):
        if older_than_18_year_old(my_age):
            print("Allowed to enter.")
        else:
            print("Enterance of minors is denited.")

    def older_than_18_year_old(self, age):
        if age > LEGAL_DRINKING_AGE:
            return True
        else: 
            return False
        


# LEGAL_DRINKING_AGE = 18
person = Person(17.9)

person.enter_night_club(person)
# enter_night_club(person)
        

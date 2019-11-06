import datetime
class MovieRental:
    def __init__(self):
        """ Our constructor class that instantiates movie rental shop. """
        self.stock = {
                      "the godfather": 10,
                      "jaws": 9,
                      "alien": 4,
                      "fury": 6,
                      "die hard": 3,
                      "lord of the rings": 2,
                      "the hobbit": 11,
                      "star wars": 5,
                      "harry potter": 4,
                      "hot fuzz": 8,
        }

    def show_stock(self):
        ''' Show current movie stock'''
        print(f"Current movie stock : {self.stock}")
        return self.stock

    def check_stock(self,movie_name):
        ''' Check if given movie is in stock'''
        if movie_name in self.stock:
            if self.stock[movie_name]>0:
                return True
            else:
                return False
        else:
            return False

    def rent_movie_hourly(self,movie_name):
        ''' Rent given movie per hour'''
        if movie_name == "":
            print("Movie name required to make rental")
            return None
        elif self.check_stock(movie_name) == False:
            print(f"{movie_name} is currently out of stock")
            return None
        else:
            now = datetime.datetime.now().replace(microsecond=0)
            print("You have rented {} on hourly basis today at {} o'clock.".format(movie_name,now))
            print("You will be charged €2 for each hour.")
            print("We hope that you enjoy our service.")
            self.stock[movie_name] -= 1
            return now

    def rent_movie_daily(self,movie_name):
        ''' Rent given movie per day'''
        if movie_name == "":
            print("Movie name required to make rental")
            return None
        elif self.check_stock(movie_name) == False:
            print(f"{movie_name} is currently out of stock")
            return None
        else:
            now = datetime.datetime.now().replace(microsecond=0)
            print("You have rented {} on daily basis today at {} o'clock.".format(movie_name,now))
            print("You will be charged €8 daily")
            print("We hope that you enjoy our service.")
            self.stock[movie_name] -= 1
            return now

    def rent_movie_weekly(self,movie_name):
        ''' Rent given movie per week'''
        if movie_name == "":
            print("Movie name required to make rental")
            return None
        elif self.check_stock(movie_name) == False:
            print(f"{movie_name} is currently out of stock")
            return None
        else:
            now = datetime.datetime.now().replace(microsecond=0)
            print("You have rented {} on weekly basis today at {} o'clock.".format(movie_name,now))
            print("You will be charged €24 weekly")
            print("We hope that you enjoy our service.")
            self.stock[movie_name] -= 1
            return now

    def return_movie(self,request):
        ''' Return rented movie '''
        movie_name, rentalTime, rentalBasis = request
        bill = 0

        # issue a bill only if all three parameters are not null!
        if movie_name and rentalTime and rentalBasis:
            if movie_name in self.stock:
                self.stock[movie_name] += 1
                now = datetime.datetime.now().replace(microsecond=0)
                rentalPeriod = now - rentalTime

                # hourly bill calculation
                if rentalBasis == 1:
                    bill = round(rentalPeriod.seconds / 3600) * 2

                # daily bill calculation
                elif rentalBasis == 2:
                    bill = round(rentalPeriod.days) * 20

                # weekly bill calculation
                elif rentalBasis == 3:
                    bill = round(rentalPeriod.days / 7) * 60

                print(f"Thanks for returning your {movie_name}. We hope you enjoyed the movie!")
                print("That would be €{}".format(bill))
                return bill
            else:
                print(f"You have not rented the movie {movie_name}")
                return None
        else:
            print("Are you sure you rented a movie with us?")
            return None


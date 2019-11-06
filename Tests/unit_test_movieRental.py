from unittest import TestCase
from datetime import datetime, timedelta
from customer import Customer
from movie_rental import MovieRental

class TestMovieRental(TestCase):
    def test_Movie_Rental_displays_correct_stock(self):
        shop = MovieRental()
        shop.stock["jaws"] = 10
        self.assertEqual(shop.check_stock("jaws"), True)
        shop.stock["jaws"] = 0
        self.assertEqual(shop.check_stock("jaws"), False)
        shop.stock["jaws"] = -4
        self.assertEqual(shop.check_stock("jaws"), False)

    def test_rent_movie_hourly_for_blank_movie_name(self):
        shop = MovieRental()
        self.assertEqual(shop.rent_movie_hourly(""), None)
    def test_rent_movie_hourly_for_movie_out_of_stock(self):
        shop = MovieRental()
        shop.stock["jaws"] = 0
        self.assertEqual(shop.rent_movie_hourly("jaws"), None)
    def test_rent_movie_hourly_for_valid_movie_name(self):
        shop = MovieRental()
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(shop.rent_movie_hourly("jaws"), now)

    def test_rent_movie_daily_for_blank_movie_name(self):
        shop = MovieRental()
        self.assertEqual(shop.rent_movie_hourly(""), None)
    def test_rent_movie_daily_for_movie_out_of_stock(self):
        shop = MovieRental()
        shop.stock["jaws"] = 0
        self.assertEqual(shop.rent_movie_hourly("jaws"), None)
    def test_rent_movie_daily_for_valid_movie_name(self):
        shop = MovieRental()
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(shop.rent_movie_hourly("jaws"), now)

    def test_rent_movie_weekly_for_blank_movie_name(self):
        shop = MovieRental()
        self.assertEqual(shop.rent_movie_hourly(""), None)
    def test_rent_movie_weekly_for_movie_out_of_stock(self):
        shop = MovieRental()
        shop.stock["jaws"] = 0
        self.assertEqual(shop.rent_movie_hourly("jaws"), None)
    def test_rent_movie_weekly_for_valid_movie_name(self):
        shop = MovieRental()
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(shop.rent_movie_hourly("jaws"),now)

    def test_return_movie_for_invalid_rentalTime(self):
        # create a shop and a customer
        shop = MovieRental()
        customer = Customer("Colm Fitzpatrick")

        # let the customer not rent a bike a try to return one.
        request = customer.return_movie()
        self.assertIsNone(shop.return_movie(request))

        # manually check return function with error values
        self.assertIsNone(shop.return_movie((0,0,0)))

    def test_return_movie_for_invalid_rentalBasis(self):
        # create a shop and a customer
        shop = MovieRental()
        customer = Customer("Colm Fitzpatrick")
        # create valid rentalTime and movie

        customer.rentalTime = datetime.now().replace(microsecond=0)
        customer.movie = "jaws"
        # create invalid rentalbasis

        customer.rentalBasis = 7
        request = customer.return_movie()
        self.assertEqual(shop.return_movie(request), 0)

    def test_return_movie_for_invalid_movie(self):
        # create a shop and a customer
        shop = MovieRental()
        customer = Customer("Colm Fitzpatrick")

        # create valid rentalTime and rentalBasis
        customer.rentalTime = datetime.now().replace(microsecond=0)
        customer.rentalBasis = 1

        # create invalid movie name
        customer.movie = "jaws 2"
        request = customer.return_movie()
        self.assertIsNone(shop.return_movie(request))
    def test_return_movie_for_valid_credentials(self):
        # create a shop and a various customers
        shop = MovieRental()
        customer1 = Customer("Colm Fitzpatrick")
        customer2 = Customer("Ryan Aylward")
        customer3 = Customer("Ross Mccann")
        customer4 = Customer("Nigel Hunter")
        customer5 = Customer("Keith Gorman")
        customer6 = Customer("Eoghan Byrne")

        # create valid rentalBasis for each customer
        customer1.rentalBasis = 1 # hourly
        customer2.rentalBasis = 1 # hourly
        customer3.rentalBasis = 2 # daily
        customer4.rentalBasis = 2 # daily
        customer5.rentalBasis = 3 # weekly
        customer6.rentalBasis = 3 # weekly

        # create valid movies for each customer
        customer1.movie = "jaws"
        customer2.movie = "alien"
        customer3.movie = "fury"
        customer4.movie = "die hard"
        customer5.movie = "lord of the rings"
        customer6.movie = "star wars"

        # create past valid rental times for each customer
        customer1.rentalTime = (datetime.now() + timedelta(hours=-4)).replace(microsecond=0)
        customer2.rentalTime = (datetime.now() + timedelta(hours=-23)).replace(microsecond=0)
        customer3.rentalTime = (datetime.now() + timedelta(days=-4)).replace(microsecond=0)
        customer4.rentalTime = (datetime.now() + timedelta(days=-13)).replace(microsecond=0)
        customer5.rentalTime = (datetime.now() + timedelta(weeks=-6)).replace(microsecond=0)
        customer6.rentalTime = (datetime.now() + timedelta(weeks=-12)).replace(microsecond=0)

        # make all customers return their bikes
        request1 = customer1.return_movie()
        request2 = customer2.return_movie()
        request3 = customer3.return_movie()
        request4 = customer4.return_movie()
        request5 = customer5.return_movie()
        request6 = customer6.return_movie()

        # check if all of them get correct bill
        self.assertEqual(shop.return_movie(request1), 8)
        self.assertEqual(shop.return_movie(request2), 46)
        self.assertEqual(shop.return_movie(request3), 80)
        self.assertEqual(shop.return_movie(request4), 260)
        self.assertEqual(shop.return_movie(request5), 360)
        self.assertEqual(shop.return_movie(request6), 720)

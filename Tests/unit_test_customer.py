from unittest import TestCase
from datetime import datetime, timedelta
from customer import Customer

class UnitTestCustomer(TestCase):
    def test_show_currently_rented_with_none(self):
        # create a customer
        customer = Customer("Colm Fitzpatrick")
        self.assertEqual(customer.show_currently_rented(),(None))
    def test_show_currently_rented_with_invalid_rentalTime(self):
        customer = Customer("Colm Fitzpatrick")
        customer.rentalBasis = 1
        customer.movie = "jaws"
        self.assertEqual(customer.show_currently_rented(),(None))
    def test_show_currently_rented_with_invalid_rentalBasis(self):
        customer = Customer("Colm Fitzpatrick")
        customer.rentalTime = datetime.now().replace(microsecond=0)
        customer.movie = "jaws"
        self.assertEqual(customer.show_currently_rented(),(None))
    def test_show_currently_rented_with_valid_movie(self):
        customer = Customer("Colm Fitzpatrick")
        customer.rentalTime = datetime.now().replace(microsecond=0)
        customer.rentalBasis = 1
        customer.movie = "jaws"
        self.assertEqual(customer.show_currently_rented(),("jaws"))

    def test_rent_movie_with_exit(self):
        customer = Customer("Colm Fitzpatrick")
        with self.assertRaises(SystemExit) as cm:
            customer.rent_movie("jaws","exit")
        self.assertEqual(cm.exception.code, 1)
    def test_rent_movie_with_invalid_movie(self):
        customer = Customer("Colm Fitzpatrick")
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(customer.rent_movie("jaws 2","hourly"),None)
    def test_rent_movie_with_valid_hourly(self):
        customer = Customer("Colm Fitzpatrick")
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(customer.rent_movie("jaws","hourly"),("jaws",now,1))
    def test_rent_movie_with_valid_daily(self):
        customer = Customer("Colm Fitzpatrick")
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(customer.rent_movie("jaws","daily"),("jaws",now,2))
    def test_rent_movie_with_valid_weekly(self):
        customer = Customer("Colm Fitzpatrick")
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(customer.rent_movie("jaws","weekly"),("jaws",now,3))

    def test_return_movie_with_valid_input(self):
        customer = Customer("Colm Fitzpatrick")

        # create valid rentalTime, rentalBasis, movie
        now = datetime.now().replace(microsecond=0)
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.movie = "jaws"
        self.assertEqual(customer.return_movie(),("jaws",now,1))

    def test_return_movie_with_invalid_input(self):
        customer = Customer("Colm Fitzpatrick")

        # create valid rentalBasis and movie
        customer.rentalBasis = 1
        customer.movie = "jaws"

        # create invalid rentalTime
        customer.rentalTime =  0
        self.assertEqual(customer.return_movie(),(0,0,0))

from random import randint, choice

import factory
from models.booking import Booking
from models.model_enums import BookingState

class BookingFactory(factory.Factory):
    class Meta:
        model = Booking

    email=factory.Faker('company_email')
    phone_no = factory.Faker('numerify', text='###-###-####')
    passcode = "123456"
    #date required
    #am_or_pm required
    #booking_type required
    num_of_persons = factory.LazyAttribute(lambda x: randint(1,8))
    vehicle_licence_plate = factory.Faker('bothify', text='?#?#?#', letters='ABCEGHJKLMNPRSTVXY')
    application_datetime = factory.Faker('past_datetime', start_date='-30d')
    state = factory.LazyAttribute(lambda x: choice([state.value for state in BookingState]))

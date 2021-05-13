import factory
from models.booking import Booking

class BookingFactory(factory.Factory):
    class Meta:
        model = Booking
    
    id = 2
    email=factory.Faker('company_email')
    phone_no = factory.Faker('numerify', text='###-###-####')
    passcode = "123456"
    #date required
    #am_or_pm required
    #booking_type required
    num_of_persons = 4
    vehicle_licence_plate = factory.Faker('bothify', text='?#?#?#', letters='ABCEGHJKLMNPRSTVXY')
    application_datetime = factory.Faker('past_datetime', start_date='-15d')
    state="WAITING"

import enum

class BookingState(enum.Enum):
    waiting = "WAITING"
    standby = "STANDBY"
    opt_out = "OPT-OUT"
    pass_offered = "PASS OFFERED"
    booking_confirmed = "BOOKING CONFIRMED"
    pass_canceled = "PASS CANCELED"

class CapacityType(enum.Enum):
    trail = "Trail"
    vehicle = "Vehicle"
    
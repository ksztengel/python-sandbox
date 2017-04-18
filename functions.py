def currency_converter(rate, euros):
    dollars = euros*rate
    return dollars
print(currency_converter(1.20, 1000))


def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

print(minutes_to_hours(135))

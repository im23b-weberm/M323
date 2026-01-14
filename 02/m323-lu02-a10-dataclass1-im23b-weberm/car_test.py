from car import Car


def test_car_initialization():
    car = Car(brand='Toyota', mileage=9500)
    assert car.brand == 'Toyota'
    assert car.mileage == 9500
    assert car.service_dates == []


def test_car_with_service_dates():
    car = Car(brand='Honda', mileage=12000, service_dates=['2024-08-28'])
    assert car.brand == 'Honda'
    assert car.mileage == 12000
    assert car.service_dates == ['2024-08-28']

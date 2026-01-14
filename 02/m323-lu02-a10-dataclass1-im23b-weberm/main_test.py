from car import Car
from main import add_mileage, check_service
import subprocess


def test_add_mileage():
    car = Car(brand='Toyota', mileage=9500)
    updated_car = add_mileage(car, 600)
    assert updated_car.mileage == 10100
    assert updated_car.service_dates == ['2024-08-28']

    updated_car = add_mileage(updated_car, 100)
    assert updated_car.mileage == 10200
    assert updated_car.service_dates == ['2024-08-28']


def test_check_service():
    car = Car(brand='Toyota', mileage=9500)
    assert check_service(car) is False

    car = Car(brand='Toyota', mileage=10500)
    assert check_service(car) is True


def test_integration():
    # Execute the main.py script and capture the output
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)

    # Expected output
    expected_output = (
        "Vor der Fahrt: Car(brand='Toyota', mileage=9500, service_dates=[])\n"
        "Nach der ersten Fahrt: Car(brand='Toyota', mileage=10100, service_dates=['2024-08-28'])\n"
        'Service erforderlich!\n'
        "Nach der zweiten Fahrt: Car(brand='Toyota', mileage=10200, service_dates=['2024-08-28'])\n"
        "Service-Daten: ['2024-08-28']\n"
    )

    assert result.stdout == expected_output

def fahrenheit_to_celsius(value: float):
  return (value - 32) * 5 / 9


def celsius_to_fahrenheit(value: float):
  return (value * 9 / 5) + 32


def kelvin_to_celsius(value: float):
  return value - 273.15


def celsius_to_kelvin(value: float):
  return value + 273.15


class Temperature:
  def __init__(self) -> None:
    self._value = None

  def set_celsius(self, value: float):
    self._value = value

  def set_fahrenheit(self, value: float):
    self._value = fahrenheit_to_celsius(value)

  def set_kelvin(self, value: float):
    self._value = kelvin_to_celsius(value)

  def get_celsius(self):
    return self._value

  def get_fahrenheit(self):
    if self._value is None:
      return None

    return celsius_to_fahrenheit(self._value)

  def get_kelvin(self):
    if self._value is None:
      return None

    return celsius_to_kelvin(self._value)


temp = Temperature()

print(temp.get_celsius())

temp.set_celsius(10)

print(temp.get_celsius())

temp.set_celsius(10)

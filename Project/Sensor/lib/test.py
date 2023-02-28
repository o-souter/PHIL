from sensors.FakeTestSensor import FakeTestSensor
from utilities.data import collect_data

sensors = [];
sensors.append(FakeTestSensor("Light One"))
sensors.append(FakeTestSensor("Mock"))



print(collect_data(sensors))

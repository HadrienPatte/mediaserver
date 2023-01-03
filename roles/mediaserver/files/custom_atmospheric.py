import smbus2
import bme280
from checks import AgentCheck


class AtmosphericCheck(AgentCheck):
    __NAMESPACE__ = "atmospheric"

    def check(self, instance):
        port = self.instance.get("port", 1)
        address = self.instance.get("address", 0x76)
        tags = self.instance.get("tags", [])

        bus = smbus2.SMBus(port)

        calibration_params = bme280.load_calibration_params(bus, address)

        data = bme280.sample(bus, address, calibration_params)

        self.gauge("temperature", data.temperature, tags=tags)
        self.gauge("pressure", data.pressure, tags=tags)
        self.gauge("humidity", data.humidity, tags=tags)

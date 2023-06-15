import smbus2
import bme280
from checks import AgentCheck


class AtmosphericCheck(AgentCheck):
    __NAMESPACE__ = "atmospheric"

    def __init__(self, name, init_config, instances):
        super(AtmosphericCheck, self).__init__(name, init_config, instances)

        port = self.instance.get("port", 1)
        self.address = self.instance.get("address", 0x76)
        self.tags = self.instance.get("tags", [])

        self.bus = smbus2.SMBus(port)

        self.calibration_params = bme280.load_calibration_params(self.bus, self.address)

    def check(self, _):
        data = bme280.sample(self.bus, self.address, self.calibration_params)

        self.gauge("temperature", data.temperature, tags=self.tags)
        self.gauge("pressure", data.pressure, tags=self.tags)
        self.gauge("humidity", data.humidity, tags=self.tags)

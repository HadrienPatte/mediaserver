import os
from checks import AgentCheck


class ThermalCheck(AgentCheck):
    __NAMESPACE__ = "thermal"

    def __init__(self, name, init_config, instances):
        super(ThermalCheck, self).__init__(name, init_config, instances)

        self.tags = self.instance.get("tags", [])

    def check(self, _):
        thermal_sysfs = "/sys/class/thermal"
        thermal = {}

        for zone in os.listdir(thermal_sysfs):
            zone_path = os.path.join(thermal_sysfs, zone)
            temp_file = os.path.join(zone_path, "temp")
            type_file = os.path.join(zone_path, "type")
            thermal[zone] = {"tags": [f"zone:{zone}"]}

            if os.path.isfile(temp_file):
                with open(temp_file) as f:
                    temp = int(f.read().strip()) / 1000
                    thermal[zone]["temp"] = temp

            if os.path.isfile(type_file):
                with open(type_file) as f:
                    thermal[zone]["tags"].append(f"type:{f.read().strip()}")

            for zone in thermal.values():
                if zone.get("temp"):
                    self.gauge(
                        "temp", zone.get("temp"), tags=zone.get("tags") + self.tags
                    )

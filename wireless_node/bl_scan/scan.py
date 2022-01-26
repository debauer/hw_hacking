# simple inquiry example
import csv
from copy import copy
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Union
import pathlib
import bluetooth
import asyncio
import time
from threading import Thread
from bleak import BleakScanner

companys = []


def get_company(mac: str):
    if len(companys) == 0:
        csv_path = pathlib.Path(__file__).parent.parent.joinpath("oui.csv")
        with open(csv_path.as_posix(), "r") as file:
            reader = csv.reader(file)
            for row in reader:
                companys.append((row[0], row[1], row[2]))
    for row in companys:
        if row[1] == mac.replace(":", ""):
            return row[2]
    return "NOT FOUND"


@dataclass
class Device:
    rssi = 0
    name = ""
    address = ""
    ble = False
    bl = False
    details: Dict[str, Union[str, Dict[str, str]]] = dict
    metadata = ""
    __timestamp = datetime.now()
    __company = "UNKNOWN"
    __outdated: int = 150

    def update_timestamp(self):
        self.__timestamp = datetime.now()

    def is_apple(self):
        return (
            self.name.replace("-", ":") == self.address
            and "props" in self.details
            and "AddressType" in self.details["props"]
            and self.details["props"]["AddressType"] == "random"
        )

    def seconds(self, seconds: int):
        maximum = 999
        if seconds > maximum:
            seconds = maximum
        return "{:3s}".format(str(seconds))
    
    def age(self):
        return int((datetime.now() - self.__timestamp).total_seconds())

    def time_status(self):
        bar_lenght = 20
        seconds = self.age()
        bar_seconds = seconds
        if bar_seconds > bar_lenght:
            bar_seconds = bar_lenght
        return (
            self.seconds(seconds)
            + " "
            + "#" * bar_seconds
            + (" " * bar_lenght)[bar_seconds:]
        )
    
    def is_outdated(self):
        return self.age() > self.__outdated
        

    def company(self):
        if self.__company == "UNKNOWN":
            self.__company = get_company(self.address[:8])
        if self.__company == "NOT FOUND" and self.is_apple():
            return "Apple? (random MAC)"
        return self.__company

    def __str__(self):
        return "{} {} {:20s} {:5s} {:5s} {:5s} {}".format(
            self.time_status(),
            self.address,
            self.name,
            self.bl and "x_x" or "",
            self.ble and "x_x" or "",
            str(self.rssi),
            self.company(),
        )
        # return f"{self.time_status()} {self.address} {self.name} {self.bl} {self.ble}"


found_devices: Dict[str, Device] = {}


def bl():
    while True:
        nearby_devices = bluetooth.discover_devices(
            duration=8, lookup_names=True, flush_cache=True, lookup_class=False
        )
        for addr, name in nearby_devices:
            if not addr in found_devices:
                found_devices[addr] = Device()
                found_devices[addr].name = name
                found_devices[addr].address = addr
            found_devices[addr].bl = True
            found_devices[addr].update_timestamp()
        time.sleep(0.1)


def ble():
    async def ble_async():
        while True:
            devices = await BleakScanner.discover()
            for dev in devices:
                if not dev.address in found_devices:
                    device = Device()
                    device.name = dev.name
                    device.address = dev.address
                    found_devices[dev.address] = device
                device = found_devices[dev.address]
                device.rssi = dev.rssi
                device.details = dev.details
                device.metadata = dev.metadata
                device.ble = True
                device.update_timestamp()
            time.sleep(0.1)

    asyncio.run(ble_async())


def print_all():
    while True:
        print(chr(27) + "[2J")
        print(
            'SEC AGE "BAR"            MAC               NAME                 BL    BLE   RSSI  COMPANY'
        )
        devices = copy(found_devices)
        for addr in sorted(devices):
            if not devices[addr].is_outdated():
                if (
                    devices[addr].name.replace("-", ":") == devices[addr].address
                    and devices[addr].details["props"]["AddressType"] == "random"
                ):
                    print(devices[addr])
                else:
                    print(devices[addr])
        time.sleep(0.2)


try:
    threads = []
    threads.append(Thread(target=bl, args=()))
    threads.append(Thread(target=ble, args=()))
    threads.append(Thread(target=print_all, args=()))

    for t in threads:
        t.daemon = True
        t.start()

    for t in threads:
        t.join()

except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting threads.")

import smbus

DEVICE_BUS = 1
SLAVE_ADDR = 0x04

bus = smbus.SMBus(DEVICE_BUS)


def turnSensorOn():
    bus.write_byte(SLAVE_ADDR, 0x01)


def getLightLevel():
    return bus.read_byte(SLAVE_ADDR)


def processLightLevel(lightLevel):
    if lightLevel < 20:
        print("Too Dark")
    elif lightLevel >= 20 and lightLevel < 40:
        print("Dark")
    elif lightLevel >= 40 and lightLevel < 60:
        print("Medium")
    elif lightLevel >= 60 and lightLevel < 80:
        print("Bright")
    elif lightLevel >= 80 and lightLevel < 100:
        print("Too Bright")


def main():
    turnSensorOn();
    lightLevel = getLightLevel()
    processLightLevel(lightLevel)


if __name__ == "__main__":
    main()


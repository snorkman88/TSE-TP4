"""
The HW will make use of the onboard RGB LED on the dev board to indicate 
the battery level.

NOTE: Use this feature FOR DEBUGGING PURPOSES ONLY. 

HOW TO USE IT:
By default, this feature is ENABLED. Short 'P10' to GND, to disable it. 
"""
#DEBUG_ENABLE_PIN = False

#RGB_LED = 0x000000
#LED_OFF = 0x000000
#RED = 0xff0000
#GREEN = 0x00ff00

#VALOR_CRITICO = 1965


###-----------------MOCKUPs----------------------###
class Pin:
    """
    This class is just a mimic of Pycom's Machine.Pin behaviour.

    https://docs.pycom.io/firmwareapi/pycom/machine/pin/
    """
    IN = 1
    PULL_UP = 1
    def __init__(self, *args, **kwargs):
        pass
    def __call__(self):
        global DEBUG_ENABLE_PIN
        return DEBUG_ENABLE_PIN

class pycom:
    def rgbled(valor):
        global RGB_LED
        RGB_LED = valor


###--------------------FUNCTION TO BE TESTED-------------------###
def voltage_indicator(adc_value):
    global RED
    global GREEN
    global VALOR_CRITICO

    ENABLE_LED_INDICATOR = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)

    if ENABLE_LED_INDICATOR():
        if adc_value < VALOR_CRITICO:
            pycom.rgbled(RED)
        if adc_value >= VALOR_CRITICO:
            pycom.rgbled(GREEN)
    else:
            pycom.rgbled(LED_OFF)


import pytest
import time
from ..voltage_indicator import *

"""
The HW will make use of the onboard RGB LED on the dev board to indicate 
the battery level.

NOTE: Use this feature FOR DEBUGGING PURPOSES ONLY. 

HOW TO USE IT:
By default, this feature is ENABLED. Short 'P10' to GND, to disable it. 
"""
DEBUG_ENABLE_PIN = False

RGB_LED = None
LED_OFF = 0x000000
RED = 0xff0000
GREEN = 0x00ff00

VALOR_CRITICO = 1965


###--------------------TESTs-------------------###
def test_voltage_indicator_disabled():
    global DEBUG_ENABLE_PIN
    global RGB_LED
    DEBUG_ENABLE_PIN = False
    ADC_VALUE = VALOR_CRITICO + 1
    voltage_indicator(ADC_VALUE)
    assert hex(RGB_LED) == hex(LED_OFF)

def test_voltage_indicator_low_batt():
    global DEBUG_ENABLE_PIN
    global RGB_LED
    DEBUG_ENABLE_PIN = True
    ADC_VALUE = VALOR_CRITICO - 1
    voltage_indicator(ADC_VALUE)
    assert hex(RGB_LED) == hex(RED)

def test_voltage_indicator_batt_ok_limit():
    global DEBUG_ENABLE_PIN
    global RGB_LED
    DEBUG_ENABLE_PIN = True
    ADC_VALUE = VALOR_CRITICO
    voltage_indicator(ADC_VALUE)
    assert hex(RGB_LED) == hex(GREEN)

def test_voltage_indicator_batt_ok():
    global DEBUG_ENABLE_PIN    
    global RGB_LED
    DEBUG_ENABLE_PIN = True
    ADC_VALUE = VALOR_CRITICO + 1
    voltage_indicator(ADC_VALUE)
    assert hex(RGB_LED) == hex(GREEN)

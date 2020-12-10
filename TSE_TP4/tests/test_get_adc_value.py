import pytest
from ..get_supercap_voltage import enable_3v3, enable_5V, get_ADC_value
VALOR_CRITICO = 1965

###-------------------------TESTS--------------------------------###

def test_get_ADC_value_invalid_pin_integer():
    value = get_ADC_value(13)
    assert value == -3

def test_get_ADC_value_from_invalid_pin_non_analog():
    value = get_ADC_value('P12')
    assert value == -3

def test_get_ADC_from_valid_pin():
    value = get_ADC_value('P13')
    assert value == 1965
    assert isinstance(value, int)


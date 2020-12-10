import pytest
from TSE_TP4.get_supercap_voltage import *
VALOR_CRITICO = 1965

###-------------------------TESTS--------------------------------###
def test_NO_habilitar_3v3_si_vcap_es_menor(mocker):
    mocker.patch(__name__ + ".get_ADC_value", return_value=1964)
    switch_3v3 = enable_3v3()
    assert switch_3v3 == False

def test_SI_habilitar_3v3_si_vcap_es_igual(mocker):
    mocker.patch(__name__ + ".get_ADC_value", return_value=1965)
    switch_3v3 = enable_3v3()
    assert switch_3v3 == True

def test_SI_habilitar_3v3_si_vcap_es_mayor(mocker):
    mocker.patch(__name__ + ".get_ADC_value", return_value=1966)
    switch_3v3 = enable_3v3()
    assert switch_3v3 == True

def test_NO_habilitar_5V_si_vcap_es_menor(mocker):
    mocker.patch(__name__ + ".get_ADC_value", return_value=1964)
    switch_5V = enable_5V()
    assert switch_5V == False

def test_SI_habilitar_5V_si_vcap_es_igual(mocker):
    mocker.patch(__name__ + ".get_ADC_value", return_value=1965)
    switch_5V = enable_5V()
    assert switch_5V == True

def test_SI_habilitar_5V_si_vcap_es_mayor(mocker):
    mocker.patch(__name__ + ".get_ADC_value", return_value=1966)
    switch_5V = enable_5V()
    assert switch_5V == True

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


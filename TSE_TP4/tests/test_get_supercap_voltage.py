import pytest
from ..get_supercap_voltage import enable_3v3, enable_5V
from .. import get_supercap_voltage

VALOR_CRITICO = 1965

###-------------------------TESTS--------------------------------###
def test_NO_habilitar_3v3_si_vcap_es_menor(mocker):
    mocker.patch(get_supercap_voltage.__name__ + ".get_ADC_value", return_value=1964)
    switch_3v3 = enable_3v3()
    assert switch_3v3 == False

def test_SI_habilitar_3v3_si_vcap_es_igual(mocker):
    mocker.patch(get_supercap_voltage.__name__ + ".get_ADC_value", return_value=1965)
    switch_3v3 = enable_3v3()
    assert switch_3v3 == True

def test_SI_habilitar_3v3_si_vcap_es_mayor(mocker):
    mocker.patch(get_supercap_voltage.__name__ + ".get_ADC_value", return_value=1966)
    switch_3v3 = enable_3v3()
    assert switch_3v3 == True

def test_NO_habilitar_5V_si_vcap_es_menor(mocker):
    mocker.patch(get_supercap_voltage.__name__ + ".get_ADC_value", return_value=1964)
    switch_5V = enable_5V()
    assert switch_5V == False

def test_SI_habilitar_5V_si_vcap_es_igual(mocker):
    mocker.patch(get_supercap_voltage.__name__ + ".get_ADC_value", return_value=1965)
    switch_5V = enable_5V()
    assert switch_5V == True

def test_SI_habilitar_5V_si_vcap_es_mayor(mocker):
    mocker.patch(get_supercap_voltage.__name__ + ".get_ADC_value", return_value=1966)
    switch_5V = enable_5V()
    assert switch_5V == True

import pytest
import time

VALOR_CRITICO = 1965

###-------------------------MOCKUPS ----------------------------------###
def sleep_ms(sleep_time_in_miliseconds):
    """
    Since 'time' library does not have delay in miliseconds implemented, 
    this function will be attached to it in order to replicate the exact 
    same one as Pycom's.
    https://medium.com/@mgarod/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6
    """
    time.sleep(sleep_time_in_miliseconds/1000)

#Attach the method "sleep_ms" to the existingclass on runtim
setattr(time, "sleep_ms", sleep_ms) 

class adc:
    """
    This is a dummy mock for Pycom's ADC class.
    It receives two useless arguments and returns another function
    that when invoked, returns a mocked ADC value of 1900
    """
    ATTN_11DB = None
    def channel(pin, attn):
        def read():
            return 1965
        return read

###-------------------Functions to be tested-------------------###

def enable_3v3():
    global VALOR_CRITICO
    v_cap = get_ADC_value()
    if v_cap < VALOR_CRITICO:
        return False
    if v_cap >= VALOR_CRITICO:
        return True

def enable_5V():
    global VALOR_CRITICO
    v_cap = get_ADC_value()
    if v_cap < VALOR_CRITICO:
        return False
    if v_cap >= VALOR_CRITICO:
        return True

def get_ADC_value(adc_input_pin):
    """
    PARAMS: adc_pin, is a 'str' contianing the analog input of the LoPy4 module
    RETURNS: an 'int' representing the average of 20 samples.
    """
    VALID_ADC_PINS = ['P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20']
    if isinstance(adc_input_pin, str) and adc_input_pin in VALID_ADC_PINS:
        samples = []
        adc_pin = adc.channel(pin=adc_input_pin, attn=adc.ATTN_11DB)
        for sample in range(20):
            val = adc_pin()# read an analog value
            samples.append(val)
            time.sleep_ms(1)
        average = sum(samples)/len(samples)
        #print("Average value: ", average)
        return int(average)
    else:
        print("The chosen pin is not a valid ADC port or not a string with the format 'Pxx'")
        print("Received ", adc_input_pin)
        return -3

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


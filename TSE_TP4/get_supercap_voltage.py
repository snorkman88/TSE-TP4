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
    that when invoked, returns a mocked ADC value of 1965
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


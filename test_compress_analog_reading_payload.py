import pytest

###------------------------FUNCTION TO BE TESTED--------------------------###
def compress_analog_reading_payload(mediciones):
     """
     # el orden es mediciones = [0x111, 0x222, 0x333, 0xccc]
     # para hacer una anidacion de todos tengo que ir corriendo de a 12 bits
     # 1 tribble = 3 nibbles = 12 bits
     """
     payload = 0
     if isinstance(mediciones, list) and len(mediciones) == 4:
        tribble_shifts = len(mediciones) - 1
     else:
        return -1
        
     if all(isinstance(medicion, int) for medicion in mediciones):
         for medicion in mediciones:
             #print(medicion << (12 * tribble_shifts))
             payload = payload | (medicion << (12 * tribble_shifts))
             tribble_shifts -=1
         return(payload)
     else:
         return -2


###--------------------------------TESTs------------------------------###
def test_tipo_de_variable_invalido_str():
    mediciones = "22"
    payload = compress_analog_reading_payload(mediciones)
    assert payload == -1

def test_tipo_de_variable_invalido_dict():
    mediciones = {'payload': 6}
    payload = compress_analog_reading_payload(mediciones)
    assert payload == -1

def test_tamano_invalido_de_lista():
    mediciones = [0x111]
    payload = compress_analog_reading_payload(mediciones)
    assert payload == -1

def test_contenido_de_lista_invalido():
    mediciones = [0x111, 0x222, 'a', 0x444]
    payload = compress_analog_reading_payload(mediciones)
    assert payload == -2

def test_valido_de_lista():
    mediciones = [0x111, 0x222, 0x333, 0x444]
    payload = compress_analog_reading_payload(mediciones)
    assert payload == 18769580864580


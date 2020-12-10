import pytest
from ..compress_analog_reading_pyload import compress_analog_reading_payload

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


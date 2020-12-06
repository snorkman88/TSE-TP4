# TSE-TP4
Trabajo Practico 4 de seminario de testing en sistemas embebidos.  

# Requerimientos  
Antes de correr las pruebas, instalar las dependencias necesarias mediante el comando:  
`pip install -r requirements.txt` 

Luego ejecutar el commando:  
`pytest -vv`  

# Comentarios acerca de los tests  
## test_voltage_indicator.py  
En este test se verifica el funcionamiento del indicador de tension en bornes del acumulador.  
El indicador de tension consiste en utilizar un led RGB integrado en la placa de desarrollo, para indicar si la tension en bornes del acumulador está por debajo o por encima de un valor critico de 1,5V.  
1.  El LED se encenderá en ROJO si la tension en bornes del acumulador esta por debajo de 1,5V.  
2.  El LED se encenderá en VERDE si la tension es igual o mayor a 1,5V.  
3.  El led permanecera APAGADO si se deshabilita el indicador.  

El indicador de tension se habilita o desabilita por hardware. Su estado por defecto es habilitado, en caso de querer deshabilitarlo se deberá hacer un corto a GND del pin "P10", contribuyendo este estado al ahorro de energía.  
### Mockups 
Para realizar una mimica del comportamiento de las dependencias externas se han agregado dos clases en la seccion "mockups" que simulan las lecturas del estado de un pin como así tambien de el control del LED RGB.  

## test_get_supercap_voltage.py
En esta bateria de tests, se verifica el funcionamiento de 3 funciones que se encargan de:
1.  habilitar o deshabilitar etapas de electronica que funcionan a 3.3V o 5V mediante un interruptor de estado solido.  
![switches][switches.png]  
..1. Si la tension es menor a 1,5V, no se deberá activar el switch de 3.3V ni 5V
..2. Si la tension es mayor a 1,5V, no se deberá activar el switch de 3.3V ni 5V
2. Tomar una lectura de una senal analogica a la entrada de un PIN de la placa de desarrollo.  

###Mockups
Para realizar una mimica del comportamiento de las dependencias externas se ha agregado una clase llamada ADC que realiza un mimica del comportamiento del hardware.  
Ademas, dado que por defecto la biblioteca "time" de python no incluye el metodo 'sleep_ms' y a fines practicos, se agrega dicho metodo en tiempo de ejecucion a la biblioteca 'time' mediante setattr(time, 'sleep_ms', sleep_ms).

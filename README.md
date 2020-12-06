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


# WTFinance

### Herramientas usadas en la prueba técnica

Se define trabajar con entornos virtuales desde la distribución anaconda bajo el lenguaje Python, por su facilidad y compatibilidad con VSCode.

### Pasos para poner en marcha el proyecto

1. Crear un enterno virtual desde los comandos Anaconda o los comandos virtualenv. Comando conda (`conda create -n nombre_entorno python=versión`). Versión de Python = 3.10.4 (El entorno es opcional)
2. Instalar las librerias necesarias para ejecutar el proyecto (`pip install requests`). La librería SQLite3 no es necesario instalarla viene por defecto en el core de Python.
3. Modificar el `API Key` en la línea de código 18 del fichero `getting.py`, ya que cada usuario tiene su propio API Key a partir de su cuenta gratuita
4. Descomentar la línea de código 15 en el fichero main.py
5. Descomentar las líneas de código `print(json)` en el fichero `getting.py` si quiere ver la trama Json que devuelve la petición `GET` desde el API de coinMarketCap
6. Ejecutar el script de Python

En los resultados por consola de visualizan los datos en Json si se descomentarón las líneas `print(json)` sino solo se verán los datos formateados en String concatenados y en tuplas dentro de una lista, con el mensaje `Done` al final.

En el siguiente enlace se puede apreciar en video la ejecución del proyecto: `https://youtu.be/iBOt3ohYEDo`

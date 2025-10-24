Si el microservicio debe comunicarse con otro que guardar el historial de cálculos, debe pasar a ser un servicio dentro de una arquitectura de microservicios, el microservicio actual sólo recibe un número por URL, calcula su factorial  y devuelve
el resultado en un JSON, todo de forma local, sin nada de persistencia, pero el nuevo servicio debe encargarse de conectarse a la base de datos y guardar el historial de cálculos, podríamos tener el primer microservicio que
envíe post al servicio historial, y el servicio historial recibiría post del servicio factorial, el código podría verse más o menos así:

** 
 try:
        requests.post("http://historial-servicio:5001/api/historial", json=datos)
    except Exception as e:
        print("No se pudo registrar el historial")

  **


  Y luego se armaría el microservicio historial.

  Los beneficios que podría traer esto son:
1. Separación de responsabilidades
2. Más oportunudad de escalabilidad
3. Mayor tolerancia a fallos

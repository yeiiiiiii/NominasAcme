import json

def DatosCargar():
    try:
        with open('Datos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def DatosGuardar(data):
    with open('Datos.json', 'w') as file:
        json.dump(data, file, indent=4) 

def validacion_EncontrarEmpleado(empleados, ID):
    for empleado in empleados:
        if empleado['Identificacion'] == ID:
            return empleado
    return None

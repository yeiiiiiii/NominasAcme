from modulos.validaciones import*

def CalcularNomina():
    empleados = DatosCargar()
    for empleado in empleados:
        salario = empleado['Salario']
        inasistencias = len(empleado['Inasistencias'])
        total_bonos = sum(bono['Valor'] for bono in empleado['Bonos'])

        descuento_salud = salario * 0.04
        descuento_pension = salario * 0.04
        descuento_faltas = (salario / 30) * inasistencias  

        auxilio_transporte = 0
        if salario < 1000000:  # Salario mínimo
            auxilio_transporte = salario * 0.10

        total_descuentos = descuento_salud + descuento_pension + descuento_faltas
        total_a_pagar = salario + total_bonos + auxilio_transporte - total_descuentos

        with open(f"{empleado['Identificacion']}.txt", 'w') as file:
            file.write(f"Identificacion: {empleado['Identificacion']}\n")
            file.write(f"Nombre: {empleado['Nombre']}\n")
            file.write(f"Cargo: {empleado['Cargo']}\n")
            file.write(f'Salario: {salario}\n')
            file.write(f'Descuento por salud: {descuento_salud}\n')
            file.write(f'Descuento por pensión: {descuento_pension}\n')
            file.write(f'Descuento por faltas: {descuento_faltas}\n')
            file.write(f'Auxilio de transporte: {auxilio_transporte}\n')
            file.write(f'Total de bonos: {total_bonos}\n')
            file.write(f'Total a pagar: {total_a_pagar}\n')

        print('********************************************************************')
        print(f"La nómina generada para {empleado['Nombre']} ya quedo lista 😊")
        print('********************************************************************')
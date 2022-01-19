# from => archivo import => la clase
from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(4.5, 300)
print(cuenta1)

cuenta2 = CuentaBancaria(6.5, 700)
print(cuenta2)

cuenta1.deposito(200).deposito(300).deposito(300).retiro(200).genera_interes().mostrar_info_cuenta()

cuenta2.deposito(200).deposito(199).retiro(20).retiro(5).retiro(67).retiro(10).genera_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas()
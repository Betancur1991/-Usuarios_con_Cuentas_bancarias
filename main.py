from CuentaBancaria import CuentaBancaria, Usuario

daniel=Usuario("Daniel","danielfbc1991@gmail.com")


daniel.info_todas_las_cuentas_de_un_usuario()
daniel.cuenta['ahorros'].deposito(3000)
daniel.info_todas_las_cuentas_de_un_usuario()
daniel.cuenta['corriente'].deposito(3000).generar_interes().retiro(300).mostrar_info_cuenta()
daniel.info_todas_las_cuentas_de_un_usuario()









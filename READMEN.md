# P1 LABS

## Ejercicio para Odoo Developer

### Contexto

La empresa Ilusiones S.A. de C.V. maneja 3 tipos de Venta:

1. Venta Prepago => Es la venta de un equipo celular: producto almacenable
2. Venta Plan => Es la venta de un tipo de un plan telefónico: servicio
3. Venta Activación => Es la venta de un producto almacenable + servicio
Para cada una de las ventas, los campos a capturar son distintos. Y se describen en la siguiente
tabla:

| Tipos de Venta| Requeridos    |
| ------------- |:-------------:|
| Prepago| Combo de productos almacenables|
| | Combo de Número de serie|
| | Campo de Número de Contrato |
| | Precio|
|Plan |Combo de servicios |
| |  Precio de Renta mensual|
| Activación| Combo de servicios|
| |Combo de productos almacenables |
| | Combo de Número de serie |
| |Campo de Número de Contrato | 
| |Precio de Renta mensual |
| |Combo Protección de equipo (Ninguno, Protección 55, Protección 105, Protección 155) |

### Objetivo del Ejercicio

Desarrollar una aplicación de ventas capaz de capturar los 3 tipos de ventas de la empresa
Ilusiones S.A. de C.V. solicitando los campos mencionados en la tabla anterior para cada venta y
mostrar cada tipo de venta en una sola línea de venta. Todo esto en un plazo no mayor a 48 horas.
Avísanos si necesitas más tiempo.

### Objetivos específicos

```
● Mostrar un formulario para capturar los campos de cada tipo de venta que se elija
● En el mismo flujo de nueva venta se pueden agregar los 3 tipos de venta. Ej. 2 Prepago y 1
activación o 1 Prepago, 1 Servicio y 1 Activación.
● Validar existencia de productos o servicios para los combos.
```

```
● Al confirmar la venta se tiene que descontar el producto del inventario (tipo de venta:
Prepago y Activación).
● Al dar click en la Línea de venta capturada mostrar el detalle.
● Repositorio del código con los small commits de lo que desarrolles.
```
### Tiempo

Límite del ejercicio 48 hrs. y siéntete libre para agregar lo que quieras para complementar el
ejercicio.

### Ground Rules

```
● Versión de Odoo: 11
● Gestión de cambios: Git
● Repositorios para el código:
    o Si es Github (Enviar invitación al repositorio): @orocesar
    o Si es Bitbucket (Enviar invitación al repositorio): @corozcom
```
### Puntos a calificar

```
● Proactividad
● Tiempo de entrega
● Arquitectura de la solución
● Enfoque o solución del problema
● Clean Code
● Versionado de código
● Usabilidad de la UI
```

## LICENSE 
 [LGPLV3](LICENSE)
## AUTHORS
* Jose Hernandez <jhbez@outlook.com>

# Trabajo_campo_Soft
# SISTEMA DE VENTA DE LOTES

## 1. Descripción del proyecto

El presente proyecto corresponde a la actividad práctica de la sesión 11 sobre programación modular.

Se desarrolló un sistema de consola en Python para la empresa ficticia Terrenos del Norte S.A.C., con la finalidad de gestionar el registro de lotes, consultar su disponibilidad, registrar ventas y generar un resumen de las operaciones realizadas.

El sistema utiliza programación modular para distribuir las funciones en diferentes archivos, facilitando su organización, mantenimiento y reutilización.

## 2. Objetivo

Desarrollar un sistema de venta de lotes utilizando funciones y módulos en Python, aplicando validaciones de datos, cálculos automáticos y control de disponibilidad para garantizar el correcto registro de las ventas.

## 3. Integrantes del equipo

- Integrante 1: [Nombre completo]
- Integrante 2: [Nombre completo]
- Integrante 3: [Nombre completo]
- Integrante 4: [Nombre completo, si corresponde]

## 4. Tecnologías utilizadas

- Lenguaje de programación: Python 3
- Entorno de desarrollo: Visual Studio Code
- Control de versiones: Git y GitHub
- Interfaz: consola

## 5. Organización del proyecto

El sistema está organizado en cinco archivos Python:

**main.py**

Contiene el menú principal y permite acceder a las distintas funciones del sistema.

**lotes.py**

Permite registrar lotes, listar todos los lotes, consultar los disponibles y buscar lotes mediante su código.

**ventas.py**

Registra las ventas, solicita los datos del comprador, calcula la cuota inicial y el saldo, actualiza el estado del lote a vendido y muestra el resumen de ventas.

**validaciones.py**

Verifica que los campos no estén vacíos, que los números sean positivos y finitos, y que no existan códigos de lote repetidos.

**calculos.py**

Contiene funciones reutilizables para calcular el precio total, la cuota inicial del 20 % y el saldo pendiente.

## 6. Funcionalidades del sistema

El programa permite:

1. Registrar un nuevo lote.
2. Listar todos los lotes registrados.
3. Consultar los lotes disponibles.
4. Registrar la venta de un lote.
5. Mostrar el resumen de ventas.
6. Salir del sistema.

Al registrar un lote, se ingresan su código, urbanización, área y precio por metro cuadrado.

Al registrar una venta, se solicita el nombre y documento de identidad del comprador. El sistema calcula los importes automáticamente y cambia el estado del lote a "Vendido".

Asimismo, impide registrar una segunda venta del mismo lote.

## 7. Requisitos para ejecutar el programa

- Tener instalado Python 3.
- Contar con los cinco archivos Python en una misma carpeta.
- Utilizar una terminal o Visual Studio Code.

No se requieren bibliotecas externas.

## 8. Instrucciones de ejecución

1. Descargar el repositorio desde GitHub.
2. Abrir la carpeta "Sistema de ventas lotes" en Visual Studio Code.
3. Abrir la terminal.
4. Ejecutar el siguiente comando:

`python main.py`

5. Seleccionar una de las opciones del menú.

## 9. Datos de prueba

**Lote LT-001**

- Urbanización: Los Jardines
- Área: 120 m²
- Precio por m²: S/ 450
- Precio total: S/ 54 000
- Cuota inicial (20 %): S/ 10 800
- Saldo pendiente: S/ 43 200

**Lote LT-002**

- Urbanización: Las Palmeras
- Área: 90 m²
- Precio por m²: S/ 500
- Precio total: S/ 45 000

## 10. Pruebas del sistema

**Prueba 1. Registro correcto**

Registrar el lote LT-001 y verificar que aparezca con estado "Disponible".

**Prueba 2. Cálculo de venta**

Registrar una venta del lote LT-001 y verificar que el sistema calcule correctamente el precio total, la cuota inicial y el saldo.

**Prueba 3. Datos inválidos**

Ingresar campos vacíos, áreas negativas, valores iguales a cero o códigos repetidos. Verificar que el sistema rechace los datos incorrectos.

**Prueba 4. Venta duplicada**

Después de vender LT-001, intentar registrar una segunda venta del mismo lote. Verificar que el sistema rechace la operación.

Las capturas de pantalla de estas pruebas servirán como evidencias de funcionamiento.

## 11. Ventajas de la programación modular

La programación modular permite organizar el sistema según la responsabilidad de cada archivo.

Entre sus principales ventajas se encuentran la reutilización de funciones, la facilidad para detectar errores, el mantenimiento del código y la posibilidad de desarrollar nuevas funcionalidades sin modificar todo el programa.

## 12. Limitaciones

La información de lotes y ventas se almacena temporalmente en listas durante la ejecución. Al cerrar el programa, los registros no se conservan.

## 13. Repositorio de GitHub

https://github.com/Javier13v/Trabajo_campo_Soft

## 14. Conclusiones

El desarrollo del sistema permitió aplicar los principios de programación modular mediante la separación de responsabilidades en diferentes archivos Python.

Se implementaron funciones para gestionar lotes y ventas, validar información, realizar cálculos automáticos y prevenir la duplicación de ventas.

La modularización facilita la comprensión, el mantenimiento y la ampliación del sistema.

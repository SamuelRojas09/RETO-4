RETO-4
Sistema de Restaurante
Descripción

Este programa simula un sistema de pedidos en un restaurante donde:

Se pueden agregar productos a una orden
Se calcula el subtotal y total con descuentos
Se procesan pagos con tarjeta o efectivo
Se usan getters y setters para modificar atributos
Estructura
Clase base: MenuItem

Representa cualquier producto del menú:

Atributos:

name
price

Métodos:

get_name(), get_price()
set_name(), set_price()
calculate_total()
Subclases
Beverage → tamaño (size)
Appetizer → compartible (shareable)
MainCourse → calorías (calories)

Cada una usa getters/setters propios.

Clase Order

Maneja los pedidos:

add_item() → agrega productos
show_order() → muestra productos
calculate_subtotal() → suma precios
calculate_total() → aplica descuentos
Descuentos aplicados

Los descuentos se aplican en este orden:

12% si hay 2 o más platos principales
20% si hay más de 5 productos
10% si hay más de 3 productos
5% extra si el subtotal es mayor a 40
Sistema de Pago
Clase base: Payment

Subclases:

Card → muestra últimos 4 dígitos
Cash → calcula cambio o valida dinero insuficiente
Ejercicio de Clase
Descripción

Este programa modela figuras geométricas en el plano cartesiano.

Permite calcular:

Distancias
Perímetros
Áreas
Ángulos internos
Verificar si una figura es regular
Estructura
Clase Point

Representa un punto (x, y)

Métodos:

distance_to() → distancia entre puntos
getters/setters
Clase Line

Representa un segmento entre dos puntos

length() → calcula longitud
Clase base Shape

Atributos:

vértices (Point)
lados (Line)

Métodos:

compute_perimeter()
compute_area()
inner_angles()
is_regular()
Figuras implementadas
Rectangle
Área = base × altura
Ángulos: 90°
Square (hereda de Rectangle)
Valida que todos los lados sean iguales
Es una figura regular
Triangle
Área: Fórmula de Herón
Ángulos: Ley de cosenos

Métodos:

get_a(), get_b(), get_c()
Triángulos especiales
Equilateral → todos iguales
Isosceles → al menos dos iguales
Scalene → todos diferentes
RightTriangle → cumple Pitágoras

# RETO 4  
# Sistema de Restaurante y Geometría (RETO-4)
---

## 1. Sistema de Restaurante

Simulación de un sistema de gestión de pedidos que permite administrar menús, aplicar lógica de descuentos y procesar diferentes métodos de pago.

### Estructura de Clases

#### Clase Base: MenuItem
Representa la unidad mínima del menú.
* **Atributos:** `_name` (Nombre), `_price` (Precio).
* **Encapsulamiento:** Implementación de *getters* y *setters* para la modificación segura de atributos.
* **Subclases Especializadas:**
    * **Beverage:** Incluye atributo `size` (Tamaño).
    * **Appetizer:** Incluye atributo `shareable` (Para compartir).
    * **MainCourse:** Incluye atributo `calories` (Calorías).

#### Clase de Gestión: Order
Encargada de la lógica y procesamiento de la cuenta del cliente.
* `add_item()`: Registro de productos en la orden.
* `calculate_subtotal()`: Sumatoria base de los precios.
* `calculate_total()`: Aplicación de descuentos jerárquicos.

### Lógica de Descuentos
Los descuentos se evalúan bajo los siguientes criterios acumulativos:
1. **12%** por la compra de 2 o más platos principales.
2. **20%** si la orden supera los 5 productos totales.
3. **10%** si la orden supera los 3 productos totales.
4. **5% Extra** si el subtotal final es mayor a 40.000.

### Sistema de Pago
Implementación de la clase `Payment`:
* **Card:** Validación y visualización de los últimos 4 dígitos.
* **Cash:** Gestión de cambio y validación de fondos.

---

## 2. Motor Geométrico

Modelado y análisis de figuras geométricas en un plano cartesiano.

### Componentes Fundamentales

| Clase | Función Principal |
| :--- | :--- |
| **Point** | Representa coordenadas (x, y) y calcula distancias entre puntos. |
| **Line** | Define un segmento entre dos puntos y calcula su longitud. |
| **Shape** | Clase base que gestiona vértices y aristas para las figuras geométricas. |

### Capacidades de Cálculo
* **Perímetros y Áreas:** Implementación de fórmulas específicas por figura.
* **Análisis de Triángulos:** Uso de la **Fórmula de Herón** para áreas y la **Ley de Cosenos** para ángulos internos.
* **Validación de Regularidad:** Comprobación de igualdad de lados y ángulos.

### Figuras Soportadas
#### Rectángulos y Cuadrados
* **Rectangle:** Define una figura de cuatro lados basada en coordenadas de puntos. Implementa el cálculo de área ($base \times altura$) y perímetro.
* **Square:** Es una extensión (subclase) de Rectangle. Su función principal es restringir la figura para que todos los lados sean iguales, asegurando la integridad geométrica del cuadrado.

#### Triángulos
Clasificación automática según sus propiedades:
* **Equilateral:** Todos los lados iguales.
* **Isosceles:** Al menos dos lados iguales.
* **Scalene:** Todos los lados diferentes.
* **RightTriangle:** Validación mediante el Teorema de Pitágoras.

---

import math
from typing import List


# ===================== POINT =====================
# Representa un punto en el plano cartesiano
class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x  # Coordenada en X
        self._y = y  # Coordenada en Y

    # -------- GETTERS --------
    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    # -------- SETTERS --------
    def set_x(self, x: float) -> None:
        self._x = x

    def set_y(self, y: float) -> None:
        self._y = y

    # Calcula la distancia entre dos puntos
    def distance_to(self, other: "Point") -> float:
        dx = self._x - other._x  # Diferencia en X
        dy = self._y - other._y  # Diferencia en Y
        return math.sqrt(dx ** 2 + dy ** 2)


# ===================== LINE =====================
# Representa un segmento de línea entre dos puntos
class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self._start = start  # Punto inicial
        self._end = end      # Punto final

    # -------- GETTERS --------
    def get_start(self) -> Point:
        return self._start

    def get_end(self) -> Point:
        return self._end

    # -------- SETTERS --------
    def set_start(self, start: Point) -> None:
        self._start = start

    def set_end(self, end: Point) -> None:
        self._end = end

    # Calcula la longitud del segmento
    def length(self) -> float:
        return self._start.distance_to(self._end)


# ===================== SHAPE =====================
# Clase base para todas las figuras geométricas
class Shape:
    def __init__(self, vertices: List[Point]) -> None:
        self._vertices = vertices      # Lista de vértices compuesta por objetos Point
        self._edges: List[Line] = []   # Lista de lados compuesta por objetos Line

    # -------- GETTERS --------
    def get_vertices(self) -> List[Point]:
        return self._vertices

    def get_edges(self) -> List[Line]:
        return self._edges

    # -------- SETTERS --------
    def set_vertices(self, vertices: List[Point]) -> None:
        self._vertices = vertices

    def set_edges(self, edges: List[Line]) -> None:
        self._edges = edges

    # Calcula el perímetro sumando la longitud de todos los lados
    def compute_perimeter(self) -> float:
        return sum(edge.length() for edge in self._edges)

    # Obliga a las subclases a implementarlo
    def compute_area(self) -> float:
        raise NotImplementedError

    # Calcula los ángulos internos
    def inner_angles(self) -> List[float]:
        raise NotImplementedError

    # Indica si la figura es regular (por defecto False)
    def is_regular(self) -> bool:
        return False


# ===================== RECTANGLE =====================
# Representa un rectángulo
class Rectangle(Shape):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        # Se crean los 4 lados del rectángulo usando los vértices
        self._edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[3]),
            Line(vertices[3], vertices[0]),
        ]

    # Área del rectángulo = base * altura
    def compute_area(self) -> float:
        base = self._edges[0].length()
        height = self._edges[1].length()
        return base * height

    # Todos los ángulos internos de un rectángulo son de 90 grados
    def inner_angles(self) -> List[float]:
        return [90.0, 90.0, 90.0, 90.0]

    # Un rectángulo no es regular (a menos que sea cuadrado)
    def is_regular(self) -> bool:
        return False


# ===================== SQUARE =====================
# Representa un cuadrado (hereda de Rectangle)
class Square(Rectangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        # Se verifica que todos los lados tengan la misma longitud
        sides = [edge.length() for edge in self._edges]
        first = sides[0]

        for side in sides:
            if abs(side - first) > 1e-6:  # Tolerancia por errores decimales
                raise ValueError("Not a square")

    # Un cuadrado sí es una figura regular
    def is_regular(self) -> bool:
        return True


# ===================== TRIANGLE =====================
# Representa un triángulo general
class Triangle(Shape):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        # Se crean los 3 lados del triángulo
        self._edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0]),
        ]

    # Métodos para obtener las longitudes de los lados
    def get_a(self) -> float:
        return self._edges[0].length()

    def get_b(self) -> float:
        return self._edges[1].length()

    def get_c(self) -> float:
        return self._edges[2].length()

    # Área usando la fórmula de Herón
    def compute_area(self) -> float:
        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        s = (a + b + c) / 2  # Semiperímetro
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Calcula los ángulos internos usando la ley de cosenos (en grados)
    def inner_angles(self) -> List[float]:
        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180.0 - angle_A - angle_B

        return [angle_A, angle_B, angle_C]

    # Un triángulo es regular si todos sus lados son iguales
    def is_regular(self) -> bool:
        a = self.get_a()
        b = self.get_b()
        c = self.get_c()
        return abs(a - b) < 1e-6 and abs(b - c) < 1e-6


# ===================== SPECIAL TRIANGLES =====================
# Triángulo equilátero: todos los lados iguales
class Equilateral(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        if not self.is_regular():
            raise ValueError("Not an equilateral triangle")

    def is_regular(self) -> bool:
        return True


# Triángulo isósceles: al menos dos lados iguales
class Isosceles(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        if not (
            abs(a - b) < 1e-6 or
            abs(b - c) < 1e-6 or
            abs(a - c) < 1e-6
        ):
            raise ValueError("Not an isosceles triangle")


# Triángulo escaleno: todos los lados diferentes
class Scalene(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        if (
            abs(a - b) < 1e-6 or
            abs(b - c) < 1e-6 or
            abs(a - c) < 1e-6
        ):
            raise ValueError("Not a scalene triangle")


# Triángulo rectángulo: cumple el teorema de Pitágoras
class RightTriangle(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        sides = sorted([self.get_a(), self.get_b(), self.get_c()])

        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) > 1e-6:
            raise ValueError("Not a right triangle")


# ===================== MAIN =====================
if __name__ == "__main__":

    # Función para mostrar información de cualquier figura
    def show_shape(name: str, shape: Shape) -> None:
        print(f"\n--- {name} ---")

        area = shape.compute_area()
        perimeter = shape.compute_perimeter()
        angles = [round(a, 2) for a in shape.inner_angles()]

        print(f"Area        : {area:.2f}")
        print(f"Perimeter   : {perimeter:.2f}")
        print(f"Angles (°)  : {angles}")
        print(f"Is regular  : {shape.is_regular()}")

    print("\n==============================")
    print("     GEOMETRY TEST PROGRAM")
    print("==============================")

    # Prueba de Point y Line
    print("\n=== POINT & LINE ===")
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    line = Line(p1, p2)

    print(f"Distance between points : {p1.distance_to(p2):.2f}")
    print(f"Line length             : {line.length():.2f}")

    # Prueba de triángulo general
    triangle = Triangle([Point(0, 0), Point(4, 0), Point(4, 3)])
    show_shape("General Triangle", triangle)

    # Prueba de rectángulo
    rectangle = Rectangle([
        Point(0, 0), Point(4, 0), Point(4, 2), Point(0, 2)
    ])
    show_shape("Rectangle", rectangle)

    # Prueba de cuadrado
    square = Square([
        Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)
    ])
    show_shape("Square", square)

    print("\n=== SPECIAL TRIANGLES ===")

    # Prueba de triángulos especiales
    scalene = Scalene([Point(0, 0), Point(4, 0), Point(4, 3)])
    show_shape("Scalene Triangle", scalene)

    isosceles = Isosceles([Point(0, 0), Point(4, 0), Point(2, 3)])
    show_shape("Isosceles Triangle", isosceles)

    right = RightTriangle([Point(0, 0), Point(4, 0), Point(4, 3)])
    show_shape("Right Triangle", right)

    equilateral = Equilateral([
        Point(0, 0), Point(2, math.sqrt(12)), Point(4, 0)
    ])
    show_shape("Equilateral Triangle", equilateral)

    print("\n==============================")
    print("        END OF TEST")
    print("==============================")

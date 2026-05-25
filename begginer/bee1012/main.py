pi = 3.14159
a, b, c = map(float, input().split())

rect_triangle_area = a * c / 2
circle_area = pi * c**2
trapezium_area = (1 / 2 * (a + b)) * c
square_area = b**2
rect_area = a * b

print(f"TRIANGULO: {rect_triangle_area:.3f}")
print(f"CIRCULO: {circle_area:.3f}")
print(f"TRAPEZIO: {trapezium_area:.3f}")
print(f"QUADRADO: {square_area:.3f}")
print(f"RETANGULO: {rect_area:.3f}")

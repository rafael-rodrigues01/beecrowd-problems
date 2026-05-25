pi = 3.14159
a, b, c = map(float, input().split())

areas = {
    "TRIANGULO": a * c / 2,
    "CIRCULO": pi * c**2,
    "TRAPEZIO": (a + b) * c / 2,
    "QUADRADO": b**2,
    "RETANGULO": a * b,
}

for name, value in areas.items():
    print(f"{name}: {value:.3f}")

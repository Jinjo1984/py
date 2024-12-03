import math
import cmath
import sys

class Complex:
    def __init__(self, re=0.0, im=0.0):
        """Инициализация комплексного числа"""
        self.re = re
        self.im = im

    def set(self, re=0.0, im=0.0):
        """Установка значений"""
        self.re = re
        self.im = im

    def set_from_complex(self, other):
        """Установка значений из другого комплексного числа"""
        self.re = other.re
        self.im = other.im

    def __str__(self):
        """Печать комплексного числа"""
        return f"({self.re}, {self.im})"

    def mod(self):
        """Модуль комплексного числа"""
        return math.hypot(self.re, self.im)

    def arg(self):
        """Аргумент (фаза) комплексного числа"""
        return math.atan2(self.im, self.re)

    def __neg__(self):
        """Унарный минус"""
        return Complex(-self.re, -self.im)

    def __add__(self, other):
        """Сложение комплексных чисел"""
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        """Вычитание комплексных чисел"""
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        """Умножение комплексных чисел"""
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        """Деление комплексных чисел"""
        denominator = other.re ** 2 + other.im ** 2
        return Complex((self.re * other.re + self.im * other.im) / denominator,
                       (self.im * other.re - self.re * other.im) / denominator)

    def __eq__(self, other):
        """Сравнение на равенство"""
        return self.re == other.re and self.im == other.im

    def __ne__(self, other):
        """Сравнение на неравенство"""
        return not self == other

    def power(self, n, m=1):
        """Возведение в рациональную степень n/m с использованием формулы Муавра"""
        r = self.mod()  # Модуль числа
        theta = self.arg()  # Аргумент числа

        # Возведение в степень n/m
        root_r = r ** (n / m)
        base_theta = theta * n / m

        roots = []
        for k in range(m):
            current_theta = base_theta + 2 * math.pi * k / m
            real_part = root_r * math.cos(current_theta)
            imag_part = root_r * math.sin(current_theta)
            roots.append(Complex(real_part, imag_part))

        return roots


def main():
    # Проверяем аргументы командной строки
    if len(sys.argv) < 4:
        print("Usage: python muavr.py x y n [m]")
        return

    # Получение аргументов
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    n = int(sys.argv[3])
    m = int(sys.argv[4]) if len(sys.argv) > 4 else 1

    # Создание комплексного числа
    z = Complex(x, y)

    # Вычисление корней
    roots = z.power(n, m)

    # Вывод результатов
    print(f"Все возможные значения ({x}, {y})^({n}/{m}):")
    for root in roots:
        print(root)


if __name__ == "__main__":
    main()

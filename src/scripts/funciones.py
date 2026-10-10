import numpy as np

# ---------- parametros del ambiente controlado ----------
tol = 1e-6
max_iter = 100

# ---------- las 6 funciones con su derivada y segunda derivada ----------
def f1(x): return x**3 - x - 2
def df1(x): return 3*x**2 - 1
def ddf1(x): return 6*x

def f2(x): return (x - 2)**2
def df2(x): return 2*(x - 2)
def ddf2(x): return 2 + 0*x

def f3(x): return np.log(x) + x - 4
def df3(x): return 1/x + 1
def ddf3(x): return -1/x**2

def f4(x): return np.exp(-x) - x
def df4(x): return -np.exp(-x) - 1
def ddf4(x): return np.exp(-x)

def f5(x): return np.cos(x) - x
def df5(x): return -np.sin(x) - 1
def ddf5(x): return -np.cos(x)

def f6(x): return np.sqrt(x) - np.cos(x)
def df6(x): return 1/(2*np.sqrt(x)) + np.sin(x)
def ddf6(x): return -1/(4*x**1.5) + np.cos(x)

nombres = ["polinomica", "raiz_doble", "logaritmica", "exponencial", "trigonometrica", "mixta"]
formulas = ["x^3 - x - 2", "(x - 2)^2", "ln(x) + x - 4", "e^(-x) - x", "cos(x) - x", "sqrt(x) - cos(x)"]
funciones = [f1, f2, f3, f4, f5, f6]
derivadas = [df1, df2, df3, df4, df5, df6]
derivadas2 = [ddf1, ddf2, ddf3, ddf4, ddf5, ddf6]

# intervalo [a, b] de cada funcion
# (en la raiz doble no hay cambio de signo, uso [1, 3] solo para mostrar que f(a)*f(b) > 0)
intervalos = [(1, 2), (1, 3), (2, 3), (0, 1), (0, 1), (0.1, 1)]

# raiz "exacta" de cada funcion (calculada con mucha precision) para medir el error |xn - raiz|
raices = [1.5213797068045676, 2.0, 2.926271062443501, 0.5671432904097838, 0.7390851332151607, 0.6417143708728826]
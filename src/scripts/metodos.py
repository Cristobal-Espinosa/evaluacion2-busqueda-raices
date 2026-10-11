def punto_fijo(g, x0, tol, max_iter):
    pasos = []
    x = x0
    for n in range(max_iter):
        x_next = g(x)
        paso = (n, x, x_next, abs(x_next - x))
        pasos.append(paso)
        if abs(x_next - x) < tol:
            return x_next, pasos
        x = x_next
    return x, pasos  


def newton(f, df, x0, tol, max_iter):
    pasos = []
    x = x0
    for n in range(max_iter):
        if df(x) == 0:
            if abs(f(x)) < tol:
                return x, pasos, True
            return x, pasos, False
        x_next = x - f(x) / df(x)
        paso = (n, x, x_next, abs(x_next - x))
        pasos.append(paso)
        if abs(x_next - x) < tol:
            return x_next, pasos, True
        x = x_next
    return x, pasos, False 


def newton_mejorado(f, df, ddf, x0, tol, max_iter):
    pasos = []
    x = x0
    for n in range(max_iter):
        D = df(x)**2 - f(x) * ddf(x)
        if D == 0:
            if abs(f(x)) < tol:
                return x, pasos, True
            return x, pasos, False
        x_next = x - (f(x) * df(x)) / D
        paso = (n, x, x_next, abs(x_next - x))
        pasos.append(paso)
        if abs(x_next - x) < tol:
            return x_next, pasos, True
        x = x_next
    return x, pasos, False  


def secante(f, x0, x1, tol, max_iter):
    pasos = []
    for n in range(max_iter):
        if f(x1) - f(x0) == 0:
            if abs(f(x1)) < tol:
                return x1, pasos, True
            return x1, pasos, False
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        paso = (n, x1, x_next, abs(x_next - x1))
        pasos.append(paso)
        if abs(x_next - x1) < tol:
            return x_next, pasos, True
        x0 = x1
        x1 = x_next
    return x1, pasos, False  


def biseccion(f, a, b, tol, max_iter):
    pasos = []
    if f(a) * f(b) >= 0:
        return None, pasos, False  
    c_ant = a
    for n in range(max_iter):
        c = (a + b) / 2
        paso = (n, c_ant, c, abs(c - c_ant))
        pasos.append(paso)
        if abs(f(c)) < tol or abs(c - c_ant) < tol:
            return c, pasos, True
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_ant = c
    return c, pasos, False  


def falsa_posicion(f, a, b, tol, max_iter):
    pasos = []
    if f(a) * f(b) >= 0:
        return None, pasos, False  
    c_ant = a
    for n in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        paso = (n, c_ant, c, abs(c - c_ant))
        pasos.append(paso)
        if abs(f(c)) < tol or abs(c - c_ant) < tol:
            return c, pasos, True
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_ant = c
    return c, pasos, False  
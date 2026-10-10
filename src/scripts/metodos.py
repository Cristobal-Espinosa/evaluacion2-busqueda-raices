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
    return x, pasos  # sin converger
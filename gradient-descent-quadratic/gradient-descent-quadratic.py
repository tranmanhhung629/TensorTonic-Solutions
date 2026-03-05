def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = x0 #khoi tao gia tri ban dau
    for i in range (steps):
        derivative = 2 * a * x + b #tinh dao ham tai gia tri x
        x = x - derivative*lr
    return x
    pass
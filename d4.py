# Lambda function
x = lambda a, b : a + b
print(x(1,5))

y = lambda c, d : c - d
print(y(8,5))

z = lambda m, n : m / n
print(z(5,2))

u = lambda p, q, r : p * q * r
print(u(9,3,2))


def my_fun(i):
    return lambda e : e + i
j = my_fun(5)
print(j(10))

def m_fn(f):
    return lambda g : g * f
h = m_fn(6)
k = m_fn(8)
print(h(5))
print(k(11))




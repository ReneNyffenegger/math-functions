import math

z = [ 0.8, -0.2, 2.1, 1.3, -0.8]

# temporary values:
t = [ math.e ** z_ for z_ in z ]

σ = [ t_ / sum(t) for t_ in t ]

for i , σ_i in enumerate(σ):
    print(f'σ_{i} = {σ_i:04.3f}')

print(f'Sum(σ) = {sum(σ):04.3f}')

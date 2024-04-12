# NumPy: How to check a Value or an Array for NaT

import numpy as np


not_a_time = np.datetime64('NaT')
print(not_a_time)  # 👉️ NaT

print('-' * 50)

if np.isnat(not_a_time):
    # 👇️ This runs
    print('The value has a type of NaT')
else:
    print('The value does NOT have a type of NaT')


print('-' * 50)

dt = np.datetime64('2024-09-24')

print(np.isnat(dt))  # 👉️ False
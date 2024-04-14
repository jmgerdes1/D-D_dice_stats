import numpy as np
import scipy.signal

arrd20 = np.empty(20)
arr1 = np.empty(10)
arr1.fill(1)
arr2 = np.empty(10)
arr2.fill(1)
arr3 = scipy.signal.fftconvolve(arr1,arr2)/(np.size(arr1)*np.size(arr2))
arr4 = np.empty(np.size(arr1)+np.size(arr2)-1)

ac = 10
mod = 3
prof = 2
expected_value = 0
CtH = 0 #chance to hit

for i in range(0,len(arrd20)):
    arrd20[i] = i+1

for i in range(0,len(arr4)):
    arr4[i] = i+2+mod
    expected_value = expected_value + arr4[i]*arr3[i]

for i in range(0,len(arrd20)):
    if arrd20[i] > 1:
        if arrd20[i] == 20:
            CtH = CtH + 1
        elif arrd20[i]+mod+prof >= ac:
            CtH = CtH + 1

CtH = CtH/20

print("Effective damage of 2d10 against AC of 10:")
print(CtH*expected_value)
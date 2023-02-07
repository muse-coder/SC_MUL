import numpy as np
import  sobol_seq
from scipy.stats import qmc
import random
# n=0
# m=31
# k=32
# # print(np.random.randint(n,m,k))#产生n--m之间的k个整数

# import random
# for i in range(10):
#     ran = random.sample(range(0, 32),32 )
#     print((ran))


seed_list =  random.sample(range(0,64),10 )
print(seed_list)
for i in range(len(seed_list)):
    sampler = qmc.Sobol(d=1, scramble=True,seed=seed_list[i])
    sample = sampler.random_base2(m=5)
    list= sample.tolist()
    
    for j in range(len(list)):
        print(int(list[j][0]*32),end=',')
# print(sample.tolist())
    print('\n',end='')
    print('\n%lf'%qmc.discrepancy(sample))
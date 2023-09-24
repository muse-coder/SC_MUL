from SC_MUL.components import *
import pandas as pd
import statistics
import os
import numpy as np
from scipy.stats import qmc
def to_bin(value, bitWidth):#十进制数据，二进制位宽
	bin_chars = ""
	temp = value
	for i in range(bitWidth):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()#输出指定位宽的二进制字符串

def genScaledSobol(dVector_bin ,sobolSeq ):
    dVector = int(dVector_bin, 2)
    scaledSobolEnd = [sobolSeq[i] ^ dVector for i in range(16)]
    return scaledSobolEnd

def testDiscrepancy(scaled_sobol):
    l_bounds = [0 ]
    u_bounds = [len(scaled_sobol) ]
        
    scaled_sobol_array = qmc.scale(np.array(scaled_sobol).reshape(len(scaled_sobol),1) ,l_bounds , u_bounds ,reverse=True)
    print('%lf'%qmc.discrepancy(scaled_sobol_array))

    
if __name__=="__main__":
    sobol_1 = [0,8,12,4,6,14,10,2,3,11,15,7,5,13,9,1]
    sobol_2 = [0,8,4,12,6,14,2,10,5,13,1,9,3,11,7,15]
    sobol_3 = [0,8,4,12,10,2,14,6,15,7,11,3,5,13,1,9]
    sobol_4 = [0,8,4,12,14,6,10,2,7,15,3,11,9,1,13,5]
    sobol_1_front = [data <<0 for data in sobol_1 ]
    sobol_2_front = [data <<0 for data in sobol_2 ]
    sobol_3_front = [data <<0 for data in sobol_3 ]
    sobol_4_front = [data <<0 for data in sobol_4 ]
    
    dVector_1_bin = "10000"
    dVector_2_bin = "10000"
    dVector_3_bin = "10000"
    dVector_4_bin = "10000"

    sobol_1_end = genScaledSobol(dVector_1_bin , sobol_1_front)
    sobol_2_end = genScaledSobol(dVector_2_bin , sobol_2_front)
    sobol_3_end = genScaledSobol(dVector_3_bin , sobol_3_front)
    sobol_4_end = genScaledSobol(dVector_4_bin , sobol_4_front)
    
    scaled_sobol_1 = sobol_1_front + sobol_1_end 
    scaled_sobol_2 = sobol_2_front + sobol_2_end 
    scaled_sobol_3 = sobol_3_front + sobol_3_end 
    scaled_sobol_4 = sobol_4_front + sobol_4_end 
    print(scaled_sobol_1)
    print(scaled_sobol_2)
    print(scaled_sobol_3)
    print(scaled_sobol_4)

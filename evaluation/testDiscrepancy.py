import numpy as np
from scipy.stats import qmc
def genScaledSobol(dVector_bin ,sobolSeq ):
    dVector = int(dVector_bin, 2)
    scaledSobolEnd = [sobolSeq[i] ^ dVector for i in range(32)]
    return scaledSobolEnd

def get_discrepancy(seq_1,seq_2):
	assert(len(seq_1)==len(seq_2))
	array =list(zip(seq_1,seq_2))
	space = np.array(array)
	l_bounds = [0 ,0]
	u_bounds = [len(seq_1),len(seq_2) ]
	scaled_sobol_array = qmc.scale( space,l_bounds , u_bounds ,reverse=True)
	print('%lf'%qmc.discrepancy(scaled_sobol_array,method="L2-star"))

if __name__=="__main__":
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    # sobol_5 = [data for  data in range(1,32)]
    sobol_1_front = [data <<1 for data in sobol_1 ]
    sobol_2_front = [data <<1 for data in sobol_2 ]
    sobol_3_front = [data <<1 for data in sobol_3 ]
    sobol_4_front = [data <<1 for data in sobol_4 ]
    
    dVector_1_bin = "000011"
    dVector_2_bin = "010001"
    dVector_3_bin = "101101"
    dVector_4_bin = "100011"

    sobol_1_end = genScaledSobol(dVector_1_bin , sobol_1_front)
    sobol_2_end = genScaledSobol(dVector_2_bin , sobol_2_front)
    sobol_3_end = genScaledSobol(dVector_3_bin , sobol_3_front)
    sobol_4_end = genScaledSobol(dVector_4_bin , sobol_4_front)

    sobol_1_64 = sobol_1_front + sobol_1_end
    sobol_2_64 = sobol_2_front + sobol_2_end
    sobol_3_64 = sobol_3_front + sobol_3_end
    sobol_4_64 = sobol_4_front + sobol_4_end
    scaled_sobol_1_64 = sobol_1_front + sobol_2_end
    scaled_sobol_2_64 = sobol_2_front + sobol_3_end
    scaled_sobol_3_64 = sobol_3_front + sobol_4_end
    scaled_sobol_4_64 = sobol_4_front + sobol_1_end
    get_discrepancy(sobol_4,sobol_1)
    get_discrepancy(sobol_4_64,sobol_1_64)
    get_discrepancy(sobol_4_64,scaled_sobol_1_64)

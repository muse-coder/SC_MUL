import isc_mul
import scaled_mul
import random
if __name__=="__main__":
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    bit_width = 32
    test_range=pow(2,16)    

    sum_1=0
    sum_2=0
    
    for i in range(test_range):
        num_1=random.randint(1,test_range)
        num_2=random.randint(1,test_range)
        error_1 = isc_mul.excute(num_1,num_2,sobol_1,sobol_2,bit_width)
        error_2 = scaled_mul.excute(num_1,num_2,sobol_1,sobol_2,bit_width)
        
        sum_1+=error_1
        sum_2+=error_2
    MRED_1=sum_1/test_range
    MRED_2=sum_2/test_range
    print("MRED_1 = %.2lf"%(MRED_1*100)+"%")
    print("MRED_2 = %.2lf"%(MRED_2*100)+"%")
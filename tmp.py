import isc_mul
import scaled_mul
import random
if __name__=="__main__":
    LD_sobol_1 =   [0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    LD_sobol_2 =   [0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    LD_sobol_3 =   [0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    LD_sobol_4 =   [0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    LD_sobol_5 =   [0,16,24,8,12,28,20,4,18,2,10,26,30,14,6,22,9,25,17,1,5,21,29,13,27,11,3,19,23,7,15,31]
    LD_sobol_6 =   [0,16,24,8,4,20,28,12,10,26,18,2,14,30,22,6,31,15,7,23,27,11,3,19,21,5,13,29,17,1,9,25]
    LD_sobol_7 =   [0,16,8,24,12,28,4,20,14,30,6,22,2,18,10,26,17,1,25,9,29,13,21,5,31,15,23,7,19,3,27,11]
    LD_sobol_8 =   [0,16,24,8,28,12,4,20,30,14,6,22,2,18,26,10,27,11,3,19,7,23,31,15,5,21,29,13,25,9,1,17]
    LD_sobol_9 =   [0,16,24,8,28,12,4,20,30,14,6,22,2,18,26,10,15,31,23,7,19,3,11,27,17,1,9,25,13,29,21,5]
    LD_sobol_10=   [0,16,24,8,20,4,12,28,10,26,18,2,30,14,6,22,5,21,29,13,17,1,9,25,15,31,23,7,27,11,3,19]
    random_1 =   [11, 20, 2, 10, 17, 8, 29, 18, 12, 19, 9, 5, 16, 21, 15, 1, 22, 7, 23, 24, 28, 4, 27, 26, 25, 31, 30, 13, 6, 3, 0, 14]
    random_2 =   [20, 15, 19, 23, 22, 8, 13, 17, 3, 10, 1, 4, 28, 29, 21, 25, 30, 6, 24, 12, 18, 16, 26, 5, 2, 14, 31, 27, 0, 7, 11, 9]
    random_3 =   [21, 9, 2, 4, 14, 11, 13, 30, 26, 7, 24, 6, 25, 1, 10, 3, 8, 23, 12, 20, 5, 31, 19, 0, 29, 16, 22, 17, 28, 15, 27, 18]
    random_4 =   [20, 31, 9, 18, 10, 15, 11, 19, 3, 28, 25, 24, 4, 16, 30, 23, 17, 22, 13, 5, 27, 6, 7, 21, 14, 29, 0, 12, 26, 2, 8, 1]
    random_5 =   [5, 22, 7, 14, 17, 1, 26, 28, 2, 21, 3, 31, 13, 19, 4, 10, 30, 9, 25, 27, 24, 8, 20, 18, 16, 15, 29, 12, 11, 23, 0, 6]
    random_6 =   [0, 19, 18, 27, 17, 1, 14, 11, 12, 4, 5, 28, 6, 2, 8, 10, 22, 7, 21, 23, 13, 3, 31, 29, 24, 16, 9, 15, 25, 26, 30, 20]
    random_7 =   [26, 21, 20, 24, 12, 19, 0, 25, 8, 9, 13, 17, 3, 31, 28, 29, 16, 30, 23, 2, 14, 22, 4, 15, 27, 5, 6, 1, 7, 18, 10, 11]
    random_8 =   [22, 8, 2, 16, 11, 1, 10, 26, 0, 21, 25, 30, 29, 3, 5, 19, 12, 18, 17, 6, 4, 15, 28, 31, 27, 24, 23, 9, 7, 20, 14, 13]
    random_9 =   [4, 17, 16, 25, 8, 10, 27, 30, 31, 26, 9, 19, 7, 6, 29, 15, 24, 28, 20, 12, 13, 18, 1, 22, 14, 5, 11, 0, 3, 23, 2, 21]
    random_10=   [21, 10, 26, 15, 16, 23, 30, 5, 3, 29, 8, 9, 20, 1, 31, 6, 14, 22, 13, 18, 2, 12, 0, 24, 11, 7, 27, 4, 17, 28, 25, 19]    
    
    LD_group_1=[LD_sobol_1 ,LD_sobol_2  ]
    LD_group_2=[LD_sobol_3 ,LD_sobol_4  ]
    LD_group_3=[LD_sobol_5 ,LD_sobol_6  ]
    LD_group_4=[LD_sobol_7 ,LD_sobol_8  ]
    LD_group_5=[LD_sobol_9 ,LD_sobol_10 ]
    
    random_group_1=[random_1 ,random_2  ]
    random_group_2=[random_3 ,random_4  ]
    random_group_3=[random_5 ,random_6  ]
    random_group_4=[random_7 ,random_8  ]
    random_group_5=[random_9 ,random_10 ]

    LD_GROUPS=[LD_group_1,LD_group_2,LD_group_3,LD_group_4,LD_group_5]
    random_GROUPS=[random_group_1,random_group_2,random_group_3,random_group_4,random_group_5]

    
    bit_width = 32
    test_range=pow(2,16)    
    sum_1=0
    sum_2=0
    size = len(LD_GROUPS)
    
    for i in range(test_range):
        num_1=random.randint(1,test_range)
        num_2=random.randint(1,test_range)
        error_1_sum=0
        error_2_sum=0
        print("****************************")
        for g in LD_GROUPS:
            error_1 = isc_mul.excute(num_1,num_2,g[0],g[1],bit_width)
            error_2 = scaled_mul.excute(num_1,num_2,g[0],g[1],bit_width)
            print("ISC_MUL: %.2lf"%(error_1*100) + '%',end='\t')
            print("ISC_MUL_plus: %.2lf"%(error_2*100) + '%',end='\n')
            # print('\n')
            error_1_sum += error_1
            error_2_sum += error_2
        
        error_1 = error_1_sum / size             
        error_2 = error_2_sum / size
        # error_1 = isc_mul.excute(num_1,num_2,sobol_2,sobol_3,bit_width)
        # error_2 = isc_mul_plus.excute(num_1,num_2,sobol_2,sobol_3,bit_width)
        # if(error_1<error_2):
        print("\nnum1: %d, num2: %d, error1: %.2lf, error2: %.2lf"%(num_1,num_2,error_1,error_2))
        print("****************************")
        print('\n')
        
        sum_1+=error_1
        sum_2+=error_2
    MRED_1=sum_1/test_range
    MRED_2=sum_2/test_range
    print("MRED_1 = %.2lf"%(MRED_1*100)+"%")
    print("MRED_2 = %.2lf"%(MRED_2*100)+"%")
    print("accuracy increases %.2lf"%((MRED_1-MRED_2)/MRED_1*100)+"%")
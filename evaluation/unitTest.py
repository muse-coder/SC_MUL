from SC_MUL.components import *
import pandas as pd
import statistics
import os
import math
if __name__=="__main__":
    # sobol_1 = [0,4,6,2,3,7,5,1]
    # sobol_2 = [0,4,2,6,3,7,1,5]
    # # sobol_1 = [0,8,12,4,6,14,10,2,3,11,15,7,5,13,9,1]
    # sobol_2 = [0,8,4,12,6,14,2,10,5,13,1,9,3,11,7,15]
    # sobol_3 = [0,8,4,12,10,2,14,6,15,7,11,3,5,13,1,9]
    # sobol_4 = [0,8,4,12,14,6,10,2,7,15,3,11,9,1,13,5]
    # sobol_5 = [0,8,12,4,6,14,10,2,9,1,5,13,15,7,3,11]
    # sobol_6 = [0,8,12,4,2,10,14,6,5,13,9,1,7,15,11,3]
    # sobol_7 = [0,8,4,12,6,14,2,10,7,15,3,11,1,9,5,13]
    # sobol_8 = [0,8,12,4,14,6,2,10,15,7,3,11,1,9,13,5]
    # sobol_1 = [0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    # sobol_2 = [0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    # sobol_3 = [0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    # sobol_4 = [0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    # sobol_5 = [0,16,24,8,12,28,20,4,18,2,10,26,30,14,6,22,9,25,17,1,5,21,29,13,27,11,3,19,23,7,15,31]
    # sobol_6 = [0,16,24,8,4,20,28,12,10,26,18,2,14,30,22,6,31,15,7,23,27,11,3,19,21,5,13,29,17,1,9,25]
    # sobol_7 = [0,16,8,24,12,28,4,20,14,30,6,22,2,18,10,26,17,1,25,9,29,13,21,5,31,15,23,7,19,3,27,11]
    # sobol_8 = [0,16,24,8,28,12,4,20,30,14,6,22,2,18,26,10,27,11,3,19,7,23,31,15,5,21,29,13,25,9,1,17]
    sobol_1=  [0,32,48,16,24,56,40,8,12,44,60,28,20,52,36,4,6,38,54,22,30,62,46,14,10,42,58,26,18,50,34,2,3,35,51,19,27,59,43,11,15,47,63,31,23,55,39,7,5,37,53,21,29,61,45,13,9,41,57,25,17,49,33,1]
    sobol_2=  [0,32,16,48,24,56,8,40,20,52,4,36,12,44,28,60,30,62,14,46,6,38,22,54,10,42,26,58,18,50,2,34,17,49,1,33,9,41,25,57,5,37,21,53,29,61,13,45,15,47,31,63,23,55,7,39,27,59,11,43,3,35,19,51]
    
#########################################################                       
    dataWidth = 16                                    ###        
    sobolWidth = int(math.log(len(sobol_1),2))        ###       
    validSegWidth = sobolWidth+1                      ###
    # validSegWidth = 16                              ###
    dataRange=(1,pow(2,16))                           ###
    iterationRange=dataRange[1]                     ###
#########################################################
    group_1=[sobol_1,sobol_2]
    sobolGroups=[group_1]

    
    # writer = pd.ExcelWriter('test.xlsx')
        
    mredGroup = []
    for i in range (len(sobolGroups)):
        mredGroup.append(0)
    
    for test in range(iterationRange):
        num_1=random.randint(int(dataRange[1]/2),dataRange[1])
        # num_1=random.randint(dataRange[0],dataRange[1])
        # num_1 = 81
        for i in range(len(sobolGroups)):
            approx_num = RepresentationError(num_1=num_1,Sobol_1=sobolGroups[i][0],validSegWidth=validSegWidth,sobolWidth=sobolWidth,dataWidth=dataWidth)
            # isc_res=scaled_mul(
            #     num_1=num_1,num_2=num_2,
            #     sobol_1= sobolGroups[i][0],sobol_2= sobolGroups[i][1],validSegWidth=validSegWidth,
            #     sobolWidth= sobolWidth,dataWidth=  dataWidth
            # )
            ED = abs(num_1-approx_num)
            error= ED/num_1
            if error>1:
                print ("error")
            mredGroup[i]+=(error)
            # print(isc_res,error, end=' ')
        # print('\n')

    mredGroup = [mredGroup [i] /iterationRange for i in range(len(mredGroup))]

    for i in range(len(mredGroup)):
        
        print("MRED %d = %.4lf"%(i+1,mredGroup[i]*100)+"% ",end=' ')
    averageMRED = statistics.mean(mredGroup)
    print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")

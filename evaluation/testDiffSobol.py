from SC_MUL.components import *
import pandas as pd
import statistics
import os
import math
def generate_df(sobolGroups ,mredGroup ,sobolWidth ,savingPath):
    dfIndex=[]
    dfMred=[]
    dfSobolWidth=[]

    
    for i in range(len(sobolGroups)):
        dfIndex.append(("sobolGroup_"+str(i)))
        mred = "%.4lf"%(mredGroup[i]*100)+"%"
        dfMred.append(mred)
        dfSobolWidth.append(sobolWidth)
        # df
    averageMRED = statistics.mean(mredGroup)
    average =  "%.4lf"%(averageMRED*100)+"%"
    dfIndex.append("averageMRED")
    dfMred.append(average)
    dfSobolWidth.append(sobolWidth)

    data={"MRED:":dfMred,"sobolWidth":dfSobolWidth}
    df=pd.DataFrame(data,index=dfIndex)
    df.to_csv(savingPath)
    return df
    

if __name__=="__main__":

    # sobol_1 = [0,4,6,2,3,7,5,1]
    # sobol_2 = [0,4,2,6,3,7,1,5]
    # sobol_3 = [0,4,2,6,5,1,7,3]
    # sobol_4 = [0,4,2,6,7,3,5,1]
    # sobol_5 = [0,4,6,2,3,7,5,1]
    # sobol_6 = [0,4,6,2,1,5,7,3]
    # sobol_7 = [0,4,2,6,3,7,1,5]
    # sobol_8 = [0,4,6,2,7,3,1,5]
    sobol_1 = [0,8,12,4,6,14,10,2,3,11,15,7,5,13,9,1]
    sobol_2 = [0,8,4,12,6,14,2,10,5,13,1,9,3,11,7,15]
    sobol_3 = [0,8,4,12,10,2,14,6,15,7,11,3,5,13,1,9]
    sobol_4 = [0,8,4,12,14,6,10,2,7,15,3,11,9,1,13,5]
    sobol_5 = [0,8,12,4,6,14,10,2,9,1,5,13,15,7,3,11]
    sobol_6 = [0,8,12,4,2,10,14,6,5,13,9,1,7,15,11,3]
    sobol_7 = [0,8,4,12,6,14,2,10,7,15,3,11,1,9,5,13]
    sobol_8 = [0,8,12,4,14,6,2,10,15,7,3,11,1,9,13,5]
    sobol_1 = [0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2 = [0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3 = [0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4 = [0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    sobol_5 = [0,16,24,8,12,28,20,4,18,2,10,26,30,14,6,22,9,25,17,1,5,21,29,13,27,11,3,19,23,7,15,31]
    sobol_6 = [0,16,24,8,4,20,28,12,10,26,18,2,14,30,22,6,31,15,7,23,27,11,3,19,21,5,13,29,17,1,9,25]
    sobol_7 = [0,16,8,24,12,28,4,20,14,30,6,22,2,18,10,26,17,1,25,9,29,13,21,5,31,15,23,7,19,3,27,11]
    sobol_8 = [0,16,24,8,28,12,4,20,30,14,6,22,2,18,26,10,27,11,3,19,7,23,31,15,5,21,29,13,25,9,1,17]


    sobol_1 = [0,32,48,16,24,56,40,8,12,44,60,28,20,52,36,4,6,38,54,22,30,62,46,14,10,42,58,26,18,50,34,2 ,3,35,51,19,27,59,43,11,15,47,63,31,23,55,39,7,5,37,53,21,29,61,45,13,9,41,57,25,17,49,33,1]
    sobol_2 = [0,32,16,48,24,56,8,40,20,52,4,36,12,44,28,60,30,62,14,46,6,38,22,54,10,42,26,58,18,50,2,34 ,17,49,1,33,9,41,25,57,5,37,21,53,29,61,13,45,15,47,31,63,23,55,7,39,27,59,11,43,3,35,19,51]
    sobol_3 = [0,32,16,48,40,8,56,24,60,28,44,12,20,52,4,36,30,62,14,46,54,22,38,6,34,2,50,18,10,42,26,58 ,45,13,61,29,5,37,21,53,17,49,1,33,57,25,41,9,51,19,35,3,27,59,11,43,15,47,31,63,39,7,55,23]
    sobol_4 = [0,32,16,48,56,24,40,8,28,60,12,44,36,4,52,20,42,10,58,26,18,50,2,34,54,22,38,6,14,46,30,62 ,35,3,51,19,27,59,11,43,63,31,47,15,7,39,23,55,9,41,25,57,49,17,33,1,21,53,5,37,45,13,61,29]
    sobol_5 = [0,32,48,16,24,56,40,8,36,4,20,52,60,28,12,44,18,50,34,2,10,42,58,26,54,22,6,38,46,14,30,62 ,9,41,57,25,17,49,33,1,45,13,29,61,53,21,5,37,27,59,43,11,3,35,51,19,63,31,15,47,39,7,23,55]
    sobol_6 = [0,32,48,16,8,40,56,24,20,52,36,4,28,60,44,12,62,30,14,46,54,22,6,38,42,10,26,58,34,2,18,50 ,59,27,11,43,51,19,3,35,47,15,31,63,39,7,23,55,5,37,53,21,13,45,61,29,17,49,33,1,25,57,41,9]
    sobol_7 = [0,32,16,48,24,56,8,40,28,60,12,44,4,36,20,52,34,2,50,18,58,26,42,10,62,30,46,14,38,6,54,22 ,51,19,35,3,43,11,59,27,47,15,63,31,55,23,39,7,17,49,1,33,9,41,25,57,13,45,29,61,21,53,5,37]
    sobol_8 = [0,32,48,16,56,24,8,40,60,28,12,44,4,36,52,20,54,22,6,38,14,46,62,30,10,42,58,26,50,18,2,34 ,43,11,27,59,19,51,35,3,23,55,39,7,47,15,31,63,29,61,45,13,37,5,21,53,33,1,17,49,25,57,41,9]




#########################################################                       
    dataWidth = 16                                    ###        
    sobolWidth = int(math.log(len(sobol_1),2))        ###       
    validSegWidth = sobolWidth+1                      ###
    # validSegWidth = 16                              ###
    dataRange=(1,pow(2,16))                           ###
    iterationRange=dataRange[1]                       ###
#########################################################

    workingPath = os.getcwd()
    
    savingPath=workingPath+'/evaluation/result'
    if not (os.path.exists(savingPath)):
        # savingPath=workingPath+'/result'
        os.mkdir(savingPath)
    
    savingPath = savingPath +'/testDiffSobol'
    if not (os.path.exists(savingPath)):
        os.mkdir(savingPath)
        
    savingPath = savingPath +'/dataRange_1_to_'+str(dataRange[1])
    if not (os.path.exists(savingPath)):
        os.mkdir(savingPath)

    resultName = "sobol_%d_SegWidth_%d.csv"%(pow(2,sobolWidth),validSegWidth)
    savingPath = savingPath + '/'+ resultName
    group_1=[sobol_1,sobol_2]
    group_2=[sobol_2,sobol_3]
    group_3=[sobol_3,sobol_4]
    group_4=[sobol_4,sobol_5]
    group_5=[sobol_5,sobol_6]
    group_6=[sobol_6,sobol_7]
    group_7=[sobol_7,sobol_8]
    group_8=[sobol_8,sobol_3]
    group_9=[sobol_2,sobol_4]
    group_10=[sobol_2,sobol_5]
    group_11=[sobol_2,sobol_6]
    group_12=[sobol_2,sobol_7]
    group_13=[sobol_2,sobol_8]
    group_14=[sobol_3,sobol_4]
    group_15=[sobol_3,sobol_5]
    group_16=[sobol_3,sobol_6]
    
    sobolGroups=[group_1,group_2,group_3,group_4,group_5,group_6]
    # sobolGroups=[group_1]
    # sobolGroups=[group_1,group_2,group_3]

    
    # writer = pd.ExcelWriter('test.xlsx')
        
    mredGroup = []
    for i in range (len(sobolGroups)):
        mredGroup.append(0)
    
    for test in range(iterationRange):
        num_1=random.randint(dataRange[0],dataRange[1])
        num_2=random.randint(dataRange[0],dataRange[1])
        exact_res=num_1*num_2
        # print("num1 = %d, num2 = %d,error = "%(num_1,num_2),end='')
        # print("num1=%d,num2=%d,exact_res=%d"%(num_1,num_2,exact_res))
        for i in range(len(sobolGroups)):
            isc_res=scaled_mul(
                num_1=num_1,num_2=num_2,
                sobol_1= sobolGroups[i][0],sobol_2= sobolGroups[i][1],validSegWidth=validSegWidth,
                sobolWidth= sobolWidth,dataWidth=  dataWidth
            )
            ED = abs(exact_res-isc_res)
            error= ED/exact_res
            mredGroup[i]+=(error)
            # print(isc_res,error, end=' ')
        # print('\n')

    mredGroup = [mredGroup [i] /iterationRange for i in range(len(mredGroup))]

    for i in range(len(mredGroup)):
        
        print("%.4lf"%(mredGroup[i]*100)+";",end=' ')
    averageMRED = statistics.mean(mredGroup)
    print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")
    generate_df(sobolGroups ,mredGroup   ,sobolWidth ,savingPath)
    # return mredGroup ,averageMRED

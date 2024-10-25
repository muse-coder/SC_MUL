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
    sobol_1= [0, 32, 48, 16, 24, 56, 40, 8, 12, 44, 60, 28, 20, 52, 36, 4, 6, 38, 54, 22, 30, 62, 46, 14, 10, 42, 58, 26, 18, 50, 34, 2, 17, 49, 1, 33, 9, 41, 25, 57, 5, 37, 21, 53, 29, 61, 13, 45, 15, 47, 31, 63, 23, 55, 7, 39, 27, 59, 11, 43, 3, 35, 19, 51]
    sobol_2= [0, 32, 16, 48, 24, 56, 8, 40, 20, 52, 4, 36, 12, 44, 28, 60, 30, 62, 14, 46, 6, 38, 22, 54, 10, 42, 26, 58, 18, 50, 2, 34, 45, 13, 61, 29, 5, 37, 21, 53, 17, 49, 1, 33, 57, 25, 41, 9, 51, 19, 35, 3, 27, 59, 11, 43, 15, 47, 31, 63, 39, 7, 55, 23]
    sobol_3= [0, 32, 16, 48, 40, 8, 56, 24, 60, 28, 44, 12, 20, 52, 4, 36, 30, 62, 14, 46, 54, 22, 38, 6, 34, 2, 50, 18, 10, 42, 26, 58, 35, 3, 51, 19, 27, 59, 11, 43, 63, 31, 47, 15, 7, 39, 23, 55, 9, 41, 25, 57, 49, 17, 33, 1, 21, 53, 5, 37, 45, 13, 61, 29]
    sobol_4= [0, 32, 16, 48, 56, 24, 40, 8, 28, 60, 12, 44, 36, 4, 52, 20, 42, 10, 58, 26, 18, 50, 2, 34, 54, 22, 38, 6, 14, 46, 30, 62, 3, 35, 51, 19, 27, 59, 43, 11, 15, 47, 63, 31, 23, 55, 39, 7, 5, 37, 53, 21, 29, 61, 45, 13, 9, 41, 57, 25, 17, 49, 33, 1]
   
#########################################################                       
    dataWidth = 16                                    ###        
    sobolWidth = int(math.log(len(sobol_1),2))        ###       
    validSegWidth = sobolWidth+1                      ###
    # validSegWidth = 16                              ###
    dataRange=(1,pow(2,8))                           ###
    iterationRange=dataRange[1]                       ###
#########################################################

    workingPath = os.getcwd()
    
    savingPath=workingPath+'/evaluation/result'
    if not (os.path.exists(savingPath)):
        # savingPath=workingPath+'/result'
        os.mkdir(savingPath)
    
    savingPath = savingPath +'/testScaledSobol'
    if not (os.path.exists(savingPath)):
        os.mkdir(savingPath)
        
    savingPath = savingPath +'/dataRange_1_to_'+str(dataRange[1])
    if not (os.path.exists(savingPath)):
        os.mkdir(savingPath)

    resultName = "sobol_%d_SegWidth_%d.csv"%(pow(2,sobolWidth),validSegWidth)
    savingPath = savingPath + '/'+ resultName
    group_1=[sobol_1,sobol_2]
    group_2=[sobol_1,sobol_3]
    group_3=[sobol_1,sobol_4]
    group_4=[sobol_2,sobol_3]
    group_5=[sobol_2,sobol_4]
    group_6=[sobol_3,sobol_4]
    
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
        
        print("MRED %d = %.4lf"%(i+1,mredGroup[i]*100)+"% ",end=' ')
    averageMRED = statistics.mean(mredGroup)
    print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")
    generate_df(sobolGroups ,mredGroup   ,sobolWidth ,savingPath)
    # return mredGroup ,averageMRED

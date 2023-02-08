from SC_MUL.components import *
import pandas as pd
import statistics
def generate_df(sobolGroups ,mredGroup  , validSegWidth ,sobolWidth ):
    dfIndex=[]
    dfMred=[]
    dfSobolWidth=[]
    dfValidSegWidth=[]
    for i in range(len(sobolGroups)):
        # print(pattern_name)
        dfIndex.append(("sobolGroup_"+str(i)))
        dfMred.append(mredGroup[i])
        dfValidSegWidth.append(validSegWidth)
        dfSobolWidth.append(sobolWidth)
        # df
    averageMRED = statistics.mean(mredGroup)
    dfIndex.append("averageMRED")
    dfMred.append(averageMRED)
    dfValidSegWidth.append(validSegWidth)
    dfSobolWidth.append(sobolWidth)

    # print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")
    data={"MRED:":dfMred,"validSegWidth":dfValidSegWidth,"sobolWidth":dfSobolWidth}
    df=pd.DataFrame(data,index=dfIndex)
    # file_path_split=file_path.split('\\')
    # print("***********************************")
    # print(df)
    # print(file_path)
    # print("***********************************")
    # to_csv_path="validSegWidth_%d_sobolWidth_%d_MRED_Result.csv"%(validSegWidth,sobolWidth)
    # df.to_csv(to_csv_path)
    return df
    

if __name__=="__main__":
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]

    dataWidth = 16
    num_1=213 <<3 
    num_2=100
    exact_res=num_1*num_2
    sobolWidth = 5
    
    group_1=[sobol_1,sobol_2]
    group_2=[sobol_1,sobol_3]
    group_3=[sobol_1,sobol_4]
    group_4=[sobol_2,sobol_3]
    group_5=[sobol_2,sobol_4]
    group_6=[sobol_3,sobol_4]
    
    sobolGroups=[group_1,group_2,group_3,group_4,group_5,group_6]
    # sobolGroups=[group_1]
    # sobolGroups=[group_1,group_2,group_3]

    testRange=(1,255)    
    iterationRange=255*255
    validSegWidth = 16
    # writer = pd.ExcelWriter('test.xlsx')
        
    mredGroup = []
    for i in range (len(sobolGroups)):
        mredGroup.append(0)
    
    for test in range(iterationRange):
        num_1=random.randint(testRange[0],testRange[1])
        num_2=random.randint(testRange[0],testRange[1])
        exact_res=num_1*num_2
        # print("num1 = %d, num2 = %d,error = "%(num_1,num_2),end='')
        print("num1=%d,num2=%d,exact_res=%d"%(num_1,num_2,exact_res))
        for i in range(len(sobolGroups)):
            isc_res=scaled_mul(
                num_1=num_1,num_2=num_2,
                sobol_1= sobolGroups[i][0],sobol_2= sobolGroups[i][1],validSegWidth=validSegWidth,
                sobolWidth= sobolWidth,dataWidth=  dataWidth
            )
            ED = abs(exact_res-isc_res)
            error= ED/exact_res
            mredGroup[i]+=(error)
            print(isc_res,error, end=' ')
        print('\n')

    mredGroup = [mredGroup [i] /iterationRange for i in range(len(mredGroup))]

    for i in range(len(mredGroup)):
        
        print("MRED %d = %.4lf"%(i+1,mredGroup[i]*100)+"% ",end=' ')
    averageMRED = statistics.mean(mredGroup)
    print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")

    # return mredGroup ,averageMRED

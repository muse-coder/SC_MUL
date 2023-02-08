# import pwd
import re
import  os
import pandas as pd
    
def generate_df(sobolGroups ,mredGroup  , validSegWidth ,sobolWidth ):
    dfIndex=[]
    dfMred=[]
    dfSobolWidth=[]
    dfValidSegWidth=[]
    for i in len(sobolGroups):
        # print(pattern_name)
        dfIndex.append(("sobolGroup_"+str(i)))
        dfMred.append(mredGroup[i])
        dfValidSegWidth.append(validSegWidth)
        dfSobolWidth.append(sobolWidth)
        # df
    data={"MRED:":dfMred,"validSegWidth":dfValidSegWidth,"sobolWidth":dfSobolWidth}
    df=pd.DataFrame(data,index=dfIndex)
    # file_path_split=file_path.split('\\')
    print("***********************************")
    print(df)
    # print(file_path)
    print("***********************************")
    to_csv_path="dataResult.csv"
    df.to_csv(to_csv_path)
    

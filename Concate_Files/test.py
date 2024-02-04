import pandas as pd
import numpy as np
import os

def compileData(path: str, header: int, tail: int):
    df=pd.DataFrame()

    files=os.listdir(path)
    count=0
    for file in files:
        file_path = os.path.join(path,file)
        
        count=count+1
        print(count)
        
        if os.path.isfile(file_path):
            df1=pd.read_excel(file_path,sheet_name='Sheet', header=header)
            df1=df1.drop(df1.tail(tail).index)
            df=df._append(df1)
            print(df1)

    print(df)
    return df

if __name__ == '__main__':
    print("This program concatenates excel files of the same headings:")
    print("The excel files should be placed in a folder and the folder should not contain any files that needn't be processed.")
    print("The resulting file will be placed in the same directory as the program and will overwrite, if exists, the file with the same name in the said directory.")
    print()
    print("Enter the file directory two lines below:","For example the current folder should be './', no need to input the quotation marks:",sep="\n")
    path=input()
    print("Enter the number of irrelevant lines prior to the header:", end=" ")
    header=int(input())
    print("Enter the number of excessive lines at the bottom of each excel file ( for example lines that record total amounts ):",end=" ")
    tail=int(input())
    df=compileData(path,header,tail)

    df.to_excel('data.xlsx')

    input()

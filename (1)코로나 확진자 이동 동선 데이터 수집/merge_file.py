import pandas as pd
import os

def conc(f):
    ans=[]
    i=0
    while (True):
        try:
            call = pd.read_excel(f, sheet_name=i)
            ans+=craft(call)
            i += 1
        except:
            break
    return ans

def craft(f):
    try:
        for i,s in enumerate(f.columns.tolist()):
            if '장소' in str(s):
                return  f[str(s)].tolist()
            elif '경로' in str(s):
                return f[str(s)].tolist()
            elif '업소' in str(s):
                return f[str(s)].tolist()
    except:
        return []

if __name__ == "__main__":
    os.chdir(r'C:\Users\입학홍보처\Desktop\파이썬\korona_data_collection')
    f_list=os.listdir()
    print(f_list)

    merge=[]
    for i in f_list:
        try:
            merge+=conc(i)
        except:
            print('error in '+ i)

    df = pd.DataFrame(merge, columns=['장소'])
    df.to_excel('merge_file.xlsx',index=False)


import pandas as pd 
import matplotlib 
import cutting
import output
import narabikae
import select

df_14=pd.read_csv("2014.csv")
df_15=pd.read_csv("2015.csv")
df_16=pd.read_csv("2016.csv")
df_17=pd.read_csv("2017.csv")
df_18=pd.read_csv("2018.csv")
df_19=pd.read_csv("2019.csv")
df_20=pd.read_csv("2020.csv")

df14_20=pd.concat([df_14,df_15,df_16,df_17,df_18,df_19,df_20])
df14_20=df14_20.drop("Unnamed: 0",axis=1)
df14_20.index+=1
print(df14_20)

print("どの操作を行いますか？")

while(1):
    choice=input("並び替え:1 ,抽出:2 ,削除:3 ,出力:4,表示:5 --->")
    if int(choice)==1:
        dt=narabikae.sorting(df14_20)
        print(dt)
        prev=df14_20
        df14_20=dt
        print("まだ操作を行いますか")
        cont=input("はい:1 ,いいえ:2---->")
        if int(cont)==1:
            continue
        elif int(cont)==2:
            break
        break
        
    elif int(choice)==2:
        dt=select.choose(df14_20)
        prev=df14_20
        df14_20=dt
        print("まだ操作を行いますか")
        cont=input("はい:1 ,いいえ:2---->")
        if int(cont)==1:
            continue
        elif int(cont)==2:
            break
        break
    elif int(choice)==3:
        dt=cutting.cut(df14_20)
        prev=df14_20
        df14_20=dt
        print("まだ操作を行いますか")
        cont=input("はい:1 ,いいえ:2---->")
        if int(cont)==1:
            continue
        elif int(cont)==2:
            break
        break
    elif int(choice)==4:
        output.out(df14_20)
        print("まだ操作を行いますか")
        cont=input("はい:1 ,いいえ:2---->")
        if int(cont)==1:
            continue
        elif int(cont)==2:
            break
        break

    elif int(choice)==5:
        pd.set_option("display.max_rows",1000)
        print(df14_20)
        break
    else:
        print("入力が適切ではありません.もう一度入力し直してください")
        continue






import pandas as pd

def choose(fl):
    while(1):
        print("どれでデータを抽出しますか")
        print("年[西暦]:1 ,月:3 ,市・区名:4")
        cho1=input("人口総数[人]:5 ,男[人]:6 ,女[人]:7 ,世帯数[世帯]:8 ---->")
        if int(cho1)==1:
            fln=year(fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==2:
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==3:
            fln=month(fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==4:
            fln=city(fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==5:
            fln=pop(cho1,fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==6:
            fln=pop(cho1,fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==7:
            fln=pop(cho1,fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==8:
            fln=pop(cho1,fl)
            print("まだ挿入操作を続けて行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        else:
            print("正しい入力が行われませんでした。もう一度入力してください")
    return fln

def pop(i,fl1):
    min=0
    max=999999999
    print("数値での条件を行います")
    cho_min=input("最小値を入力してください(最小値の指定がない場合minと入力してください):")
    cho_max=input("最小値を入力してください(最大値の指定がない場合maxと入力してください):")
    if int(i)==5:
        if cho_min=="min":
            fl1=fl1[(fl1["人口総数[人]"] >=min ) & (fl1["人口総数[人]"] <=int(cho_max))]

        elif cho_max=="max":
            fl1=fl1[(fl1["人口総数[人]"] >=int(cho_min) ) & (fl1["人口総数[人]"] <=max)]
        else :
            fl1=fl1[(fl1["人口総数[人]"] >=int(cho_min) ) & (fl1["人口総数[人]"] <=int(cho_max))]

    elif int(i)==6:
        if cho_min=="min":
            fl1=fl1[(fl1["男[人]"] >=min ) & (fl1["男[人]"] <=int(cho_max))]

        elif cho_max=="max":
            fl1=fl1[(fl1["男[人]"] >=int(cho_min) ) & (fl1["男[人]"] <=max)]
        else :
            fl1=fl1[(fl1["男[人]"] >=int(cho_min) ) & (fl1["男[人]"] <=int(cho_max))]

    elif int(i)==7:
        
        if cho_min=="min":
            fl1=fl1[(fl1["女[人]"] >=min ) & (fl1["女[人]"] <=int(cho_max))]

        elif cho_max=="max":
            fl1=fl1[(fl1["女[人]"] >=int(cho_min) ) & (fl1["女[人]"] <=max)]
        else :
            fl1=fl1[(fl1["女[人]"] >=int(cho_min) ) & (fl1["女[人]"] <=int(cho_max))]

    elif int(i)==8:
        if cho_min=="min":
            fl1=fl1[(fl1["世帯数[世帯]"] >=min ) & (fl1["世帯数[世帯]"] <=int(cho_max))]

        elif cho_max=="max":
            fl1=fl1[(fl1["世帯数[世帯]"] >=int(cho_min) ) & (fl1["世帯数[世帯]"] <=max)]
        else :
            fl1=fl1[(fl1["世帯数[世帯]"] >=int(cho_min) ) & (fl1["世帯数[世帯]"] <=int(cho_max))]
   


    return fl1
def year(fl1):
    min=0
    max=99999999
    cho_min=input("抽出する開始年を入力してください(開始年なしの場合はmin):")
    cho_max=input("終了年を入力してください(終了年の場合はmax):")
    if cho_min=="min":
            fl1=fl1[(fl1["年[西暦]"] >=min ) & (fl1["年[西暦]"] <=int(cho_max))]

    elif cho_max=="max":
            fl1=fl1[(fl1["年[西暦]"] >=int(cho_min) ) & (fl1["年[西暦]"] <=max)]
    else :
            fl1=fl1[(fl1["年[西暦]"] >=int(cho_min) ) & (fl1["年[西暦]"] <=int(cho_max))]



    return fl1
def city(fl1):
    while(1):
        print("どの市・区を抽出しますか")
        print("新潟市:1 ,西区:2 ,東区:3 ,北区:4 ,南区:5 ")
        cho1=input("中央区:6 ,秋葉区:7 ,西蒲区:8 ,江南区:9 ---->")
        if int(cho1)==1:
            fl1=fl1[fl1["市・区名"].isin(["新潟市"])]
            break
        elif int(cho1)==2:
            fl1=fl1[fl1["市・区名"].isin(["西区"])]
            break
        elif int(cho1)==3:
            fl1=fl1[fl1["市・区名"].isin(["東区"])]
            break
        elif int(cho1)==4:
            fl1=fl1[fl1["市・区名"].isin(["北区"])]
            break
        elif int(cho1)==5:
            fl1=fl1[fl1["市・区名"].isin(["南区"])]
            break
        elif int(cho1)==6:
            fl1=fl1[fl1["市・区名"].isin(["中央区"])]
            break
        elif int(cho1)==7:
            fl1=fl1[fl1["市・区名"].isin(["秋葉区"])]
            break
        elif int(cho1)==8:
            fl1=fl1[fl1["市・区名"].isin(["西蒲区"])]
            break
        elif int(cho1)==9:
            fl1=fl1[fl1["市・区名"].isin(["江南区"])]
            break
        else:
            print("正しい入力が行われませんでした")
            print("もう一度入力してください")

    return fl1
def month(fl1):
    while(1):
        print("どちらの操作を行いますか")
        cho1=input("一月抽出:1 ,範囲抽出:2 ---->")
        if int(cho1)==1:
            while(1):
                cho2=input("どの月を抽出しますか:")
                if 1<=int(cho2)<=12:
                    fl1=fl1[fl1["月"]==int(cho2)]
                    break
                else:
                    print("もう一度入力し直してください")
        elif int(cho1)==2:
            while(1):
                cho_s=input("開始月:")
                cho_g=input("終了月:")
                if int(cho_s)<int(cho_g):
                    fl1=fl1[(fl1["月"] >=int(cho_s) ) & (fl1["月"] <=int(cho_g))]
                    return fl1
                else:
                    print("もう一度入力し直してください")    
    return fl1

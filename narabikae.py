import pandas as pd
def sorting(fi):
    print("どれをソートしますか")
    print("年[西暦]:1 ,月:2 ,市・区名:3")
    cho1=input("人口総数[人]:4 ,男[人]:5 ,女[人]:6 ,世帯数[世帯]:7 ---->")

    cho2=input("昇順:1 ,降順:2---->")

    st=sorting2(fi,cho1,cho2)

    return st
def sorting2(fi1,a,b):
    if int(a)==1:
        if int(b)==1:
            st1=fi1.sort_values("年[西暦]",ascending=True)
        else:
            st1=fi1.sort_values("年[西暦]",ascending=False)

    elif int(a)==2:
        if int(b)==1:
            st1=fi1.sort_values("月",ascending=True)
        else:
            st1=fi1.sort_values("月",ascending=False)

    elif int(a)==3:
        if int(b)==1:
            st1=fi1.sort_values("市・区名",ascending=True)
        else:
            st1=fi1.sort_values("市・区名",ascending=False)
    
    elif int(a)==4:
        if int(b)==1:
            st1=fi1.sort_values("人口総数[人]",ascending=True)
        else:
            st1=fi1.sort_values("人口総数[人]",ascending=False)
    
    elif int(a)==5:
        if int(b)==1:
            st1=fi1.sort_values("男[人]",ascending=True)
        else:
            st1=fi1.sort_values("男[人]",ascending=False)
    
    elif int(a)==6:
        if int(b)==1:
            st1=fi1.sort_values("女[人]",ascending=True)
        else:
            st1=fi1.sort_values("女[人]",ascending=False)

    elif int(a)==7:
        if int(b)==1:
            st1=fi1.sort_values("世帯数[世帯]",ascending=True)
        else:
            st1=fi1.sort_values("世帯数[世帯]",ascending=False)
    

    return st1

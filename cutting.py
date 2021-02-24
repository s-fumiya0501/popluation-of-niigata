import pandas as pd 

def cut(fl):
    
    while(1):
        print("どちらを削除しますか")
        cho1=input("行:1 ,列:2---->")
        if int(cho1)==1:
            cut_row(fl)
            print("まだ削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        elif int(cho1)==2:
            fln=cut_colmun(fl)
            print("まだ削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
            break
        else:
            print("正しく入力が行われませんでした。もう一度入力して下さい")
            print("どちらを削除しますか")
            
    
    return fln

def cut_row(fl1):
    while(1):
        print("行の削除は指定1行ですか,指定範囲行ですか")
        cho1=input("指定1行:1 ,指定範囲:2 ---->")
        if int(cho1)==1:
            cho2=input("行番号を入力してください:")
            fl1=fl1.drop(int(cho2))
            print("まだの行の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==2:
            cho_s=input("範囲開始の行番号を入力してください")
            cho_g=input("範囲終了の行番号を入力してください")
            fl1=fl1.drop(range(int(cho_s),int(cho_g)))
            print("まだの行の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        else:
            print("正しい入力が行われませんでした。もう一度入力してください")
        
        return fl1





    return

def cut_colmun(fl1):
    
    
    while(1):
        print("どの列を削除しますか")
        print("年[西暦]:1 ,年[和暦]:2 ,月:3 ,市・区名:4")
        cho1=input("人口総数[人]:5 ,男[人]:6 ,女[人]:7 ,世帯数[世帯]:8 ---->")
        if int(cho1)==1:
            fl1=fl1.drop("年[西暦]",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==2:
            fl1=fl1.drop("年[和暦]",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==3:
            fl1=fl1.drop("月",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==4:
            fl1=fl1.drop("市・区名",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==5:
            fl1=fl1.drop("人口総数[人]",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==6:
            fl1=fl1.drop("男[人]",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==7:
            fl1=fl1.drop("女[人]",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        elif int(cho1)==8:
            fl1=fl1.drop("世帯数[世帯]",axis=1)
            print("まだ列の削除操作を行いますか")
            cont=input("はい:1 ,いいえ:2---->")
            if int(cont)==1:
                continue
            elif int(cont)==2:
                break
        else:
            print("正しい入力が行われませんでした。もう一度入力してください")

    return fl1
#coding=Big5
def meun():
    while True:
        print("請輸入指令: 1.英翻中 2.中翻英 3.離開")
        trs = input()
        if trs=="3":
            print("")
            break
        elif trs== "1":
            etc()
        elif trs== "2":
            cte()      
        else:
            print("請輸入正確的指令!")
        print("")
def etc():
    a = {'bird':'鳥','cat':'貓','dog':'狗','fish':'魚','mouse':'老鼠','rabbit':'兔子','cow':'母牛','horse':'馬','pig':'豬','sheep':'綿羊'}
    quest=input("請輸入英文單字:")
    if (a.get(quest) != None):
        print(quest + " => " + a.get(quest))
    else:
        print ("查無此單字")
        
def cte():
    b= {'鳥':'bird','貓':'cat','狗':'dog','魚':'fish','老鼠':'mouse','兔子':'rabbit','母牛':'cow','馬':'horse','豬':'pig','綿羊':'sheep'}
    quest2=input("請輸入中文單字:")
    if (b.get(quest2) != None):
        print(quest2 + " => " + b.get(quest2))
    else:
        print ("查無此單字")
        
    
if __name__ == '__main__':
    meun()
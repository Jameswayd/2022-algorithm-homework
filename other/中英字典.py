#coding=Big5
def meun():
    while True:
        print("�п�J���O: 1.�^½�� 2.��½�^ 3.���}")
        trs = input()
        if trs=="3":
            print("")
            break
        elif trs== "1":
            etc()
        elif trs== "2":
            cte()      
        else:
            print("�п�J���T�����O!")
        print("")
def etc():
    a = {'bird':'��','cat':'��','dog':'��','fish':'��','mouse':'�ѹ�','rabbit':'�ߤl','cow':'����','horse':'��','pig':'��','sheep':'����'}
    quest=input("�п�J�^���r:")
    if (a.get(quest) != None):
        print(quest + " => " + a.get(quest))
    else:
        print ("�d�L����r")
        
def cte():
    b= {'��':'bird','��':'cat','��':'dog','��':'fish','�ѹ�':'mouse','�ߤl':'rabbit','����':'cow','��':'horse','��':'pig','����':'sheep'}
    quest2=input("�п�J�����r:")
    if (b.get(quest2) != None):
        print(quest2 + " => " + b.get(quest2))
    else:
        print ("�d�L����r")
        
    
if __name__ == '__main__':
    meun()
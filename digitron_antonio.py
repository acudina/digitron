
def password():
    lozinka=input("UNESU LOZINKU ")
    while lozinka != "keko":
        lozinka=input("PONOVO UNESU LOZINKU ")
        if len (lozinka)<3:
            print("PRE KRATKO")
            print(" ")
            print("VAS UNOS IMA-",len(lozinka),"-")
        elif len (lozinka)>7:
            print("PRE DUGO-",len(lozinka),"-")    
            print(" ")
            
        
    if lozinka=="keko":
        print(" ")
        print("ISPRAVNA LOZINKA")
        

def izbornik():
    print(" ")
    print(" ODABERITE RACUNSKU RADNJU")
    print(" -----------------------------")
    print(" 1=ZBRAJANJE")
    print(" ")
    print(" 2=ODUZIMANJE ")
    print(" ")
    print(" 3=MNOZENJE ")
    print(" ")
    print(" 4=DJELJENJE ")
    print(" ")
    print(" 5=HELP")
    print(" ")






    
    
    
    
    
def funkcije(): 
    menu=int(input("OPERACIJA="))
    while menu !=1 and menu !=2 and menu !=3 and menu !=4 and menu !=5:
        menu=int(input("IZBOR MORA BITI OD 1 DO 5 :"))    
    if menu==1:
        zbrajanje()
    elif menu==2:
        oduzimanje()
    elif menu==3:
        mnozenje()
    elif menu==4:
        djeljenje()
    elif menu==5:
        help()

    else:
        print("KRAJ")
       

    
    
    
    
    

    
    
    
    
    
    
def zbrajanje():
    print(" ")
    a=float(input("UNESITE PRVI BROJ a="))
    print(" ")
    b=float(input("UNESITE DRUGI BROJ b="))
    print(" ")       
    print("ZBROJ JE=",a+b)
    izlaz=input("ZA IZLAZ STISNI i")
    if izlaz == "i":
        izbornik()
        funkcije()
    else:
        print("HVALA STO STE UPOTREBLJAVALI PROGRAM")   
        
        
def oduzimanje():
    print(" ")
    a=float(input("UNESITE PRVI BROJ a="))
    print(" ")
    b=float(input("UNESITE DRUGI BROJ b="))
    print(" ")       
    print("RAZLIKA JE=",a-b)
    izlaz=input("ZA IZLAZ STISNI i")
    if izlaz == "i":
        izbornik()
        funkcije()
    else:
        print("HVALA STO STE UPOTREBLJAVALI PROGRAM")    

def mnozenje():
    print(" ")
    a=float(input("UNESITE PRVI BROJ a="))
    print(" ")
    b=float(input("UNESITE DRUGI BROJ b="))
    print(" ")       
    print("UMNOZAK JE",a*b)
    izlaz=input("ZA IZLAZ STISNI i")
    if izlaz == "i":
        izbornik()
        funkcije()
    else:
        print("HVALA STO STE UPOTREBLJAVALI PROGRAM")    
    
def djeljenje():
    print(" ")
    a=float(input("UNESITE PRVI BROJ a="))
    print(" ")
    b=float(input("UNESITE DRUGI BROJ b="))
    print(" ")       
    print("KOLICNIK JE",a//b,"A OSTATAK JE",a%b)
    izlaz=input("ZA IZLAZ STISNI i")
    if izlaz == "i":
        izbornik()
        funkcije()
    else:
        print("HVALA STO STE UPOTREBLJAVALI PROGRAM")    
    
    
def help():
    print(" zbrajanje je...")
    print(" oduzimanje je...")
    print(" mnozenje je...")
    print(" djeljennje je...")
    izlaz=input("ZA IZLAZ STISNI i")
    if izlaz == "i":
        izbornik()
        funkcije()
    else:
        print("HVALA STO STE UPOTREBLJAVALI PROGRAM")
    
    
#PROGRAM--------------------------------------

print("------DIGITRON------")
password()
izbornik()
funkcije()

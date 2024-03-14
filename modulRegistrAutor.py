

def kirjutata_failisse(fail:str, jarjend=[]):
    """
    
    :param fail: 
    :param jarjend: 
    :return: 
    """
    #n = int(input("Sisestage mitu elemendi: "))
    #for i in range(n):
    # jarjend.append(input(f"{i+1}.element: "))
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()




def kirjutata_log_pas(fail:str, jarjend1=[], jarjend2=[]):
    """
    Funktsioon, mis kirjutab iga elemendi eraldi rida
    :param fail:
    :param jarjend:
    :rtype: fail
    """
    f = open(fail,'w', encoding = "utf-8")
    for i in range(len(jarjend1)):
        f.write(jarjend1[i]+";"+jarjend2[i]+"\n")
    f.close()



def loe_pas_ja_log(fail:str)->any:
    """
    Loeb failist andmed, mis oli sisestatud formaadis "login:password" igas reas eraldi
    :param fail:
    :rtype: fail
    """
    fail = open(fail,"r", encoding = "utf-8")
    log = []
    pas = []
    #log_pas
    for line in fail:
        n = line.find(":") #login:password - разделить
        log.append(line[0:n].strip())
        pas.append(line[n+1:len(line)].strip())
        #l,p=line.strip().split(":")
        #log_pas[l]=p
        fail.close()
        return log,pas

def kontrollimne_inimine_loendis(fail:str)-> any:
    """
    See funktsioon kontrollib, kas selline kasutaja on loendis v
    :param fail:
    :return:
    """

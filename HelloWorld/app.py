import random

pyetjet = { #dictionary
    "Sa ditë ka viti?": ("365", ["365", "360", "366", "364"]), #KEY dhe value = tuple me 2 items/list
    "Cili është kryeqyteti i Italisë?": ("Roma ", ["Milano", "Venecia", "Roma ", "Napoli"]),
    "Cili është elementi kimik me simbolin H?": ("Hidrogjen", ["Helium", "Hidrogjen", "Hekur", "Hidrazin"]),
    "Kush e shkroi veprën Hamleti?": ("William Shakespeare", ["Jane Austen", "Charles Dickens", "William Shakespeare", "Mark Twain"]),
    "Sa ështe shuma e numrave 500+365? ": ("865", ["765", "550", "800", "865"])
}

def shfaq_pyetjet(pytj, opsionet): #Fuksioni 1
    print("\n" + pytj) #Printon pyetjen
    for index, ops in enumerate(opsionet): #For loop - I merr secilin prej opsioneve nje nga nje permes indexit
        print(f"{chr(65 + index)}. {ops}") #I paraqet opsionet me karaktere: A,B,C,D

def pergjigjja(): #Funksioni 2 nuk ka parametra vetem punon me input nga perdoruesi
    while True:
        prgj = input("Zgjedhja jote (A-D): ").upper() #E merr pergjigjjen // Inputi
        if prgj in ["A", "B", "C", "D"]: #E kontrollon  //Validimi
            return prgj #Nese eshte pjese e listes e kthen dhe ndalet while loop
        else:   #Nese nuk eshte pjese e listes e printon fjaline me poshte
            print("Zgjedhja juaj nuk është valide, duhet të zgjedhni nga A - D.")

def kontrollo_pergjigjjen(prgj_userit, prgj_esakte, opsionet): #Funksioni 3 me 3 inputa - kontrollon a eshte pergjigjja e sakte
    index = ord(prgj_userit) - 65 #E llogarit karakterin qe e ka shenu useri - 65 dhe jep indexin e pergjigjjes psh. A=65, 65-65=0, e mer indexin 0
    return opsionet[index] == prgj_esakte #Kthen True ose False

def rezuktati(piket, totali): #Funksioni 4 paraqet piket ne fund te lojes
    print(f"\nLoja përfundoi! Pikët e tua: {piket} nga {totali}")

def main():
    piket = 0 #variabla qe do te mbaj numrin e pikeve te sakta
    lista_pyetjeve = list(pyetjet.items()) #Pyetjet dhe pergjigjeti kthen si liste
    random.shuffle(lista_pyetjeve) #I rendit pyetjet random

    for pyetje, (sakte, opsionet) in lista_pyetjeve: #E mer pyetjen, pergjigjjen e sakte dhe listen e opsioneve nga lista
        random.shuffle(opsionet) #I perxien pergjigjet te dalin random // Gjenerimi automatik i diqkaje
        shfaq_pyetjet(pyetje, opsionet) # E thirr funksionin e pare
        prgj = pergjigjja()
        if kontrollo_pergjigjjen(prgj, sakte, opsionet): #Nese kthen True
            print("E Saktë!")
            piket += 1
        else:
            print(f"Gabim! Përgjigjja e saktë ishte: {sakte}")

    rezuktati(piket, len(pyetjet)) #Llogarit sa pike i mori nga numri i pyetj

if __name__ == "__main__":
    main()


id_student="buteanu_cosmin_97@yahoo.com"
password = "ZGXDWZ"
lista_jocuri=[]
vocale=['A','Ă','Î','Â','E','I','O','U']
consoane1=['R','N','T','Ș','Ț','C','S','L','D','M','P']
consoane2=['V','B','F','G','Z','H','J','K','X','Y','W','Q']
nr_jocuri=0
nr_total_incercari=0


# Function where I check where the letter is fitting
def unde_se_potriveste_litera(id_student,id_joc,litera):
    i=0
    j=0
    lista_pozitii=[]
    while i<len(cuvantul_stiut):
        if (i > len(cuvantul_stiut)):
            lista_pozitii = []
        while j<len(cuvantul_ascuns):
            if (cuvantul_ascuns[j]=="*"):
                if(litera==cuvantul_stiut[i]):
                    lista_pozitii.append(j)
                    i=i+1
                    j=j+1
                else:
                    i=i+1
                    j=j+1
            else:
                i=i+1
                j=j+1
    return lista_pozitii

# Function that is checking the word

def verifica_cuvantul(id_student,id_joc,cuvantul_format):
    i=0;
    nr=0
    while(i<len(cuvantul_format)):
        if(cuvantul_format[i]=="*"):
            nr+=1
        i+=1
    if nr==0:
        return 1
    else:
        return 0
    return verifica_cuvantul(id_joc,cuvantul_format)

# Function that counts the number of games from the txt file
def numar_jocuri(id_student,nr_jocuri):
    f1 = open("cuvinte_de_verificat.txt")
    nr_jocuri=0
    for linii in f1.readlines():
        nr_jocuri+=1
    print("nr_jocuri =", nr_jocuri)
    return nr_jocuri
nr_jocuri= numar_jocuri(id_student,nr_jocuri)
f1 = open ("cuvinte_de_verificat.txt")
for linii in f1.readlines():
    joc=[]
    for linie in linii.split(";"):
        joc.append(linie.replace("\n",""))
    lista_jocuri.append(joc)
    id_joc=joc[0]
    cuvantul_ascuns=joc[1]
    cuvantul_stiut=joc[2]
    c=list(cuvantul_ascuns)

    nr_incercari=0
    for litera in vocale:
        nr_incercari+=1
        nr_total_incercari+=1
        lista_pozitii = unde_se_potriveste_litera(id_student, id_joc, litera)
        if lista_pozitii:
            i=0
            while(i<len(lista_pozitii)):
                j=lista_pozitii[i]
                del c[j]
                c.insert(j,litera)
                i+=1
        if verifica_cuvantul(id_student,id_joc,c)==1:
            ok=1
            break
    for litera in consoane1:
        lista_pozitii = unde_se_potriveste_litera(id_student, id_joc, litera)
        nr_incercari+=1
        nr_total_incercari+=1
        if lista_pozitii:
            i=0
            while(i<len(lista_pozitii)):
                j=lista_pozitii[i]
                del c[j]
                c.insert(j,litera)
                i+=1
        if verifica_cuvantul(id_student,id_joc,c)==1:
            ok=1
            break
    print("id_joc =", id_joc, ";", "nr_incercari =", nr_incercari)
cuvantul_format=" ".join(c)


nr_incercari=0
print ("nr_total_incercari =",nr_total_incercari)
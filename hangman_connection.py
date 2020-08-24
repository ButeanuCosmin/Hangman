import hangmanClient
id_student="buteanu_cosmin_97@yahoo.com"
password = "ZGXDWZ"
lista_jocuri=[]
vocale=['A','Ă','Î','Â','E','I','O','U']
consoane1=['R','N','T','Ș','Ț','C','S','L','D','M','P']
consoane2=['V','B','F','G','Z','H','J','K','X','Y','W','Q']
nr_jocuri=0
nr_total_incercari=0
def unde_se_potriveste_litera(id_student,id_joc,litera):
    lista_pozitii=[]
    lista_pozitii=hangmanClient.check_letter(id_joc,litera)
    return lista_pozitii
def verifica_cuvantul(id_student,id_joc,cuvantul_format):
    return hangmanClient.verifica_cuvantul(id_joc,cuvantul_format)
hangmanClient.login(id_student,password)
print ("nr_jocuri =", numar_jocuri(id_student,nr_jocuri))

while True:
    game=hangmanClient.new_game()
    print(game)
    if(game["game_id"]==100):
        break
    id_joc=game["game_id"]
    cuvant_ascuns=game["word_to_guess"]
    nr_incercari=0
    for litera in vocale:
        nr_incercari+=1
        nr_total_incercari+=1
        lista_pozitii = unde_se_potriveste_litera(id_student, id_joc, litera)
        if lista_pozitii:
            i=0
            while(i<len(lista_pozitii)):
                j=lista_pozitii[i]
                i+=1
    for litera in consoane1:
        lista_pozitii = unde_se_potriveste_litera(id_student, id_joc, litera)
        nr_incercari+=1
        nr_total_incercari+=1
        if lista_pozitii:
            i=0
            while(i<len(lista_pozitii)):
                j=lista_pozitii[i]
                i+=1
print ("id_joc =",id_joc,";","nr_incercari =",nr_incercari)
nr_incercari=0
print ("nr_total_incercari =",nr_total_incercari)

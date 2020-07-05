
print ("Benvenuto sul mio test gioco.")
print ("Come ti chiami?")
nome_giocatore = input()
print("Autenticato  " + nome_giocatore)

numero_segreto = 8
print ("Indovina il numero da 1 a 10")

while(True):
 numero_inserito = int(input())
 if (numero_inserito == numero_segreto):
  print (nome_giocatore + "Hai indovinato il numero segreto, bravo!")
  break
 if (numero_inserito > numero_segreto):
  print (nome_giocatore + "Ci sei quasi, ma il numero inserito è maggiore del numero segreto..")
 if (numero_inserito < numero_segreto):
  print (nome_giocatore + "Ci sei quasi, ma il numero inserito è minore del numero segreto..")
  
if (numero_inserito == numero_segreto):
  print("Sessione finita.")
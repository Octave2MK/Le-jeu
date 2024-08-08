
#      Mon jeu qui regroupe les notions de base.

#from tkinter import *
import tkinter

class MonJeu():
  def __init__(self):
      self.gameMorel = tkinter.Tk()
      self.gameMorel.title("P'tit jeu de Morel")
      self.gameMorel.geometry("1280x768")
      self.gameMorel.resizable(width=False, height=False)
      self.gameMorel.config(bg='dark olive green')

      self.welcome = tkinter.Label(self.gameMorel, text=" Bienvenue dans mon Jeu ", font=("Matura MT Script Capitals", 30, "bold"), bg="lemon chiffon", fg='gray', relief=tkinter.SUNKEN)
      self.welcome.pack()

      self.name = tkinter.Label(self.gameMorel, text="Entrez votre nom :", font=("Forte", 15))
      self.name.pack(side=tkinter.TOP, padx=10, pady=10, fill=tkinter.NONE, anchor="w", expand=0)

      self.background_text1 = "Entrez votre nom ici"
      self.entername = tkinter.Entry(self.gameMorel, width=25, bg="azure2", fg="gray", font=(20))
      self.entername.insert(0, self.background_text1)
      self.entername.pack(side=tkinter.TOP, padx=10, pady=0, fill=tkinter.NONE, anchor="w", expand=0)
      self.entername.bind("<FocusIn>", self.on_click1)  # Correction ici

      self.age = tkinter.Label(self.gameMorel, text="Entrez votre age :", font=("Cooper Black", 15))
      self.age.pack(side=tkinter.TOP, padx=10, pady=10, fill=tkinter.NONE, anchor="w", expand=0)

      self.background_text2 = "Entrez votre age ici"
      self.enterage = tkinter.Entry(self.gameMorel, width=20, bg="azure2", fg="gray", font=(20))
      self.enterage.insert(0, self.background_text2)
      self.enterage.pack(side=tkinter.TOP, padx=10, pady=0, fill=tkinter.NONE, anchor="w", expand=0)
      self.enterage.bind("<FocusIn>", self.on_click2)  # Correction ici

      self.validate = tkinter.Button(self.gameMorel, text="Valider", width=8, height=2, command=self.recuperate_name_age)  # Correction ici
      self.validate.pack(side=tkinter.TOP, padx=20, pady=10, fill=tkinter.NONE, anchor="w", expand=0)

  def on_click1(self, event):  # Correction ici
    if self.entername.get() == self.background_text1:
      self.entername.delete(0, END)
      self.entername.configure(foreground="black")

  def on_click2(self, event):  # Correction ici
    if self.enterage.get() == self.background_text2:
      self.enterage.delete(0, END)
      self.enterage.configure(foreground="black")

  def recuperate_name_age(self):  # Correction ici
    self.validate.config(state=DISABLED)
    self.contenu_name = self.entername.get()
    self.contenu_age = self.enterage.get()
    self.salutation = tkinter.Label(self.gameMorel, text="Salut {}, vous avez {} ans".format(self.contenu_name, self.contenu_age))
    self.salutation.pack(side=tkinter.TOP, padx=10, pady=10, fill=tkinter.NONE, anchor="w", expand=0)

  def mainloop(self):
    self.gameMorel.mainloop()

# Instanciation de l'objet MonJeu
#jeu = MonJeu()
# Lancement de la boucle principale
#jeu.mainloop()


Bonjour = lambda:print(" 👉👉 Tapez ”1” pour OUI et ”2” pour NON.")

nomJoueur = str(input("Entrez votre nom🤩:\n🖋🖊🖍 "))
print("")
print("Salut 🤖❗,", nomJoueur+"🤩")

def instruction1():

  inscription = True
  while inscription:
    try:
      Age = int(input("Entrez votre age:\n🖋🖊🖍 "))
    except ValueError:
      print("⛔⛔😬😬 Vous devez entrer un age")
      instruction1()
    else:
      if Age in range(2, 101):
      
        text = "Salut {}, vous avez {}ans donc vous ètes majeur."
        text2 = "Salut {}, vous avez {}ans donc vous ètes mineur."
        text3 = "Salut {}, vous avez {}ans donc vous venez d'être majeur."

        # Age > 1 and Age <=100 ---> 1 < Age < 100
        #  and (ET)
        #  or(OU)
        #  in/ not in(DANS/PAS DANS)

        print("Votre age est valide👌.")
        print("Vous êtes dans votre" , Age,"ème année.")

        if Age > 18:
          print(text.format(nomJoueur, Age))
          break
        elif Age < 18:
          print(text2.format(nomJoueur, Age))
          break
        else:
          print(text3.format(nomJoueur, Age))
          break
      elif Age not in range(2, 101):
        print("⛔⛔Votre age n'est pas valide👎.\n")
        print("😬😬 Veillez réessayer en entrant un age valide.")
        print("")
        instruction1()
    break
instruction1()
print("")


Bonjour()
def Niveau1():
  OUI = 1
  NON = 2

  try:
    Decision = int(input("Souhaitez-vous commencer le jeu🎮 ❓:\n🖋🖊🖍 "))
  except ValueError:
    print("⛔⛔😬😬 Choix invalide❗ Veillez entrer ”1” pour OUI et ”2” pour NON.")
    Niveau1()
  else:
    
    if Decision == OUI:
      print("\t🤸🙌 Vous êtes à present dans le NIVEAU 1 du jeu.")
      print("")

      jeux = True
      Reponse = 18
      def instruction():
        
        # Cette partie du code peut s'ecrire d'une autre maniere sans la boucle "while".
        # Un exemple du meme concepte un peut plus bas sans la boucle "while".

        while jeux:
          print("Entrez l'age qui permet d'identifier si on est majeur💪💪.")
          #   Pour gere le genre d'erreur ou l'utilisateur entre autre chose qu'un nombre
          try:
            Devinette = int(input("🖋🖊🖍 "))
          except:
            print("⛔⛔😬😬 Vous devez entrer un age")
            instruction()
          else:
            if Devinette in range(1, 101):
              if Devinette == Reponse:
                print("✔✔Felicitation👍👏👏 vous avez trouvez juste.")
              else:
                print("Désolé 😫😞❌ ce n'est pas la bonne réponse. Veillez réessayer.")
                print("")
                instruction()
              break
            elif Devinette not in range(1, 101):
              print("⛔⛔😬😬 Veillez réessayer en entrant un age valide.")
              print("")
              continue
          break
      instruction() 
      print("")

      print("  🤸🙌 A present vous avez acces au NIVEAU2 du jeu")
      print("")


      Bonjour()
      def Niveau2():
        OUI = 1
        NON = 2
        try:
          Decision2 = int(input("Souhaitez-vous commencer le NIVEAU2 du jeu🎮 ❓:\n🖋🖊🖍 "))
        except ValueError:
          print("⛔⛔😬😬 Choix invalide❗ Veillez entrer ”1” pour OUI et ”2” pour NON.")
          Niveau2()
        else:

          if Decision2 == OUI:
            print("\t🤸🙌 Bienvenue dans le NIVEAU2 du jeu.")
            print("")

            def voyelle():
              lettre = str(input("Entrez une voyelle:\n🖋🖊🖍 "))
              if lettre in "aeuioy":
                print("✔👍🤩 C'est une voyelle.")
              if lettre not in "aeuioy":
                print("😫😞❌ Ce n'est pas une voyelle.")
                print("👉 Veillez reesayer")
                print("")
                voyelle()
              print("")
            voyelle()

            #  Meme concepte que le precedent mais sans "not in"
            def consonne():
              lettre2 = str(input("Entrez un consonne:\n🖋🖊🖍 "))
              if lettre2 in "zrtpqsdfghjklmwxcvbn":
                print("✔👍🤩 C'est une consonne.")
              else:
                print("😫😞❌ Ce n'est pas une consonne.")
                print("👉 Veillez reesayer")
                print("")
                consonne()
            consonne()
            print("")
          

            print("  🤸🙌 A present vous avez acces au NIVEAU3 du jeu")
            print("")

            Bonjour()
            def Niveau3():
              OUI = 1
              NON = 2
              
              try:
                Decision3 = int(input("Souhaitez-vous commencer le NIVEAU3 du jeu ❓:\n🖋🖊🖍 "))
              except ValueError:
                print("⛔⛔😬😬 Choix invalide❗ Veillez entrer ”1” pour OUI et ”2” pour NON.")
                Niveau3()
              else:

                if Decision3 == OUI:
                  print("\t 🤸🙌 Bienvenue dans le NIVEAU3 du jeu.")
                  print("Bienvenue dans le mon jeu de Pierre Papier Ciseaux".center(40, '✨'))
                
                  import random

                  print("")
                  manches = int(input("Combien de manches voulez-vous jouer ❓\n🖋🖊🖍 "))
                  print("")

                  score_joueur = 0
                  score_ordi = 0

                  options = ["pierre", "papier", "ciseaux"]
                
                  while score_joueur < manches and score_ordi < manches:
                    choix_joueur = input("Que jouez-vous ❓ Tapez 'pierre', 'papier' ou 'ciseaux'\n🖋🖊🖍 ")

                    while choix_joueur not in options:
                      choix_joueur = input("Choix invalide❗ Choissisez pierre, papier ou ciseaux(sans les guillemets)\n🖋🖊🖍 ")
                      break

                    choix_ordi = random.choice(options)
                    print("L'ordinateur💻 choisi: ", choix_ordi)
                    print("")

                    if choix_joueur == choix_ordi:
                      print("Egalite😁😁. Rejouez")
                      print("")
                    elif choix_joueur == 'pierre' and choix_ordi == 'ciseaux' \
                    or choix_joueur == 'ciseaux' and choix_ordi == 'papier' \
                    or choix_joueur == 'ciseaux' and choix_ordi == 'papier':
                      print("😎👍🤩 Vous remportez la manche.", choix_joueur, "bat", choix_ordi)
                      score_joueur += 1
                      print("Votre score est: {}".format(score_joueur))
                      reste_joueur = manches - score_joueur
                      if reste_joueur == 1:
                        print("Il vous reste une manche a gagner.")
                        print("")
                      elif reste_joueur > 1:
                        print("Il vous reste {} manches a gagner.".format(reste_joueur))
                        print("")
                      else:
                        print("👏👏👏")
                    else:
                      print("L'ordinateur gagne la manche😎😎😎.", choix_ordi, "bat", choix_joueur)
                      score_ordi += 1
                      print("Le score de l'ordinateur est: {}".format(score_ordi))
                      reste_ordi = manches - score_ordi
                      if reste_ordi == 1:
                        print("Vous perdez si l'ordinateur gagne encore une manche.")
                        print("")
                      elif reste_ordi > 1:
                        print("Vous perdez si l'ordinateur gagne encore {} manches.".format(reste_ordi))
                        print("")
                      else:
                        print("😫😞 Desole") 
                        print("")

                  if score_joueur == manches:
                    print("😎👍🤩👏👏👏 Vous avez gagne la partie.")
                  else:
                    print("😎😎😎 C'est l'ordinateur gagne la partie.")
                  print("")

                  print("  🤸🙌 A present vous avez acces au NIVEAU4 du jeu")
                  print("")

                  Bonjour()
                  def Niveau4():
                    OUI = 1
                    NON = 2
                    
                    try:
                      Decision4 = int(input("Souhaitez-vous commencer le NIVEAU4 du jeu ❓:\n🖋🖊🖍 "))
                    except ValueError:
                      print("⛔⛔😬😬 Choix invalide❗ Veillez entrer ”1” pour OUI et ”2” pour NON.")
                      Niveau4()
                    else:

                      if Decision4 == OUI:
                        print("\t 🤸🙌 Bienvenue dans le NIVEAU4 du jeu.")
                        print("Bienvenue dans le mon jeu du Morpion".center(40, '✨'))
                        
                        plateau = ["  " for _ in range(9)]  # Creation d'un tableau de 9 caracteres espaces""

                        def affichePlateau(p, gagnant=None):
                          print(" " + p[0] + "|" + p[1] + " " + "|" + p[2] + " ")
                          print("---+---+---")
                          print(" " + p[3] + "|" + p[4] + " " + "|" + p[5] + " ")
                          print("---+---+---")
                          print(" " + p[6] + "|" + p[7] + " " + "|" + p[7] + " ")
                          if gagnant:
                            print("*Partie terminee: le joueur {0} a gagne.*".format(gagnant))
                          
                        def morpion():
                          joueur = "X"
                          tour = 0

                          while True:
                            affichePlateau(plateau)
                            print("> Tour du joueur " + joueur + " Entrez un nombre de 1 a 9.")

                            move = int(input()) - 1  # Notre tableau est de 0 a 8, don on retire 1.
                            
                            if plateau[move] == "  ":
                              plateau[move] = joueur 
                              tour += 1
                            else:
                              print("❗ Case deja occupee, choisissez-en une autre.")
                              continue  # On passe au prochain passage de boucle sans executer le code ci-dessous.
                            
                            if plateau[0] == plateau[1] == plateau[2] != "  " \
                            or plateau[3] == plateau[4] == plateau[5] != "  " \
                            or plateau[6] == plateau[7] == plateau[8] != "  " \
                            or plateau[0] == plateau[3] == plateau[6] != "  " \
                            or plateau[1] == plateau[4] == plateau[7] != "  " \
                            or plateau[2] == plateau[5] == plateau[8] != "  " \
                            or plateau[0] == plateau[4] == plateau[8] != "  " \
                            or plateau[2] == plateau[4] == plateau[6] != "  ":
                              affichePlateau(plateau, joueur)
                              break

                            if tour == 9:
                              print("Egalite")
                              break

                            joueur = "O" if joueur == "X" else "X"  # On change de joueur.
                        morpion()
                        """
                        if __name__ == "__jeu__":
                        morpion()
                        """                           
                      else:
                        print("A bientôt👋👋👋.")
                        print("")
                  Niveau4()
                else:
                  print("A bientôt👋👋👋.")
                  print("")
            Niveau3()
          else:
            print("A bientôt👋👋👋.")
            print("")
      Niveau2()
    else:
      print("A bientôt👋👋👋.")
      print("")
Niveau1()

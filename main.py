class CompteBancaire:
    def __init__(self, nom_utilisateur, mot_de_passe, solde_initial=0):
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.solde = solde_initial
        self.historique = []
    
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            transaction = f"Dépôt: +{montant}€"
            self.historique.append(transaction)
            print(f"Dépôt de {montant}€ effectué.")
        else:
            print("Le montant doit être positif.")
    
    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                transaction = f"Retrait: -{montant}€"
                self.historique.append(transaction)
                print(f"Retrait de {montant}€ effectué.")
            else:
                print("Solde insuffisant.")
        else:
            print("Le montant doit être positif.")
    
    def afficher_solde(self):
        print(f"Solde actuel: {self.solde}€")
    
    def afficher_historique(self):
        print("\nHistorique des transactions:")
        for transaction in self.historique:
            print(transaction)

class Banque:
    def __init__(self):
        self.comptes = {}
    
    def creer_compte(self, nom_utilisateur, mot_de_passe):
        if nom_utilisateur not in self.comptes:
            self.comptes[nom_utilisateur] = CompteBancaire(nom_utilisateur, mot_de_passe)
            print("Compte créé avec succès!")
        else:
            print("Ce nom d'utilisateur existe déjà.")
    
    def authentifier(self, nom_utilisateur, mot_de_passe):
        if nom_utilisateur in self.comptes and self.comptes[nom_utilisateur].mot_de_passe == mot_de_passe:
            return self.comptes[nom_utilisateur]
        return None
        
    def supprimer_compte(self, nom_utilisateur, mot_de_passe):
        if nom_utilisateur in self.comptes:
            if self.comptes[nom_utilisateur].mot_de_passe == mot_de_passe:
                del self.comptes[nom_utilisateur]
                print("Compte supprimé avec succès!")
                return True
        print("Échec de la suppression: identifiants incorrects")
        return False

def main():
    banque = Banque()
    print("Simulateur de système bancaire")
    
    while True:
        print("\nMenu Principal:")
        print("1. Créer un compte")
        print("2. Se connecter")
        print("3. Supprimer un compte")
        print("4. Quitter")
        
        choix = input("Votre choix (1-4): ")
    
        if choix == "1":
            nom = input("Nom d'utilisateur: ")
            mdp = input("Mot de passe: ")
            banque.creer_compte(nom, mdp)
        elif choix == "2":
            nom = input("Nom d'utilisateur: ")
            mdp = input("Mot de passe: ")
            compte = banque.authentifier(nom, mdp)
            if compte:
                print(f"\nBienvenue, {nom}!")
                while True:
                    print("\nOptions:")
                    print("1. Déposer de l'argent")
                    print("2. Retirer de l'argent")
                    print("3. Afficher le solde")
                    print("4. Afficher l'historique")
                    print("5. Déconnexion")
        
                    choix_compte = input("Votre choix (1-5): ")
                    
                    if choix_compte == "1":
                        try:
                            montant = float(input("Montant à déposer: "))
                            compte.deposer(montant)
                        except ValueError:
                            print("Veuillez entrer un nombre valide.")
                    elif choix_compte == "2":
                        try:
                            montant = float(input("Montant à retirer: "))
                            compte.retirer(montant)
                        except ValueError:
                            print("Veuillez entrer un nombre valide.")
                    elif choix_compte == "3":
                        compte.afficher_solde()
                    elif choix_compte == "4":
                        compte.afficher_historique()
                    elif choix_compte == "5":
                        print("Déconnexion réussie.")
                        break
                    else:
                        print("Choix invalide. Veuillez sélectionner une option entre 1 et 5.")
            else:
                print("Nom d'utilisateur ou mot de passe incorrect.")
        elif choix == "3":
            nom = input("Nom d'utilisateur: ")
            mdp = input("Mot de passe: ")
            banque.supprimer_compte(nom, mdp)
        elif choix == "4":
            print("Merci d'avoir utilisé notre simulateur bancaire.")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option entre 1 et 4.")

if __name__ == "__main__":
    main()

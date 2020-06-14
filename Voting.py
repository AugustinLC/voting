class Voting:

    def __init__(self, v, t, vpu):
        self.vote = v
        self.title = t
        self.vote_per_user = vpu

    def Vote(self):
        if self.title == 'user' and self.vote_per_user < 1:
            print("Votez 'oui' ou 'non'")
            self.vote = input()
            while self.vote_per_user < 1:
                if self.vote == 'oui' or self.vote == 'non':
                    print("Votre vote a bien été pris en compte")
                    self.vote_per_user = 1
                else:
                    print("Saisie incorrect veuillez réessayer en tapant 'oui' ou 'non'")
                    self.vote = input()
        else:
            print("Désolé vous n'êtes pas en mesure de voter")


users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10', 'user11', 'user12']
nb_vote_total = 0
nb_oui = 0
nb_non = 0

for i in users:
    if nb_vote_total >= 10:
        if nb_non > nb_oui:
            print('Le résultat du vote est non avec ', nb_non, ' voix.')
            break
        elif nb_oui > nb_non:
            print('Le résultat du vote est oui avec ', nb_oui, ' voix.')
            break
        else:
            print('Le résultat est égalité, il y a eu 5 votes oui et 5 votes non')
            break
    else:
        print(i)
        i = Voting('', 'user', 0)
        i.Vote()
        nb_vote_total += 1
        if i.vote == 'oui':
            nb_oui += 1
        else:
            nb_non += 1



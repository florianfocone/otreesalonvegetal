from otree.api import *

class Constants(BaseConstants): # des constantes https://otree.readthedocs.io/en/master/models.html#constants
    name_in_url = 'TestFF'
    players_per_group = 4 #participant par groupe
    num_rounds = 1 # ça peut se répéter
    endowment = cu(180) # un peu d'hectare'
    multiplier = 2 # un int


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):#group model pour quand les résultats impactent le groupe
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()



class Player(BasePlayer): #player model
# formfield https://otree.readthedocs.io/en/latest/forms.html
#ici que des statiques mais ça peut-être des dynamics : assign des réponses random, en fct des réponses d'avant, etc, affiche qqc si tu réponds à coté de la plaque, etc.
# possibilité de faire des optionnels (pas obligé de répondre

    contrib1=models.CurrencyField();
    contrib2=models.CurrencyField();
    contrib3=models.CurrencyField();
    contrib4=models.CurrencyField();

    choix_multiples_genre = models.StringField(
    choices=[['femme', 'Une femme'], ['homme', 'Un homme']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='femme'
    )

    choix_multiples_age = models.StringField(
    choices=[['1844', '18-44ans'], ['4554', '45-54ans'],['5464', '54-64ans'], ['65+', '65ans et +']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='1844'
    )


    choix_multiples_job = models.StringField(
    choices=[['dirigeant', 'Dirigeant'], ['salarié', 'Salarié'], ['autre', 'Autre']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='autre'
)

    choix_multiples_etude = models.StringField(
    choices=[['aucun', 'Aucun diplome'], ['bepc', 'Brevet des collèges ou BEPC'], ['cap-bep', 'CAP / BEP'], ['bac', 'Bac'], ['bac2', 'Bac +2'], ['bac3', 'Bac +3'], ['bac5', 'Bac +5'], ['bac8', 'Bac +8'], ['autre', 'Autre']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='autre'
)

    choix_multiples_typeentreprise = models.StringField(
    choices=[['privee', 'Entreprise privée'], ['assos', 'Association'], ['cooperative', 'Coopérative'], ['orga', 'Organisation professionnelle et technique'], ['autre', 'Autre']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='autre'
)

    choix_multiples_secteur = models.IntegerField(
    choices=[['1', 'Production'], ['2', 'Commercialisation'],['3', 'Paysage'], ['4', 'autres']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=1
    )


    choix_multiples_secteur1 = models.IntegerField(
    choices=[['1', 'Pépiniéristes'], ['2', 'Horticulteurs'], ['3', 'Fleurs coupées'], ['4', 'Producteurs mixtes'], ['5', 'Autres']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=5
    )

    choix_multiples_secteur2 = models.IntegerField(
    choices=[['1', 'Jardineries'], ['2', 'Libre-Service Agricole'], ['3', 'Fleuristes'], ['4', 'Grossistes'], ['5', 'Coopératives'], ['6', 'Autres']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=6
    )

    choix_multiples_secteur3 = models.IntegerField(
    choices=[['1', 'Entreprises du paysage'], ['2', 'Paysagistes concepteurs'], ['3', 'Autres']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=3
    )

    choix_multiples_secteur4 = models.StringField(
        label='''optionnel''',
        blank=True
    )

    freetext_optionnel_nom_entreprise = models.StringField(
    label='''optionnel''',
    blank=True
)

    choix_multiples_personne = models.StringField(
    choices=[['05', '0 à 5'], ['620', '6 à 20'], ['2150', '21 à 50'], ['51100', '51-100'], ['101+', '101 et plus']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='05'
)

#     choix_multiples_vente = models.StringField(
#     choices=[['producteurs', 'Producteurs'], ['grossistes', 'Grossistes'], ['fleuristes', 'Fleuristes'], ['jardineries', 'Jardineries'], ['surfaces', 'Grandes et moyennes surfaces'], ['entreprisepaysage', 'Entreprises de paysage'], ['collectivités', 'Collectivités'], ['libreservice', 'Libre-Service Agricole'], ['autre', 'Autre']],
#     label='Une seule réponse possible.',
#     widget=widgets.RadioSelect,
#     blank=False,
#     initial='autre'
# )
#
#     choix_multiples_achat = models.StringField(
#     choices=[['producteurs', 'Producteurs'], ['grossistes', 'Grossistes'], ['fleuristes', 'Fleuristes'], ['jardineries', 'Jardineries'], ['surfaces', 'Grandes et moyennes surfaces'], ['entreprisepaysage', 'Entreprises de paysage'], ['collectivités', 'Collectivités'], ['libreservice', 'Libre-Service Agricole'], ['autre', 'Autre']],
#     label='Une seule réponse possible.',
#     widget=widgets.RadioSelect,
#     blank=False,
#     initial='autre'
# )

    # choix multiples ventes
    ProducteursV = models.BooleanField(blank=True, initial=False)
    GrossistesV = models.BooleanField(blank=True, initial=False)
    FleuristesV = models.BooleanField(blank=True, initial=False)
    JardineriesV = models.BooleanField(blank=True, initial=False)
    GrandesetmoyennessurfacesV = models.BooleanField(blank=True, initial=False)
    EntreprisesdepaysageV= models.BooleanField(blank=True, initial=False)
    CollectivitésV = models.BooleanField(blank=True, initial=False)
    LibreServiceAgricoleV = models.BooleanField(blank=True, initial=False)
    AutreV = models.BooleanField(blank=True, initial=False)


    # choix multiples Achats
    ProducteursA = models.BooleanField(blank=True, initial=False)
    GrossistesA = models.BooleanField(blank=True, initial=False)
    FleuristesA = models.BooleanField(blank=True, initial=False)
    JardineriesA = models.BooleanField(blank=True, initial=False)
    GrandesetmoyennessurfacesA = models.BooleanField(blank=True, initial=False)
    EntreprisesdepaysageA = models.BooleanField(blank=True, initial=False)
    CollectivitésA = models.BooleanField(blank=True, initial=False)
    LibreServiceAgricoleA  = models.BooleanField(blank=True, initial=False)
    AutreA = models.BooleanField(blank=True, initial=False)

    choix_vf_enquete_ligne = models.StringField(
    choices=[['oui', 'Oui'], ['non', 'Non']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial='oui'
)

    #p14 attente
    choix_multiples_confiance_fournisseur = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    choix_multiples_confiance_client = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    #p16
    choix_multiples_confiance_concurrent = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    sat_inrae = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_astredhor = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_bhr = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_inrae = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_chambre = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    chambre_agriculture = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'], ['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_fnphp = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_vegepolys = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_valhor = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )

    sat_plantecite = models.IntegerField(
    choices=[['991', 'Je ne connais pas'], ['992', 'je n ai pas de relation'],['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=991
    )


   # choix multiples possibles
    ASTREDHOR = models.BooleanField(blank=True, initial=False)
    BHR = models.BooleanField(blank=True, initial=False)
    Chambre = models.BooleanField(blank=True, initial=False)
    FNPHP = models.BooleanField(blank=True, initial=False)
    INRAE = models.BooleanField(blank=True, initial=False)
    PlanteCite = models.BooleanField(blank=True, initial=False)
    Valhor = models.BooleanField(blank=True, initial=False)
    VEGEPOLYS = models.BooleanField(blank=True, initial=False)
    Autre = models.BooleanField(blank=True, initial=False)

    #p26
    freetext_commentaire_orga = models.StringField(
    label='''optionnel''',
    blank=True
)


    innovation = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    reprise = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    logistique = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    cooperative = models.IntegerField(
    choices=[['0', '0'], ['1', '1'],['2', '2'], ['3', '3'], ['4', '4'],['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'], ['10', '10']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=0
    )

    choix_pot_commun = models.IntegerField(
    choices=[['0', '0'], ['15', '15'], ['30', '30']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=None
    )

    potcommun = models.IntegerField(
    choices=[['0', '0€ (0€ - 0€ - 0€)'], ['15', '15€ (15€ - 0€ - 0€)'],['30', '30€ (15€ - 15€ - 0€ ou 30€ - 0€ -0€)'],['45', '45€ (15€ - 15€ - 15€ ou 30€ - 15€ - 0€)'],['60', '60€ (30€ - 15€ - 15€ ou 30€ - 30€ - 0€)'], ['75', '75€ (30€ - 30€ - 15€)'],['90', '90€ (30€ - 30€ - 30€)']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
    initial=None
    )

    freetext_commentaire_fin = models.StringField(
    label='''optionnel''',
    blank=True
)

    freetext_mail = models.StringField(
    label='''optionnel''',
    blank=True
)


# FUNCTIONS

def set_payoffs(group):
    players = group.get_players()
    contributions = [p.choix_pot_commun for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * Constants.multiplier / Constants.players_per_group
    for player in players:
        player.payoff = group.individual_share + 30 - player.choix_pot_commun
        player.contrib1 = players[0].choix_pot_commun
        player.contrib2= players[1].choix_pot_commun
        player.contrib3 = players[2].choix_pot_commun
        player.contrib4 = players[3].choix_pot_commun





# PAGES
class p1(Page):
    form_model = 'player'

class p2(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_genre']

class p3(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_age']

class p4(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_job']

class p5(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_etude']

class p6(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_typeentreprise']

class p7avant(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_secteur']

class p7(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_secteur1','choix_multiples_secteur2','choix_multiples_secteur3','choix_multiples_secteur4']

class p8(Page):
    form_model = 'player'
    form_fields = ['freetext_optionnel_nom_entreprise']

class p9(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_personne']

class p10(Page):
    form_model = 'player'
    form_fields = ['ProducteursV' ,'GrossistesV','FleuristesV','JardineriesV','GrandesetmoyennessurfacesV','EntreprisesdepaysageV','CollectivitésV','LibreServiceAgricoleV','AutreV']

class p11(Page):
    form_model = 'player'
    form_fields = ['ProducteursA', 'GrossistesA', 'FleuristesA', 'JardineriesA', 'GrandesetmoyennessurfacesA',
                   'EntreprisesdepaysageA', 'CollectivitésA', 'LibreServiceAgricoleA', 'AutreA']


class p13(Page):
    form_model = 'player'
    form_fields = ['choix_vf_enquete_ligne']

class p14(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_confiance_fournisseur']

class p15(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_confiance_client']

class p16(Page):
    form_model = 'player'
    form_fields = ['choix_multiples_confiance_concurrent']

class p17(Page):
    form_model = 'player'
    form_fields = ['sat_inrae']

class p18(Page):
    form_model = 'player'
    form_fields = ['sat_astredhor']

class p19(Page):
    form_model = 'player'
    form_fields = ['sat_bhr']

class p20(Page):
    form_model = 'player'
    form_fields = ['sat_chambre']

class p21(Page):
    form_model = 'player'
    form_fields = ['sat_fnphp']

class p22(Page):
    form_model = 'player'
    form_fields = ['sat_vegepolys']

class p23(Page):
    form_model = 'player'
    form_fields = ['sat_valhor']

class p24(Page):
    form_model = 'player'
    form_fields = ['sat_plantecite']

class p25(Page):
    form_model = 'player'
    form_fields = ['ASTREDHOR' ,'BHR','Chambre','FNPHP','INRAE','PlanteCite','Valhor','VEGEPOLYS','Autre']

class p26(Page):
    form_model = 'player'
    form_fields = ['freetext_commentaire_orga']

class p27(Page):
    form_model = 'player'
    form_fields = ['innovation']

class p28(Page):
    form_model = 'player'
    form_fields = ['reprise']

class p29(Page):
    form_model = 'player'
    form_fields = ['logistique']

class p30(Page):
    form_model = 'player'
    form_fields = ['cooperative']

class p31strategie(Page):
    form_model = 'player'
    form_fields = ['choix_pot_commun']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs  # condition pour lancer la fonction set_payoffs et passer à la page suivante
    body_text = "Attente des réponses des autres participants avant de continuer."

class waitPage(WaitPage):
    body_text = "Attente des réponses des autres participants avant de continuer."

class p32(Page):
    form_model = 'player'
    form_fields = ['potcommun']

class PageResults(Page):
    form_model = 'player'
    form_fields = ['freetext_commentaire_fin','freetext_mail']

class Pagefin(Page):
    form_model = 'player'



class attente(Page):
    form_model = 'player'

#page_sequence = [p31strategie,ResultsWaitPage,p32,PageResults,Pagefin]
page_sequence = [p1,p2,p3,p4,p5,p6,p7avant,p7,p8,p9,p10,p11,p13,waitPage,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,waitPage,p31strategie,ResultsWaitPage,p32,PageResults,Pagefin]

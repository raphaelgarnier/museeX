## Déclaration des personnages
define préjoueur = Character("...")
define inconnu = Character("?", who_color="454545")
define c = Character("Le conservateur du musée", image="conservateur")
define cquizz = Character("Le conservateur du musée ?", image="conservateurquizz")
define ch = Character("Le chêne")
define no = Character("Le noble")
define ou1 = Character("Un ouvrier")
define ou2 = Character("Un autre ouvrier")
define ou3 = Character("Encore un autre ouvrier")

## Déclaration des scènes supplémentaires
screen selever:
    imagemap:
        ground "fond-debut.jpg"
        hover "fond-debut-hover.jpg"

        hotspot (500,270,750,400) clicked Jump("starttrue")

screen preAbbaye:
    imagemap:
        ground "intro-abbaye.jpg"
        hover "intro-abbaye-hover.jpg"

        hotspot (230,160,850,370) clicked Jump("inAbbaye")

screen preDejeuner:
    imagemap:
        ground "intro-versailles.jpg"
        hover "intro-versailles-hover.jpg"

        hotspot (230,160,850,370) clicked Jump("inDejeuner")

screen preLunch:
    imagemap:
        ground "intro-lunch.jpg"
        hover "intro-lunch-hover.jpg"

        hotspot (230,160,850,370) clicked Jump("inLunch")

screen etapes:
    add "notes"
    textbutton "Fermer" action Jump("suite"):
        xalign 0.17
        yalign 0.75

screen troisTableaux:
    add "recap-trois-tableaux":
        xalign 0.55
        yalign 0.55
    textbutton "Je suis prêt" action Jump("suite2"):
        xalign 0.52
        yalign 0.75



## Lancer le jeu
label start:
    $renpy.sound.play("cloches.mp3", loop=True)
    call screen selever with Fade(3.0, 0.0, 0.5, color="#fff")

## Scene 1, chambre (début)
label starttrue:
    stop sound fadeout 3.0
    scene blanc
    play music "Dreamcatcher.mp3"
    scene bg-chambre2
    with Fade(3.0, 0.0, 0.5, color="#fff")
    
    préjoueur "Enfin !"
    préjoueur "C'est le grand jour."
    préjoueur "Je suis finalement prêt."
    préjoueur "C'est mon premier jour de travail, il faut que je sois au top !"
    préjoueur "Direction le Musée X ! Il ne faut pas que j'arrive en retard."
    préjoueur "On m'y attend !"

## Scene 2, extérieur musée X
    scene bg-museeext

    préjoueur "Je crois bien que c'est ici..."
    préjoueur "J’ai vraiment hâte de commencer mon premier jour dans ce magnifique musée."
    préjoueur "Hm."
    préjoueur "Je pense qu’il préférable de rentrer."
    préjoueur "Je trouverai bien quelqu’un pour m’aider."
    préjoueur "{i}(Allez respire un bon coup et c'est parti.)"

## Scene 3, intérieur musée X
    scene musee-interieur
    stop music
    $renpy.sound.play("foule.mp3", loop=True)

    préjoueur "Woah, quel lieu immense ! Et quelle affluence !"
    préjoueur "Des milliers d’œuvres sont conservées ici." 
    préjoueur "Quelle chance de pouvoir les côtoyer tous les jours."

    stop sound fadeout 1.0

    inconnu "Ha-ha-ha !"
    préjoueur "Hm ?!"
    inconnu "Bienvenue au Musée X !"
    préjoueur "Oh ! Vous m'avez fait peur."

    play music "Moose.mp3"

    c "Je suis le conservateur du musée, ha-ha-ha !"
    préjoueur "Oh ! Enchanté."
    c "Tu es la nouvelle personne qui vient travailler ici, n'est-ce pas ?"
    préjoueur "C'est ça."
    c "Rappelle-moi juste ton prénom, j’ai une mémoire de poisson rouge ha-ha-ha !"

    $ nomJoueur = renpy.input("{b}Entrez votre prénom :")
    
    play sound "click.mp3"
    nomJoueur "Je m'appelle [nomJoueur]."
    c "Enchanté [nomJoueur] !"
    nomJoueur "J'ai vraiment hâte de commencer à travailler ici."
    nomJoueur "Ce musée est gigantesque et les œuvres qu'il renferme sont toutes plus prestigieuses les unes que les autres !"
    nomJoueur "Quel bonheur !"
    c "Ha-ha-ha !"
    c "Quel enthousiasme, [nomJoueur] !"
    c "Je suis ravi que tu fasses partie de l'équipe."
    c "Enfin... pas tout à fait encore."
    nomJoueur "Hm ?"
    c "Tu es ici pour ta première journée de test."
    nomJoueur "Effectivement, je suis prêt à tout pour décrocher ce poste !"
    c "Parfait, ha-ha-ha !"
    c "J'ai justement quelques détails à te faire part avant que tu ne puisses débuter ton aventure ici."
    c "Rendons-nous dans mon bureau, veux-tu ?"
    nomJoueur "Avec plaisir !"

## Scene 4, dans bureau conservateur
    play music "Ambiance.mp3"
    scene bureau-conservateur

    c "Et voilà !"
    c "J'espère que tout est clair à présent."
    nomJoueur "Tout à fait."
    c "As-tu d'autres questions avant de commencer ?"

    menu:
        "Demander un récapitulatif.":
            jump taches1
        "Dire que vous êtes prêt.":
            jump taches2

label taches1:
    play sound "click.mp3"
    c "Eh bien ! Je vois que ta mémoire est pire que la mienne, ha-ha-ha !"
    c "Heureusement, j'ai tout prévu !"
    c "Voici une petite note sur laquelle tu trouveras toutes les informations nécessaires à la bonne réussite de cette journée."
    call screen etapes

label taches2:
    play sound "click.mp3"
    nomJoueur "Je suis prêt !"
    c "Eh bien... Tu sembles bien trop sûr de toi."
    c "Je vais quand même te montrer cette petite note importante."
    call screen etapes

label suite:
    play sound "click.mp3"
    nomJoueur "Parfait. Merci beaucoup !"
    nomJoueur "Je me lance immédiatement."
    c "Bonne chance [nomJoueur]."
    c "J'attendrai sagement ton retour !"
    c "Et n'oublie pas : amuse-toi mais retiens bien tout ce que tu vas voir, ha-ha-ha !"

## Scene 5
    scene musee-interieur
    stop music
    $renpy.sound.play("foule.mp3", loop=True)

    nomJoueur "Bon, maintenant que j'ai eu accès à ce petit récapitulatif je devrai m'en sortir."
    nomJoueur "Je pense que le conservateur me réserve quelque chose..."
    nomJoueur "Enfin bon, je verrai ça plus tard."
    nomJoueur "Pour le moment, direction la première salle !"

## Scene 6, dans la salle de l'art allemand du XIXe
    scene salle-allemand
    with blinds
    stop sound

    nomJoueur "J'y suis."
    nomJoueur "Quelle grande salle !"
    nomJoueur "C'est donc l'espace consacré aux peintures allemandes du XIXe (19) siècle."
    nomJoueur "Je viens donc de réaliser la première étape."
    nomJoueur "Mais quelle était la deuxième étape déjà ?"
    
    menu :
            "Mémoriser":
                jump notesFausses
            "Collecter":
                jump notesFausses
            "Dessiner":
                jump notesFausses
            "Pénétrer":
                jump notesCorrectes

label notesFausses:
    play sound "click.mp3"
    nomJoueur "Je ne crois pas que c'était ça..."

    menu :
        "Mémoriser":
            jump notesFausses
        "Collecter":
            jump notesFausses
        "Dessiner":
            jump notesFausses
        "Pénétrer":
            jump notesCorrectes

label notesCorrectes:
    play sound "click.mp3"
    nomJoueur "C'est ça !"
    nomJoueur "Je dois pénétrer dans les tableaux !"
    nomJoueur "Mais dans lequel ?"
    nomJoueur "Hm..."
    nomJoueur "Celui-ci a l'air intéressant."
    nomJoueur "Voyons voir ce que le petit cartel indique."
    nomJoueur "{b}Caspar David Friedrich, Abtei im Eichwald, 1809-1810..."
    nomJoueur "Oh mais je reconnais cette toile !"
    nomJoueur "C'est une oeuvre incroyable !"
    nomJoueur "Je meurs d'envie de voir à quoi ça ressemble à l'intérieur."
    nomJoueur "C'est parti !"
    
    play sound "pianoloop.mp3"
    scene jaune
    with Fade(3.0, 0.0, 0.5, color="#d1ca73")

    call screen preAbbaye

##Scene 7, dans le tableau "Abbaye"
label inAbbaye:
    play sound "click2.mp3"
    play music "Corbeaux-crop.mp3"
    scene bg-abbaye1
    with Dissolve(8.0)
    $ renpy.pause()

    nomJoueur "Quel endroit lugubre..."
    nomJoueur "Je n'imaginais pas ce lieu comme ça avant de devoir littéralement plonger à l'intérieur."
    nomJoueur "Bon... Commençons par approcher cette ruine."
    nomJoueur "Je dois en savoir plus."
    nomJoueur "De toute façon je ne peux pas rentrer auprès du conservateur sans avoir fouillé toute cette peinture."
    inconnu "Halte-là !"
    nomJoueur "Hm ?!"
    nomJoueur "Qui est là ?!"
    inconnu "Par ici ! Lève les yeux."
    nomJoueur "Bon sang !"
    nomJoueur "Un arbre qui parle !!!"
    inconnu "Je suis un chêne."
    nomJoueur "Vous paraissez si vieux et... dégarni."

    menu :
        "Que vous est-il arrivé ?":
            jump abbaye1
        "Quel est ce lieu étrange ?":
            jump abbaye2

label abbaye1:
    play sound "click.mp3"
    ch "Celui qui a représenté cette scène, et donc qui m'a peint, était sans doute triste et mélancolique."
    ch "Cela se ressent indéniablement sur mon apparence."
    jump abbayeSuite1

label abbaye2:
    play sound "click.mp3"
    ch "Cet endroit est une sorte de chemin vers l'autre monde."
    ch "Celui qui peint cette désolation était très mélancolique et empreint de tristesse."
    jump abbayeSuite1

label abbayeSuite1:
    nomJoueur "Je comprends mieux cette ambiance..."
    nomJoueur "Le peintre était donc quelqu'un de très attaché au rendu de ses sentiments, n'est-ce pas ?"
    ch "Tout à fait."
    ch "On le rattache au romantisme allemand qui prône un retour à la nostalgie, tout en s'opposant à la raison pure."
    ch "Tu peux voir que cette idée de la nature se traduit ici par un paysage désolé, presque horrifique..."
    ch "Mais le tout est baigné dans une lumière plutôt rassurante."
    ch "Étrange, n'est-ce pas ?"
    nomJoueur "Oui. Il y'a quelque chose d'intemporel dans ce paysage."
    nomJoueur "Comme si l'image était fixée ainsi à tout jamais."
    ch "C'est cela."
    nomJoueur "Mais une question me taraude l'esprit."
    ch "Oui ?"

    menu :
        "Pourquoi une abbaye en ruines ?":
            jump abbaye3
        "Pourquoi des chênes ?":
            jump abbaye4

label abbaye3:
    play sound "click.mp3"
    ch "L'abbaye en ruines est un motif cher à Friedrich."
    ch "Elle participe à créer une ambiance « gothique » très importante pour le Romantisme qui cherche à retrouver les traces du Moyen-Âge."
    jump abbayeSuite2
label abbaye4:
    play sound "click.mp3"
    ch "Nous, les chênes, sommes des liens entre la terre sombre et le ciel clair."
    ch "Nous représentons métaphoriquement la mort environnante qui est un motif important du Romantisme."
    jump abbayeSuite2

label abbayeSuite2:
    nomJoueur "C'est une véritable représentation mystique du paysage et de ses éléments."
    ch "Oui, c'est exactement ce à quoi tu as affaire ici."
    nomJoueur "Mais dites-moi."
    nomJoueur "J'aperçois également de petits personnages au pied de l'abbaye."
    scene abbaye-personnages

    menu :
        "Se dirigent-ils dans les ruines ?":
            jump abbaye5
        "Que font-ils ici ?":
            jump abbaye6

label abbaye5:
    play sound "click.mp3"
    ch "Oui, tout à fait. Ils sont en pleine cérémonie d’inhumation."
    ch "Enterrer quelqu’un de mort dans un lieu aussi désolé peut paraitre un peu étonnant, n’est-ce pas ?"
    nomJoueur "En effet..."
    jump abbayeSuite3
label abbaye6:
    play sound "click.mp3"
    ch "Ils sont apparemment en train d’emmener une personne pour son inhumation."
    ch "Quelle étrange cérémonie, n’est-ce pas ?"
    nomJoueur "Effectivement..."
    jump abbayeSuite3

label abbayeSuite3:
    scene bg-abbaye1
    ch "Mais dis-moi..."
    ch "Que viens-tu donc faire ici ?"
    nomJoueur "Eh bien je dois absolument en savoir plus sur certaines œuvres."
    nomJoueur "Et quoi de mieux que d’y plonger littéralement pour en déceler tous les secrets."
    ch "Hm."
    ch "Effectivement, c'est une démarche très avisée."
    ch "Même si ce n’est pas l’endroit le plus accueillant du monde de l’art."
    nomJoueur "En effet..."
    ch "Tu sais, il existe tout un pan de l'histoire de l'art qui traite de ce genre de paysage."
    nomJoueur "Ah bon ?"
    nomJoueur "Hm..."
    nomJoueur "Il me semble que j'en ai déjà entendu parler."
    nomJoueur "Est-ce que ça ne serait pas..."

    menu :
        "...le kitsch ?":
            jump abbayeKitsch
        "...le sublime ?":
            jump abbayeSublime

label abbayeKitsch:
    play sound "click.mp3"
    ch "Non ce n'est pas ça."
    ch "Le kitsch peut être vu comme une catégorie esthétique qui se base sur l'exagération et l'accumulation d'éléments."
    ch "Une oeuvre kitsch c'est par exemple..."
    ch "Hm..."
    ch "Une oeuvre pleine de couleurs vives et d'objets qui n'ont rien à voir les uns avec les autres."
    nomJoueur "J'ai compris."
    nomJoueur "Mais alors dites-moi ce qu'est le sublime."
    jump abbayeSuite4

label abbayeSublime:
    play sound "click.mp3"
    ch "Oui c'est bien cela."
    ch "Je vais t'expliquer en quoi consiste le sublime."
    jump abbayeSuite4

label abbayeSuite4:
    ch "Le sublime met en scène le plaisir et la terreur."
    ch "On y retrouve les ténèbres, l'obscurité et parfois la douleur..."
    ch "...mêlés à la grandeur, l'immensité et l'infini."
    ch "Ici tu peux voir que ce paysage semble infini et figé dans le temps."
    ch "Il y'a une ambiance presque terrifique mais rassurante en même temps."
    ch "Le peintre s'attache ici à lier la nature et les sentiments religieux..."
    nomJoueur "C'est vraiment intéressant."
    nomJoueur "Je ne connaissais pas cette approche de la peinture."
    nomJoueur "Que me conseillez-vous donc de retenir à propos de ce sublime endroit, bien que très lugubre ?"
    ch "Hm."
    scene abbaye-clairobscur
    ch "Souviens-toi de cette très grande maîtrise du clair-obscur..."
    scene abbaye-mort
    ch "...de l’omniprésence symbolique de la mort..."
    scene bg-abbaye1
    ch "...et de cette composition jouant avec les passions et les sentiments nostalgiques et tragiques de Friedrich."
    ch "Toute cette œuvre recèle quelque chose de sublime, comme tu viens de le dire à l’instant."
    ch "Mais n’oublie pas."
    ch "Elle est sublime dans la seule mesure où elle recèle quelque chose de terrifique."
    nomJoueur "Je vois..."
    ch "Mais tout cela ne concerne que cette œuvre évidemment."
    nomJoueur "Très bien !"
    nomJoueur "Je vous remercie infiniment pour ces précieuses informations, le conservateur du musée sera ravi !"
    ch "Le conservateur ?"
    nomJoueur "Euh, non rien !"
    nomJoueur "Hm. Dites-moi."
    nomJoueur "J'ai encore une question."
    ch "Hm ?"
    nomJoueur "J'entends des corbeaux depuis mon arrivée. Pourtant je n'en ai pas vu..."
    ch "Bien vu !"
    ch "Il n’y en a effectivement aucun ici."
    ch "Mais sans leur croassement, l’ambiance ne serait pas du tout la même, tu ne trouves pas ?"
    $renpy.sound.play("cloches.mp3", loop=True)
    nomJoueur "C'est vrai. Vous avez raison..."
    nomJoueur "Oh !"
    nomJoueur "Je dois y aller !"
    nomJoueur "Merci encore pour tout."
    ch "Adieu..."

    stop sound fadeout (3.0)
    stop music fadeout (3.0)
    scene jaune
    with Fade(3.0, 0.0, 0.5, color="#d1ca73")

## Scene 8, retour dans la salle allemande
    scene salle-allemand
    with Fade(1.0, 0.0, 0.5, color="#d1ca73")
    play music "Ambiance.mp3"
    
    nomJoueur "Et de un !"
    nomJoueur "Quelle ambiance surprenante..."
    nomJoueur "J’espère avoir retenu l’essentiel concernant cette œuvre."
    nomJoueur "Il ne faut pas que j’oublie de mémoriser l'essentiel !"
    nomJoueur "Il en va de ma future carrière ici."
    nomJoueur "Le conservateur voudra sûrement me tester."
    nomJoueur "Ah ! La prochaine salle s'est ouverte..."

## Scene 9, dans la salle des tableaux royaux
    scene salle-royale
    with blinds
    stop music

    nomJoueur "Oh !"
    nomJoueur "Voici la salle des tableaux royaux."
    nomJoueur "C'est une salle incroyable et pleine de chefs-d'œuvre."
    nomJoueur "J'ai compris le fonctionnement de {b}Abtei im Eichwald."
    nomJoueur "Celui-ci ne devrait pas poser de problème."
    nomJoueur "Par contre je ne vois aucun cartel décrivant les tableaux."
    nomJoueur "Bon ce n'est pas grave."
    nomJoueur "Je vais choisir un tableau au hasard et voir où il me mène !"
    
    stop music
    play sound "pianoloop.mp3"
    scene jaune
    with Fade(3.0, 0.0, 0.5, color="#d1ca73")

## Scene 10 dans Déjeuner
    call screen preDejeuner
    
label inDejeuner:
    play sound "click2.mp3"
    play music "Baroque.mp3"
    scene dejeuner-huitres
    with Dissolve(8.0)
    $ renpy.pause()

    inconnu "Et que ce moment délicieux dure longtemps !"
    inconnu "Ha-ha-ha !"
    inconnu "Amenez les plateaux d'huîtres ! Que tout le monde se régale !"
    nomJoueur "Mais où suis-je encore tombé ?"
    nomJoueur "C’est une ambiance complètement différente cette fois-ci."
    inconnu "Hé vous ! Que diable faites-vous debout ?"
    nomJoueur "Euh... moi ?"
    inconnu "Oui, c’est à vous que je parle."
    inconnu "Hâtez-vous à table je vous prie. Le festin est sur le point de commencer."
    inconnu "Vous ne voulez certainement pas en manquer une seule miette, n’est-ce pas ?"
    nomJoueur "Oh... euh... Bien sûr que non !"
    inconnu "Parfait !"
    inconnu "Mais qui êtes-vous ?"
    inconnu "Je n’ai pas souvenir de vous avoir rencontré auparavant, me tromperai-je ?"
    nomJoueur "{i}(Que lui répondre ?)"
    nomJoueur "{i}(Il semble être quelqu’un d’important au vu de la manière dont il parle et les vêtement qu’il porte.)"
    nomJoueur "{i}(Je devrai peut-être lui demander qui il est avant tout.)"

    menu:
        "Qui êtes-vous ?":
            jump dejeunerSuite1
        "Comment vous appelez-vous ?":
            jump dejeunerSuite2

label dejeunerSuite1:
    play sound "click.mp3"
    inconnu "Je suis un noble, pardi !"
    no "Je fais partie de la cour et suis un proche de notre cher roi, le grand Louis XV !"
    jump dejeunerSuite3

label dejeunerSuite2:
    play sound "click.mp3"
    inconnu "Qu'importe comment je me prénomme, je suis un noble !"
    no "J'appartiens à la noblesse et donc à la cour qui entoure Louis XV, notre cher roi !"
    jump dejeunerSuite3

label dejeunerSuite3:
    nomJoueur "{i}(Hm... Je comprends mieux cette ambiance royale.)"
    nomJoueur "Oh je vois !"
    no "Vous n'avez cependant pas répondu à ma question, aimable personnage."
    no "Qui êtes-vous donc ?"

    menu:
        "Lui dire la vérité.":
            jump dejeunerSuite4
        "Lui mentir.":
            jump dejeunerSuite5

label dejeunerSuite4:
    play sound "click.mp3"
    nomJoueur "Je suis en vadrouille parmi les endroits les plus reconnus de ce monde."
    nomJoueur "Je cherche à comprendre comment chaque lieu fonctionne et ce qui contribue à le rendre unique."
    jump dejeunerSuite6

label dejeunerSuite5:
    play sound "click.mp3"
    nomJoueur "Je suis un noble tout comme vous, voyons !"
    nomJoueur "J'arrive tout juste d'une contrée lointaine et souhaitais prendre part à ce magnifique festin !"
    jump dejeunerSuite6

label dejeunerSuite6:
    no "Parfait, alors tout va pour le mieux, ha-ha !"
    no "Servez-vous donc d'huîtres. Elles sont particulièrement exquises cette année !"
    nomJoueur "Je vous remercie."
    scene dejeuner-zoomtable
    "{b}Quelques minutes plus tard..."
    nomJoueur "Dites-moi. Puis-je vous poser quelques questions à propos de ce lieu si particulier ?"
    no "Particulier ? C'est un endroit magnifique au contraire !"
    scene dejeuner-plafond
    no "Admirez ces dorures, ces sculptures murales et ce décor grandiose !"
    no "Tout ici est somptueux."
    nomJoueur "En effet..."
    no "Pour répondre à votre questionnement, nous nous trouvons dans la salle à manger dite « de retour de chasse »."
    nomJoueur "Intéressant."
    nomJoueur "J’en déduis qu’il existe plusieurs salles de ce type dans ce château."

    menu:
        "Lui demander des précisions sur cette salle":
            jump dejeunerSuite7
        "Lui demander plus d'informations sur le château":
            jump dejeunerSuite8

label dejeunerSuite7:
    play sound "click.mp3"
    scene dejeuner-zoomtable
    no "Après chaque session de chasse avec le Roi, nous nous retrouvons ici pour déguster quelques mets raffinés."
    no "Se retrouver ici est une tradition instaurée par notre cher Roi."
    no "Il aime se retrouver entouré de ses plus proches amis et collègues de chasse pour partager un moment de délice."
    jump dejeunerSuiteA

label dejeunerSuite8:
    play sound "click.mp3"
    scene dejeuner-zoomtable
    no "Nous nous trouvons actuellement à Versailles, pardi !"
    no "Notre cher roi Louis XV a établi ses appartements privés ici-même, tout en réunissant la cour et le gouvernement."
    no "Cela dure comme cela depuis 13 années, ce n’est que du bonheur, ha-ha !"
    jump dejeunerSuiteA

label dejeunerSuiteA:
    nomJoueur "Quel privilège de se trouver ici." 
    no "N’est-ce pas, aimable personnage ?"
    no "Joie de vivre et insouciance rythment ce moment."
    no "Nos mets sont fins et raffinés et invitent au plaisir !"
    nomJoueur "Celui qui a peint cette scène était certainement une personne qui aimait les plaisirs et les délices de la vie."
    nomJoueur "Mais dites m'en plus sur ces mets."

    menu:
        "Des huîtres et pas de gibier ? Étrange pour une rentrée de chasse...":
            jump dejeunerSuite9
        "Que buvez-vous pour accompagner ces huîtres ?":
            jump dejeunerSuite10

label dejeunerSuite9:
    play sound "click.mp3"
    scene dejeuner-dressage
    no "Effectivement, aimable personnage."
    no "Les huîtres sont pour nous un met des plus raffinés et nous aimons en consommer après nos escapades champêtres."
    no "Qui plus est, nous sommes à une période de l’année où les plus fraîches débarques tout droit de nos côtes françaises !"
    no "­Voyez donc, nous les mangeons pures ! Juste accompagnées de sel, d’ail ou de beurre."
    jump dejeunerSuite11

label dejeunerSuite10:
    play sound "click.mp3"
    scene dejeuner-dressage
    no "Du champagne, pardi !"
    no "Savez-vous que vous avez affaire avec la première figuration du champagne dans l’iconographie du XVIIIe (18) siècle ?"
    no "C’est tout bonnement incroyable, ha-ha !"
    no "Ce magnifique breuvage pétillant a été inventé par le moine Dom Pérignon, il y a une cinquantaine d’années."
    jump dejeunerSuite11

label dejeunerSuite11:
    nomJoueur "C’est très intéressant."
    nomJoueur "Je vous remercie pour toutes ces informations."
    nomJoueur "Que me conseillez-vous de retenir à propos de ce lieu ?"
    no "Eh bien, aimable personnage, nous nous trouvons dans un moment de l’histoire qui est essentiel."
    no "Essentiel pour comprendre les manières de table du début du XVIIIe (18) siècle en France."
    no "Comme vous le voyez, les couverts sont en argent et la vaisselle en porcelaine."
    no "Cela montre bien que Versailles met tout en œuvre pour régaler ses hôtes."
    nomJoueur "Je comprends. Mais dites m'en plus."
    no "Regardez donc attentivement les verres et les bouteilles."
    no "Quelque chose ne vous étonne-t-il pas ?"
    nomJoueur "Hm. Je vois qu’ils ne sont pas posés à même la table."
    no "Effectivement !"
    no "Ici et maintenant, nous ne posons jamais ces éléments sur la table. Seuls les aliments et les assiettes peuvent y être déposés."
    no "C’est une règle essentielle des arts de la table, à l’heure où nous parlons."
    nomJoueur "Et que dire du peintre ?"
    no "Ce cher Jean-François de Troy ?"
    no "Eh bien, c’est quelqu’un d’extrêmement sensible aux raffineries et délices de notre temps."
    no "Sa touche, très élégante et raffinée, sublime les moments pareils à celui que nous vivons actuellement." 
    no "Une grande légèreté s’en dégage."
    nomJoueur "Que dire alors de la composition qui ici semble très..."

    menu:
        "...chargée.":
            jump dejeunerSuite12
        "...vivante.":
            jump dejeunerSuite13

label dejeunerSuite12:
    play sound "click.mp3"
    no "Chargée ? Voyons, aimable personnage, elle est tout sauf chargée."
    no "L’accent est mis sur le regard des nombreux personnages qui animent ainsi la scène."
    scene dejeuner-bouchon
    no "Un bouchon de champagne gicle en l’air par ci..."
    scene dejeuner-sol
    no "...une huître tombe au sol par là..."
    no "Tout est rythmé ici !"
    jump dejeunerSuite14

label dejeunerSuite13:
    play sound "click.mp3"
    no "En effet, aimable personnage !"
    no "Les nobles se regardent, jouent avec l’espace par le biais de leur regard."
    scene dejeuner-bouchon
    no "Un bouchon de champagne s’envoie en l’air..."
    scene dejeuner-sol
    no "...un serviteur travaille au sol, et d’autres éléments rythment toute cette scène de cette manière."
    jump dejeunerSuite14

label dejeunerSuite14:
    scene dejeuner-zoomtable
    nomJoueur "Je comprends donc mieux l’intention du peintre De Troy."
    nomJoueur "Oh mais que le temps passe vite !"
    nomJoueur "Je dois malheureusement vous quitter."
    nomJoueur "J’ai passé un très bon moment à vos côtés."
    no "Oh déjà ?"
    no "Très bien, je comprends, aimable personnage."
    no "Que votre voyage soit semé de fructueuses rencontres !"
    nomJoueur "Je vous remercie chaleureusement."
    no "Ah ! Et encore une chose !"
    nomJoueur "Hm ?"
    scene dejeuner-huitres
    no "N’oubliez pas : nous sommes précisément à un moment somptueux digne des heures fastes de Versailles."
    no "Abondance, excès, insouciance : tels sont des termes qui conviennent le mieux pour ce magnifique dîner, ha-ha !"
    nomJoueur "Je l'avais effectivement bien compris."
    $renpy.sound.play("cloches.mp3", loop=True)
    nomJoueur "Mais j'aimerais juste..."
    nomJoueur "Oh ! Il est vraiment temps pour moi de m'en aller."
    nomJoueur "Merci infinement pour tout et au revoir."
    no "Adieu, aimable personnage. Et bon vent !"

    stop sound fadeout (3.0)
    stop music fadeout (3.0)
    scene jaune
    with Fade(3.0, 0.0, 0.5, color="#d1ca73")

## Scene 11 retour dans la salle royale
    play music "Ambiance.mp3"
    scene salle-royale
    with Fade(1.0, 0.0, 0.5, color="#d1ca73")

    nomJoueur "Et de deux !"
    nomJoueur "Quel incroyable {b}Déjeuner d'huîtres !"
    nomJoueur "Ca commence à faire pas mal d’informations à retenir, mais j’y arriverai !"
    nomJoueur "Bon maintenant direction la dernière salle."

## Scene 12 dans la salle des photos américaines
    scene salle-photo
    with blinds
    stop music

    nomJoueur "Oh !"
    nomJoueur "Quel endroit épuré contrairement aux deux dernières salles."

    stop music fadeout (1.0)
    play music "Moose.mp3"

    c "Eh bien, ha-ha-ha !"
    nomJoueur "Oh, c'est vous !"
    c "Comment se passe ton petit périple artistique, ha-ha-ha ?"
    c "Les œuvres ont-elles été réceptives à ton arrivée ?"
    nomJoueur "Oui, je n’ai eu aucun problème à trouver des informations, je vous remercie !"
    c "Ha-ha-ha ! Tu es sur la bonne voie."
    c "Avant de te laisser continuer, j’aimerais te faire remarquer quelque chose."
    c "Tu ne remarques pas que cette salle est différente des autres ?"
    nomJoueur "Oui, effectivement !"
    nomJoueur "Cette salle est plus épurée et neutre, je dirai."
    c "En effet !"
    c "Tu te trouves dans une salle qui arbore une architecture intérieure spécifique."
    c "Elle n'est pas sans rappeler une certaine influence muséologique."
    c "Saurais-tu me dire laquelle, ha-ha-ha ?"
    c "C’est juste pour enrichir ta culture générale à propos de l’histoire de l’art et des musées."
    c "Donc, de quoi parle-t-on quand on est face à une telle salle ?"
    nomJoueur "{i}(Hm… Des murs épurés, un éclairage clair et diffus, des œuvres espacées entre elles, c’est évidemment...)"

    menu:
        "...une salle de style baroque.":
            jump quizz1
        "...une salle de type « white cube ».":
            jump quizz2

label quizz1:
    play sound "click.mp3"
    c "Quoi ?!"
    c "Comment oses-tu dire de telles sornettes !"
    c "Tu n'as visiblement pas compris grand chose jusqu'à présent..."
    c "Mais comme je suis aimable, je vais te dire pourquoi tu te trompes."
    jump quizz3

label quizz2:
    play sound "click.mp3"
    c "Tout juste, ha-ha-ha ! Quel oeil !"
    jump quizz3

label quizz3:
    c "On ressent ici clairement une influence du « white cube », qu’on appelle en français « cube blanc »."
    c "Cette manière particulière de concevoir un espace d’exposition possède la forme d’une grande enceinte de murs blancs."
    c "Et le tout sans aucune fenêtre !"
    c "Cette conception de l’espace d’exposition est apparue dans les années 1970."
    c "Afin de permettre aux œuvres de s’exposer dans la plus grande neutralité possible."
    nomJoueur "Cette manière de faire peut parfois « aseptiser » les œuvres, non ?"
    c "En effet !"
    c "Pour certains, exposer ainsi des œuvres enlèverait de leur charme et les rendrait plus stériles."
    c "Mais bien sûr c’est à toi de te faire ton propre avis là-dessus, ha-ha-ha !"
    nomJoueur "Merci pour ces informations, ça ne peut que m’enrichir !"
    c "Allez !"
    c "Poursuis ton aventure, je te retrouverai après cette ultime œuvre, ha-ha-ha !"
    stop music fadeout (2.0)
    nomJoueur "Merci !"
    nomJoueur "Bon..."
    nomJoueur "J'y retourne !"
    nomJoueur "Je saute dans la première œuvre que je vois."
    nomJoueur "C'était une bonne surprise quand je l'ai fais juste avant."
    play sound "pianoloop.mp3"
    scene jaune
    with Fade(3.0, 0.0, 0.5, color="#d1ca73")

## Scene 13 : dans la photo Lunch
    call screen preLunch

label inLunch:
    play sound "click2.mp3"
    play music "Jazz.mp3"
    scene lunch-skyscraper
    with Dissolve(8.0)
    $ renpy.pause()

    nomJoueur "Woah !!!"
    nomJoueur "Où suis-je ?"
    nomJoueur "Je suis suspendu à plusieurs mètres au-dessus du sol !"
    nomJoueur "Il faut bien que je fasse attention à ne pas tomber, une chute à cette hauteur serait clairement mortelle."
    inconnu "Hé ! Toi !"
    nomJoueur "Hm ?"
    nomJoueur "C'est... c'est à moi que vous parlez ?"
    inconnu "Oui. T'fais quoi ici ? Et t’es qui ?"
    nomJoueur "Je m’appelle [nomJoueur]. Et, euh..."
    nomJoueur "Je visite !"
    inconnu "T'visites ? Un endroit pareil ?"
    inconnu "C’est un chantier ici, c’est hyper dangereux pour des gens comme toi."
    nomJoueur "Des gens comme moi ? Vous, vous travaillez ici c’est ça ?"
    inconnu "Eh oui [nomJoueur] ! Moi et mes 10 autres collègues on est des ouvriers !"
    nomJoueur "Mais vous n’êtes pas attachés !"
    nomJoueur "Comment faites-vous pour tenir en équilibre et ne pas chuter pendant vos travaux ?"
    ou1 "Et bah c’est l’habitude !"
    ou1 "T'sais on a toujours travaillé dans ces conditions."
    ou1 "Et ici, à New York, c’est la course à qui construira le plus haut building."
    ou2 "Du coup, on est tous réquisitionnés pour construire cette belle bête !"
    ou3 "Et tout ça le plus rapidement possible, tu vois un peu le courage qu’on a !"
    nomJoueur "Quel genre de bête c’est ?"
    ou1 "Bah le bâtiment principal du Rockefeller Center : le RCA building !"
    nomJoueur "C’est vraiment impressionnant..."
    nomJoueur "Et vous voir manger ainsi avec une telle aisance, à plus de..."
    nomJoueur "D’ailleurs, à combien de mètres sommes-nous du sol ?"
    ou1 "Plus de 200 mètres, pour sûr !"
    ou2 "On s’trouve actuellement au niveau du 69ème étage si j’me trompe pas !"
    ou3 "C'est ça !"
    nomJoueur "{i}(200 mètres… Plus je regarde en bas, plus j’ai envie de vite m’en aller d’ici, quelle angoisse...)"
    nomJoueur "{i}(M’enfin. Reprends-toi [nomJoueur]. Faut pas oublier pour quelle raison tu es ici.)"
    nomJoueur "Je peux vous déranger quelques instants pendant que vous mangez ? J’ai quelques questions."
    ou1 "T'gêne pas [nomJoueur]!"
    
    menu:
        "D'où venez-vous ?":
            jump lunch1
        "Pourquoi travaillez-vous sur ce chantier ?":
            jump lunch2

label lunch1:
    play sound "click.mp3"
    ou1 "De tous les horizons !"
    ou1 "On est quasiment tous, entre ce chantier et les autres de la ville, des immigrés qui viennent principalement d’Europe."
    ou2 "On cherche du boulot et ici on en trouve pas mal !"
    ou3 "Regarde tous ces chantiers, ils ont besoin de main d’œuvre et on est là pour y répondre."
    jump lunch3

label lunch2:
    play sound "click.mp3"
    ou1 "C’est Mr. John Davison Rockfeller qui nous a engagé."
    ou1 "Il a embauché plusieurs d’entre nous pour tenter de relancer l’économie après le fameux krach de 1929."
    ou2 "Quel homme !"
    ou3 "Tu l’as dit. Y’a pas plus généreux."
    jump lunch3

label lunch3:
    nomJoueur "Je comprends."
    nomJoueur "Vous êtes donc contents d’être ici ?"
    ou1 "Pour sûr !"
    ou1 "Y’a évidemment des conditions de travail bien meilleures ailleurs mais nous on est fier de construire ce bâtiment !"
    nomJoueur "En effet, ça se voit ! Mais dites m’en plus..."

    menu:
        "Vous représentez donc une certaine « ode à la fierté » ?":
            jump lunch4
        "Quelques détails historiques ?":
            jump lunch5

label lunch4:
    play sound "click.mp3"
    ou1 "Ouaip’ !"
    ou1 "En réalité, cette photographie fait partie d’un ensemble et ont été toutes prises le même jour."
    ou2 "C’est pour d'la pub !"
    ou2 "On a voulu montrer le travail qu’on mène ici et le risque qu’on prend tous les jours."
    ou3 "Y’avait plusieurs photographes ce jour-là d’ailleurs !"
    jump lunch6

label lunch5:
    play sound "click.mp3"
    ou1 "Cette photographie est apparue pour la première fois dans le New York Herald Tribune."
    ou2 "Le 2 octobre 1932 pour être exact."
    ou3 "Ça a généré une grande pub pour nous."
    ou3 "On voyait enfin les efforts et le travail qu’on donnait sur ce genre d'chantier."
    jump lunch6

label lunch6:
    nomJoueur "Mais alors qui vous a donc photographié ?"
    ou1 "On n’sait pas !"
    ou1 "Y’en avait trois : Thomas Ebbet, William Leftwich et Thomas Kelly."
    ou1 "Les trois étaient vraiment courageux de venir jusqu’ici pour vivre ce qu’on vit tous les jours !"
    nomJoueur "Vous voulez donc dire que personne ne sait qui est l’origine de cette photo précise ?"
    ou2 "C’est ça !"
    nomJoueur "Concernant vos identités, on sait qui vous êtes non ?"
    ou1 "Eh beh figure toi que non !"
    ou2 "Nous, les hommes qui avons construit ce bâtiment, avons finalement été oubliés par l’histoire..."
    ou3 "Seule cette image, et les autres de la série bien sûr, témoigne de notre travail et de notre présence ici !"
    nomJoueur "Je pense donc que cette image..."

    menu:
        "...fixe un moment de l’histoire important pour New York.":
            jump lunch7
        "...témoigne de votre travail d’une manière humble et véridique.":
            jump lunch8

label lunch7:
    play sound "click.mp3"
    ou1 "C’est ça !"
    ou2 "La construction du Rockfeller Center a engagé beaucoup de main d’œuvre..."
    ou3 "...et a permis de montrer notre existence et notre travail au reste du monde !"
    jump lunch9

label lunch8:
    play sound "click.mp3"
    ou1 "On a été un maillon essentiel dans la construction du Rockfeller Center !"
    ou2 "La démarche des photographes nous donne de l’importance..."
    ou3 "...et donne du crédit à nous qui généralement n’en avons pas."
    jump lunch9

label lunch9:
    nomJoueur "C’est vraiment incroyable ce qu’une photographie peut raconter sur une période précise d’une ville."
    ou1 "Ouaip’ !"
    ou1 "Et on était plus de 4000 ouvriers parmi tous les chantiers du Center ! Imagine un peu !"
    nomJoueur "Très impressionnant effectivement..."
    nomJoueur "Décidément, je ne m’y fais toujours pas à ce vide sous mes pieds..."
    ou1 "Ha-ha-ha ! En bossant ici, tu t’y habitues vite !"
    ou2 "Tu l’as dit !"
    nomJoueur "J’en suis sûr !"
    nomJoueur "Encore une chose."
    nomJoueur "Si je devais retenir quelque chose d’essentiel à propos de cette image, qu’est-ce que ça serait ?"
    ou1 "Eh bien, je pense que cette photo montre de manière plus large que l’Amérique va bien."
    ou1 "Si tu vois ce que j’veux dire."
    ou2 "Des ouvriers de tous les horizons bossent ensemble au développement de la ville de New York dans un moment de prospérité général."
    ou3 "Et n’oublie pas !"
    ou3 "Fierté, travail et effort sont les maîtres mots qui résument notre décontraction déconcertante, assis sur cette poutre..."
    $renpy.sound.play("cloches.mp3", loop=True)
    nomJoueur "Mais que dire de..."
    nomJoueur "Mince ! Je dois vraiment vous quitter."
    ou1 "Pas d'soucis [nomJoueur] !"
    nomJoueur "Merci pour tout !"

    stop sound fadeout (3.0)
    stop music fadeout (3.0)
    scene jaune
    with Fade(3.0, 0.0, 0.5, color="#d1ca73")

##Scene 14 : retour dans la salle des photos
    play music "Ambiance.mp3"
    scene salle-photo
    with Fade(1.0, 0.0, 0.5, color="#d1ca73")

    nomJoueur "Woah !"
    nomJoueur "Ce {b}Lunch atop a skyscraper{/b} était vraiment hors du commun !"
    nomJoueur "Quelle aventure..."
    nomJoueur "Ces trois univers étaient tous plus enrichissants les uns que les autres."
    nomJoueur "J'espère avoir retenu l'essentiel."
    nomJoueur "Bon."
    nomJoueur "C’est le moment de vérité."
    nomJoueur "Courage [nomJoueur], il faut que t’assures !"
    nomJoueur "Le conservateur m'attend sûrement de pied ferme."
    nomJoueur "Direction son bureau !"

    stop music

## Scene 15 : retour dans le bureau du conservateur (quizz final)
    play music "Moose.mp3"
    scene bureau-conservateur
    with dissolve

    c "Alors [nomJoueur], déjà de retour, ha-ha-ha ?"
    nomJoueur "Oui ! C’était vraiment trois aventures excitantes."
    nomJoueur "J’ai appris beaucoup de choses sur ces œuvres emblématiques de l’histoire de l’art."
    c "Ha-ha-ha ! Tant mieux !"
    c "C'est maintenant l'heure de vérité."
    c "Je vais te faire vivre une petite expérience sympathique tu verras, ha-ha-ha."
    nomJoueur "Hm ?"
    c "Es-tu prêt à me suivre ?"
    stop music fadeout 2.0

    menu:
        "Oui. Allons-y !":
            jump suite2
        "Euh, pas tout à fait encore...":
            jump PrepQuizz

label PrepQuizz:
    play sound "click.mp3"
    c "Très bien, ha-ha-ha !"
    c "Je te laisse quelques instants pour te préparer."
    c "Voici les trois œuvres que tu as visité."
    c "Tu peux les revoir autant de temps que le souhaites."
    call screen troisTableaux

label suite2:
    play sound "click.mp3"
    c "Très bien, c'est parti !"

##Scene 16 : dans le quizz final
    $renpy.music.play("Quizz2.mp3", loop=True)
    scene damier
    with Pixellate(4.5,20)

    cquizz "Bienvenue [nomJoueur] au {b}GRAND QUIZZ X{/b} !"
    cquizz "Je vais tester tes connaissances avec plusieurs questions."
    cquizz "Accroche-toi bien, ça ne sera pas du gâteau !"
    cquizz "Si tu ne réponds pas correctement, tout sera terminé pour toi."
    cquizz "Alors donne tout !!!"
    cquizz "Question n°1."

label quizzFinal1:
    cquizz "De quelle année date l'oeuvre {b}Lunch atop a skyscraper{/b} ?"
    menu:
        "1932":
            play sound "correct.mp3"
            cquizz "Correct !"
        "1952":
            play sound "error.mp3"
            cquizz "Dommage, ce n'est pas la bonne réponse..."
            jump quizzFinal1
        "1992":
            play sound "error.mp3"
            cquizz "Dommage, ce n'est pas la bonne réponse..."
            jump quizzFinal1

    cquizz "Question n°2."

    label quizzFinal2:
    cquizz "Qui a peint {b}Abtei im Eichwald{/b} ?"
    menu:
        "Caspar David Friedrich":
            play sound "correct.mp3"
            cquizz "C'est juste !"
        "Arnold Böcklin":
            play sound "error.mp3"
            cquizz "Aïe ! C'est faux..."
            jump quizzFinal2
        "Rembrandt":
            play sound "error.mp3"
            cquizz "Dommage, ce n'est pas la bonne réponse..."
            jump quizzFinal2

    cquizz "Troisième question."

    label quizzFinal3:
    cquizz "L'œuvre {b}Le déjeuner d'huîtres{/b}..."
    menu:
        "...est un pastel.":
            play sound "error.mp3"
            cquizz "Eh non..."
            jump quizzFinal3
        "..est fait d'acrylique.":
            play sound "error.mp3"
            cquizz "Dommage, ce n'est pas la bonne réponse..."
            jump quizzFinal3
        "...est une huile sur toile.":
            play sound "correct.mp3"
            cquizz "Bien joué !"

    cquizz "Très bien, continuons !"
    
    cquizz "Place à la quatrième question."

    label quizzFinal4:
    cquizz "Sur quoi étaient assis les ouvriers de New York ?"
    menu:
        "Sur une grue":
            play sound "error.mp3"
            cquizz "C'est faux..."
            jump quizzFinal4
        "Sur une poutre métallique":
            play sound "correct.mp3"
            cquizz "Exact !"
        "Sur un banc spécialement aménagé pour les chantiers":
            play sound "error.mp3"
            cquizz "C'est faux..."
            jump quizzFinal4

    cquizz "Question suivante."

    label quizzFinal5:
    cquizz "À quelle question sommes-nous ?"
    menu:
        "La quatrième question":
            play sound "error.mp3"
            cquizz "Eh non..."
            jump quizzFinal5
        "La cinquième question":
            play sound "correct.mp3"
            cquizz "C'est juste ! Quelle mémoire !"
        "La sixième question":
            play sound "error.mp3"
            cquizz "Eh non..."
            jump quizzFinal5

    cquizz "Question n°6."

    label quizzFinal6:
    cquizz "Des huîtres, des nobles et..."
    menu :
        "...du champagne.":
            play sound "correct.mp3"
            cquizz "Bien vu !"
        "...du vin rouge.":
            play sound "error.mp3"
            cquizz "Dommage..."
            jump quizzFinal6
        "...du cognac.":
            play sound "error.mp3"
            cquizz "Dommage..."
            jump quizzFinal6

    cquizz "Question suivante"

    label quizzFinal7:
    cquizz "Comment pourrait-on traduire en français le tableau de Friedrich intitulé {b}Abtei im Eichwald{/b} ?"
    menu :
        "L'abbaye dans une forêt d'arbres":
            play sound "error.mp3"
            cquizz "Je ne crois pas..."
            jump quizzFinal7
        "L'abbaye dans une forêt de chênes":
            play sound "correct.mp3"
            cquizz "Oui c'est ça !"
        "L'abbaye dans un paysage désolé":
            play sound "error.mp3"
            cquizz "Je ne crois pas..."
            jump quizzFinal7

    cquizz "Attention ça va se corser maintenant!"

    label quizzFinal8:
    cquizz "Sous quel règne se passe {b}Le Déjeuner d'huîtres{/b} ?"
    menu:
        "Louis XV":
            play sound "correct.mp3"
            cquizz "Exactement, il a régné de 1715 à 1774."
        "Louis-Philippe Ier":
            play sound "error.mp3"
            cquizz "Ce n'est pas la bonne réponse..."
            jump quizzFinal8
        "Louis XIV":
            play sound "error.mp3"
            cquizz "Ce n'est pas la bonne réponse..."
            jump quizzFinal8
        "Henri IV":
            play sound "error.mp3"
            cquizz "Ce n'est pas la bonne réponse..."
            jump quizzFinal8
        "Charles VII":
            play sound "error.mp3"
            cquizz "Ce n'est pas la bonne réponse..."
            jump quizzFinal8

    cquizz "Tu y es presque !"

    label quizzFinal9:
    cquizz "À quel courant peut-on rattacher le tabeau de Friedrich ?"
    menu:
        "L'expressionnisme allemand":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal9
        "L'art nouveau":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal9
        "Le pré-impressionnisme":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal9
        "Le romantisme allemand":
            play sound "correct.mp3"
            cquizz "C'est ça ! Et il a duré jusqu'en 1850 !"
        "Le symbolisme":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal9

    cquizz "Et enfin la dernière question !"

    label quizzFinal10:
    cquizz "Combien de personnages au total as-tu rencontré dans ces trois œuvres ?"
    menu :
        "3":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal10
        "8":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal10
        "5":
            play sound "correct.mp3"
            cquizz "Et oui !"
            cquizz "Il y'avait le chêne, le noble et les trois ouvriers."
        "2":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal10
        "4":
            play sound "error.mp3"
            cquizz "Absolument pas..."
            jump quizzFinal10

    cquizz "{b}C'est fini !"
    cquizz "C'est le moment de vérité."
    cquizz "Nous allons savoir si tu es engagé ou recalé !"
    stop music fadeout 3.0

## Scene 17 : retour dans le bureau (apres le quizz)
    scene bureau-conservateur
    with Pixellate(4.5,20)
    play music "Ambiance.mp3"

    c "Alors ? Ha-ha-ha !"
    c "Comment as-tu vécu ce petit moment stressant ?"
    nomJoueur "Plus simple que je ne l'imaginais à vrai dire."
    c "Effectivement !"
    c "Tout cela n'était qu'une mise en scène."
    c "Je voulais juste m'assurer que tu avais au moins retenu l'essentiel."
    c "Je t'annonce officilement que..."
    c "{b}TU ES ENGAGÉ !"
    nomJoueur "Oh !!"
    nomJoueur "Mais c'est incroyable !!!"

    stop music fadeout 4.0
    scene black
    with Fade(3.0, 0.0, 0.5, color="#000000")

## Scene 18 : dans la rue de nuit (fin)
    play music "Fin.mp3"
    scene rue-nuit
    with dissolve

    nomJoueur "Ah..."
    nomJoueur "Quelle journée."
    nomJoueur "C'était vraiment une aventure incroyable."
    nomJoueur "Je savais que le conservateur me faisait confiance."
    nomJoueur "Même si ce petit quizz était intense, j'ai appris beaucoup de choses aujourd'hui."
    nomJoueur "Quand je reverrai ces trois tableaux, je saurai de quoi il en retourne maintenant."
    nomJoueur "M'enfin..."
    nomJoueur "Il est l'heure de rentrer."

    call credits from _call_credits
    return

label credits:
    $ credits_speed = 40
    scene blanc
    with Fade(3.0, 0.0, 0.5, color="#fff")
    scene hommagepapa
    show hommage:
        yanchor 0.18 ypos 0.18
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide hommage
    scene blanc
    with dissolve
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause()
    stop music fadeout (3.0)
    hide thanks
    with Fade(3.0, 0.0, 0.5, color="#fff")
    return

init python:
    credits = ('Développé par', 'Raphaël Garnier'), ('Codé sur', 'Visual Studio Code'), ('Images des tableaux', 'Google Arts & Culture'), ('Images de fond et sprites', 'Unsplash, Pixabay'), ('Textes', 'Raphaël Garnier'), ('Musiques', 'Bensound, The Sound Resource'), ('Sons et bruitages', 'Universal Soundbank, Freesound'), ('Testeurs', 'Julien Norberg, Caroline Garnier, Gentiana Sejdija, Adèle Zufferey'), ('Remerciements', 'Communauté RenPy, PicMonkey, PicsArt'), ('Informations complémentaires', 'Consulter la section « À propos » sur le menu principal')
    credits_s = "{size=100}Crédits\n\n"
    d1 = ''
    for d in credits:
        if not d1==d[0]:
            credits_s += "\n{size=35}" + d[0] + "\n"
        credits_s += "{size=50}" + d[1] + "\n"
        d1=d[0]
    credits_s += "\n{size=35}Moteur de jeu\n{size=50}Ren'py\n7.3.3.568"
    
init:
    image cred = Text(credits_s, text_align=0.5)
    image hommage = Text("{size=80}À mon père.", text_align=0.5)
    image thanks = Text("{size=80}Merci d'avoir joué !", text_align=0.5)
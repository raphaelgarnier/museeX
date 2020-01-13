## Sides-images des personnages qui parlent
image conservateur:
    "sprite-conservateur-final.png"
    size(300,800)

image side conservateur:
    LiveCrop((20,0,300,350), "conservateur")

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform

define config.say_attribute_transition = Dissolve(0.2, alpha=True)



image conservateurquizz:
    "sprite-conservateur-final-quizz.png"
    size(300,800)

image side conservateurquizz:
    LiveCrop((30,0,300,350), "conservateurquizz")

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform

define config.say_attribute_transition = Dissolve(0.2, alpha=True)



##Déclaration des images 
image blanc:
    "white.jpg"
    size(1280,720)

image jaune:
    "fondjaune.jpg"
    size(1280,720)

image damier:
    "damier-quizz.jpg"
    size(1280,720)

image hommagepapa:
    "bg-hommage.jpg"
    size(1280,720)

image notes:
    "parchemin-etapes2.png"

image recap-trois-tableaux:
    "recap-trois-tableaux.jpg"

image musee-interieur:
    "bg-museeint.jpg"
    size(1280,720)

image rue-nuit:
    "bg-ruenuit.jpg"
    size(1280,720)

image bureau-conservateur:
    "bg-bureau.jpg"
    size(1280,720)

image sol-puzzle:
    "bg-sol.jpg"
    size(1280,720)

image salle-allemand:
    "bg-salleallemand.png"
    size(1280,720)

image salle-royale:
    "bg-salleroyal.png"
    size(1280,720)

image salle-photo:
    "bg-salleusa.png"
    size(1280,720)

image rue-nuit:
    "bg-ruenuit.jpg"
    size(1280,720)

image abbaye-clairobscur:
    "bg-abbaye-clairobscur.jpg"
    size(1280,720)

image abbaye-mort:
    "bg-abbaye-mort.jpg"
    size(1280,720)

image dejeuner-huitres:
    "dejeuner-huitres-final.png"
    size(1280,720)

image dejeuner-zoomtable:
    "bg-dejeuner-table.jpg"
    size(1280,720)

image dejeuner-plafond:
    "bg-dejeuner-plafond.jpg"
    size(1280,720)

image dejeuner-dressage:
    "bg-dejeuner-dressage.jpg"
    size(1280,720)

image dejeuner-bouchon:
    "bg-dejeuner-bouchon.jpg"
    size(1280,720)

image dejeuner-sol:
    "bg-dejeuner-sol.jpg"
    size(1280,720)

image lunch-skyscraper:
    "bg-lunch1.png"
    size(1280,720)

image abbaye-personnages:
    "bg-abbaye-zoom.jpg"
    size(1280,720)
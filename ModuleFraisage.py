import math

# On utilise EPS pour tester les egalites et differences entre variables (suite a des erreurs numeriques rencontrees en python)
EPS = 0.00000001 

###########
# Point2D #
###########

class Point2D:

  # __init__ : Constructeur
  # Entree : double xx, double yy : coordonnees
  # Sortie :
  def __init__(self, xx, yy):
    self.x = xx
    self.y = yy


  # __eq__ : Retourne si le point est egal a un autre
  # Entree : Point2D A : un autre point
  # Sortie : booleen : vrai si egalite entre le point et A
  def __eq__(self, A):
    return (math.fabs(self.x-A.x) < EPS) and (math.fabs(self.y-A.y) < EPS)

  
  # __neq__ : Retourne si le point est different d'un autre
  # Entree  : Point2D A : un autre point
  # Sortie  : booleen : vrai si difference entre le point et A
  def __neq__(self, A):
    return (math.fabs(self.x-A.x) > EPS) or (math.fabs(self.y-A.y) > EPS)

  
  # getX : Retourne l'abscisse
  # Entree :
  # Sortie : double : abscisse
  def getX(self):
    return self.x

  
  # getY : Retourne l'ordonnee
  # Entree :
  # Sortie : double : ordonnee
  def getY(self):
    return self.y

#  # setX : Modifie l'abscisse
#  # Entree : double : abscisse
#  # Sortie :
#  def setX(self, xx):
#    self.x = xx

#  
#  # setY : Modifie l'ordonnee
#  # Entree : double : ordonnee
#  # Sortie :
#  def setY(self, yy):
#    self.y = yy
  
  # afficher : Affiche les coordonnees dans la console
  # Entree :
  # Sortie :
  def afficher(self):
    print str(self.x)+" "+str(self.y)

  
  # norme : Retourne la norme euclidienne du point (vu comme vecteur)
  # Entree :
  # Sortie : double : la norme
  def norme(self):
    return math.sqrt(self.x*self.x + self.y*self.y)

  
  # normaliser : Normalise (modifie les coordonnees pour que la norme vaille 1) le point (vu comme vecteur)
  # Entree :
  # Sortie :
  def normaliser(self):
    norme = self.norme()
    self.x = self.x/norme
    self.y = self.y/norme

  
  # produitScalaire : Produit scalaire entre le point (vu comme vecteur) et un autre (vu comme vecteur)
  # Entree : Point2D p : autre point
  # Sortie : double : produit scalaire
  def produitScalaire(self, p):
    return self.x*p.x + self.y*p.y


  # estColineaireA : Teste si le point (vu comme vecteur) et un autre (vu comme vecteur) sont colineaires
  # Entree : Point2D p : autre point
  # Sortie : booleen : vrai si colineaire, faux sinon
  def estColineaireA(self, p):
    return (EPS > math.fabs(self.x*p.y - self.y*p.x) )


###########
# Segment #
###########

class Segment:
  
  # __init__ : Constructeur
  # Entree : Point2D AA, Point2D BB : points definissant le segment
  # Sortie :
  def __init__(self, AA, BB):
    if ( AA != BB ):
      self.A = AA
      self.B = BB
    else:
      print "ERREUR : declaration d'un segment avec deux points identiques"


  # afficher : Affiche les coordonnees dans la console
  # Entree :
  # Sortie :
  def afficher(self):
    print "[ ("+str(self.A.x)+","+str(self.A.y)+") --- ("+str(self.B.x)+","+str(self.B.y)+") ]"


  # afficher : Affiche les coordonnees dans la console du point initial et du point final
  # Entree :
  # Sortie :
  def afficherPointsSeulement(self):
    print str(self.A.x)+" "+str(self.A.y)
    print str(self.B.x)+" "+str(self.B.y)


  # croise : Teste si le segment en croise un autre
  # Entree : Segment s : autre segment
  # Sortie : booleen : vrai s'il croise le segment, faux sinon
  def croise(self, s):
#    print "[[["+str(self.A.x)+","+str(self.A.y)+"-"+str(self.B.x)+","+str(self.B.y)+"]]] [[["+str(s.A.x)+","+str(s.A.y)+"-"+str(s.B.x)+","+str(s.B.y)+"]]]"
    
    A1=1; B1=0; C1=0; # parametres de self
    if( math.fabs(self.A.x - self.B.x) < EPS ): # self.A.x == self.B.x
      C1 = self.A.x
    else:
      A1 = (self.A.y - self.B.y)/(self.A.x - self.B.x)
      B1 = -1
      C1 = A1*self.A.x - self.A.y
    
    A2=1; B2=0; C2=0; # parametres de s 
    if(math.fabs(s.A.x - s.B.x) < EPS): # s.A.x == s.B.x
      C2 = s.A.x
    else:
      A2 = (s.A.y - s.B.y)/(s.A.x - s.B.x)
      B2 = -1
      C2 = A2*s.A.x - s.A.y
    det = A1*B2 - A2*B1
#    print "A1:"+str(A1)+" B1:"+str(B1)+" C1:"+str(C1)+" A2:"+str(A2)+" B2:"+str(B2)+" C2:"+str(C2)+" det:"+str(det)
    
    # point d'intersection:
    X=0 
    Y=0
    res = False
    if(math.fabs (det) > EPS): # (det != 0) segments non paralleles
      X = (B2*C1 - B1*C2)/det
      Y = (A1*C2 - A2*C1)/det
      
      # on retourne vrai si (X,Y) appartient aux 2 segments
      res = (min(self.A.x,self.B.x) <= X and X <= max(self.A.x,self.B.x) and min(self.A.y,self.B.y) <= Y and Y <= max(self.A.y,self.B.y) ) and (min(s.A.x,s.B.x) <= X and X <= max(s.A.x,s.B.x) and min(s.A.y,s.B.y) <= Y and Y <= max(s.A.y,s.B.y) )
      
    return res


#################################################################
# Arc                                                           #
# /!\ Les arcs sont pour l'instant definis dans le sens horaire #
#################################################################

class Arc:

  # __init__ : Constructeur
  # Entree : Point2D cc, Point2D AA, Point2D BB, booleen lesens : centre, debut et fin de l'arc, sens de rotation (True : sens horaire, False : sens antihoraire)
  # Sortie :
  def __init__(self, cc, AA, BB, lesens):
    if ( AA!=BB ):
      self.c = cc         # centre
      self.A = AA         # premier point
      self.B = BB         # deuxieme point
      self.sens = lesens  # sens de rotation


  # afficher : Affiche les coordonnees dans la console
  # Entree :
  # Sortie :
  def afficher(self):
    lesens = "horaire"
    if not self.sens:
      lesens = "antihoraire"
    print "Arc de cercle "+lesens+" de centre ("+str(self.c.x)+","+str(self.c.y)+"), entre ("+str(self.A.x)+","+str(self.A.y)+") et ("+str(self.B.x)+","+str(self.B.y)+")"


  # afficher : Affiche les coordonnees dans la console des points initial et final seulement
  # Entree :
  # Sortie :
  def afficherPointsSeulement(self):
    print str(self.A.x)+" "+str(self.A.y)
    print str(self.B.x)+" "+str(self.B.y)
    

##############
# Polygone2D #
##############

class Polygone2D:

  # __init__ : Constructeur (on ajoute les points apres declaration du polygone)
  # Entree :
  # Sortie :
  def __init__(self):
    self.liste = []


  # getListe : Retourne la liste des points
  # Entree :
  # Sortie : liste : liste des points du polygone
  def getListe(self):
    return self.liste


  # getOrdonneeMinimale : Retourne l'ordonnee minimale parmi tous les points
  # Entree :
  # Sortie : double : ordonnee minimale
  def getOrdonneeMinimale(self):
    Ymin=self.getListe()[0].y
    for i in self.getListe():
      if(i.y < Ymin):
        Ymin = i.y
    return Ymin


  # getAire : Retourne l'aire du polygone. Le polygone est suppose acceptable ( tester avec la fonction Polygone2D.estAcceptable() avant )
  # Entree :
  # Sortie : double : aire
  def getAire(self):
    listeSegments = self.getListeSegments()
    Ymin = self.getOrdonneeMinimale()
    aire=0
    for i in listeSegments:
      aire = aire + (i.B.x - i.A.x)*( ( i.B.y + i.A.y)/2 - Ymin )
    return aire


  # estHoraire : Teste si les points sont declares dans le sens horaire ou pas. Le polygone est suppose acceptable ( tester avec la fonction Polygone2D.estAcceptable() avant )
  # Entree :
  # Sortie : booleen : vrai si horaire, faux sinon
  def estHoraire(self):
    return self.getAire() > 0


  # possedeDesSegmentsCroises : Teste s'il existe des segments qui se croisent
  # Entree :
  # Sortie : booleen : vrai s'il en existe, faux sinon
  def possedeDesSegmentsCroises(self):
    lstSegments = self.getListeSegments()
    continuer=True

    # on isole le cas i=0 (on doit s'arreter a j<len(lstSegments)-1)
    i=0
    j=i+2
    while (j<len(lstSegments)-1 and continuer):
#      print str(i)+"/"+str(j)
#      lstSegments[i].afficher()
#      lstSegments[j].afficher()
      continuer =  not (lstSegments[i].croise(lstSegments[j])) # s'ils se croisent continuer vaudra faux
      j=j+1
    
    # on passe a la suite
    i=i+1
    while (i<len(lstSegments) and continuer): # on s'arrete a l'avant dernier pour ne pas tester le croisement entre le dernier segment et le premier segment (qui se croisent forcement)
      j=i+2
      while (j<len(lstSegments) and continuer):
#        print str(i)+"/"+str(j)
#        lstSegments[i].afficher()
#        lstSegments[j].afficher()
        continuer =  not (lstSegments[i].croise(lstSegments[j])) # s'ils se croisent continuer vaudra faux
        j=j+1
      i=i+1
    return (not continuer) # si continuer vaut True, c'est qu'on n'a pas rencontre de segment qui se croisent, donc on renvoie False


  # estAcceptable : Teste si le polygone est acceptable
  # Criteres : Avoir 3 points ou plus ET il n'existe aucun segment qui se croisent ET ne pas etre plat (aire non nulle)
  # Entree :
  # Sortie : booleen : vrai s'il l'est, faux sinon
  def estAcceptable(self):
    ab=Point2D(self.get(1).x-self.get(0).x, self.get(1).y-self.get(0).y)
    bc=Point2D(self.get(2).x-self.get(1).x, self.get(2).y-self.get(1).y)
    if (self.taille() >= 3 and not self.possedeDesSegmentsCroises()): # polygone ayant plus de 3 points et ne possedant pas de segment qui se coupent
      return (self.getAire() != 0) # on teste si le polygone est plat
    else:
      return False


  # getListeSegments : Retourne la liste des segments du polygone
  # Entree :
  # Sortie : liste : segments du polygone
  def getListeSegments(self):
    lst = []
    for i in range(0,len(self.liste)):
      s = Segment (self.get(i),self.get(i+1))
      lst.append(s)
    return lst


  # taille : Retourne le nombre de points du polygone
  # Entree :
  # Sortie : entier : nombre de points
  def taille(self):
    return len(self.liste)


  # ajouter : Ajoute un point au polygone
  # Entree : Point2D p : point a ajouter
  # Sortie :
  def ajouter(self, p):
    self.liste.append(p)


  # get : Retourne le ieme point en tenant compte du fait que la liste des points est cyclique
  # Entree : entier i : indice du point a retourner (i entier positif quelconque)
  # Sortie : Point2D  : ieme point modulo le nombre de points
  def get(self, i):
    return self.liste[i%len(self.liste)]


  # afficher : Affiche les coordonnees des points du polygone par segment dans la console
  # Entree :
  # Sortie :
  def afficher(self):
    for k in self.liste:
      k.afficher()
    self.liste[0].afficher()


  # afficherPointsSeulement : Affiche dans la console les coordonnees des points du polygone
  # Entree :
  # Sortie :
  def afficherPointsSeulement(self):
    for k in self.liste:
      print str(k.x)+" "+str(k.y)
    print str(self.liste[0].x)+" "+str(self.liste[0].y)


  # calculerPointDecale : Calcule le point decale de dec unites perpendiculairement au segment, en partant du debut du segment ou de la fin
  # Entree : entier i   : indice du point a decaler dans la liste du polygone
  #          entier nb  : si nb==0 : calcule le point decale pour le point i   selon le segment [i,i+1]
  #                       si nb==1 : calcule le point decale pour le point i+1 selon le segment [i,i+1]
  #          double dec : decalage en unites de longueur du bord du polygone
  # Sortie : Point2D : point decale
  def calculerPointDecale(self, i, nb, dec):
    perp=Point2D(-(self.get(i+1).y-self.get(i).y),self.get(i+1).x-self.get(i).x)
    perp.normaliser()

    if(nb==0):
      res=Point2D(self.get(i).x + perp.x*dec, self.get(i).y + perp.y*dec)
    elif(nb==1):
      res=Point2D(self.get(i+1).x + perp.x*dec, self.get(i+1).y + perp.y*dec)
    else:
      print "ERREUR : nb doit valoir 0 ou 1"
    
    return res


  # typeDangleApres : Retourne le type d'angle venant apres le segment donne
  # Entree : entier i : indice du point A a partir duquel on calcule l'angle, c'est a dire l'angle ABC, donc l'angle a l'interieur du polygone
  # Sortie : entier : 1 si l'angle est convexe, -1 si concave, 0 si plat
  def typeDangleApres(self,i):
    ba=Point2D(-(self.get(i+1).x-self.get(i).x), -(self.get(i+1).y-self.get(i).y)) #vecteur BA
    bc=Point2D(self.get(i+2).x-self.get(i+1).x, self.get(i+2).y-self.get(i+1).y) #vecteur BC
    
    # si le produit vectoriel a la composante Z positive : convexe
    # si le produit vectoriel a la composante Z negative : concave
    # sinon                                              : colineaires
    if (ba.x*bc.y - ba.y*bc.x) > 0: # convexe
      return 1
    elif (ba.x*bc.y - ba.y*bc.x) < 0: # concave
      return -1
    else: # colineaires
      return 0

  

##########################################################################################################
# Fraisage                                                                                               #
# Classe qui construit la liste d'instructions pour fraiser un polygone avec une fraise d'un rayon donne #
# Par convention, un polygone declare dans le sens horaire sera fraise depuis son exterieur,             #
# et fraise de l'interieur s'il est declare dans le sens antihoraire                                     #
##########################################################################################################

class Fraisage:
  
  # __init__ : Constructeur
  # Entree : double r : rayon de la fraise
  # Sortie :
  def __init__(self,r):
    self.liste = []
    self.rayon = r
    self.listePoints = [] # liste des points seulement (definissant les segments et arcs). Sert a tester si le fraisage est possible


  # ajouter : Ajoute une instruction
  # Entree : Segment ou Arc : instruction
  # Sortie :  
  def ajouter(self, ins):
    self.liste.append(ins)
    self.listePoints.append(ins.A) # premier point du segment/arc. On ne met que celui-ci puisque l'instruction suivante commencera par le 2e point
  
  
  # afficherInstructions : Affiche les instructions
  # Entree :
  # Sortie :
  def afficherInstructions(self):
    for k in self.liste:
      k.afficher()


  # afficherInstructionsPointsSeulement : Affiche les points successifs definissant les segments et arcs de cercles de la decoupe
  # Entree :
  # Sortie :
  def afficherInstructionsPointsSeulement(self):
    for k in self.listePoints:
      print str(k.x)+ " " + str(k.y)
    # on affiche le premier point pour fermer la boucle
    print str(self.listePoints[0].x)+" "+str(self.listePoints[0].y)


  # calculerInstructions : Construit la liste des instructions etant donne un polygone
  # Entree : Polygone2D poly : polygone a fraiser
  # Sortie :
  def calculerInstructions(self, poly):
    if poly.estAcceptable():
      
      # on enregistre si la decoupe est exterieure (arire positive) ou interieure (aire negative)
      estExterne = poly.getAire() > 0
      
      # on ajoute le premier point:
      ptDecaleCourant = poly.calculerPointDecale(0,0,self.rayon)
      ptDecalePremier = ptDecaleCourant
      
      # pour tous les points, on verifie si l'angle d'apres est convexe ou concave ou droit
      for k in range(0,poly.taille()):
        # on ajoute le point courant
        
        # on commence un segment
        segCourant = Segment(Point2D(0,0),Point2D(1,1)) # declaration arbitraire
        segCourant.A = ptDecaleCourant
        
        angle=poly.typeDangleApres(k)
        
        # convexe
        if(angle == 1):
          # on ajoute le point decale du sommet suivant plus l'arc de cercle jusqu'au point decale suivant
          ptDecaleFin=poly.calculerPointDecale(k,1,self.rayon)
          
          # on finit le segment et on l'ajoute a la liste
          segCourant.B = ptDecaleFin
          self.ajouter(segCourant)
          
#          segCourant.afficher()
          
          ptDecaleDebSuiv = poly.calculerPointDecale(k+1,0,self.rayon)

          # on cree un arc et on l'ajoute a la liste
          arc = Arc(poly.get(k+1),ptDecaleFin,ptDecaleDebSuiv,estExterne)
          self.ajouter(arc)
          
#          arc.afficher()
          
          ptDecaleCourant = ptDecaleDebSuiv
          
        # concave
        elif (angle == -1):
          
          # on renomme les points ici pour plus de lisibilite
          A = poly.get(k)
          B = poly.get(k+1)
          C = poly.get(k+2)
          Ap = ptDecaleCourant
          Bp = poly.calculerPointDecale(k,1,self.rayon)
          
          # v = (BA normalise + BC normalise) normalise : vecteur directeur de la bissectrice
          ba=Point2D(-(B.x-A.x), -(B.y-A.y)) #vecteur BA
          bc=Point2D(C.x-B.x, C.y-B.y) #vecteur BC
          
          vba=Point2D(-(B.x-A.x), -(B.y-A.y)) #vecteur BA
          vba.normaliser()
          vbc=Point2D(C.x-B.x, C.y-B.y) #vecteur BC
          vbc.normaliser()
          v=Point2D(vba.x + vbc.x, vba.y + vbc.y)
          v.normaliser()
          
          intersec = Point2D(0,0)
          
          if (math.fabs(Ap.x - Bp.x) > EPS) : # Ap.x != Bp.x
            if (math.fabs(v.x) > EPS) : # v.x !=0
#              print "equation D1 : y="+str((Ap.y-Bp.y)/(Ap.x-Bp.x))+" x + "+str(Ap.y - (Ap.y-Bp.y)/(Ap.x-Bp.x)*Ap.x)
#              print "equation D2 : y="+str(v.y/v.x)+" x + "+str(v.y/v.x*B.x)
              intersec.x = (B.y-Ap.y + (Ap.y-Bp.y)/(Ap.x-Bp.x)*Ap.x - B.x/v.x * v.y)/((Ap.y-Bp.y)/(Ap.x-Bp.x) - v.y/v.x)
              intersec.y = (Ap.y-Bp.y)/(Ap.x-Bp.x) * intersec.x + Ap.y - (Ap.y-Bp.y)/(Ap.x-Bp.x)*Ap.x
            else:
#              print "equation D1 : y="+str((Ap.y-Bp.y)/(Ap.x-Bp.x))+" x + "+str(Ap.y - (Ap.y-Bp.y)/(Ap.x-Bp.x)*Ap.x)
#              print "equation D2 : x="+str(B.x)
              intersec.x = B.x
              intersec.y = (Ap.y-Bp.y)/(Ap.x-Bp.x) * intersec.x + Ap.y - (Ap.y-Bp.y)/(Ap.x-Bp.x)*Ap.x
          else:
            intersec.x = Ap.x
            intersec.y = v.y/v.x*Ap.x - B.x*v.y/v.x + B.y
          
          # on finit le segment et on l'ajoute a la liste
          segCourant.B = intersec
          
#          segCourant.afficher()
          
          self.ajouter(segCourant)
          
          ptDecaleCourant = intersec
        
        # points alignes
        elif (angle == 0):
          # on ajoute le point du bout du segment
          ptDecaleFin=poly.calculerPointDecale(k,1,self.rayon)
          
          # on finit le segment et on l'ajoute a la liste
          segCourant.B = ptDecaleFin
          self.ajouter(segCourant)
          
          # au tour d'apres, on va recalculer le point decale qui sera le meme que le dernier
          ptDecaleCourant = ptDecaleFin
        
        # impossible:
        else:
          print "ERREUR : type d'angle impossible"

      # Correction du premier point de la premiere instruction qui peut etre faux.
      self.liste[0].A = self.liste[len(self.liste)-1].B
      self.listePoints[0] = self.liste[len(self.liste)-1].B
        
    else:
      print "ERREUR : polygone non acceptable."
  
  
  # testerSiCroisementDecoupe : teste si la trajectoire de la fraise se croise ou pas
  # Entree :
  # Sortie : booleen : vrai si la decoupe est bonne (ne se croise pas), faux sinon
  def testerDecoupe(self):
    p = Polygone2D()
    for k in range(0,len(self.listePoints)-1): # on s'arrete a l'avant dernier point pour ne pas ajouter de nouveau le premier point
      p.ajouter(self.listePoints[k])
    return (not p.possedeDesSegmentsCroises())
  
      

########
# Main #
########

def main():
    poly = Polygone2D()

#    # Carre:
#    poly.ajouter(Point2D(1,1))
#    poly.ajouter(Point2D(1,4))
#    poly.ajouter(Point2D(4,4))
#    poly.ajouter(Point2D(4,1))

    # M:
    poly.ajouter(Point2D(0,0))
    poly.ajouter(Point2D(0,4))
    poly.ajouter(Point2D(2,2))
    poly.ajouter(Point2D(4,4))
    poly.ajouter(Point2D(4,0))

#    # M declare a l'envers (antihoraire)
#    poly.ajouter(Point2D(0,0))
#    poly.ajouter(Point2D(4,0))
#    poly.ajouter(Point2D(4,4))
#    poly.ajouter(Point2D(2,2))
#    poly.ajouter(Point2D(0,4))

#    # Biscornu
#    poly.ajouter(Point2D(0,0))
#    poly.ajouter(Point2D(2,2))
#    poly.ajouter(Point2D(0,5))
#    poly.ajouter(Point2D(0,6))
#    poly.ajouter(Point2D(0,7))
#    poly.ajouter(Point2D(1,7))
#    poly.ajouter(Point2D(2,3))
#    poly.ajouter(Point2D(4,4))
#    poly.ajouter(Point2D(5,2))
#    poly.ajouter(Point2D(7,0))

##    # Biscornu antihoraire
#    poly.ajouter(Point2D(0,0))
#    poly.ajouter(Point2D(7,0))
#    poly.ajouter(Point2D(5,2))
#    poly.ajouter(Point2D(4,4))
#    poly.ajouter(Point2D(2,3))
#    poly.ajouter(Point2D(1,7))
#    poly.ajouter(Point2D(0,7))
#    poly.ajouter(Point2D(0,6))
#    poly.ajouter(Point2D(0,5))
#    poly.ajouter(Point2D(2,2))

#    # Cas pathologique si le rayon est trop grand (superieur a 0.35 ici), les  :
#    poly.ajouter(Point2D(0,0))
#    poly.ajouter(Point2D(0,5))
#    poly.ajouter(Point2D(0.7,5))
#    poly.ajouter(Point2D(0.7,0))
#    poly.ajouter(Point2D(1.4,0))
#    poly.ajouter(Point2D(1.4,7))
#    poly.ajouter(Point2D(2.1,7))
#    poly.ajouter(Point2D(2.1,-1))

#    # polygone croise pour tester si les segments se croisent
#    poly.ajouter(Point2D(0,0))
#    poly.ajouter(Point2D(0,10))
#    poly.ajouter(Point2D(10,0))
#    poly.ajouter(Point2D(10,10))
#    poly.ajouter(Point2D(15,5))
#    poly.ajouter(Point2D(-5,5))
#    poly.ajouter(Point2D(5,0))

    
    

#    print ""
#    print "Polygone :"
#    print ""
#    poly.afficher()
    poly.afficherPointsSeulement()
    
    print
    print
    
#    print ""
#    print "Liste des segments :"
#    print ""
    lstSegments = poly.getListeSegments()
#    for k in lstSegments:
#      k.afficher()

#    print 
#    print "Le polygone possede des segments croises : " + str(poly.possedeDesSegmentsCroises())
#    print


#    print 
#    print "Aire du polygone : " + str(poly.getAire())
#    print

#    fraise = Fraisage(0.36) # rayon de 0.36cm
    fraise = Fraisage(0.2)
    
#    print ""    
#    print "Instructions :"
#    print "" 
    fraise.calculerInstructions(poly)

    if (not fraise.testerDecoupe()):
      print "ERREUR : la decoupe se chevauche. Modifier le rayon de la fraise ou revoir le plan de decoupe"
    else:
      fraise.afficherInstructionsPointsSeulement()
#      fraise.afficherInstructions()
      

if __name__ == "__main__":
    main()


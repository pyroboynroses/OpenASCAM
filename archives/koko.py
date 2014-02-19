import math



###########
# Point2D #
###########

class Point2D:
  def __init__(self, xx, yy):
    self.x = xx
    self.y = yy
  
  
  # egalite entre points
  def __eq__(self, A):
    return (self.x==A.x) and (self.y==A.y)
  
  # difference entre points
  def __neq__(self, A):
    return (self.x!=A.x) or (self.y!=A.y)
  
  def getX(self):
    return self.x
    
  def getY(self):
    return self.y
    
  def afficher(self):
    print str(self.x)+" "+str(self.y)
  
  def norme(self):
    return math.sqrt(self.x*self.x + self.y*self.y)
  
  def normaliser(self):
    norme = self.norme()
    self.x = self.x/norme
    self.y = self.y/norme
    
  def produitScalaire(self, p):
    return self.x*p.x + self.y*p.y
  
  def estColineaireA(self, p):
    return (0.0000000001 > self.x*p.y - self.y*p.x)


###########
# Segment #
###########

class Segment:
  def __init__(self, AA, BB):
    if ( AA!=BB ):
      self.A = AA
      self.B = BB
    else:
      print "ERREUR : declaration d'un segment avec deux points identiques"

  def afficher(self):
    print "[ ("+str(self.A.x)+","+str(self.A.y)+") --- ("+str(self.B.x)+","+str(self.B.y)+") ]"

#  # ce segment croise-t-il un autre segment s?
#  def croise(self, s):


#######
# Arc #
#######

# definis dans le sens horaire
class Arc:
  def __init__(self, cc, AA, BB):
    if ( AA!=BB ):
      self.c = cc # centre
      self.A = AA # premier point
      self.B = BB # deuxieme point
      
  def afficher(self):
    print "Arc de cercle de centre ("+str(self.c.x)+","+str(self.c.y)+"), entre ("+str(self.A.x)+","+str(self.A.y)+") et ("+str(self.B.x)+","+str(self.B.y)+")"

##############
# Polygone2D #
##############

class Polygone2D:
  def __init__(self):
    self.liste = []
  
  def getListe(self):
    return self.liste
  
  def estAcceptable(self):
    # on teste si le polygone a au moins 3 points et s'il n'y a que 3 points, qu'ils ne sont pas colineaires.
    # !!! il faudrait aussi verifier si les cotes du polygone ne se croisent pas, qu'ils ne sont pas tous colineaires entre eux, et aussi que les points sont dans le sens horaire !!!
    ab=Point2D(self.get(1).x-self.get(0).x, self.get(1).y-self.get(0).y)
    bc=Point2D(self.get(2).x-self.get(1).x, self.get(2).y-self.get(1).y)
    if (self.taille() > 3):
      return 1==1
    elif (self.taille() == 3 and ab.estColineaireA(bc)):
      return 1==0
    else:
      return 1==1
    
    
  
  def taille(self):
    return len(self.liste)
   
  def ajouter(self, p):
    self.liste.append(p)
  
  def get(self, i):
    return self.liste[i%len(self.liste)]
  
  def afficher(self):
    for k in self.liste:
      k.afficher()
    self.liste[0].afficher()

  # i   : indice du point a decaler dans la liste du polygone
  # nb  : si nb==0 : calcule le point decale pour le point i   selon le segment [i,i+1]
  #       si nb==1 : calcule le point decale pour le point i+1 selon le segment [i,i+1]
  # dec : decalage en cm du bord du polygone
  def calculerPointDecale(self, i, nb, dec):
#    print "Dans calculerPointDecale"
#    print "Points A/B"
#    self.get(i).afficher()
#    self.get(i+1).afficher()
    
    perp=Point2D(-(self.get(i+1).y-self.get(i).y),self.get(i+1).x-self.get(i).x)
#    print "perp"
#    perp.afficher()
    perp.normaliser()
#    print "perp normalise"
#    perp.afficher()


    if(nb==0):
      res=Point2D(self.get(i).x + perp.x*dec, self.get(i).y + perp.y*dec)
    elif(nb==1):
      res=Point2D(self.get(i+1).x + perp.x*dec, self.get(i+1).y + perp.y*dec)
    else:
      print "ERREUR : nb doit valoir 0 ou 1"
    
#    print "Point decale:"
#    res.afficher()
    return res
  
  
  # i : indice du point A a partir duquel on calcule l'angle,
  # c'est a dire l'angle ABC, donc l'angle a l'interieur du polygone
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


#    # BA . BC = cos(alpha) BA x BC (. est le produit scalaire entre vecteurs, x est la multiplication de leur norme)


############
# Fraisage #  
############

class Fraisage:
  def __init__(self,r):
    self.liste = []
    self.rayon = r
    
  def ajouter(self, ins):
    self.liste.append(ins)
    
  def afficherInstructions(self):
    for k in self.liste:
      k.afficher()
  
  def calculerInstructions(self, poly):
    if poly.estAcceptable():
      
      # on ajoute le premier point:
#      self.ajouter(poly.calculerPointDecale(0,0,self.r))
      ptDecaleCourant = poly.calculerPointDecale(0,0,self.rayon)
      ptDecalePremier = ptDecaleCourant
      
      # pour tous les points, on verifie si l'angle d'apres est convexe ou concave ou droit
      for k in range(0,poly.taille()):
        # on ajoute le point courant
###
#        ptDecaleCourant.afficher()
        
        # on commence un segment
        segCourant = Segment(Point2D(0,0),Point2D(1,1)) # declaration arbitraire
        segCourant.A = ptDecaleCourant
        
        
        angle=poly.typeDangleApres(k)
        
        # convexe
        if(angle == 1):
          # on ajoute le point decale du sommet suivant plus l'arc de cercle jusqu'au point decale suivant
          ptDecaleFin=poly.calculerPointDecale(k,1,self.rayon)
###
#          ptDecaleFin.afficher()
          
          # on finit le segment et on l'ajoute a la liste
          segCourant.B = ptDecaleFin
          self.ajouter(segCourant)
          
          
          
          ptDecaleDebSuiv = poly.calculerPointDecale(k+1,0,self.rayon)
#          msgarc="Arc de cercle de centre ("+str(poly.get(k+1).x)+","+str(poly.get(k+1).y)+"), entre ("+str(ptDecaleFin.x)+","+str(ptDecaleFin.y)+") et ("+str(ptDecaleDebSuiv.x)+","+str(ptDecaleDebSuiv.y)+")"
#          print msgarc

          # on cree un arc et on l'ajoute a la liste
          arc = Arc(poly.get(k+1),ptDecaleFin,ptDecaleDebSuiv)
          self.ajouter(arc)


          
          ptDecaleCourant = ptDecaleDebSuiv
          
        # concave
        elif (angle == -1):
          
          # on renomme les points ici pour plus de lisibilite
          A = poly.get(k)
          B = poly.get(k+1)
          C = poly.get(k+2)
          Ap = ptDecaleCourant
          Bp = poly.calculerPointDecale(k,1,self.rayon)
          
#          print "A"
#          A.afficher()
#          print "B"
#          B.afficher()
#          print "C"
#          C.afficher()
#          print "Ap"
#          Ap.afficher()
#          print "Bp"
#          Bp.afficher()
#          
          
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
          
          if Ap.x != Bp.x:
            if v.x != 0:
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
###          
#          intersec.afficher()
          
          # on finit le segment et on l'ajoute a la liste
          segCourant.B = intersec
          self.ajouter(segCourant)
          
          ptDecaleCourant = intersec
        
        # points alignes
        elif (angle == 0):
          # on ajoute le point du bout du segment
          ptDecaleFin=poly.calculerPointDecale(k,1,self.rayon)
###
#          ptDecaleFin.afficher()
          
          # on finit le segment et on l'ajoute a la liste
          segCourant.B = ptDecaleFin
          self.ajouter(segCourant)
          
          # au tour d'apres, on va recalculer le point decale qui sera le meme que le dernier
          ptDecaleCourant = ptDecaleFin
        
        # impossible:
        else:
          print "ERREUR : type d'angle impossible"
        
      # !!! ATTENTION ICI, on suppose que le dernier angle est convexe. Il faut aussi traiter le cas concave !!!
      # Tout a la fin, on ajoute l'arc de cercle entre le dernier point decale et le premier


#      msgarc="Arc de cercle de centre ("+str(poly.get(0).x)+","+str(poly.get(0).y)+"), entre ("+str(ptDecaleCourant.x)+","+str(ptDecaleCourant.y)+") et ("+str(ptDecalePremier.x)+","+str(ptDecalePremier.y)+")"
      
#      print msgarc
      
      # on cree l'arc et on l'ajoute a la liste
      arc = Arc(poly.get(0),ptDecaleCourant,ptDecalePremier)
      self.ajouter(arc)
      
        
    else:
      print "ERREUR : polygone tchernobyl"
  
 
      

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

#    # M:
#    poly.ajouter(Point2D(0,0))
#    poly.ajouter(Point2D(0,4))
#    poly.ajouter(Point2D(2,2))
#    poly.ajouter(Point2D(4,4))
#    poly.ajouter(Point2D(4,0))

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


    # Cas pathologique si le rayon est trop grand (superieur a 0.35 ici), les  :
    poly.ajouter(Point2D(0,0))
    poly.ajouter(Point2D(0,5))
    poly.ajouter(Point2D(0.7,5))
    poly.ajouter(Point2D(0.7,0))
    poly.ajouter(Point2D(1.4,0))
    poly.ajouter(Point2D(1.4,7))
    poly.ajouter(Point2D(2.1,7))
    poly.ajouter(Point2D(2.1,-1))

    
    

    print ""
    print "Polygone :"
    print ""
    poly.afficher()

#    poly.calculerPointDecale(0,0,1).afficher()
    fraise = Fraisage(0.3) # rayon de 0.3cm
    print ""    
    print "Instructions :"
    fraise.calculerInstructions(poly)
    print ""
    fraise.afficherInstructions()
    print""

if __name__ == "__main__":
    main()

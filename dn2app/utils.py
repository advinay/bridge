from flask_table import Table, Col

from sqlalchemy import desc

from dn2app.models import Equipe,Rencontre,tirage,init_db

import random
import pandas as pd

# Declare your table
class ItemTable(Table):
  nom = Col('Nom')
  score = Col('Score')

def load_equipe():

  items = Equipe.query.order_by(desc(Equipe.score)).all()
  table = ItemTable(items)

  return table

class ItemRencontre(Table):

  tour=Col('Tour')
  equipe1=Col('Equipe1')
  equipe2=Col('Equipe2')
  score1=Col('Score1')
  score2=Col('Score2')


def load_rencontres():

  items=Rencontre.query.all()
  table = ItemRencontre(items)

  return table



def tirage_global(db):

  for rencontre in Rencontre.query.all():
    tirage(rencontre,db)

  results=load_equipe()
  rencontres=load_rencontres()

  return(results,rencontres)

def stats(db):

  for i in range(10):

    (results,rencontres)=tirage_global(db)
    print(results.nom,results.score)

    # for equipe in Equipe.query.all():

    #   results[equipe.nom]=equipe.score

    # df=pd.DataFrame.from_dict(results,orient="index")

    # print (df)


















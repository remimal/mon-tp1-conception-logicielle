from datetime import datetime
import pytz
import logging
import os
import requests


def get_fichier_sortie_args():
    import sys
    if len(sys.argv) > 1:
        return sys.argv[1]
    return ".log"

def get_fichier_sortie_env():
    from dotenv import load_dotenv
    load_dotenv()
    if os.environ["CHEMIN_FICHIER_LOG"] is not None:
        return os.environ["CHEMIN_FICHIER_LOG"]
    return ".log"

def get_fichier_sortie():
    return get_fichier_sortie_env()


def get_time(timezone):
    if timezone is None:
        logging.error("aucune timezone n'a été renseignée")
        raise ValueError("aucune timezone n'a été renseignée")
    tz=pytz.timezone(timezone) 
    logging.debug(f"Demande d'heure sur le timezone : {tz}")
    datetime_tz=datetime.now(tz)
    return "Heure de " + timezone + " " + datetime_tz.strftime("%H:%M:%S")


def get_product(barcode: str)-> dict:
    url=f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    logging.info(f"recherche du produit {barcode}")
    response = requests.get(url)
    data=response.json()
    return data


# s'execute avec :
# uvicorn main:app --reload
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# if __name__=="__main__":

    # logging.basicConfig(filename=get_fichier_sortie(), encoding='utf-8', level=logging.DEBUG)
    # logging.info(f"Lancement du traitement")

    # print(get_time('Indian/Reunion'))
    # print(get_time('Europe/Paris'))
    # print(get_time(None))

    # print(get_product("8000500273296"))

   
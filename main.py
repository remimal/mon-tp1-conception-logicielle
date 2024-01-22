from datetime import datetime
import pytz
import logging

def get_time(timezone):
    if timezone is None:
        logging.error("aucune timezone n'a été renseignée")
        raise ValueError("aucune timezone n'a été renseignée")
    tz=pytz.timezone(timezone) 
    logging.debug(f"Demande d'heure sur le timezone : {tz}")
    datetime_tz=datetime.now(tz)
    return "Heure de " + timezone + " " + datetime_tz.strftime("%H:%M:%S")

if __name__=="__main__":

    logging.basicConfig(filename=".log", encoding='utf-8', level=logging.DEBUG)
    logging.info(f"Lancement du traitement")

    print(get_time('Indian/Reunion'))
    print(get_time('Europe/Paris'))
    print(get_time(None))


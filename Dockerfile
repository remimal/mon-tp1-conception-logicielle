# On part d'un environnement ubuntu 22.04, connu.
FROM ubuntu:22.04
# on installe python comme sur un ubuntu
RUN apt-get update && apt-get install -y python3-pip
# On copie les fichier de notre projet dans le zip
COPY . .
# On installe les dépendances du fichier requirements.txt qui est dans notre projet dans l'image
RUN pip install -r requirements.txt
# On lance notre application
CMD ["python","main.py"]
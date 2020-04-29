# Asennusohje

## Lataa sovellus GitHubista 

Kirjoita komentoriville:

```
git clone https://github.com/puuro-maria/artikkelitietokanta
cd artikkelitietokanta
```

![alt-text](https://media3.giphy.com/media/TlK63EA6F1qRb7lll6M/200w.webp?cid=ecf05e471e3fb2ff39279dcb6e81ba1c3d381a8e959f0c15&rid=200w.webp)

## Lataa riippuvuudet

Kun olet kloonannut sovelluksen tiedostot Githubista, kirjoita komentoriville:

```
source venv/bin/activate
pip install -r requirements.txt
```

## Käynnistä sovellus

Käynnistä sovellus kirjoittamalla komentoriville: 

```
python run.py
```

Nyt sovellukseen on luotu tietokanta ja sovellus on käytettävissä selaimella osoitteessa [http://127.0.0.1:5000/](http://127.0.0.1:5000/) tai [http://localhost:5000/](http://localhost:5000/).


## Pääkäyttäjän (admin) oikeudet

Pääkäyttäjäoikeuksia ei luonnollisesti voi lisätä itselleen rekisteröityessä. Pääkäyttäjäoikeudet saat myönnettyä suoraan sqlite3:n kautta. 

Avaa ensin tietokanta seuraavalla komennolla:

```
sqlite3 application/artikkelit.db
```

Sitten päivitä account-tauluun pääkäyttäjäoikeudet seuraavalla komennolla (alla myönnetään admin-oikeudet käyttäjänimelle "nimimerkki"):

```
UPDATE account SET isadmin = 1 WHERE username = 'nimimerkki';
```

Pääkäyttäjällä on oikeus katsella koko artikkelitietokantaa ja poistaa artikkeleita, muuttaa niiden lähteitä ja merkitä luetuksi. 

## Sovelluksen vieminen pilveen

Sovelluksen voi viedä pilveen. Projektissa on konfiguraatiotiedostot, jotta sovelluksen voi viedä Herokuun. [Yksityiskohtaiset ohjeet sovelluksen viemiseen Herokuun](https://devcenter.heroku.com/articles/git)

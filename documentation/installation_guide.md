# Asennusohje

## Lataa sovellus GitHubista

Kirjoita komentoriville:

```console
git clone https://github.com/puuro-maria/artikkelitietokanta
cd artikkelitietokanta
```

## Lataa riippuvuudet

Kun olet kloonannut sovelluksen tiedostot Githubista, kirjoita komentoriville:

```console
pip install -r requirements.txt
```

## Käynnistä sovellus

Käynnistä sovellus kirjoittamalla komentoriville: 

```console
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


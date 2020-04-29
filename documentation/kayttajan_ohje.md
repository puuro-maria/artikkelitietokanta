# Käyttäjän ohje Artikkelitietokantaan

## Käyttöliittymä

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/kayttoliittyma.png)

## Rekisteröityminen

Rekisteröityminen tapahtuu etusivulla klikkaamalla **Sign up** nappia. 

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/register.png)

Käyttäjältä pyydetään:

- nimimerkki (username)

- nimi (name)

- salasana (password)

- toista salasana (repeat password).

Kun käyttäjä on syöttänyt tarvittavat kentät, sovellus luo uuden tunnuksen kun painaa **Register** nappia.

## Sisäänkirjautuminen

Sisäänkirjautuminen tapahtuu klikkaamalla yläpalkista **Sign in** nappia. Sovellus pyytää nimimerkin ja salasanan.

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/login.png)

## Uuden teoksen lisääminen

Uuden artikkelin/teoksen lisääminen tapahtuu klikkaamalla **Add an article** nappia. 

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/addArticle.png)

Sovellus pyytää käyttäjältä:

- artikkelin otsikon (title)

- kirjoittajat (authors), jotka erotellaan toisistaan pilkulla

- julkaisijan (publisher)

- avainsanat (keywords), jotka erotellaan toisistaan pilkulla

- julkaisuvuoden (year published)

- lähteen (source).

Klikkaamalla **Add an article** nappia sovellus luo uuden artikkelin käyttäjän omalle listalle.

## Teosten tarkastelu

Käyttäjä voi tarkastella omia artikkeleitaan klikkaamalla yläpalkista **List articles** nappia. Tällöin avautuu lista kaikista käyttäjän artikkeleista. 

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/listYourArticles.png)

Listalla voit:

- vaihtaa artikkelin lähdettä (esim. uusi linkki) kirjoittamalla uuden lähteen tekstikenttään ja klikkaamalla **Change source** nappia.

- merkitä teoksen luetuksi klikkaamalla **Mark as read** nappia.

- poistaa teoksen klikkaamalla **Delete this article** nappia.

Näkymään aukeaa myös lista lukemattomista artikkeleista ja artikkelien lukumäärä kirjoittajittain.

## Koko tietokannan tarkastelu admin-oikeuksilla

Pääkäyttäjä (admin) voi tarkastella ja muokata koko tietokantaa klikkaamalla yläpalkin nappia **List all articles in database**.

## Teosten hakeminen

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/search.png)

Teoksia voi hakea tietokannasta:

- teoksen nimellä

- kirjoittajan nimellä

- julkaisijalla

- avainsanoilla.

Haku tapahtuu yläpalkissa syöttämällä hakusana *Search*-tekstikenttään ja klikkaamalla **Search**. Kaikki haetulla sanalla löytyvät hakutunnukset avautuvat näkymään.

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/searchResults.png)

## Oman tilin hallinnointi

Käyttäjä voi hallita omaa tiliään. Tämä tapahtuu yläpalkin napista **Manage my account**. 

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/manageMyAccount.png)

Käyttäjä pystyy:

- muuttamaan salasanan

- poistamaan tilin.

Kun käyttäjätili poistetaan, myös kyseisen käyttäjän kaikki artikkelit poistetaan samalla tietokannasta. Pääkäyttäjä pystyy tekemään yllämainitut toimenpiteet kaikille artikkelitietokannan käyttäjätileille **Manage accounts** -painikkeesta.

![alt-text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/manageAccounts.png)

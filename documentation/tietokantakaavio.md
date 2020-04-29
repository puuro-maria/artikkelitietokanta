# Tietokannan arkkitehtuuri 

## Tietokantakaavio

![alt.text](https://github.com/puuro-maria/artikkelitietokanta/blob/master/documentation/kuvat/ATK_Tietokantakaavio.PNG)

## Tietokannan CREATE TABLE -lauseet

- Käyttäjätilin taulu *account*

```sql
   CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        isadmin BOOLEAN NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (isadmin IN (0, 1))
  );
  ```
  
- Artikkelitaulu *artikkeli* 
  
  ```sql
  CREATE TABLE artikkeli (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        publisher VARCHAR(144) NOT NULL, 
        source VARCHAR(144) NOT NULL, 
        year INTEGER NOT NULL, 
        read BOOLEAN NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (read IN (0, 1)), 
        FOREIGN KEY(account_id) REFERENCES account (id)
  );
  ```
  
- Kirjoittajan taulu *author* ja liitostaulu artikkelien ja kirjoittajien välillä *articleauthor*
  
  ```sql
  CREATE TABLE author (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
  );
  
  CREATE TABLE articleauthor (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        article_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(article_id) REFERENCES artikkeli (id),
        FOREIGN KEY(author_id) REFERENCES author (id)
  );
  
  ```
  
- Avainsanojen taulu *keyword* ja avainsanojen ja artikkelien liitostaulu *articlekeyword*
  
  ```sql
  
  CREATE TABLE keyword (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
   );
  
  CREATE TABLE articlekeyword (
        date_created DATETIME, 
        date_modified DATETIME, 
        id INTEGER NOT NULL, 
        article_id INTEGER, 
        keyword_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(article_id) REFERENCES artikkeli (id), 
        FOREIGN KEY(keyword_id) REFERENCES keyword (id)
  );
  
  ```

# Käyttötapaukset ja niihin liittyvät SQL-kyselyt

- [x] Käyttäjä voi luoda tunnuksen

    - [x] Valitaan uniikki nimimerkki ja käyttäjän valitsema salasana
    
    ```sql
    INSERT INTO account (id, username, name, password, isadmin) 
        VALUES (1, 'käyttäjätunnus', 'käyttäjän nimi', 'salaSana', 0);
    ```

- [x] Käyttäjä voi kirjautua sisään järjestelmään

- [x] Käyttäjä voi lisätä uuden teoksen tietokantaan

    ```sql
    INSERT INTO artikkeli (id, name, publisher, year, source, read)
        VALUES (1, 'Artikkelin otsikko', 'Julkaisija', 2020, 'www.googlescholar.com/artikkeli', 0);
        
    INSERT INTO articleauthor (id, article_id, author_id) 
        VALUES (1, 1, 1),
        (2, 1, 2)
        (3, 1, 3);
        
    INSERT INTO author (id, name)
        VALUES (1, 'Kirjailija Yksi'),
        (2, 'Kirjailija Kaksi'),
        (3, 'Kirjailija Kolme');
    ```

- [x] Käyttäjä voi jälkikäteen muuttaa teoksen sijaintia (jos esim. linkki pdf-tiedostoon muuttuu)

    ```sql
    UPDATE artikkeli SET source = 'www.googlescholar.com/uusisijainti'
        WHERE artikkeli.id = 1;
    ```

- [x] Käyttäjä voi merkata teoksen luetuksi

    ```sql
    UPDATE artikkeli SET read = 1
        WHERE artikkeli.id = 1;
    ```

- [x] Käyttäjä voi hakea artikkeleita:

    - [x] avainsanalla

    - [x] artikkelin nimellä

    - [x] julkaisijan nimellä

    - [x] kirjoittajan nimellä
    
    ```sql

    SELECT * FROM author
        INNER JOIN articleauthor ON author.id = articleauthor.author_id
        INNER JOIN artikkeli ON artikkeli.id = articleauthor.article_id
        INNER JOIN articlekeyword ON artikkeli.id = articlekeyword.article_id
        INNER JOIN keyword ON keyword.id = articlekeyword.keyword_id
            WHERE (author.name LIKE '%hakusana%') OR 
            (artikkeli.name LIKE '%hakusana%') OR
            (artikkeli.pulisher LIKE '%hakusana%') OR
            (keyword.name LIKE '%hakusana%');
     ```
     
     Sovelluksessa tulokset näkyvät yo. kyselystä huolimatta niin, että duplikaattiartikkeleita ei tule, vaan avainsanat ja kirjailijat listataan samalle riville artikkelin kanssa. 

- [x] Käyttäjä voi poistaa artikkelin omasta kannastaan halutessaan

    ```sql
    DELETE FROM artikkeli WHERE id = 1;
    
    DELETE FROM articleauthor WHERE article_id = 1;
    
    DELETE FROM articlekeyword WHERE article_id = 1;
    ```

- [x] Käyttäjä voi kirjautua ulos

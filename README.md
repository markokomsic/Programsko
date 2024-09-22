# ZOO Management APP koncept

1. Nastambe
Vrste: Mračne, Grijane, Osunčane
Atributi: Broj (PK), Vrsta, Ime (opcionalno), Centralna tačka, Geometrijski opis (bonus)
Infrastruktura: Biljke, stabla, Sekundarne životinje (kukci, mravi), Evidencija prisutnosti (slučajno ili namjerno)
Povijest: Soft delete (arhiviranje povijesnih podataka)
2. Životinje
Vrsta: Hrvatski, Latinski, Engleski naziv
Atributi: Vrsta, Ime, ID, Broj (za skupne životinje)
Povezanost s Nastambama: Jedna životinja u jednoj nastambi; jedna nastamba može imati više vrsta životinja
Evidencija: Porijeklo (kupovina, donacija, rođenje u ZOO-u), Datum nastanka, Arhiviranje umrlih životinja
Obaveze: Vrsta (npr. hranjenje), Status (obavljeno, zakazano), Datum, Komentari, Planiranje periodičnih obaveza, Provjera kalendara
3. Radnici
Atributi: Ime, Prezime, Kontakt, Obrazovanje, Sposobnost (kvalificiranost)
Kalendar Rada: Godišnji odmori, Bolovanja, Dostupnost, Rok trajanja kvalifikacija (ako su vremenski ograničene)
Troškovi: Radni sati, Trošak radnika
4. Troškovi i Posjeti
Troškovi: Povezivanje s životinjama, Trošak materijala
Grupne Posjete: Evidencija, Određivanje vodiča (kvalificirani i dostupni radnik)
Nezgode: Vrsta, Utjecaj, Nastambe i životinje uključene, Komentari, Troškovi sanacije
5. Izvještaji
Generiranje: Troškovi po životinjama, Troškovi po dobavljačima, Histogram radnih sati
---
## Pokretanje projekta
### 1. Klonirajte repozitorij:
    git clone https://github.com/markokomsic/Programsko.git
    cd Programsko
### 2. Instalirajte pipenv
    pip install pipenv
### 3. Kreirajte virtualno okruženje i instalirajte ovisnosti
    pipenv install --dev
### 4. Aktivirajte virtualno okruženje
    pipenv shell
### 5. Migrirajte bazu podataka
    python manage.py migrate
### 6. Pokrenite razvojni server
    python manage.py runserver

## Do testów została użyta aplikacja internetowa (https://blazedemo.com), w której testowane były trzy fukcjonalności rezerwację, zakup i potwierdzenie zamówienia.

/reserve.php - Rezerwacja <br />
/purchase.php - Zakup <br />
/confirmation.php - Potwierdzenie <br />

## Parametry testów <br />

Scenariusz 1: 1000 użytkowników, ramp-up 20 sekund <br />
| /reserve.php: | 770 r/s, | średni czas odpowiedzi 8.791s, | błąd 859 | <br />
| /purchase.php: | 879 r/s,| średni czas odpowiedzi 10.399s,| błąd 330 | <br />
| /confirmation.php: | 885 r/s, | średni czas odpowiedzi 8.117s, | błąd 333 | <br />
Ogółem:  3000 użytkowników, | średni czas odpowiedzi 8.769s, | błąd 483 | <br />

Scenariusz 2: 100 użytkowników, ramp-up 20 sekund <br />
| /reserve.php: | 770 r/s, | średni czas odpowiedzi 0.429s, | błąd 400 | <br />
| /purchase.php: | 879 r/s, | średni czas odpowiedzi 0.32s, | błąd 290 | <br />
| /confirmation.php: | 885 r/s, | średni czas odpowiedzi 0.334s, | błąd 310 | <br />
Ogółem: 300 użytkowników, | średni czas odpowiedzi 0.361s, | błąd 345 | <br />

## Analiza wyników <br />

Scenariusz 1 (1000 użytkowników) <br />
Aplikacja zaczęła wykazywać anomalia przy 1000 użytkowników, gdzie średni czas odpowiedzi znacznie wzrósł (8.769s), a liczba błędów wyniosła 483. <br /> Aplikacja prawdopodobnie zaczęła zwalniać i nie odpowiadać efektywnie na tak dużą liczbę żądań.

Scenariusz 2 (100 użytkowników) <br />
Przy mniejszym obciążeniu (100 użytkowników) aplikacja działała znacznie efektywniej, ze średnim czasem odpowiedzi wynoszącym 0.361s i niewielką liczbą błędów (345). <br /> Aplikacja wydaje się być w stanie obsłużyć to obciążenie.

## Wnioski <br />
Aplikacja wydaje się działać poprawnie do pewnego stopnia obciążenia. W przypadku 100 użytkowników, jej wydajność była zadowalająca. <br />
W scenariuszu z 1000 użytkownikami pojawiły się znaczne problemy z wydajnością, co objawiało się znacznym wzrostem średniego czasu odpowiedzi i liczbą błędów. <br />
Długi czas odpowiedzi i duże ilości błędów mogą wskazywać na problemy z infrastrukturą, konieczność optymalizacji kodu aplikacji lub zasobami serwera. <br />

*Graph Results - 100 users*
![100u_Graph_Results.png](screenshots/100u_Graph_Results.png)

*View Results in Table - 100 users*
![100u_View_Results_in_Table.png](screenshots/100u_View_Results_in_Table.png)

*Aggregate Report - 100 users*
![100u_Aggregate_Report.png](screenshots/100u_Aggregate_Report.png)

*Graph Results - 1000 users*
![1000u_Graph_Results.png](screenshots/1000u_Graph_Results.png)

*View Results in Table - 1000 users*
![1000u_View_Results_in_Table.png](screenshots/1000u_View_Results_in_Table.png)

*Aggregate Report - 1000 users*
![1000u_Aggregate_Report.png](screenshots/1000u_Aggregate_Report.png)

# IN2010 Innlevering 3 halvorin

## Bygg grafen

#### deloppgave 1

implementert i `populateGraph.GraphBuilder.java`.

#### deloppgave 2

implementert i `printGraphSize.GraphBuilder.java`.
Siden denne løsningen har filmer som egne noder, har den betydelig færre kanter.
Om en film har N kanter, vil det i denne implementasjonen finnes et Movie-objekt med N kanter, mens det i implementasjonen uten Movie-noder vil være totalt `N*(N-1)/2` kanter mellom skuespillerne i filmen.
Denne formelen går imidlertidig ikke opp med programmets output uten videre; i denne implementasjonen telles filmer med 1 skuespiller som å ha 1 kant.
I implementasjonen uten Movie-noder ville dette tilsvare en kant fra en skuespiller til ingenting. Om vi filtrerer ut disse får vi 751931 kanter, og om vi for hver av disse filmene med mer enn 1 skuespiller plugger inn N i formelen `N*(N-1)/2` for å regne ut ekvivalente kanter i løsningen som vises i oppgaveteksten får vi 5342530 kanter.

## Six Degrees of IMDB

# IN2010 oblig 2 - halvorin

## effektive mengder

både det binære søketreet og avl-treet er kjørbart med `effektive_mengder/main.py`.
For å endre om programmet kjører med binært søketre eller avl-tre, endre structure-variabelen i `main.py` til å enten være et objekt av typen `BinarySearchTree[int]` eller `AvlTree[int]`.

_alle input-filene består av integers, men programmet skal i teorien håndtere alle andre sorterbare typer._

## binære søketrær

#### oppgave a

- pseudokode:

```
INPUT: et sortert array A av lengde n
OUTPUT: et array B i rekkkefølge som gir et balansert søketre

Procedure Balance(A):
    if |A| <=1:return A
    middle ← ⌊n/2⌋
    left ← Balance(A[0...middle-1])
    right ← Balance(A[middle+1...n])
    Return [left + A[middle]+right]
```

- kjørbar i `balanserte_soeketraer/oppgave_a.py`

#### oppgave b

- pseudokode:

```
INPUT: en sortert heap A av lengde n
OUTPUT: skriver ut elementene i A i rekkefølge som gir et balansert søketre

Procedure Balance(A):
    if |A| is 1: print pop(A)
    else:
        left ← empty heap
        middle ← ⌊n/2⌋
        count ← 0
        while count < middle:
            left ← pop(A)
            count++
        print(pop(A))
        Balance(left)
        right ← A
        Balance(right)
```

- kjørbar i `balanserte_soeketraer/oppgave_b.py`

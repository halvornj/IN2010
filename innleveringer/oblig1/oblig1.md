# IN2010 oblig 1 - halvorin

## Teque

(a)
pseudokode for en array-basert implementasjon, `collection[]`

```
function push_back(element)
   collection.append(element)

```

```
function push_front(element)
   collection.insert(0,element)

```

```
function push_middle(element)
   collection.insert(⌊|collection|/2⌋, element)

```

```
function get(index)
   print(collection[index])
```

b)
kjørbar i `python3 teque/teque.py`

c)

- push_back(): enkel tilordning. O(1)
- push_front():enkel tilordning. O(1)
- push_middle(): enkel tilordning. O(1)
- get(): oppslag i array. O(1)

d) med ubegrenset input-størrelse kan vi redusere konstanter, som 10^6^ til 1. **_TODO_**

## Sortering

MergeSort og InsertionSort er implementert i hhv. `sortering/python-src/merge.py` og `sortering/python-src/insertion.py`, og csv-filene genereres med `python3 sortering/python-src/main.py [FILENAME]`.

_grafer kan plottes vha. plotter.py i samme mappe. programmet tar sti til en .csv som argument, men aksetitler mm. må konfigureres i filen_

### spørsmål fra eksperimenter

- Q: I hvilken grad stemmer kjøretiden overens med kjøretidsanalysene (store
  O) for de ulike algoritmene?

  A: ![graph of time/n for insertion- and merge-sort](sortering/output_graphs/tid_n_100.png "tid/elementer for merge- og insertion-sort")

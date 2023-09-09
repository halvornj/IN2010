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

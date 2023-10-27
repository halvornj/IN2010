import java.util.LinkedList;

//making this spesifically for Integer, to make generation of the full array easier. (harder to do for generic E)
public class Set<Integer> {
    // * abstract - HashSet needs to be a map still, but the key is irrelevant/not
    // * supplied.
    // * using linear probing, because i've already implemented a hashmap w/
    // * separate chaining as practice.

    Object[] array;
    int size;
    int capacity;

    public Set(int initialCapacity) {
        array = new Object[initialCapacity];
        capacity = initialCapacity;
    }

    public Set() {
        // guessing at initial capacity 10
        array = new Object[10];
        capacity = 10;
    }

    public void insert(Object val) {
        if ((double) size / (double) capacity > 0.75) {
            rehash();
        }
        int hash = Hash(val, capacity);
        int position = hash;
        while (array[position] != null) {
            if (array[position] == val) {
                // already in set
                return;
            }
            position = (position + 1) % capacity;
        }

        array[position] = val;
        size++;
    }

    private void rehash() {
        Object[] oldArray = array.clone();
        capacity *= 2;
        size = 0;
        array = new Object[capacity];
        for (Object o : oldArray) {
            if (o != null) {
                insert(o);
            }
        }
    }

    public boolean contains(int val) {
        int hash = Hash(val, capacity);
        int position = hash;

        if (array[position] == null) {
            return false;
        }

        if ((int) array[position] == val) {
            return true;
        }
        position = (position + 1) % capacity;
        while (position != hash) {// while we haven't made a full revolution
            if (array[position] == null) {
                return false;
            }
            if ((int) array[position] == val) {
                return true;
            }
            position = (position + 1) % capacity;
        }
        return false;
    }

    public void remove(int val) {
        size--;
        int hash = Hash(val, capacity);
        int position = hash;
        if (array[position] == null) {
            // element wasn't in set
            size++;
            return;
        }
        if ((int) array[position] == val) {
            array[position] = null;
            fillGap(position);
            return;
        }
        position = (position + 1) % capacity;
        while (position != hash) {// while not a full revolution
            if (array[position] == null) {
                size++;
                return;
            }
            if ((int) array[position] == val) {
                array[position] = null;
                fillGap(position);
                return;
            }
            position = (position + 1) % capacity;
        }
    }

    private void fillGap(int position) {
        int originalPosition = position;
        position = (position + 1) % capacity;
        Object current = array[position];
        if (current == null) {
            return;
        }
        while (Hash(current, capacity) > originalPosition) {
            position = (position + 1) % capacity;
            current = array[position];
            if (current == null) {
                return;
            }
        }
        array[originalPosition] = array[position];
        array[position] = null;
        fillGap(position);

    }

    public int size() {
        return size;
    }

    // siden oppgaven bare bruker int jukser jeg og parser val til int.
    // alternativt kunne man da finne en hex-val og hashet den.
    public static int Hash(Object val, int n) {
        return ((int) val * 31) % n;
    }
}
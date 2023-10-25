import java.util.LinkedList;

public class HeshMep<K, V> {
    LinkedList<Tuple<K, V>>[] buckets;
    int size;
    int capacity;

    @SuppressWarnings("unchecked")
    public HeshMep(int initialCapacity) {
        buckets = new LinkedList[initialCapacity];
        capacity = initialCapacity;
    }

    @SuppressWarnings("unchecked")
    public HeshMep() {
        // guess at initialSize
        buckets = new LinkedList[10];
        capacity = 10;
    }

    public void put(K key, V value) {
        size++;
        // todo rehash on size/capacity > 0.75
        if (size / capacity > 0.75) {
            System.err.println("rehashing");
            rehash();
        }

        int hash = Hesh(key, capacity);
        LinkedList<Tuple<K, V>> bucket = buckets[hash];
        Tuple<K, V> tuple = new Tuple<K, V>(key, value);
        if (bucket == null) {
            System.err.println("creating bucket for key " + key);
            bucket = new LinkedList<Tuple<K, V>>();
            buckets[hash] = bucket;
            bucket.add(tuple);
            return;
        }
        for (Tuple<K, V> found : bucket) {
            if (found.getFirst().equals(key)) {
                System.err.println("found key, replacing " + key);
                found = tuple;
                size--;
                return;
            }
        }
        System.err.println("adding key " + key + " to already existing bucket");
        bucket.add(tuple);
    }

    @SuppressWarnings("unchecked")
    private void rehash() {
        capacity *= 2;

        LinkedList<Tuple<K, V>>[] oldBuckets = buckets.clone();
        buckets = new LinkedList[capacity];
        size = 0;
        for (LinkedList<Tuple<K, V>> bucket : oldBuckets) {
            if (bucket == null) {
                continue;
            }
            for (Tuple<K, V> tuple : bucket) {
                put(tuple.getFirst(), tuple.getSecond());

            }
        }
    }

    public V get(K key) {
        int hash = Hesh(key, capacity);
        LinkedList<Tuple<K, V>> bucket = buckets[hash];
        for (Tuple<K, V> found : bucket) {
            if (found.getFirst().equals(key)) {
                return found.getSecond();
            }
        }
        return null;
    }

    public void remove(K key) {
        int hash = Hesh(key, capacity);
        LinkedList<Tuple<K, V>> bucket = buckets[hash];
        // må ha selve Tuple-objektet for å fjerne det, så itererer for å finne
        if (bucket == null) {
            System.err.println("ay caramba");
            return;
        }
        for (Tuple<K, V> found : bucket) {
            if (found.getFirst().equals(key)) {
                bucket.remove(found);
                size--;
                return;
            }
        }

    }

    public static int Hesh(Object val, int n) {
        String value = (String) val.toString();
        int total = 0;
        for (int i = 0; i < value.length(); i++) {
            total = value.charAt(i) * 31 + total;
        }
        return total % n;
    }

    public int size() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }

    @Override
    public String toString() {
        String full = "{\n";
        for (LinkedList<Tuple<K, V>> bucket : buckets) {
            if (bucket == null) {
                continue;
            }
            for (Tuple<K, V> tuple : bucket) {
                full += (tuple.toString() + "\n");
            }
        }
        return (full + "} (size: " + size + ", capacity: " + capacity + ")");
    }

    public void errorPrint() {
        System.err.println("bucket count: " + buckets.length);
        for (LinkedList<Tuple<K, V>> bucket : buckets) {
            System.out.println(bucket);
        }
    }
}

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
        if ((size / (double) capacity) > 0.7) {
            System.err.println("rehashing, size=" + size + ", capacity=" + capacity);
            rehash();
        }

        int hash = Hesh(key, capacity);
        LinkedList<Tuple<K, V>> bucket = buckets[hash];
        Tuple<K, V> tuple = new Tuple<K, V>(key, value);
        if (bucket == null) {
            bucket = new LinkedList<Tuple<K, V>>();
            buckets[hash] = bucket;
            bucket.add(tuple);
            return;
        }
        for (Tuple<K, V> found : bucket) {
            if (found.getFirst().equals(key)) {
                found.setSecond(value);
                size--;
                return;
            }
        }
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
        for (LinkedList<Tuple<K, V>> bucket : buckets) {
            System.out.println(bucket);
        }
    }
}

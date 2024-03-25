import java.util.*;

public class LRUCache {
    public static void main(String[] args) {
        final LRUCacheWithLinkedHashMap<Integer,Integer> cache1 = new LRUCacheWithLinkedHashMap<>(3);

        cache1.put(1,10);
        cache1.put(2,20);
        cache1.put(3,30);
        cache1.get(1);
        cache1.put(2,200);
        cache1.print(); // {3=30, 1=10, 2=200}

        final LRUCacheWithExtension<Integer, Integer> cache2 = new LRUCacheWithExtension<>(3);
        cache2.put(1,10);
        cache2.put(2,20);
        cache2.put(3,30);
        cache2.get(1);
        cache2.put(2,200);
        cache2.print(); // [3=30, 1=10, 2=200]

        final LRUCacheWithMapAndList<Integer, Integer> cache3 = new LRUCacheWithMapAndList<>(3);
        cache3.put(1,10);
        cache3.put(2,20);
        cache3.put(3,30);
        cache3.get(1);
        cache3.put(2,200);
        cache3.print(); // 3=30 1=10 2=200
    }
}

public class LRUCacheWithLinkedHashMap<K,V> {

    private final int capacity;
    private final LinkedHashMap<K,V> cache;

    LRUCacheWithLinkedHashMap(int capacity) {
        this.cache = new LinkedHashMap<K,V>(capacity, 0.75f, true) { // capacity, load factor of ratio of entries to its capacity before resizing, access ordering mode
            @Override
            protected boolean removeEldestEntry(java.util.Map.Entry<K, V> eldest) { // called after insertion
                return cache.size() > capacity;
            }
        };
        this.capacity = capacity;
    }

    public V get(K key) {
        return cache.getOrDefault(key, null);
    }

    public void put(K key, V value) {
        cache.put(key, value);
    }

    public void print() {
        System.out.println(cache);
    }
}

public class LRUCacheWithExtension<K,V> extends LinkedHashMap<K,V> {
    private final int capacity;

    LRUCacheWithExtension(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }

    @Override
    protected boolean removeEldestEntry(java.util.Map.Entry<K,V> eldest) {
        return size() > capacity;
    }

    public void print() {
         System.out.println(entrySet());
    }
}

public class LRUCacheWithMapAndList<K,V> {
    private final int capacity;
    private final Map<K,V> cache;
    private final LinkedList<K> queue;
    
    LRUCacheWithMapAndList(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.queue = new LinkedList<>();
    }

    public V get(K key) {
        if (!cache.containsKey(key)) {
            return null;
        }

        moveToNewest(key);
        return cache.get(key);
    }

    public void put(K key, V value) {
        if (cache.containsKey(key)) {
            removeKey(key);
        } else if (cache.size() >= capacity){
            removeOldest();
        }

        queue.add(key);
        cache.put(key, value);
    }

    public void moveToNewest(K key) {
        queue.remove(key); // remove(value of type k), not to be confused with remove(int) which removes by index
        queue.add(key);
    }

    public void removeKey(K key) {
        queue.remove(key);
        cache.remove(key);
    }

    public void removeOldest() {
        final K key = queue.removeFirst(); // or remove(0) at index 0
        cache.remove(key);
    }

    public void print() {
        queue.forEach(key -> {
            V value = cache.get(key);
            System.out.printf("%s=%s ", key, value);
        });
        System.out.println();
    }
}
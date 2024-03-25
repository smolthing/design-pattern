import java.util.concurrent.atomic.AtomicInteger;

class Concurrency {
    public static void main (String[] args){
        AtomicInteger atomicCounter = new AtomicInteger(0);
        final Counter counter = new Counter(0);

        Thread thread1 = new Thread(() -> {
            for(int i=0;i<10000;i++) {
                counter.increment();
                counter.incrementSynchronously();
                atomicCounter.getAndIncrement();
            }
        });

        Thread thread2 = new Thread(() -> {
            for(int i=0;i<10000;i++) {
                counter.increment();
                counter.incrementSynchronously();
                atomicCounter.getAndIncrement();
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (Exception error) {

        }

        System.out.println("Counter value with race condition: " + counter.getCountRaceCondition());
        // Counter value with race condition: 19958
        System.out.println("Counter value with synchronous increment: " + counter.getCountSynchronously());
        // Counter value with synchronous increment: 20000
        System.out.println("Counter value with atomic integer: " + atomicCounter.get());
        // Counter value with atomic integer: 20000
    }
}

class Counter {
    int counter;
    int fixedCounter;

    Counter(int counter) {
        this.counter = counter;
        this.fixedCounter = counter;
    }

    public void increment() {
        counter += 1;
    }

    public synchronized void incrementSynchronously() {
        fixedCounter += 1;
    }

    public int getCountRaceCondition() {
        return counter;
    }

    public int getCountSynchronously() {
        return fixedCounter;
    }
}
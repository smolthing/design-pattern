class Deadlock {

    public static void main(String[] args) {
        Object object1 = new Object();
        Object object2 = new Object();

        Thread thread1 = new Thread(() -> {
            synchronized (object1) {
                System.out.println("thread1: lock object1");

                try {
                    Thread.sleep(1000);
                } catch (Exception e){
                }

                synchronized (object2) {
                    System.out.println("thread1: get object2");
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            synchronized (object2) {
                System.out.println("thread1: lock object2");
                try {
                    Thread.sleep(1000);
                } catch (Exception e){

                }

                synchronized (object1) {
                    System.out.println("thread2: get object1");
                }
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread1.join();
        } catch (Exception error) {

        }

        System.out.println("done");

    }
}
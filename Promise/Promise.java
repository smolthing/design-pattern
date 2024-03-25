import java.util.concurrent.CompletableFuture;

public class Promise {
    public static void main(String[] args) {
        CompletableFuture<String> future1 = getCompletableFuture1();
        CompletableFuture<String> future2 = getCompletableFuture2();

        future1
            .thenCompose(result -> getCompletableFuture2())
            .thenAccept(result -> {
                System.out.println(result);
            }).join(); // Wait for the future to complete
    }

    static CompletableFuture<String> getCompletableFuture1() {
        return CompletableFuture.supplyAsync(() -> {
            try {
                Thread.sleep(1000); // Simulate a delay of 1 second
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "done1";
        });
    }


    static CompletableFuture<String> getCompletableFuture2() {
        return CompletableFuture.supplyAsync(() -> {
            try {
                Thread.sleep(1000); // Simulate a delay of 1 second
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "done2";
        });
    }
}

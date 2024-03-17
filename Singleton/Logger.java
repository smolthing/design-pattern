import java.time.LocalDateTime;

class Logger {
    private static Logger logger;
    private final String name;

    Logger() {
        this.name = "logger " + LocalDateTime.now();
    }

    public static synchronized Logger getInstance() {
        if (logger == null) {
            logger = new Logger();
        }
        return logger;
    }

    public void log(String message) {
        final String logMessage = String.format("[INFO] %s from %s",message, this.name);
        System.out.println(logMessage);
    }

    public static void main(String[] args) {
        final var logger1 = Logger.getInstance();
        final var logger2 = Logger.getInstance();

        logger1.log("message");
        // [INFO] message from logger 2024-03-17T00:30:28.027467
        logger2.log("message");
        // [INFO] message from logger 2024-03-17T00:30:28.027467
    }
}
# SOLID Principles

## Single Responsibility Principle (SRP)
A class should have only one responsibility.

Example:

```java
public class UserService {
    public void registerUser(User user) {
        // Register the user
    }

    public void sendNotification(User user, String message) {
        // Send notification to the user
    }
}
```
In the above example, UserService handles both user registration and sending notifications. To adhere to SRP, we can split these responsibilities into separate classes.

## Open/Closed Principle (OCP)
Open for extension but closed for modification. Extend a method or class to support more use cases.

Example:

```java
public interface Shape {
    double area();
}

public class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double area() {
        return Math.PI * radius * radius;
    }
}

public class Rectangle implements Shape {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double area() {
        return width * height;
    }
}
```
In the above example, the Shape interface is open for extension, allowing us to create new shapes like circles and rectangles without modifying existing code.

## Liskov Substitution Principle (LSP)
Objects of a superclass(Shape) should be replaceable with objects of its subclasses(Rectangle, Square) without affecting the correctness of the program.

Example:

```java
public class Shape {
    protected double width;
    protected double height;

    public Shape(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double calculateArea() {
        return width * height;
    }
}

public class Rectangle extends Shape {
    public Rectangle(double width, double height) {
        super(width, height);
    }
}

public class Square extends Shape {
    public Square(double sideLength) {
        super(sideLength, sideLength);
    }
}

public class Main {
    public static void printArea(Shape shape) {
        double area = shape.calculateArea();
        System.out.println("Area: " + area);
    }

    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(5, 10);
        Square square = new Square(5);

        printArea(rectangle);  // Output: Area: 50.0
        printArea(square);     // Output: Area: 25.0
    }
}
```
In this example, even though Rectangle and Square have different implementations for calculating area (based on their specific shapes), they can both be used in place of a Shape object without affecting the correctness of the program.

## Interface Segregation Principle (ISP)
The Interface Segregation Principle states that clients should not be forced to depend on interfaces they do not use. It promotes smaller, more specific interfaces over large, general ones.

Example:

```java
// Bad design violating ISP
public interface MediaPlayer {
    void playAudio();

    void playVideo();

    void playImage();
}

public class BasicMediaPlayer implements MediaPlayer {
    @Override
    public void playAudio() {
        System.out.println("Playing audio");
    }

    @Override
    public void playVideo() {
        // Basic media player does not support video
        System.out.println("Video playback not supported");
    }

    @Override
    public void playImage() {
        // Basic media player does not support image
        System.out.println("Image display not supported");
    }
}


// Good design following ISP
public interface AudioPlayer {
    void playAudio();
}

public interface VideoPlayer {
    void playVideo();
}

public interface ImagePlayer {
    void playImage();
}

// Updated implementation
public class BasicMediaPlayer implements AudioPlayer {
    @Override
    public void playAudio() {
        System.out.println("Playing audio");
    }
}

```
In the bad design, clients that only need work behavior are forced to implement eat behavior as well, violating ISP. In the good design, separate interfaces are used for distinct behaviors.

## Dependency Inversion Principle (DIP)
The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details. Details should depend on abstractions.

Example:

```java
// High-level module directly depends on low-level modules
public class NotificationService {
    private EmailService emailService;
    private SMSService smsService;
    private PushNotificationService pushNotificationService;

    public NotificationService() {
        this.emailService = new EmailService();
        this.smsService = new SMSService();
        this.pushNotificationService = new PushNotificationService();
    }

    public void sendNotification(String recipient, String message) {
        emailService.sendEmail(recipient, message);
        smsService.sendSMS(recipient, message); // Here, recipient is used as phone number for SMS (just for demonstration purposes)
        pushNotificationService.sendPushNotification(recipient, message); // Here, recipient is used as device token (just for demonstration purposes)
    }
}

// High-level module depends on abstractions (interfaces)
public class NotificationService {
    private final NotificationChannel emailService;
    private final NotificationChannel smsService;
    private final NotificationChannel pushNotificationService;

    public NotificationService(NotificationChannel emailService, NotificationChannel smsService, NotificationChannel pushNotificationService) {
        this.emailService = emailService;
        this.smsService = smsService;
        this.pushNotificationService = pushNotificationService;
    }

    public void sendNotification(String recipient, String message) {
        emailService.send(recipient, message);
        smsService.send(recipient, message);
        pushNotificationService.send(recipient, message);
    }
}
```
In the above example, NotificationService class no longer directly creates instances of concrete implementations. Instead, it accepts instances of interfaces via its constructor, adhering to the Dependency Inversion Principle.

This approach makes the system more flexible and maintainable. We can easily swap out different implementations of different services wtihout modifying NotificationService class.

By following these SOLID principles, developers can create more modular, maintainable, and scalable software systems.


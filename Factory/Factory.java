class VehicleFactory {
    static Vehicle create(VehicleType type) throws Exception{
        if (type == null || type == type.UNKNOWN) {
            throw new Exception("type is required"); 
        }

        switch (type){
            case CAR: return new Car();
            case MOTORBIKE: return new Motorbike();
            case BUS: return new Bus();
            default: return new Car();
        }
    }

    public static void main(String[] args) {
        try {
            final Vehicle vehicle = VehicleFactory.create(VehicleType.BUS);
            vehicle.print();
            final var wheels = vehicle.getNumberOfWheels();
            final var message = String.format("Vehicle type: %s ,has %s wheels.", vehicle.getClass(), wheels);
            System.out.println(message);
            // Vehicle type: class Bus ,has 8 wheels.
        } catch (Exception exception) {
            System.out.println(exception);
        }
    }
}

enum VehicleType {
    UNKNOWN(0), CAR(4), MOTORBIKE(2), BUS(8);
    private final int numberOfWheels;
    
    VehicleType(int numberOfWheels) {
        this.numberOfWheels = numberOfWheels;
    }

    public int getNumberOfWheels() {
        return this.numberOfWheels;
    }
}

interface Vehicle {
    void print();
    int getNumberOfWheels();
}

class Car implements Vehicle {
    @Override
    public void print() {
        System.out.println("car");
    }

    @Override
    public int getNumberOfWheels() {
        return VehicleType.CAR.getNumberOfWheels();
    }
}

class Motorbike implements Vehicle {
    @Override
    public void print() {
        System.out.println("motorbike");
    }
    @Override
    public int getNumberOfWheels() {
        return VehicleType.MOTORBIKE.getNumberOfWheels();
    }
}

class Bus implements Vehicle {
    @Override
    public void print() {
        System.out.println("bus");
    }
    @Override
    public int getNumberOfWheels() {
        return VehicleType.BUS.getNumberOfWheels();
    }
}

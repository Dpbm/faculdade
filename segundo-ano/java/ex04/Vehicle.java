package vehicle;

public class Vehicle{
    private String brand, model, color, licensePlate;
    public Vehicle(String brand, String model, String color, String licensePlate){
        this.brand = brand;
        this.model = model;
        this.color = color;
        this.licensePlate = licensePlate;
    }

    public String getLicensePlate(){
        return this.licensePlate;
    }
}
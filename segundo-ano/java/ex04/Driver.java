package driver;

import vehicle.Vehicle;

public class Driver{
    private String cnh, category, name;
    private Vehicle car;

    public Driver(String cnh, String category, String name){
        this.cnh = cnh;
        this.category = category;
        this.name = name;
    }

    public String getCNH(){
        return this.cnh;
    }

    public String getCategory(){
        return this.category;
    }

    public String getName(){
        return this.name;
    }

    public Vehicle getVehicle(){
        return this.vehicle;
    }

    public void setVehicle(Vehicle vehicle){
        this.vehicle = vehicle;
    }
}
import driver.Driver;
import vehicle.Vehicle;

public class Main{
    public static void main(String[] args){
        Driver driver = new Driver("11111111", "A", "alaaa");
        Vehicle vehicle = new Vehicle("11112", "teste", "outros", "verde");
        driver.setVehicle(vehicle);
        System.out.println(driver.getVehicle().getLicensePlate());
    }
}
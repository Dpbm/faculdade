package manufacturer;

public class Manufacturer{
  private String name, address, phone;
  
  public Manufacturer(String name, String address, String phone){
    this.name = name;
    this.address = address;
    this.phone = phone;
  }

  public void setPhone(String phone){
    this.phone = phone;
  }

  public String getPhone(){
    return this.phone;
  }
}

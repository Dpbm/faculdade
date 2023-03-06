public class Ex02{
  public static Scanner console = new Scanner(System.in);

  public static void main(String[] args){
    char sex = getSex();
    float height = getHeight();
    float idealWeight = getIdealWeightBySexAndHeight(sex, height);
    Sysmtem.out.println("Seu peso ideal éÇ %.2f\n", idealWeight);
  }

  public static char getSex(){
    System.out.print("Seu sexo[F/M]: ");
    String inputSex = console.next();
    char sex = inputSex.toUpperCase().charAt(0);
    return sex;
  }

  public static float getHeight(){
    System.out.print("Sua altura: ");
    float height = console.nextFloat();
    return height;
  }

  public static float getIdealWeightBySexAndHeight(char sex, float height){
    if(sex == 'M'){
      return idealWeightMale(height);
    }
  
    return idealWeightFeMale(height);
  }

  public static float idealWeightMale(float height){
    return 72.7f * height - 58;
  }

  public static float idealWeightFeMale(float height){
    return 62.1f * height - 44.7f;
  }

}

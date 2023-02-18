public class Case{
  public static void main(String[] args){
    char value = 'a';

    switch (value) {
      case 'a': System.out.println("Hello world!");
        break;

      case 'b': System.out.println("Other");
        break;

      default:
        System.out.println("None");
    }
  }
}

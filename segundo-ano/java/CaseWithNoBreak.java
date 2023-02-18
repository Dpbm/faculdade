public class CaseWithNoBreak{
  public static void main(String[] args){
    char value = 'b';

    switch (value) {
      case 'a':
        System.out.println("Hello world!");      
      case 'b':
        System.out.println("Other");
      default:
        System.out.println("None");
    }
  }
}

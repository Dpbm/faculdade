import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListTest{
  public static void main(String[] args){
    Scanner console = new Scanner(System.in);
    ArrayList<Integer> numbers = new ArrayList<Integer>();

    int total = console.nextInt();

    for(int i = 0; i < total; i++)
      numbers.add(console.nextInt());
    System.out.println(numbers);
    for(Integer n: numbers)
      System.out.print(n + " -> ");
    numbers.remove(2);
    System.out.println("size: " + numbers.size());
    System.out.println(numbers);
    System.out.println("1 --> "+ numbers.get(1));
    System.out.println("1 in list " + numbers.contains(1));
  }
}

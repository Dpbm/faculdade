public class Ex07{
  public static void main(String[] args){
    String course = "Bacharelado em ciencias da computacao";
    char[] vowels = {'a', 'e', 'i', 'o', 'u'};
    int totalVowels = 5;
    int totalCountedVowels = 0;
    for(int i = 0; i < course.length(); i++)
      for(int j = 0; j < totalVowels; j++)
        if(course.charAt(i) == vowels[j]){
          totalCountedVowels ++;
          break;
        }
    System.out.printf("Total counted vowels: %d\n", totalCountedVowels);
  }
}

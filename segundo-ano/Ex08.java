public class Ex08{
  public static void main(String[] args){
    String course = "Bacharelado em ciencias da computacao";
    String newCourse = "";

    for(int i = 0; i < course.length(); i++){
      char actualChar = course.charAt(i);
      if(!isAVowel(actualChar))
        newCourse += actualChar;
    }
    System.out.println(newCourse);
  }

  public static boolean isAVowel(char character){
    char[] vowels = {'a', 'e', 'i', 'o', 'u'};
    int totalVowels = 5;

    for(int i = 0; i < totalVowels; i++)
      if(character == vowels[i])
        return true;

    return false;
  }
}

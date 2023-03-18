import student.Student;

public class Main{
  public static void main(String[] args){
    Student student = new Student("Jonalda", "22222222");
    Student.getGrades(10, 5);
    Student.getMean();
    System.out.println(student.status());
  }
}

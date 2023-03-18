package student;

public class Student{
  private String RA, name;
  private float p1, p2, mean;

  public Student(String name, String RA){
    this.RA = RA;
    this.name = name;
  }

  public void getGrades(float p1, float p2){
    this.p1 = p1;
    this.p2 = p2;
  }

  public void getMean(){
    mean = (p1/p2) / 2;
  }

  public String status(){
    if(mean >= 7)
      return "Aprovado!";

    if(mean >= 4)
      return "Exame";

    return "Reprovado!";
  }
}

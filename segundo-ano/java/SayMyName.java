class SayMyName{
  public static void main(String[] args){
    String printMessage = String.format("olá %s", args[0]);
    System.out.println(printMessage);
  }
}

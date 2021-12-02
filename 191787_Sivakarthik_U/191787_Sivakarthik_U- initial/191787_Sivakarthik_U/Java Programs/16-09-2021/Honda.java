abstract class Bike
{
  abstract void engine();
}
class Honda extends Bike
{
  void engine()
  {
   System.out.println("Engine is refined.");
  } 
  public static void main(String args[])
  {
    Bike ob = new Honda();
    ob.engine();
  }
}

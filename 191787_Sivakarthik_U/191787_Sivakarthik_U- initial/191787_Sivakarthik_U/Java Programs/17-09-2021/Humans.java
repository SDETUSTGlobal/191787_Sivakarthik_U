interface Emotions
{
  void happy();
}
interface Feelings
{
  void sad();
}
class Humans implements Emotions,Feelings
{
  public void happy()
  {
    System.out.println("We are happy!!!");
  }
  public void sad()
  {
	  System.out.println("\nWe are not happy!!!");
  }
  public static void main(String args[])
  {
    Humans h = new Humans();
	h.happy();
	h.sad();
  }
}

	
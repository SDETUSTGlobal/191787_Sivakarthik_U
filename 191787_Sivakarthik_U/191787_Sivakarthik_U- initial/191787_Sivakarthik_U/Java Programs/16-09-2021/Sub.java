class Set
{
  String s;
  public Set(String b)
  {
    s = b;
  }
}
public class Sub extends Set
 {
  String s;
  public Sub(String q, String w)
  {
    super(q);       
    this.s = w;
    System.out.println("Hey");
  }
 
  {
	System.out.println("Hola");
  }

  public void show()
  {
   System.out.println(super.s+" and "+s);
  }
  public static void main(String[] args)
  {
   Sub a = new Sub
   ("Java","Programing");
   a.show();
 }
}
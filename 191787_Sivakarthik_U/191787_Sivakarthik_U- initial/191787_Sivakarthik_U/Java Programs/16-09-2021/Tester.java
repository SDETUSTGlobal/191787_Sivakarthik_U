class Tech
{  

  void dev()
  {
	  System.out.println("Software Developer");
  }  
}  
class Tester extends Tech
{  
  void dev()
  {
	  System.out.println("Tester");
  }  
  
  public static void main(String args[])
  {  
    Tech t = new Tester();
    t.dev(); 
	Tester s =new Tester();
	System.out.println(s instanceof Tech);
  }  
}  
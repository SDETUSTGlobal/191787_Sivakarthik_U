class Music
{ 
final int m=9; 
void tune()
	{
		 
	System.out.println("Music is Peace");
	System.out.println(m);
	
	}  
}  
class Guitar extends Music
{  
  void beat()
  {
	System.out.println("Strings");
  }  
}  
final class Keyboard extends Music
{  

final void notes()
	{
	System.out.println("Keys");
	}  
}  
class Sound
{  
  public static void main(String args[]){  
  Keyboard k=new Keyboard();  
  k.notes();  
  k.tune();  

}} 
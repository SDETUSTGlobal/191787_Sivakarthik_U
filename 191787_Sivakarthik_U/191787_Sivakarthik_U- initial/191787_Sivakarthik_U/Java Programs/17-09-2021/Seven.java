interface One
{
	interface Two
	{
		void welcome();
	}
}
abstract class Three
{
	Three()
	{
		System.out.println("Hey Three here.");
	}
	abstract void four();
	void five()
	{
		System.out.println("\nHey Five here.");
	}
}
class Six extends Three
{
	void four()
	{
		System.out.println("\nHey Four here.");
	}
}
public class Seven implements One.Two
{
	public void welcome()
	{
		System.out.println("\nHey everyone.");
	}
	public static void main(String args[])
	{
		Three t = new Six();
		t.four();
		t.five();
		One.Two obj = new Seven();
		obj.welcome();
	}
}

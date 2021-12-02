public class Add
{
	public int add(int a,int b)
	{
		return(a+b);
	}
	public int add(int a,int b,int c)
	{
		return(a+b+c);
	}
	public double add(double a,double b)
	{
		return(a+b);
	}
	public static void main(String args[])
	{
		Add s =new Add();
		System.out.println(s.add(20,30));
		System.out.println(s.add(20,30,40));
		System.out.println(s.add(20.5,30.2));
	}
}
		
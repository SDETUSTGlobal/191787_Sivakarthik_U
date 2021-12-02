class Mobile
{
	public void oneplus()
	{
		System.out.println("This is Oneplus.");
	}
	protected void samsung()
	{
		System.out.println("\nThis is Samsung.");
	}
	//private void apple()
	//{
	//	System.out.println("\nThis is Apple.");
	//}
	
}
public class Phone extends Mobile
{
	public static void main(String args[])
	{
		Mobile obj = new Mobile();
		obj.oneplus();
		obj.samsung();
		//obj.apple();
		Phone obj2 = new Phone();
		
			obj2.sony(); 
		
	}
	private void sony()
	{
		System.out.println("\nThis is Sony.");
	}
}
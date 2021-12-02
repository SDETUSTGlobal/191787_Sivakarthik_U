class Bank
{
	int getRate()
	{
		return 0;
	}
}
	class ICICI extends Bank
	{
		int getRate()
		{
			return 8;
		}
	}
	class SBI extends Bank
	{
		int getRate()
		{
			return 7;
		}
	}
	class HDFC extends Bank
	{
		int getRate()
		{
			return 5;
		}
	}
	
	class B2
	{
		public static void main(String args[])
		{
			ICICI i=new ICICI();
			SBI s=new SBI();
			HDFC h=new HDFC();
			System.out.println("ICIC Interest : "+i.getRate());
			System.out.println("SBI Interest : "+s.getRate());
			System.out.println("HDFC Interest : "+h.getRate());
		}
	}
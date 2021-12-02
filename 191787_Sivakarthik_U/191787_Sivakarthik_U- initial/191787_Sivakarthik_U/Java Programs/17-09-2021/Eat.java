interface Food
{
	default void types()
	{
		System.out.println("Chinese, North Indian & Arabic");
	}
	static void desserts()
	{
		System.out.println("Ice Cream, Puddings & Sweets");
	}
	
}
class Eat implements Food
{
	public static void main(String args[])
	{
		Eat e = new Eat();
        e.types();
		Food.desserts();
	}
}

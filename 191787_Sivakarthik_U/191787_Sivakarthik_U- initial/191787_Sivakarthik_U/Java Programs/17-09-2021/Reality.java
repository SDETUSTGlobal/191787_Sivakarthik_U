interface Life
{
	void career();
}
interface Personal extends Life
{
	void growth();
}
class Reality implements Personal
{
	public void career()
	{
   		System.out.println("Career growth.");
	}
	public void growth()
	{
		System.out.println("Maintain a work-life balance");
	}
	public static void main(String args[])
	{
		Reality r = new Reality();
        r.career();
        r.growth();
    }
}
	
	
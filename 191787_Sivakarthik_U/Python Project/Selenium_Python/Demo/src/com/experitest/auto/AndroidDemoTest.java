package com.experitest.auto;

import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Optional;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;


public class AndroidDemoTest extends BaseTest {
	
	@BeforeMethod
	@Parameters("deviceQuery")
	public void setUp(@Optional("@os='android'") String deviceQuery) throws Exception{
		init(deviceQuery, "AndroidDemoTest");
		client.install("cloud:com.experitest.ExperiBank/.LoginActivity:1.0", false, false);
		client.launch("com.experitest.ExperiBank/.LoginActivity", false, true);

	}
	
	@Test
	public void test(){
		
	}
	
	
}

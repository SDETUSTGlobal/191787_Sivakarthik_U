package com.app.mockito;
import java.util.Arrays;  
import java.util.List;  
 public class ToDoServicestub implements ToDoService   {    
    public List<String> getTodos(String user) {        
    return Arrays.asList(" Use Core Java ", " Use Spring Core ", " Use Hibernate ", " Use Spring MVC ");  
    }  
 } 


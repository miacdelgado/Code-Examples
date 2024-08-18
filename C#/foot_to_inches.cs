using System;

public class Program
{
    static void Main(string[] args)
    {
        double foot = Convert.ToDouble(Console.ReadLine());
        Converter(foot);
    }

    static void Converter(double foot)
    { 
    Console.Write(foot*12);
        
    }
    
}
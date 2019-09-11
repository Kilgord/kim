using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp11
{
    public class Calculator
    {
        



        public static int Summa(int a, int b)
        {
           
            
            
            
            return a+b;
        }
        public static int mi(int a, int b)
        {
            
            return a - b;
        }
        public static int umn(int a, int b)
        {


           
            
            return a*b;
        }

        public static int del(int a, int b)
        {


            
            
            return a/b;
        }
        
    }


    
        
        
    class Program
    {
        

        
        static void Main(string[] args)
        {
            
            
            Console.WriteLine(Calculator.mi(2, 2));
            Console.WriteLine(Calculator.del(2, 2));
            Console.WriteLine(Calculator.umn(2, 2));
            Console.WriteLine(Calculator.Summa(2, 2));
            Console.ReadKey();

        }
    }
}


using System;
using System.Globalization;

namespace Giraffe
{
    class Program
    {
        static void Main(string[] args)
        {
            // Classes and objects
            Book book1 = new Book();
            book1.title = "baa baa black sheep";

            Book book2 = new Book("title this is", "sani");

            book2.Author = "sani";  // using the set method

            Console.WriteLine(Book.bookCount);



            // Exception handling
            try
            {
                int y = Convert.ToInt32(Console.ReadLine());
                int x = 2 / y;
            } catch (DivideByZeroException e)
            {
                Console.WriteLine(e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                Console.WriteLine("this will run at the end");
            }


            // 2d Arrays
            int[,] twoDArray = { {1, 2, 3}, {2, 4, 6} };
            Console.WriteLine(twoDArray[1, 2]);

            int[,] another2DArray = new int[2, 3]; // 2 rows(elements) and 3 columns(3 elements inside each of the 2 elements)

            // For loops
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine(i * 3);
            }


            // while loops
            int index = 1;
            while (index <=3)
            {
                Console.WriteLine(index);
                index++;
            }
            Console.WriteLine(index);
            index += 2;
            do
            {
                Console.WriteLine(index);
                index++;
            } while (index <= 7);


            // --- Switch statements ---
            int switcher = 2;
            string day;
            switch (switcher)
            {
                case 0:
                    day = "monday";
                    break;
                case 1:
                    day = "Tuesday";
                    break;
                case 2:
                    day = "Wednesday";
                    break;
                default:
                    Console.WriteLine("Invalid number");
                    break;
            }

            // --- Arrays ---
            int[] numbers = { 4, 8, 6, 7, 3, 4, 6 };
            int secondNumber = numbers[1];
            string[] words = new string[5];

            // ---- Variables ---
            string name = "Sanishka";
            int age = 26;
            char initials = 'S';
            double accurate = 1.01;
            bool isMale = true;

            int strLength = name.Length;
            string lowerCase = name.ToLower();
            string sub = name.Substring(0, 4);

            int absValue = Math.Abs(-123);

            Console.WriteLine("My name is " + name + "\nI am " + age + " years old.");

            Console.Write("Enter your name: ");
            string newName = Console.ReadLine();
            Console.WriteLine(newName);

            string numStr = "34";
            int numInt = Convert.ToInt32(numStr);
        }

        static void sayHi(string message)
        {
            // callthis method from the main method
            // string message = "hello";
            Console.WriteLine(message);
        }

    }
}

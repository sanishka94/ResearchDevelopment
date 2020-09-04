using System;
using System.Collections.Generic;
using System.Globalization;
using System.Text;

namespace Giraffe
{
    //static class Book   // If the class is static, an instance of it cannot be created

    // class Book : Papers // This is extending, book is extends from papers (inheritance)
    class Book
    {
        public string title;
        private string author;
        public static int bookCount = 0;  // static variable, associated with the class and not the object

        public Book()
        {
            bookCount++;
        }
        public Book(string aTitle, string aAuthor)
        {
            this.title = aTitle;
            this.author = aAuthor;
            bookCount++;
        }

        public static void desc()
        {
            Console.WriteLine("this is a book");  // static method
        }

        public virtual string overrideThis()  // The 'virtual' keyword enables this method to be overriden by the sub classes
        {
            return "hello";
        }

        public string Author
        {
            get { return author; }
            set { author = value; }
        }
    }
}

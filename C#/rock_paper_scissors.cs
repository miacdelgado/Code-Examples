using System;

class Program
{
    static void Main(string[] args)
    {

        bool game = true;
        int scoreu = 0; //user score
        int scorec = 0; //computer score

        while (game)
        {
            Console.WriteLine("Welcome to the rock, paper, scissors game. Please enter a number to start.\n");
            Console.WriteLine("1. Rock\n2. Paper\n3. Scissors\n");

            int uChoice = Convert.ToInt32(Console.ReadLine());

            Random rObj = new Random();
            int cChoice = rObj.Next(1, 4);

            /*
            1 = rock
            2 = paper
            3 = scissors
            */

            switch (cChoice)
            {
                case 1:

                    switch (uChoice)
                    {
                        case 1: //user chose rock
                            Console.WriteLine("Computer chose rock.\nYou chose rock.");
                            Console.WriteLine($"It's a tie. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                        case 2: //user chose paper
                            scoreu++;
                            Console.WriteLine("Computer chose rock.\nYou chose paper.");
                            Console.WriteLine($"User wins. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                        case 3: //user chose scissors
                            scorec++;
                            Console.WriteLine("Computer chose rock.\nYou chose scissors.");
                            Console.WriteLine($"Computer wins. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                    }

                    break;

                case 2:

                    switch (uChoice)
                    {
                        case 1: //user chose rock
                            scorec++;
                            Console.WriteLine("Computer chose paper.\nYou chose rock.");
                            Console.WriteLine($"Computer wins. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                        case 2: //user chose paper
                            Console.WriteLine("Computer chose paper.\nYou chose paper.");
                            Console.WriteLine($"It's a tie. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                        case 3: //user chose scissors
                            scoreu++;
                            Console.WriteLine("Computer chose paper.\nYou chose scissors.");
                            Console.WriteLine($"User wins. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                    }


                    break;

                case 3:

                    switch (uChoice)
                    {
                        case 1: //user chose rock
                            scoreu++;
                            Console.WriteLine("Computer chose scissors.\nYou chose rock.");
                            Console.WriteLine($"User wins. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                        case 2: //user chose paper
                            scorec++;
                            Console.WriteLine("Computer chose scissors.\nYou chose paper.");
                            Console.WriteLine($"Computer wins. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                        case 3: //user chose scissors

                            Console.WriteLine("Computer chose scissors.\nYou chose scissors.");
                            Console.WriteLine($"It is a tie!. Computer has a score of {scorec} and you have a score of {scoreu}");
                            break;
                    }

                    break;

            }

            Console.WriteLine("\nDo you want to play again?");
            string ans = Console.ReadLine();
            ans.ToLower();

            if (ans == "no" || ans == "n")
            {
                game = false;
                Console.WriteLine("\nThanks for playing!");
            }
        }

     
  }
}
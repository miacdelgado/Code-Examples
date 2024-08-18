using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Sololearn
{
    class WordtoMorse
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            
            string capitalAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            
            string smallAlphabets = "abcdefghijklmnopqrstuvwxyz";
            
            string[ ] morseCode = new string[26]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---"," .--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
            for(int i = 0; i < input.Length; i++)
            {
                if(capitalAlphabets.Contains(input[i]))
                {
                    int indx = capitalAlphabets.IndexOf(input[i]);
                    Console.Write(morseCode[indx] + "  ");
                }
                else if(smallAlphabets.Contains(input[i]))
                {
                    int indx = smallAlphabets.IndexOf(input[i]);
                    Console.Write(morseCode[indx] + "  ");
                }
            }
        }
    }
}

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Password_Generator
{
    class Program
    {
        static void Main(string[] args)
        {
            CheckPassword password = new CheckPassword(3, 2, 2, 3, 8);
            Console.Write("Enter your password: ");
            password._password = Console.ReadLine();
            Console.WriteLine($"Your password is: {password._password}");
            password.showResult();
            if (!password.again())
                return;
            password.makeItStrong();
            Console.WriteLine($"Your new password is: {password._password}");
            password.showResult();


        }
    }
    interface ICheckPassword
    {
        bool isStrong();
        void makeItStrong();
        bool isValid();
        void showResult();
    }
    public class CheckPassword : ICheckPassword
    {
        enum number
        {
            valid,
            smallLetters,
            capitalLetters,
            symbols,
            digits
        }
        enum lib
        {
            numbers,
            symbols,
            smallLetters,
            capitalLetters,
            forbidden
        }
        public String _password { get; set; }
        Dictionary<lib, String> _digits;
        Dictionary<number, int> _numbers;
        private int countIt(lib key)
        {
            int count = 0;
            foreach (char letter in _password)
            {
                if (_digits[key].Contains(letter))
                    count++;
            }
            return count;
        }
        private bool check(lib key,int limit)
        {
            return countIt(key) >= limit;
        }
        private void addStrong(lib dkey,number nKey)
        {
            Random r = new Random();
            int number = countIt(dkey);
            while (number < (int)_numbers[nKey])
            {
                string words = _digits[dkey];
                int randomPosPassword = r.Next(0, _password.Length - 1);
                int randomPosWord = r.Next(0, words.Length - 1);
                char randomChar = words[randomPosWord];
                _password = _password.Substring(0, randomPosPassword) + randomChar + _password.Substring(randomPosPassword);
                number++;
            }
        }
        private void deleteForbidderChar()
        {
            foreach (char letter in _digits[lib.forbidden])
                _password=_password.Replace(letter.ToString(),"");
        }
        public CheckPassword(int nS,int nC,int nSb,int nD,int nV)
        {
            _digits = new Dictionary<lib, String>();
            _numbers=new Dictionary<number, int>();
            _numbers.Add(number.smallLetters, nS);
            _numbers.Add(number.capitalLetters, nC);
            _numbers.Add(number.symbols, nSb);
            _numbers.Add(number.digits, nD);
            _numbers.Add(number.valid,nV);
            _digits.Add(lib.numbers, "0123456789");
            _digits.Add(lib.symbols, "!@#$&_");
            _digits.Add(lib.forbidden, "%^*()+=-");
            _digits.Add(lib.smallLetters, "qwertyuiopasdfghjklzxcvbnm");
            _digits.Add(lib.capitalLetters, "QWERTYUIOPASDFGHJKLZXCVBNM");
        }
        public bool isValid()
        {
            return _password.Length >= _numbers[number.valid];
        }
        public bool again()
        {
            return !isStrong() || check(lib.forbidden, 1);
        }
        public bool isStrong()
        {
            return this.isValid() && check(lib.numbers, _numbers[number.digits]) && check(lib.symbols, _numbers[number.symbols])
                && check(lib.smallLetters, _numbers[number.smallLetters]) && check(lib.capitalLetters, _numbers[number.capitalLetters]);
        }
        public void makeItStrong()
        {
            addStrong(lib.smallLetters, number.smallLetters);
            addStrong(lib.capitalLetters, number.capitalLetters);
            addStrong(lib.symbols, number.symbols);
            addStrong(lib.numbers, number.digits);
            deleteForbidderChar();
        }
        public void showResult()
        { 
            System.Console.WriteLine($"-> has {_numbers[number.valid]} digits :         {isValid()}");
            System.Console.WriteLine($"-> has {_numbers[number.digits]} numbers:         {check(lib.numbers, _numbers[number.digits])}");
            System.Console.WriteLine($"-> has {_numbers[number.symbols]} symbols:         {check(lib.symbols, _numbers[number.symbols])}");
            System.Console.WriteLine($"-> has {_numbers[number.smallLetters]} small Letter:    {check(lib.smallLetters, _numbers[number.smallLetters])}");
            System.Console.WriteLine($"-> has {_numbers[number.capitalLetters]} capital Letters: {check(lib.capitalLetters, _numbers[number.capitalLetters])}");
            System.Console.WriteLine($"-> has not forbidden char:{!check(lib.forbidden, 1)}");
            System.Console.WriteLine("Result: your password is: " + ((isStrong()) ? "Strong" : "Week") + " and "+((check(lib.forbidden, 1)?"no valid":"valid")));
        }
    }
}
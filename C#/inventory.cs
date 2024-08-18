using System;
using System.Collections.Generic;

namespace Inventory
{
    class Item {
        public string Name {get; set;}
        
        public Item(string name){
            this.Name = name;
        }
        
        public override string ToString(){
            return Name;
        }
    }
    
    class Inventory<Type> {
        private Type[,][] inventory = new Type[4,10][];
        
        private List<Type> allItems = new List<Type>();
        
        public void AddItem(int[] index, Type[] item){
            for (int i = 0; i < item.Length; i++){
                if (i != item.Length-1)
                    Console.Write($"{item[i]} & ");
                else 
                    Console.Write($"{item[i]}; ");
                    
                allItems.Add(item[i]);
            }
            Console.WriteLine($"has been added to [{index[0]}, {index[1]}]");
            inventory[index[0], index[1]] = item;
        }
        
        public Type RemoveOneItem(int[] index){
            Console.WriteLine($"Items in [{index[0]}, {index[1]}][{index[2]}] have been removed");
            allItems.Remove(inventory[index[0], index[1]][index[2]]);
            return inventory[index[0], index[1]][index[2]];
        }
        
        public Type[] RemoveItems(int[] index){
            Console.WriteLine($"Items in [{index[0]}, {index[1]}] have been removed");
            Console.WriteLine($"{inventory[index[0], index[1]].Length} items have been removed");
            foreach (Type i in inventory[index[0], index[1]])
                allItems.Remove(i);
            return inventory[index[0], index[1]];
        }
        
        public void GetAnItem(int[] index){
            Console.WriteLine($"Items in [{index[0]}, {index[1]}][{index[2]}]: {inventory[index[0], index[1]][index[2]]}");
        }
        
        public void GetItems(int[] index){
            Console.Write($"Items in [{index[0]}, {index[1]}]: ");
            foreach (Type item in inventory[index[0], index[1]]){
                Console.Write($"{item} ");
            }
            Console.WriteLine("");
        }
        
        public void DisplayItems(){
            Console.Write("All items:\t");
            foreach (Type item in allItems){
                Console.Write($"{item} ");
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Item book = new("book");
            Item bag = new("bag");
            Item camera = new("camera");
            
            Inventory<Item> i = new Inventory<Item>();
            i.AddItem(new int[]{0,0}, new Item[]{book, bag, camera});
            
            Console.WriteLine("");
            i.GetAnItem(new int[]{0,0,1});            
            i.GetItems(new int[]{0,0});
            Console.WriteLine("");
            i.RemoveOneItem(new int[]{0,0,0});
            i.DisplayItems();
        }
    }
}

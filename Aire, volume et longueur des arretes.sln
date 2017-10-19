//Déclaration des variables
            decimal lo, la, h;
            bool testOk;
            string cm = "Cm";
            string cm1 = "Cm²";
            string cm2 = "Cm³";
            
                do{
                    Console.Write("Entrez la longueur en cm : ...");
                    testOk = decimal.TryParse(Console.ReadLine(), out lo);
                    if (testOk == false) {Console.WriteLine("Veillez à entrer une valeur decimale");}
                
                } while (!testOk);
                        Console.WriteLine(); //Génère une ligne vide

            
   
                do{
                    Console.Write("Entrez la largeur en cm : ...");
                    testOk = decimal.TryParse(Console.ReadLine(), out la);
                    if (testOk == false) { Console.WriteLine("Veuillez à entrez une valeur decimale"); }

                } while (!testOk);
                        Console.WriteLine(); //Génère une ligne vide

               
            
                do {
                     Console.Write("Entrez la hauteur en cm : ...");
                     testOk = decimal.TryParse(Console.ReadLine(),out h);
                     if (testOk == false) {Console.WriteLine("Veillez à entrer une valeur decimale");}
               
                } while (!testOk);
                        Console.WriteLine(); //Génère une ligne vide


                        Console.WriteLine(); //Génère une ligne vide
                        Console.WriteLine(); //Génère une ligne vide
                        Console.WriteLine(); //Génère une ligne vide

                //Calcul de l'aire.
                decimal aire = lo * la;

                //Calcul du volume.
                decimal volume = lo * la * h;

                //Calcul de la longueur total des arretes.
                decimal lt = (4 * lo) + (4 * la) + (4 * h);

                //Affichage des valeurs calculées
                Console.WriteLine("L'aire du parallélépipède rectangle est de : . . . . {0} {1}", aire, cm1);
                Console.WriteLine(); //Génère une ligne vide

                Console.WriteLine("Le volume du parallélépipède rectangle est de : . .  {0} {1}", volume, cm2);
                Console.WriteLine(); //Génère une ligne vide

                Console.WriteLine("La longueur total des arrètes est de : . . . . . . . {0} {1}", lt, cm);
                Console.WriteLine(); //Génère une ligne vide
                
            Console.ReadKey(true);


        }

    }
}

class dua: 
    def print_pattern(n):
        
        for row in range(n):

            
            for column in range(n):

                
                if ((row == 0 or row == n // 2) or

                        
                        column == 0):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


    size = int(input("Enter any number between 11 and 99: \t"))

    if size <= 10 or size >= 100 or size %2 == 0 :
        print("Masukkan angka <=11 dan  >= 99 (harus ganjil)")
    else:
        print_pattern(size)
        





            



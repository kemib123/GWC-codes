alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x" , "y", "z"]

length_list = len(alphabet)
bottom=0
top= length_list
target= "t"

while(top >= bottom):
    midpoint = int( bottom+top / 2)
    if(target == alphabet[midpoint]):
        print("Yay! you found the letter")

        break

    if( target < alphabet[midpoint]):
        top = midpoint
        print("left")

    if( target > alphabet[midpoint]):
            bottom = midpoint
            print("right")

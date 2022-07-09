books_purchased = int(input("Enter the number of books bought:"))
if books_purchased == 0:
    print("You have 0 points")
elif books_purchased == 1:
    print("You earn 6 points")
elif books_purchased == 2:
    print("You earn 16 points")
elif books_purchased == 3:
    print("You earn 32 points")
else:
    print("You earn 60 points")

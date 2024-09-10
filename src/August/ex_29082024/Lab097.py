squares = [1,4,9,16,25]
# List is Mutable in nature
# mutable - change -

squares[3] = 64

print(squares)

# Tuple - Collection of Items
my_tuple = (1,4,9,16,25)
#my_tuple[3] = 64
print(my_tuple)



shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real world project

my_tuple = ("tta.com","sdet.live")
my_api_list = list(my_tuple) # conversion
my_api_list = list(my_api_list) # conversion
print(my_api_list)
print(my_api_list)

my_api_list = tuple(my_api_list)
print(my_api_list)
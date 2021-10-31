is_male = False #this is a boolen
is_tall = False
# if is_male  or is_tall: #indentation for the if-statement when is_male is true
#     print("you are a male or tall or both")
# else:
#     print("you are neither male nor tall")

if is_male  and is_tall: #indentation for the if-statement when is_male is true
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not a male nor tall")
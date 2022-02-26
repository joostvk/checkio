# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


lijst = ["Jacob"]    
if len(lijst) == 0:
    ret_str = "no one likes this"
elif len(lijst) == 1:
    ret_str = lijst[0].capitalize() + ' likes this'
elif len(lijst) == 2:
    ' and '.join(lijst) + ' like this'



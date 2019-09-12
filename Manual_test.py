#Function that prints one less space for each letter that is looped through
def World_Hello_function(World_Hello, total):
    #total is subtracted by one for aesthetic appeal
    total = total - 1
    for i in (World_Hello):
        print(total*" "+i)
        total = total - 1

#Function statement that prints an extra space for each letter that is looped through
def Hello_World_function(Hello_World, World_Hello, total):
    for i in Hello_World:
        print(total*" "+i)
        total = total + 1
#Function that stores the world hello and total
    World_Hello_function(World_Hello, total)

#Main Function stores the phrase hello world, world hello, and total
def main():
    Hello_World = 'Hello World!'.upper()
    World_Hello = '!World Hello'.upper()
    total = 0
    # function call that stores the variables hello world, world hello, and total
    Hello_World_function(Hello_World, World_Hello, total)


main()

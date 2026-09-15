#Write a Python program to count and print the frequency of each vowel (a, e, i, o, u) in a given multi-line string.


x = '''
    hello, my name is vrajesh mer
    '''
vowel_count = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0,
}
for i in x:
    if(i in "aeiou"):
        vowel_count[i] +=1

print(vowel_count)
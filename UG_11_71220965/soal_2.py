def funPalindrome(s):
    s = s.lower()#case insensitive
    ispalindrome = 'Yes' if s == s[::-1] else 'No'
    return f'{ispalindrome}\nJika Dibalik: {s[::-1]}'

kata = input('Masukan Kata: ')
print(funPalindrome(kata))
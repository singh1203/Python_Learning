# Escape Character
Escape sequences allow you to include special characters in strings. To do this, simply add a backslash (\) before the character you want to escape.

Example: 
```
s = 'Hey, what\'s up?'
    print(s)
```

### Note

An important thing to remember is that, if you want to include a backslash character in a string, you will need to escape that. For example, if you want to print a directory path in Windows, you'll need to escape each backslash in the string:  ```print("C:\\Users\\Pat\\Desktop")```
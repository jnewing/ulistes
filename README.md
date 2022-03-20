##  ulistes - Username List Generation

A quick and easy username list generator for your pentesting / brute forcing toolkit.

It takes a full given name "Bob Smith" and cultivates a nice list of plausible login names. If the `-o` or `--output` option is omitted it will display the list to _STDOUT_

This tool comes with a predefined set of patterns  that will work right out of the box, however you're encouraged to customize this to suite your needs.

** Existing Patterns**
```
patterns =  [
'name[0] + name[1]',             # BobSmith
'name[0] + "." + name[1]',       # Bob.Smith
'name[0] + "_" + name[1]',       # Bob_Smith
'name[0][0:1] + name[1]',        # BSmith
'name[0][0:1] + "." + name[1]',  # B.Smith
'name[0][0:1] + "_" + name[1]',  # B_Smith
'name[0] + name[1][0:1]',        # BobS
'name[0] + "." + name[1][0:1]',  # Bob.S
'name[0] + "_" + name[1][0:1]',  # Bob_S
'name[1] + name[0]',             # SmithBob
'name[1] + "." + name[0]',       # Smith.Bob
'name[1]+ "_" + name[0]',        # Smith_Bob
'name[1][0:1] + name[0]',        # SBob
'name[1][0:1] + "." + name[0]',  # S.Bob
'name[1][0:1] + "_" + name[0]',  # S_Bob
'name[1] + name[0][0:1]',        # SmithB
'name[1] + "." + name[0][0:1]',  # Smith.B
'name[1] + "_" + name[0][0:1]',  # Smith_B
]
```

The `name` variable will be passed into this and it expects a list consisting of `['First', 'Last']` name. Because this is a list of strings you can use any string formatting you like within the pattern.

---

**ulistes Usage**:

`./ulistes.py [OPTINOS] <full name>`

**Example**:

` ./ulistes.py Bob Smith`

  
**Options**:
```
-o : <filename> Writes all results to specified file
-l : Will force name into lowercase. Otherwise case will be preserved
--append : <string> Will append this string to the username
--prepend : <string> Will prepend this string to the username
```

This tool is as always meant for ethical uses **only**. Nuf said, I'm not your mother.

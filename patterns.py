''' Pre-defined patterns for use.

Here are just a few pre-defined patterns that I've found to be useful. However
feel free to add more.

Check the comments for example assuming name is ['Bob', 'Smith']

'''

patterns = [
    
    'name[0] + name[1]',                # BobSmith
    'name[0] + "." + name[1]',          # Bob.Smith
    'name[0] + "_" + name[1]',          # Bob_Smith
    'name[0][0:1] + name[1]',           # BSmith
    'name[0][0:1] + "." + name[1]',     # B.Smith
    'name[0][0:1] + "_" + name[1]',     # B_Smith
    'name[0] + name[1][0:1]',           # BobS
    'name[0] + "." + name[1][0:1]',     # Bob.S
    'name[0] + "_" + name[1][0:1]',     # Bob_S
    
    'name[1] + name[0]',                # SmithBob
    'name[1] + "." + name[0]',          # Smith.Bob
    'name[1]+ "_" + name[0]',           # Smith_Bob
    'name[1][0:1] + name[0]',           # SBob
    'name[1][0:1] + "." + name[0]',     # S.Bob
    'name[1][0:1] + "_" + name[0]',     # S_Bob
    'name[1] + name[0][0:1]',           # SmithB
    'name[1] + "." + name[0][0:1]',     # Smith.B
    'name[1] + "_" + name[0][0:1]',     # Smith_B
    
]
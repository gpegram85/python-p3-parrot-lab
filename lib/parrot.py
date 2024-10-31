def parrot(string=None, default_string="Squawk!"):
    if not string:
        print(default_string)
        return(default_string)
    else:    
        print(string)
        return string
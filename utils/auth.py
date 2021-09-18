
def load_rapidapi_key(path='/Users/bhavnasultana/.secrets/rapidapi.key'):
    with open(path, 'r') as of:
        x = of.read()
        return(x.rstrip())
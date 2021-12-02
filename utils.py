def get_api_key(path='private/API KEY.txt'):
    ''''
        Return the api key of NEW API
    '''
    with open(path, 'r') as f:
        key = f.read()
    return key



output = ''
with open('list.txt', 'r') as rawLib:
        with open('libraries.txt', 'w') as libraries:
            for lib in rawLib:
                if lib.find('-') == -1 and lib.find('Package') == -1:
                    lib = lib.split(' ',2)
                    libName = lib[0]
                    libraries.write(libName.strip() + '\n')


with open('libraries.txt', 'r') as libraries:
    with open('run.sh', 'a') as run:
        for lib in libraries:
            output += lib.strip()+' '
        run.write('pip install '+output)

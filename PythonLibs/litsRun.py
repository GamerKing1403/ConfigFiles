with open('list.txt', 'r') as rawLib:
        with open('libraries.txt', 'w') as libraries:
            for lib in rawLib:
                if lib.find('-') == -1 and lib.find('Package') == -1:
                    lib = lib.split(' ',2)
                    libName = lib[0]
                    libraries.write(libName.strip() + '\n')
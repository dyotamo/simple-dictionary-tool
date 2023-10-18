import sys
import utils

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: [key] | --help")
        exit(1)
    else:
        key = " ".join(args)
        if key == '--help':
            print("Usage: [key] | --help")
            exit(0)

        with open("src/assets/dictionary") as fd:
            fflag = False

            for x in fd:
                temp_str = x[:-1]

                # [:-1] because this string in \n-ended. lower() for being icase ...
                if temp_str.lower() == key.lower():
                    fflag = True
                    print("Result found for:", temp_str)
                    break

            if not fflag:
                print("Results not found for:", key)
                fd.seek(0)

                c = 0

                for y in utils.get_keys(fd):
                    if utils.analyze_str(key.lower(), y.lower()):
                        print("Did you mean: ", y)
            else:
                for x in fd:
                    if x[0] == "\t" or x == "\n":
                        print(x, end='')
                    else:
                        break

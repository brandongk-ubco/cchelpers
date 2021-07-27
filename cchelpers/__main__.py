import argh
from . import status

parser = argh.ArghParser()
parser.add_commands([status])

# dispatching:

if __name__ == '__main__':
    parser.dispatch()

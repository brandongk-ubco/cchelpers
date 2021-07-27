import argh
from .commands import status, grid_search

parser = argh.ArghParser()
parser.add_commands([status, grid_search])

if __name__ == '__main__':
    parser.dispatch()

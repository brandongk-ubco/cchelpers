import yaml
import os
import itertools
from flatten_dict import flatten, unflatten
import operator
import hashlib
import shutil


def grid_search(in_dir: str = "."):

    in_dir = os.path.abspath(in_dir)

    sweep_config_file = os.path.join(in_dir, 'sweep.yaml')

    with open(sweep_config_file, 'r') as f:
        sweep_config = yaml.load(f, Loader=yaml.loader.SafeLoader)
    sweep_config = flatten(sweep_config, reducer='dot')
    sweep_config = dict(sorted(sweep_config.items(),
                               key=operator.itemgetter(0)))

    files = [
        os.path.join(in_dir, f)
        for f in os.listdir(in_dir)
        if os.path.isfile(os.path.join(in_dir, f)) and f != 'sweep.yaml'
    ]

    keys = sweep_config.keys()
    values = sweep_config.values()
    permutations = itertools.product(*values)

    for permutation in permutations:
        configuration = unflatten(dict(zip(keys, permutation)), splitter='dot')
        config_yaml = yaml.dump(configuration)
        config_hash = hashlib.md5(config_yaml.encode()).hexdigest()
        out_dir = os.path.join(in_dir, config_hash)
        os.makedirs(out_dir, exist_ok=True)
        config_file = os.path.join(out_dir, 'config.yaml')
        if not os.path.exists(config_file):
            with open(config_file, 'w') as f:
                f.write(config_yaml)
        for f in files:
            shutil.copy(f, out_dir)

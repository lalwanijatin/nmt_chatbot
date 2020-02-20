import sys
import os
import argparse
from setup.settings import hparams, out_dir
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
sys.path.append(os.path.realpath(os.path.dirname(__file__)) + "/nmt")
from nmt import nmt
import tensorflow as tf

from datetime import datetime


# Modified autorun from nmt.py (bottom of the file)
# We want to use original argument parser (for validation, etc)
nmt_parser = argparse.ArgumentParser()
nmt.add_arguments(nmt_parser)
# But we have to hack settings from our config in there instead of commandline options
flags, unparsed = nmt_parser.parse_known_args(['--'+k+'='+str(v) for k,v in hparams.items()])
flags.out_dir = out_dir
hparams = nmt.create_hparams(flags)
hparams = nmt.create_or_load_hparams(flags.out_dir, hparams, flags.hparams_path, save_hparams=True)
print(" :: ",hparams.attention)
print(nmt.utils.get_config_proto())
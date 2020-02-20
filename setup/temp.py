import sys
sys.path.insert(0, '../')
import os
from setup.settings import preprocessing, hparams
from multiprocessing import Pool
from tqdm import tqdm
from itertools import zip_longest
from core.tokenizer import tokenize
import argparse

print(os.path.realpath(os.path.dirname(__file__)))

print(preprocessing['train_folder'])


files = {
    'train.from': {'amount': 1, 'up_to': -1},  # copy all of data (up to "samples")
    'tst2012.from': {'amount': .1, 'up_to': preprocessing['test_size']},  # copy 1/10th but up to 'test_size'
    'tst2013.from': {'amount': .1, 'up_to': preprocessing['test_size']},
    'train.to': {'amount': 1, 'up_to': -1},
    'tst2012.to': {'amount': .1, 'up_to': preprocessing['test_size']},
    'tst2013.to': {'amount': .1, 'up_to': preprocessing['test_size']},
}

print("->",os.getcwd())

nmt_parser = argparse.ArgumentParser()

a,b = nmt_parser.parse_known_args(['--'+k+'='+str(v) for k,v in hparams.items()])
print("a : ",a)
print("b : ",b)
print([os.getcwd() + '\nmt\nmt\nmt.py'] + b)




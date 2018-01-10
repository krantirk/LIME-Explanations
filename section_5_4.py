import argparse

import generate_data_for_compare_classifiers
import compare_classifiers

import matplotlib.pyplot as plt

import time
import os

# ---------------- Arguments ------------------
parser = argparse.ArgumentParser(description='Evaluate some explanations')
parser.add_argument('--output_dir', '-o', type=str, default='output_section_5_2/', help='dataset name')


DATASETS = ['multi_polarity_books', 'multi_polarity_kitchen', 'multi_polarity_dvd']
PICKS = ['submodular', 'random']
NUM_ROUNDS = 10
NUM_INSTANCES = 10
NUM_FEATURES = 10

OUTPUT_DIR = 'out_comparing'


def main():
  args = parser.parse_args()  # get arguments

  # create output folder
  try:
    os.stat(OUTPUT_DIR)
  except:
    os.mkdir(OUTPUT_DIR)


  for dataset in DATASETS:
    print '-' * 50
    print 'Running experiment with %s' % dataset
    print '-' * 50

    #start_time = time.time()
    #generate_data_for_compare_classifiers.run_experiment(dataset, OUTPUT_DIR, NUM_FEATURES, NUM_ROUNDS)
    #print("--- %s seconds ---" % (time.time() - start_time)) 

    for pick in PICKS:
      start_time = time.time()
      compare_classifiers.run_experiment(dataset, OUTPUT_DIR, NUM_FEATURES, pick, NUM_INSTANCES, NUM_ROUNDS)
      print("--- %s seconds ---" % (time.time() - start_time)) 

if __name__ == "__main__":
    main()
  


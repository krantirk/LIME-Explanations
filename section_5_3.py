import argparse

import data_trusting

import matplotlib.pyplot as plt

import time
import os

import pandas as pd

# ---------------- Arguments ------------------
parser = argparse.ArgumentParser(description='Evaluate some explanations')
parser.add_argument('--output_dir', '-o', type=str, default='output_section_5_3/', help='dataset name')

# 'multi_polarity_kitchen' is also a valid option but was not used in the paper.
DATASETS = ['multi_polarity_books', 'multi_polarity_dvd']
ALGORITHMS = ['logreg', 'tree', 'random_forest', 'svm'] 

NUM_FEATURES = 10
PERCENT_UNTRUSTWORTHY = .25
NUM_ROUNDS = 5


def save_as_csv(df, output_path):
  # create directory if needed
  directory = os.path.dirname(output_path)
  if not os.path.exists(directory):
    os.makedirs(directory)
  # save df as csv
  df.to_csv(output_path, encoding='utf-8', index=False)


def main():
  args = parser.parse_args()  # get arguments
  for dataset in DATASETS:
    print '-' * 50
    print 'Running experiment with %s' % dataset
    print '-' * 50

    df = pd.DataFrame(columns=['classifier', 'LIME', 'random', 'greedy', 'parzen'])
    for algorithm in ALGORITHMS:
      res = {}
      print 'using algorithm %s' % algorithm
      start_time = time.time()
      df = data_trusting.run_experiment(df, dataset, algorithm, NUM_FEATURES, PERCENT_UNTRUSTWORTHY, NUM_ROUNDS)
      print("--- %s seconds ---" % (time.time() - start_time))
    
    save_as_csv(df, args.output_dir + dataset + '.csv')
    
if __name__ == "__main__":
    main()
  


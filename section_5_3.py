import argparse

import data_trusting

import matplotlib.pyplot as plt

import time
import os

# ---------------- Arguments ------------------
parser = argparse.ArgumentParser(description='Evaluate some explanations')
parser.add_argument('--output_dir', '-o', type=str, default='output_section_5_3/', help='dataset name')


DATASETS = ['multi_polarity_books', 'multi_polarity_kitchen', 'multi_polarity_dvd']
ALGORITHMS = ['logreg', 'random_forest', 'svm', 'tree']

NUM_FEATURES = 10
PERCENT_UNTRUSTWORTHY = .25
NUM_ROUNDS = 5

def bar_plot(recalls, img_path, output_dir):
  # create output dir if it does not exist
  try:
    os.stat(output_dir)
  except:
    os.mkdir(output_dir)       

  # bar plot  
  plt.bar(range(len(recalls)), recalls.values(), align='center')
  plt.xticks(range(len(recalls)), list(recalls.keys()))

  # saving image  
  fig = plt.gcf()
  fig.savefig(output_dir + img_path)
  
  # showing image
  # plt.show()

  # clear image
  fig.clear()

  
def main():
  args = parser.parse_args()  # get arguments
  for dataset in DATASETS:
    print '-' * 50
    print 'Running experiment with %s' % dataset
    print '-' * 50
    for algorithm in ALGORITHMS:
      res = {}
      print 'using algorithm %s' % algorithm
      start_time = time.time()
      data_trusting.run_experiment(dataset, algorithm, NUM_FEATURES, PERCENT_UNTRUSTWORTHY, NUM_ROUNDS)
      print("--- %s seconds ---" % (time.time() - start_time)) 

if __name__ == "__main__":
    main()
  


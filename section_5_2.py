import argparse

import evaluate_explanations

import matplotlib.pyplot as plt

import time
import os

# ---------------- Arguments ------------------
parser = argparse.ArgumentParser(description='Evaluate some explanations')
parser.add_argument('--output_dir', '-o', type=str, default='output_section_5_2/', help='dataset name')


DATASETS = ['multi_polarity_books', 'multi_polarity_kitchen', 'multi_polarity_dvd']
ALGORITHMS = ['l1logreg', 'tree']
EXPLAINERS = ['random', 'greedy', 'lime']

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
      for explainer in EXPLAINERS:
        start_time = time.time()
        print 'using explainer %s' % explainer
        recall, outputs = evaluate_explanations.run_experiment(dataset, algorithm, explainer)

        print 'Recall of %s %s %s' % (dataset, algorithm, explainer), recall
        res[explainer] = recall
        print("--- %s seconds ---" % (time.time() - start_time)) 
    
      img_name = dataset + '_' + algorithm + '.pdf'
      print 'Plotting and saving result as %s at %s' % (img_name, args.output_dir)
      bar_plot(res, img_name, args.output_dir)

if __name__ == "__main__":
    main()
  


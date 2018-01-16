import argparse

import evaluate_explanations

import matplotlib.pyplot as plt

import time
import os

# ---------------- Arguments ------------------
parser = argparse.ArgumentParser(description='Evaluate some explanations')
parser.add_argument('--output_dir', '-o', type=str, default='output_section_5_2/', help='dataset name')


# 'multi_polarity_kitchen' is also a valid option but was not used in the paper.
DATASETS = ['multi_polarity_books', 'multi_polarity_dvd']
ALGORITHMS = ['l1logreg', 'tree']
EXPLAINERS = ['random', 'parzen', 'greedy', 'lime']

def bar_plot(recalls, img_path, output_dir, show_image=False):
  # create output dir if it does not exist
  try:
    os.stat(output_dir)
  except:
    os.mkdir(output_dir)       

  fig, ax = plt.subplots()

  # bar plot
  opacity = 0.4
  bar_width = 0.35

  plt.xlabel('Algorithms')
  plt.ylabel('Recall for golden features')

  x = recalls.keys()
  y = [ r * 100 for r in recalls.values()]

  bar = plt.bar(range(len(recalls)), y, align='center', alpha=opacity, color='b')
  plt.xticks(range(len(recalls)), x, rotation=30)

  # add counts above the bars
  for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height,
             '%.2f' % height, ha='center', va='bottom')

  # format y axis as percent
  vals = ax.get_yticks()
  ax.set_yticklabels(['{:3.2f}%'.format(x) for x in vals])

  plt.legend()
  plt.tight_layout()

  # showing image
  if show_image:
    plt.show()

  # saving image  
  fig.savefig(output_dir + img_path)

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
    
      img_name = dataset + '_' + algorithm + '.png'
      print 'Plotting and saving result as %s at %s' % (img_name, args.output_dir)
      bar_plot(res, img_name, args.output_dir)

if __name__ == "__main__":
    main()
  


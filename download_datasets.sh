#!/bin/sh

# downloads and unzips Religion dataset
mkdir religion_dataset
wget -qO- https://github.com/marcotcr/lime-experiments/blob/master/religion_dataset.tar.gz?raw=true | tar xvz -C religion_dataset

# downloads and unzips Multi-polarity datasets
wget -qO- https://www.cs.jhu.edu/~mdredze/datasets/sentiment/processed_acl.tar.gz | tar xvz

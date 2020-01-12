
# Synthetic data generation for graph ML experiments

This codebase generates interesting graphs for ML experiments. We've currently focussed on the challenges of review prediction, given three types of nodes:
- Product
- Person
- Review

A review has a score, which is the goal of each experiment to determine.

There are a range of datasets you can generate:
- experiment_0
- experiment_1
- experiment_2
- experiment_3
- experiment_4
- experiment_5
- article_0 - companion to the article "*An introduction to machine learning on graph databases*"
- article_1 - companion to the article "*Review prediction using graph data in Neo4j and an embedding in Tensorflow*"



## HOWTO generate data

To generate a dataset (for example, article_0) run the following in this repository's root directory:

1) `pip install pipenv`
2) `pipenv install`
3) `pipenv bash`
4) `./generate.py --dataset article_0`

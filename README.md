# PREFMoDeL - the Public Repository of Engineered Features for Molecular Deep Learning
A repository and Python API of features describing single molecules (especially proteins) and metrics for each of these features in analysis and design tasks.

This library is a collection of functions for generating features for single molecules from a variety of inputs. Of particular interest are those which include *structural* and *dynamic* detail, but *nonstructural* or *composite* features are also included. The ```.pdb``` file format is used extensively, getting processed by internal or external libraries.

The ultimate goal of this project is to create a central repository for users to access state-of-the-art features in an accessible, efficient Python API. It is the author's belief that providing such a library with standardized tests for molecular analysis and design tasks will help standardize molecular science and engineering.

# Inspirations
Multiple other projects inspired this one, such as the DeepChem library designed by the Pande lab at Stanford.

# Planned integrations
* Molecular dynamics suites for on-the-fly calculation of structural and dynamic metrics to evaluate simulations

# More background information
This repository was inspired at the conclusion of my Honors thesis, in which I characterized the taxonomy of biomolecular features that I noticed while reading through a collection of articles. You can read that [here][https://ir.library.oregonstate.edu/concern/honors_college_theses/d217qx73b].

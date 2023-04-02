# PREFMoDeL - the Public Repository of Engineered Features for Molecular Deep Learning
A repository and Python API of features describing single molecules (especially proteins) and metrics for each of these features in analysis and design tasks.

This library is a collection of functions for generating features for single molecules from a variety of inputs. Of particular interest are those which include *structural* and *dynamic* detail, but *nonstructural* or *composite* features are also included. The ```.pdb``` file format is used extensively, getting processed by internal or external libraries.

The ultimate goal of this project is to create a central repository for users to access state-of-the-art features in an accessible, efficient Python API. It is the author's belief that providing such a library with standardized tests for molecular analysis and design tasks will help standardize molecular science and engineering.

# Inspirations
Multiple other projects inspired this one, such as the DeepChem library designed by the Pande lab at Stanford.

# Planned integrations
* Molecular dynamics suites for on-the-fly calculation of structural and dynamic metrics to evaluate simulations

# Citations and more background information
Please cite the PREFMoDeL paper as here:

```bibtex
@Article{app13074356,
AUTHOR = {North, Jacob L. and Hsu, Victor L.},
TITLE = {PREFMoDeL: A Systematic Review and Proposed Taxonomy of Biomolecular Features for Deep Learning},
JOURNAL = {Applied Sciences},
VOLUME = {13},
YEAR = {2023},
NUMBER = {7},
ARTICLE-NUMBER = {4356},
URL = {https://www.mdpi.com/2076-3417/13/7/4356},
ISSN = {2076-3417},
ABSTRACT = {Of fundamental importance in biochemical and biomedical research is understanding a molecule&rsquo;s biological properties&mdash;its structure, its function(s), and its activity(ies). To this end, computational methods in Artificial Intelligence, in particular Deep Learning (DL), have been applied to further biomolecular understanding&mdash;from analysis and prediction of protein&ndash;protein and protein&ndash;ligand interactions to drug discovery and design. While choosing the most appropriate DL architecture is vitally important to accurately model the task at hand, equally important is choosing the features used as input to represent molecular properties in these DL models. Through hypothesis testing, bioinformaticians have created thousands of engineered features for biomolecules such as proteins and their ligands. Herein we present an organizational taxonomy for biomolecular features extracted from 808 articles from across the scientific literature. This objective view of biomolecular features can reduce various forms of experimental and/or investigator bias and additionally facilitate feature selection in biomolecular analysis and design tasks. The resulting dataset contains 1360 nondeduplicated features, and a sample of these features were classified by their properties, clustered, and used to suggest new features. The complete feature dataset (the Public Repository of Engineered Features for Molecular Deep Learning, PREFMoDeL) is released for collaborative sourcing on the web.},
DOI = {10.3390/app13074356}
}
```

This repository was inspired at the conclusion of my Honors thesis, in which I characterized the taxonomy of biomolecular features that I noticed while reading through a collection of articles. You can read that [here][https://ir.library.oregonstate.edu/concern/honors_college_theses/d217qx73b]. It is essentially a preliminary version of the PREFMoDeL paper above.

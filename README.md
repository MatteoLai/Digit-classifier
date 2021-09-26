# Digit-classifier

The dataset consists of handwritten digits (0-9), contained in the folder "DBs". 
Both training datasets conteins 7330 labeled patterns:
- "_pendigits_tr.txt_" contains 16-dimensional patterns (x,y coordinates of eigth point equidistant after normalization and resampling); the respective test set is in the file "_pendigits_te.txt_"
- "_pendigits_tr_Pca_K2.txt_" is a two-dimensional version obtained by PCA, to visualize the results; the respective test set is in the file "_pendigits_te_Pca_K2.txt_".

The Jupyter Notebook "_Digit-classifier.ipynb_" proposes the application of a classification algorithm and the choice of the correct hyperparameters. It's also possible to visualize 2D classified data thanks to the code - not written by myself - "_visualization.py_".

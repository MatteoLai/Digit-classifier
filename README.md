# Digit-classifier

The dataset consists of handwritten digits (0-9), contained in the folder "DBs". 
Both training datasets conteins 7330 labeled patterns:
- "pendigits_tr.txt" conteins 16-dimensional patterns (x,y coordinates of eigth point equidistant after normalization and resampling); the respective test set is in the file pendigits_te.txt
- "pendigits_tr_Pca_K2.txt" is a two-dimensional version obtained by PCA, to visualize the results; the respective test set is in the file "pendigits_te_Pca_K2.txt".

The Jupyter Notebook "Digit-classifier" proposes the application of a classification algorithm and the choice of the correct hyperparameters. It's also possible to visualize 2D classified data thanks to the code in visualization.py.

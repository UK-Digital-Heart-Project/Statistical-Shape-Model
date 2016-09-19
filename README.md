# Statistical-Shape-Model

This repository describes a statistical shape model for the ventricles of the heart. The shape model is constructed by registering 1093 hearts to the template space using rigid registration (so that the position and orientation differences are removed) and applying principal component analysis (PCA) to the surface meshes of all these hearts.

## Data

We have performed PCA three times, namely on the left ventricle (LV), the right ventricle (RV) and both ventricles. The mean shape model, the first 100 principal components (PC) and the corresponding eigenvalues or variances are provided. Suppose X denote a m-by-n matrix containing the point coordinates for m hearts. n denotes the number of coordinates, which is three times the number of points. Using Matlab language, the mean shape model and the PC decomposition are computed by,
```
mean_shape = mean(X, 1);
[pc, score, variance, tsquare] = princomp(X, 'econ');
```
The mean shape model is saved as a VTK file. The PCs and variances are saved as csv files. We only store the first 100 PCs and the their variances, which already encode over 99.9% of the shape variation. To reduce file sizes on github, the csv files are compressed using gzip. The numpy.genfromtxt() function in Python normally recognises the gzip format automatically. If not, you may need to decompress the files first.

## Script

If you are interested in a specific mode and would like to see how it affects the heart shape, we have also included a Python script which loads the data and computes the shape at a certain standard deviation from the mean shape.

## How to cite

This study is part of the UK Digital Heart Project, which was set up by Prof. Stuart Cook and Dr. Declan O'Regan at the MRC Clinical Sciences Centre, Imperial College London, UK. It is co-funded by the BHF, MRC and NIHR. In the event you find the shape model useful, please consider giving appropriate credit to it by citing the following relevant papers, which describe the atlas construction methodology [1], the imaging prototol and clinical background [2]. Thank you.

[1] W. Bai, W. Shi, A. de Marvao, T.J.W. Dawes, D.P. O’Regan, S.A. Cook, D. Rueckert. A bi-ventricular cardiac atlas built from 1000+ high resolution MR images of healthy subjects and an analysis of shape and motion. Medical Image Analysis, 26(1):133-145, 2015. [doi:10.1016/j.media.2015.08.009](http://dx.doi.org/10.1016/j.media.2015.08.009)

[2] A. de Marvao, T. Dawes, W. Shi, C. Minas, N.G. Keenan, T. Diamond, G. Durighel, G. Montana, D. Rueckert, S.A. Cook, D.P. O'Regan. Population-based studies of myocardial hypertrophy: high resolution cardiovascular magnetic resonance atlases improve statistical power. J Cardiovasc Magn Reson, 16:16, 2014. [doi:10.1186/1532-429x-16-16](http://dx.doi.org/10.1186/1532-429x-16-16)

Copyright 2016 Imperial College London

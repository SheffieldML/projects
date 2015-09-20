---
layout: default
title: "StyleIK"
---
# StyleIK Project

## Overview

This project was a pump priming project concerning large scale learning
of human motion capture data sets using latent variable models, in
particular the GP-LVM. The aim of the project is to develop the
dimensionality reduction methods for modelling human motion with a view
towards constructing systems for markerless motion capture.

The achievements in the project were:

-   We have developed a set of tools for loading MOCAP data into MATLAB
    (see software below).
-   We now have convergent sparse GP-LVM for sparse learning, details
    are given in the large scale learning paper below.
-   We have developed a hierarchical model for decomposition of the
    component parts of human motion (see the Hierarchical GP-LVM
    paper below).
-   We have developed a shared latent space model for jointly learning
    about joint angles and silhouettes (see the MLMI paper below).
-   We presented a paper on extensions of the shared latent space model
    (see the second MLMI paper below).
-   We presented a paper on topological extensions of the model that
    allow different styles to be interpolated (see ICML paper below,
    this was an international collaboration with MIT, Toronto
    and \`Berkeley).

The project is sponsored by [EU FP6 Project Ref ](http://www.pascal-network.org) and is a collaboration with [Professor Philip Torr](http://cms.brookes.ac.uk/staff/PhilipTorr/) of Oxford Brookes.



<a name="personnel"></a>

## Personnel from ML@SITraN

- [Carl Henrik Ek](http://www.carlhenrik.com/) PhD student and Manchester RA

- [Huma Lodhi](http://www.doc.ic.ac.uk/~hml/) Former Post-doctorate Researcher



<a name="software"></a>

## Software

The following software has been made available either wholly or partly as a result of work on this project:- [fgplvm](http://inverseprobability.com/fgplvm/) FGPLVM Toolbox for large scale learning of GP-LVMs.

- [hgplvm](http://inverseprobability.com/hgplvm/) HGPLVM Toolbox for hierarchical learning of GP-LVMs.

- [mocap](http://inverseprobability.com/mocap/) Simple MATLAB utility toolbox for loading motion capture data sets.

<a name="publications"></a>

## Publications

<span class="author">N. D. Lawrence</span> (2006) <span
class="papertitle">"The Gaussian process latent variable model"</span>
Technical Report no CS-06-03, The University of Sheffield, Department of
Computer Science.
\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/gplvmTutorial.pdf)\]\[[Demos
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/oxford/)\]\[[Main
Software](https://github.com/SheffieldML/GPmat/)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=The+Gaussian+Process+Latent+Variable+Model+&btnG=Search)\]

#### Abstract

The Gaussian process latent variable model (GP-LVM) is a recently
proposed probabilistic approach to obtaining a reduced dimension
representation of a data set. In this tutorial we motivate and describe
the GP-LVM, giving reviews of the model itself and some of the concepts
behind it.


<span class="author">N. D. Lawrence</span> (2006) <span
class="papertitle">"Computer vision reading group: the Gaussian process
latent variable model"</span>. Presented at Computer Vision Reading
Group, Visual Geometry Group, Department of Engineering Science,
University of Oxford, U.K. on 27/1/2006. \[[PDF
Slides](ftp://ftp.dcs.shef.ac.uk/home/neil/gplvmTutorialSlides.pdf)\]\[[PDF
Notes](ftp://ftp.dcs.shef.ac.uk/home/neil/gplvmTutorial.pdf)\]\[[Demos
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/oxford/)\]\[[Main
Software](https://github.com/SheffieldML/GPmat/)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Computer+Vision+Reading+Group:+The+Gaussian+Process+Latent+Variable+Model+&btnG=Search)\]

#### Abstract

The Gaussian process latent variable model (GP-LVM) is a recently
proposed probabilistic approach to obtaining a reduced dimension
representation of a data set. In this tutorial we motivate and describe
the GP-LVM, giving a review of the model itself and some of the concepts
behind it.


<span class="author">N. D. Lawrence</span> (2007) <span
class="papertitle">"Probabilistic dimensional reduction with the
Gaussian process latent variable model"</span>. Presented at Google
Research, New York, N.Y., U.S.A. on 12/2/2007.
\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/gplvm_07_02.pdf)\]\[[YouTube](http://www.youtube.com/watch?v=DS853uA0u4I)\]\[[Demos
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/oxford/)\]\[[Main
Software](https://github.com/SheffieldML/GPmat/)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Probabilistic+Dimensional+Reduction+with+the+Gaussian+Process+Latent+Variable+Model+&btnG=Search)\]\[[Video](http://video.google.com/videoplay?docid=-5127068978792458641)\]

#### Youtube

#### Abstract

Density modelling in high dimensions is a very difficult problem.
Traditional approaches, such as mixtures of Gaussians, typically fail to
capture the structure of data sets in high dimensional spaces. In this
talk we will argue that for many data sets of interest, the data can be
represented as a lower dimensional manifold immersed in the higher
dimensional space. We will then present the Gaussian Process Latent
Variable Model (GP-LVM), a non-linear probabilistic variant of principal
component analysis (PCA) which implicitly assumes that the data lies on
a lower dimensional space. Having introduced the GP-LVM we will review
extensions to the algorithm, including dynamics, learning of large data
sets and back constraints. We will demonstrate the application of the
model and its extensions to a range of data sets, including human motion
data, a vowel data set and a robot mapping problem.


The following conference publications were made associated with this project.

<span class="author">N. D. Lawrence</span> (2007) <span
class="papertitle">"Learning for larger datasets with the Gaussian
process latent variable model"</span> in M. Meila and X. Shen (eds)
<span class="journal">Proceedings of the Eleventh International Workshop
on Artificial Intelligence and Statistics</span>, Omnipress, San Juan,
Puerto Rico, pp 243--250.
\[[Software](https://github.com/SheffieldML/GPmat/%20)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/gplvmLarger.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Learning+for+Larger+Datasets+with+the+Gaussian+Process+Latent+Variable+Model+&btnG=Search)\]

#### Abstract

In this paper we apply the latest techniques in sparse Gaussian process
regression (GPR) to the Gaussian process latent variable model (GP-LVM).
We review three techniques and discuss how they may be implemented in
the context of the GP-LVM. Each approach is then implemented on a well
known benchmark data set and compared with earlier attempts to sparsify
the model.


<span class="author">N. D. Lawrence and A. J. Moore. </span> (2007)
<span class="papertitle">"Hierarchical Gaussian process latent variable
models"</span> in Z. Ghahramani (ed.) <span class="journal">Proceedings
of the International Conference in Machine Learning</span>, Omnipress, ,
pp 481--488.
\[[Software](https://github.com/SheffieldML/hgplvm/%20)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/hgplvm.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Hierarchical+Gaussian+Process+Latent+Variable+Models+&btnG=Search)\]

#### Abstract

The Gaussian process latent variable model (GP-LVM) is a powerful
approach for probabilistic modelling of high dimensional data through
dimensional reduction. In this paper we extend the GP-LVM through
hierarchies. A hierarchical model (such as a tree) allows us to express
conditional independencies in the data as well as the manifold
structure. We first introduce Gaussian process hierarchies through a
simple dynamical model, we then extend the approach to a more complex
hierarchy which is applied to the visualisation of human motion data
sets.


<span class="author">C. H. Ek, P. H. Torr and N. D. Lawrence. </span>
(2008) <span class="papertitle">"Gaussian process latent variable models
for human pose estimation"</span> in A. Popescu-Belis, S. Renals and H.
Bourlard (eds) <span class="journal">Machine Learning for Multimodal
Interaction (MLMI 2007)</span>, Springer-Verlag, Brno, Czech Republic,
pp 132--143.
\[[Software](https://github.com/SheffieldML/SGPLVM/%20)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/mlmi.pdf)\]\[[DOI](http://dx.doi.org/10.1007/978-3-540-78155-4_12)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Gaussian+Process+Latent+Variable+Models+For+Human+Pose+Estimation+&btnG=Search)\]

#### Abstract

We describe a method for recovering 3D human body pose from silhouettes.
Our model is based on learning a latent space using the Gaussian Process
Latent Variable Model (GP-LVM) \[1\] encapsulating both pose and
silhouette features Our method is generative, this allows us to model
the ambiguities of a silhouette representation in a principled way. We
learn a dynamical model over the latent space which allows us to
disambiguate between ambiguous silhouettes by temporal consistency. The
model has only two free parameters and has several advantages over both
regression approaches and other generative methods. In addition to the
application shown in this paper the suggested model is easily extended
to multiple observation spaces without constraints on type.


<span class="author">C. H. Ek, J. Rihan, P. Torr, G. Rogez and N. D.
Lawrence. </span> (2008) <span class="papertitle">"Ambiguity modeling in
latent spaces"</span> in A. Popescu-Belis and R. Stiefelhagen (eds)
<span class="journal">Machine Learning for Multimodal Interaction (MLMI
2008)</span>, Springer-Verlag, , pp 62--73.
\[[Software](https://github.com/SheffieldML/SGPLVM/%20)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/mlmi2008.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Ambiguity+Modeling+in+Latent+Spaces+&btnG=Search)\]

#### Abstract

We are interested in the situation where we have two or more
representations of an underlying phenomenon. In particular we are
interested in the scenario where the representation are complementary.
This implies that a single individual representation is not sufficient
to fully discriminate a specific instance of the underlying phenomenon,
it also means that each representation is an ambiguous representation of
the other complementary spaces. In this paper we present a latent
variable model capable of consolidating multiple complementary
representations. Our method extends canonical correlation analysis by
introducing additional latent spaces that are specific to the different
representations, thereby explaining the full variance of the
observations. These additional spaces, explaining representation
specific variance, separately model the variance in a representation
ambiguous to the other. We develop a spectral algorithm for fast
computation of the embeddings and a probabilistic model (based on
Gaussian processes) for validation and inference. The proposed model has
several potential application areas, we demonstrate its use for
multi-modal regression on a benchmark human pose estimation data set.


<span class="author">R. Urtasun, D. J. Fleet, A. Geiger, J. Popović, T.
J. Darrell and N. D. Lawrence. </span> (2008) <span
class="papertitle">"Topologically-constrained latent variable
models"</span> in S. Roweis and A. Mccallum (eds) <span
class="journal">Proceedings of the International Conference in Machine
Learning</span>, Omnipress, , pp 1080-1087.
\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/topology.pdf)\]\[[DOI](http://dx.doi.org/10.1145/1390156.1390292)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Topologically-Constrained+Latent+Variable+Models+&btnG=Search)\]

#### Abstract

In dimensionality reduction approaches, the data are typically embedded
in a Euclidean latent space. However for some data sets this is
inappropriate. For example, in human motion data we expect latent spaces
that are cylindrical or a toroidal, that are poorly captured with a
Euclidean space. In this paper, we present a range of approaches for
embedding data in a non-Euclidean latent space. Our focus is the
Gaussian Process latent variable model. In the context of human motion
modeling this allows us to (a) learn models with interpretable latent
directions enabling, for example, style/content separation, and (b)
generalise beyond the data set enabling us to learn transitions between
motion styles even though such transitions are not present in the data.



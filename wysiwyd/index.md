---
layout: default
title: "WYSIWYD"
---
# WYSIWYD Project

## Overview

WYSIWYD is a research project funded by the 7th Framework Programme of
the European Commission. The project started on January 1st 2014.

The What You Say Is What You Did project (WYSIWYD) will create a new
transparency in human robot interaction (HRI) by allowing robots to both
understand their own actions and those of humans, and to interpret and
communicate these in human compatible intentional terms expressed as a
language-like communication channel we call WYSIWYD Robotese (WR).
WYSIWYD will advance this critical communication channel following a
biologically and psychologically grounded developmental perspective
allowing the robot to acquire, retain and express WR dependent on its
individual interaction history. In order to achieve transparency and
communication in HRI a number of elements must be put in place: a well
defined experimental paradigm, an integrated architecture for
perception, cognition, action and intrinsic motivation that, among other
things, provides the backbone for the acquisition of an autonomous
communication structure, a mechanism of robot self that together with
mirroring mechanisms allows for mind reading, an autobiographical memory
that compresses data streams and develops a personal narrative of the
interaction history, a conceptual space that provides for an interface
from memory to linguistic structures and their expression in speech and
communicative actions. WYSIWYD will deliver these components as elements
of an integrated architecture WR-DAC. The WYSIWYD project will advance
all these elements building on the strong track record of the project
partners in robotics, cognitive science, psychology and computational
neuroscience. WYSIWYD will contribute to a qualitative change in
human-robot interaction (HRI) and cooperation, unlocking new
capabilities and application areas together with enhanced safety,
robustness and monitoring. It is only through this step that humans will
be able to trust robots: when they say what they do and do what they
say.
The project is sponsored by [EU FP7-ICT Project Ref 612139](http://cordis.europa.eu/projects/rcn/110658_en.html) and is a collaboration with [Tony Prescott](http://www.abrg.group.shef.ac.uk/people/tony/) of University of Sheffield, [Mat Evans](http://www.abrg.group.shef.ac.uk/people/mat/) of University of Sheffield, [Paul Verschure](http://specs.upf.edu/people/331) of Universitat Pompeu Fabra, [Peter Ford Dominey](http://pfdominey.perso.sfr.fr/RobotDemos.htm) of Institute National de la Sante et de la Recherche Medicale (INSERM), [Giorgio Metta](http://pasa.liralab.it/) of Fondazione Istituto Italiano di Tecnologia, [Peter Gardenfors](http://www.fil.lu.se/en/department/staff/PeterGardenfors/) of Lunds University and [Yiannis Demiris](http://www.iis.ee.ic.ac.uk/yiannis/webcontent/HomePage.html) of Imperial College.

<a name="personnel"></a>

## Personnel from ML@SITraN

- [Andreas Damianou](A.Damianou) Post-doctoral research assistant



<a name="publications"></a>

## Publications

The following publications have provided background to our work in this project.

<span class="author">J. Hensman, N. Fusi and N. D. Lawrence. </span>
(2013) <span class="papertitle">"Gaussian processes for big data"</span>
in A. Nicholson and P. Smyth (eds) <span class="journal">Uncertainty in
Artificial Intelligence</span>, AUAI Press, .
\[[PDF](http://auai.org/uai2013/prints/papers/244.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Gaussian+Processes+for+Big+Data+&btnG=Search)\]


<span class="author">A. Damianou and N. D. Lawrence. </span> (2013)
<span class="papertitle">"Deep Gaussian processes"</span> in C. Carvalho
and P. Ravikumar (eds) <span class="journal">Proceedings of the
Sixteenth International Workshop on Artificial Intelligence and
Statistics</span>, JMLR W&CP 31, AZ, USA, pp .
\[[Software](https://github.com/SheffieldML/multigp%20)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/deepGPsAISTATS.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Deep+Gaussian+Processes+&btnG=Search)\]

#### Abstract

In this paper we introduce deep Gaussian process (GP) models. Deep GPs
are a deep belief network based on Gaussian process mappings. The data
is modeled as the output of a multivariate GP. The inputs to that
Gaussian process are then governed by another GP. A single layer model
is equivalent to a standard GP or the GP latent variable model (GP-LVM).
We perform inference in the model by approximate variational
marginalization. This results in a strict lower bound on the marginal
likelihood of the model which we use for model selection (number of
layers and nodes per layer). Deep belief networks are typically applied
to relatively large data sets using stochastic gradient descent for
optimization. Our fully Bayesian treatment allows for the application of
deep models even when data is scarce. Model selection by our variational
bound shows that a five layer hierarchy is justified even when modelling
a digit data set containing only 150 examples.


<span class="author">N. D. Lawrence</span> (2005) <span
class="papertitle">"Probabilistic non-linear principal component
analysis with Gaussian process latent variable models"</span> in <span
class="journal">Journal of Machine Learning Research</span> 6, pp
1783--1816
\[[Errata](./bibpage.cgi?keyName=Lawrence:pnpca05&printErrata=1)\]\[[C++
Software](https://github.com/SheffieldML/GPc/)\]\[[MATLAB
Software](https://github.com/SheffieldML/GPmat/)\]\[[JMLR
PDF](http://www.jmlr.org/papers/volume6/lawrence05a/lawrence05a.pdf)\]\[[JMLR
Abstract](http://www.jmlr.org/papers/v6/lawrence05a.html)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Probabilistic+Non-linear+Principal+Component+Analysis+with+Gaussian+Process+Latent+Variable+Models+&btnG=Search)\]

#### Abstract

Summarising a high dimensional data set with a low dimensional embedding
is a standard approach for exploring its structure. In this paper we
provide an overview of some existing techniques for discovering such
embeddings. We then introduce a novel probabilistic interpretation of
principal component analysis (PCA) that we term dual probabilistic PCA
(DPPCA). The DPPCA model has the additional advantage that the linear
mappings from the embedded space can easily be non-linearised through
Gaussian processes. We refer to this model as a Gaussian process latent
variable model (GP-LVM). Through analysis of the GP-LVM objective
function, we relate the model to popular spectral techniques such as
kernel PCA and multidimensional scaling. We then review a practical
algorithm for GP-LVMs in the context of large data sets and develop it
to also handle discrete valued data and missing attributes. We
demonstrate the model on a range of real-world and artificially
generated data sets.


<span class="author">N. D. Lawrence and J. C. Platt. </span> (2004)
<span class="papertitle">"Learning to learn with the informative vector
machine"</span> in R. Greiner and D. Schuurmans (eds) <span
class="journal">Proceedings of the International Conference in Machine
Learning</span>, Omnipress, , pp 512--519.
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/mtivm/%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/mtivm.ps.gz)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/mtivm.pdf)\]\[[DOI](http://dx.doi.org/10.1145/1015330.1015382)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Learning+to+Learn+with+the+Informative+Vector+Machine+&btnG=Search)\]

#### Abstract

This paper describes an efficient method for learning the parameters of
a Gaussian process (GP). The parameters are learned from multiple tasks
which are assumed to have been drawn independently from the same GP
prior. An efficient algorithm is obtained by extending the informative
vector machine (IVM) algorithm to handle the multi-task learning case.
The multi-task IVM (MT-IVM) saves computation by greedily selecting the
most informative examples from the separate tasks. The MT-IVM is also
shown to be more efficient than sub-sampling on an artificial data-set
and more effective than the traditional IVM in a speaker dependent
phoneme recognition task.


<span class="author">N. D. Lawrence, M. Seeger and R. Herbrich. </span>
(2003) <span class="papertitle">"Fast sparse Gaussian process methods:
the informative vector machine"</span> in S. Becker, S. Thrun and K.
Obermayer (eds) <span class="journal">NIPS</span>, MIT Press, Cambridge,
MA, pp 625--632.
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ivm%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/ivm.ps.gz)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Fast+Sparse+Gaussian+Process+Methods:+The+Informative+Vector+Machine+&btnG=Search)\]

#### Abstract

We present a framework for sparse Gaussian process (GP) methods which
uses forward selection with criteria based on information-theoretical
principles, previously suggested for active learning. In contrast to
most previous work on sparse GPs, our goal is not only to learn sparse
predictors (which can be evaluated in *O(d)* rather than *O(n)*,
*d&lt;&lt;n*, *n* the number of training points), but also to perform
training under strong restrictions on time and memory requirements. The
scaling of our method is at most *O(nd^2^)*, and in large real-world
classification experiments we show that it can match prediction
performance of the popular support vector machine (SVM), yet it requires
only a fraction of the training time. In contrast to the SVM, our
approximation produces estimates of predictive probabilities (\`error
bars'), allows for Bayesian model selection and is less complex in
implementation.



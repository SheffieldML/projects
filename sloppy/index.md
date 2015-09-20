---
layout: default
---

Learning Classifiers from Sloppily Labelled Data
================================================

Overview
--------

This project was about learning classification decision boundaries when
careful labelling of the data set is required. It was originally
inspired by [joint work with Bernhard Schoelkopf](#Lawrence:noisy01) on
images.

Key contributions of the project were:

-   An approach to learning kernel parameters in kernel Fisher's
    discriminant described in [this JMLR paper](#Pena:fbd04).
-   An approach to semi-supervised learning in Gaussian processes which
    allows free choice of kernel, first presented in [this NIPS
    paper](#Lawrence:semisuper04).
-   An approximation for Gaussian process classification which allows
    practical learning of large data sets described in this [this NIPS
    paper](#Lawrence:ivm02).

Informal collaborations with [Michael
Jordan](http://www.cs.berkeley.edu/~jordan/), [Ralf
Herbrich](http://www.research.microsoft.com/~rherb) and [Matthias
Seeger](http://www.kyb.tuebingen.mpg.de/bs/people/seeger) were an
important part of the project.

The project is sponsored by [EPSRC Grant no
GR/R84801/01](http://www.epsrc.ac.uk).

Personnel at Sheffield
----------------------

  ---------------------------------------------------------------------------------------------------
  [Tonatiuh Peña-Centeno](http://www.dcs.sheffield.ac.uk/cgi-bin/makeperson?T.Centeno), PhD Student
  ---------------------------------------------------------------------------------------------------

Software
--------

The following software has been made available either wholly or partly
as a result of work on this project:

  -----------------------------------------------------------------------------------------------------
  [Bayesian interpretation of kernel Fisher's discriminants.](http://ml.sheffield.ac.uk//~neil/bfd)
  [Semi-supervised learning for Gaussian process classifiers.](http://ml.sheffield.ac.uk//~neil/ncnm)
  [Sparse approximation for Gaussian process classifiers.](http://ml.sheffield.ac.uk//~neil/ivm)
  -----------------------------------------------------------------------------------------------------

Publications
------------

The following publications have provided background to our work in this
project.

### Journal Papers

<span class="author">T. Peña-Centeno and N. D. Lawrence. </span> (2006)
<span class="papertitle">"Optimising kernel parameters and
regularisation coefficients for non-linear discriminant analysis"</span>
in <span class="journal">Journal of Machine Learning Research</span> 7,
pp 455--491 An earlier version is available as technical report number
CS-04-13, see
[\[Pena:fbd-tech04\]](/~neil/cgi-bin/publications/bibpage.cgi?keyName=Pena:fbd-tech04&printAbstract=1).\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/bfd/%20)\]\[[PDF](http://www.jmlr.org/papers/volume7/centeno06a/centeno06a.pdf)\]\[[JMLR
Abstract](http://www.jmlr.org/papers/v7/centeno06a.html)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Optimising+Kernel+Parameters+and+Regularisation+Coefficients+for+Non-linear+Discriminant+Analysis+&btnG=Search)\]
#### Abstract

In this paper we consider a novel Bayesian interpretation of Fisher's
discriminiant analysis. We relate Rayleigh's coefficient to a noise
model that minimizes a cost based on the most probable class centres and
that abandons the \`regression to the labels' assumption used by other
algorithms. This yields a direction of discrimination equivalent to
Fisher's discriminant. We use Bayes' rule to infer the posterior
distribution for the direction of discrimination and in this process,
priors and constraining distributions are incorporated to reach the
desired result. Going further, with the use of a Gaussian process prior
we show the equivalence of our model to a regularised kernel Fisher's
discriminant. A key advantage of our approach is the facility to
determine kernel parameters and the regularisation coefficient through
the optimisation of the marginal log-likelihood of the data. An added
bonus of the new formulation is that it enables us to link the
regularisation coefficient with the generalisation error.

------------------------------------------------------------------------

### NIPS Papers

<span class="author">N. D. Lawrence, M. Seeger and R. Herbrich. </span>
(2003) <span class="papertitle">"Fast sparse Gaussian process methods:
the informative vector machine"</span> in S. Becker, S. Thrun and K.
Obermayer (eds) <span class="journal">Advances in Neural Information
Processing Systems</span>, MIT Press, Cambridge, MA, pp 625--632.
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

------------------------------------------------------------------------

<span class="author">N. D. Lawrence and M. I. Jordan. </span> (2005)
<span class="papertitle">"Semi-supervised learning via Gaussian
processes"</span> in L. Saul, Y. Weiss and L. Bouttou (eds) <span
class="journal">Advances in Neural Information Processing
Systems</span>, MIT Press, Cambridge, MA, pp 753--760.
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ncnm/%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/ncnm.ps.gz)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Semi-supervised+Learning+via+Gaussian+Processes+&btnG=Search)\]
#### Abstract

We present a probabilistic approach to learning a Gaussian Process
classifier in the presence of unlabeled data. Our approach involves a
"null category noise model" (NCNM) inspired by ordered categorical noise
models. The noise model reflects an assumption that the data density is
lower between the class-conditional densities. We illustrate our
approach on a toy problem and present comparative results for the
semi-supervised classification of handwritten digits.

------------------------------------------------------------------------

### Other Conferences

<span class="author">N. D. Lawrence and B. Schölkopf. </span> (2001)
<span class="papertitle">"Estimating a kernel Fisher discriminant in the
presence of label noise"</span> in C. Brodley and A. P. Danyluk (eds)
<span class="journal">Proceedings of the International Conference in
Machine Learning</span>, Morgan Kauffman, San Francisco, CA.
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/nkfd/%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/noisyfisher.ps.gz)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Estimating+a+Kernel+Fisher+Discriminant+in+the+Presence+of+Label+Noise+&btnG=Search)\]
#### Abstract

Data noise is present in many machine learning problems domains, some of
these are well studied but others have received less attention. In this
paper we propose an algorithm for constructing a kernel Fisher
discriminant (KFD) from training examples with *noisy labels*. The
approach allows to associate with each example a probability of the
label being flipped. We utilise an expectation maximization (EM)
algorithm for updating the probabilities. The E-step uses class
conditional probabilities estimated as a by-product of the KFD
algorithm. The M-step updates the flip probabilities and determines the
parameters of the discriminant. We have applied the approach to two
real-world data-sets. The results show the feasibility of the approach.

------------------------------------------------------------------------

### Book Chapters

<span class="author">N. D. Lawrence, J. C. Platt and M. I. Jordan.
</span> (2005) <span class="papertitle">"Extensions of the informative
vector machine"</span> in J. Winkler, N. D. Lawrence and M. Niranjan
(eds) <span class="journal">Deterministic and Statistical Methods in
Machine Learning</span>, Springer-Verlag, Berlin, pp 56--87.
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ivm/%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/ivmdev.ps.gz)\]\[[Springer
Site](http://www.springeronline.com/3-540-29073-7)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Extensions+of+the+Informative+Vector+Machine+&btnG=Search)\]
#### Abstract

The informative vector machine (IVM) is a practical method for Gaussian
process regression and classification. The IVM produces a sparse
approximation to a Gaussian process by combining assumed density
filtering with a heuristic for choosing points based on minimizing
posterior entropy. This paper extends IVM in several ways. First, we
propose a novel noise model that allows the IVM to be applied to a
mixture of labeled and unlabeled data. Second, we use IVM on a
block-diagonal covariance matrix, for "learning to learn" from related
tasks. Third, we modify the IVM to incorporate prior knowledge from
known invariances. All of these extensions are tested on artificial and
real data.

------------------------------------------------------------------------

<span class="author">N. D. Lawrence and M. I. Jordan. </span> (2006)
<span class="papertitle">"Gaussian processes and the null-category noise
model"</span> in O. Chapelle, B. Schölkopf and A. Zien (eds) <span
class="journal">Semi-supervised Learning</span>, MIT Press, Cambridge,
MA, pp 152--165. \[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/gpncnm.ps)\]\[[MATLAB
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ncnm/)\]\[[C++
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ivmcpp/)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Gaussian+Processes+and+the+Null-Category+Noise+Model+&btnG=Search)\]
#### Abstract

With Gaussian process classifiers (GPC) we aim to predict the posterior
probability of the class labels given an input data point,
*p(y~i~|x~i~)*. In general we find that this posterior distribution is
unaffected by unlabeled data points during learning. Support vector
machines are strongly related to GPCs, but one notable difference is
that the decision boundary in an SVM can be influenced by unlabeled
data. The source of this discrepancy is the SVM's margin: a
characteristic which is not shared with the GPC. The presence of the
marchin allows the support vector machine to seek low data density
regions for the decision boundary, effectively allowing it to
incorporate the cluster assumption (see Chapter 6). In this chapter we
present the *null category noise model*. A probabilistic equivalent of
the margin. By combining this noise model with a GPC we are able to
incorporated the cluster assumption without explicitly modeling the
input data density distributions and without a special choice of kernel.

------------------------------------------------------------------------

### Technical Reports

<span class="author">T. Peña-Centeno and N. D. Lawrence. </span> (2004)
<span class="papertitle">"Optimising kernel parameters and
regularisation coefficients for non-linear discriminant analysis"</span>
Technical Report no CS-04-13, The University of Sheffield, Department of
Computer Science.
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/bfd/%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/bfdPaper.ps.gz)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Optimising+Kernel+Parameters+and+Regularisation+Coefficients+for+Non-linear+Discriminant+Analysis+&btnG=Search)\]
#### Abstract

In this paper we consider a Bayesian interpretation of Fisher's
discriminant. By relating Rayleigh's coefficient to a likelihood
function and through the choice of a suitable prior we use Bayes' rule
to infer a posterior distribution over projections. Through the use of a
Gaussian process prior we show the equivalence of our model to a
regularised kernel Fisher's discriminant. A key advantage of our
approach is the facility to determine kernel parameters and the
regularisation coefficient through optimisation of the marginalised
likelihood of the data.

------------------------------------------------------------------------

<span class="author">N. D. Lawrence, M. Seeger and R. Herbrich. </span>
(2004) <span class="papertitle">"The informative vector machine: a
practical probabilistic alternative to the support vector
machine"</span> Technical Report no CS-04-07, Department of Computer
Science, University of Sheffield. Last updated December 2005 \[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/ivmTechreport.ps.gz)\]\[[Matlab
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ivm/)\]\[[C++
Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/ivmcpp/)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=The+Informative+Vector+Machine:+A+Practical+Probabilistic+Alternative+to+the+Support+Vector+Machine+&btnG=Search)\]
#### Abstract

We present a practical probabilistic alternative to the popular support
vector machine (SVM). The algorithm is an approximation to a Gaussian
process, and is probabilistic in the sense that it maintains the process
variance that is implied by the use of a kernel function, which the SVM
discards. We show that these variances may be tracked and made use of
selection of an active set which gives a sparse representation for the
model. For an active set size of *d* our algorithm exhibits *O(d^2^N)*
computational complexity and *O(dN)* storage requirements. It has
already been shown that the approach is comptetive with the SVM in terms
of performance and running time, here we give more details of the
approach and demonstrate that kernel parameters may also be learned in a
practical and effective manner.

------------------------------------------------------------------------


---
layout: default
title: "TIGRE"
---
# TIGRE Project

## Overview

Our goal in this project was to develop and apply new methods for
inferring the parameters of mechanistic models of biological systems and
to apply these methods to uncover the mechanisms of transcriptional
regulation. This goal was be achieved by unifying two disparate
approaches to network analysis: the systems biology approach of
specifying differential equation models of transcription (see this
[book](#Alon:systems06)), and the statistical/machine learning approach
of constructing probabilistic models of the data (see Related Papers
below). Our approach was to infer the parameters of differential
equation models through constructing probabilistic models which respect
the relationships specified by the differential equation. This was
achieved by combining information from gene expression time series data
with differential equation models of transcriptional regulation. The
advantage of using probabilistic models is that we can simultaneously
handle uncertainty in the model parameters along with experimental and
biological noise.

### Objectives

1.  Process the expression data from the Drosophila blastoderm and
    construct differential equation models of the underlying processes
    by generalising equations developed previously by Jaeger et al.

    The expression data processing and development of the models was
    undertaken at the Nottingham site. The Manchester site developed
    models for mesoderm development in Drosophila whilst awaiting the
    data and in recent submissions (Titsias et al, PLoS Computational
    Biology, under review) have developed the Markov Chain Monte Carlo
    framework for inference in these models and a linearization of the
    model with initial conditions determined by Gaussian processes
    (Alvarez et al, TPAMI, submission imminent).

2.  Adapt the preliminary work to account for non-linear response models
    and more complicated network motifs.We will expand the Gaussian
    process methodology we have developed beyond the single input
    module motif. We will consider other network motifs such as feed
    forward loops and dense overlapping regions. We will integrate
    transcriptional delays within the model.
    The nonlinear framework under review allows for time delays and
    multiple input transcription factors. The framework relies on the
    Markov chain Monte Carlo approach described in [this NIPS
    paper](#Titsias:mcmcgp11) and [this book
    chapter](#Titsias:mcmcgp11).
3.  Develop Monte Carlo Sampling methods We will develop the Monte Carlo
    methods, both as a gold standard for comparison with our
    approximations and as a practical approach for parameter inference.
    We developed Monte Carlo approaches and an approach based on the
    Laplace approximation. For the non-linear models the Monte Carlo
    approach proved efficient enough to act as a practical substitute
    for the Laplace approximation. Implementation was also easier as the
    second order derivatives for the Monte Carlo approach are
    not required.
4.  Variational Approximations: We will develop and validate Gaussian
    process variational approximations for the systems of interest. Such
    approximations are typically faster than Monte Carlo sampling and
    are far easier to monitor as far as convergence is concerned.
    We developed a range of variational approximations for Gaussian
    process models derived from differential equations. These techniques
    also apply more genericaly to multiple output Gaussian processes.
    They included [this NIPS paper](#Alvarez:convolved08), [this AISTATS
    paper](#Titsias:variational09), [this JMLR
    paper](#Alvarez:computationally11) and [this AISTATS
    paper](#Alvarez:efficient10).
5.  Validation of Techniques Against Drosophila data: We will develop
    models of the gap gene network involved in the blastoderm
    development stage of Drosophila. Parameter inference in these models
    will be undertaken by the methodologies developed in the
    objectives above. Since the protein concentrations are known in this
    Drosophila system it can be used as a validation data set for the
    techniques we develop.
    In our [PNAS paper](#Honkela:modelbased10) we validated our
    techniques against ChIP-chip studies on Drosophila mesoderm. Our
    latest studies in preparation and review are also being compared to
    the Drosophila mesoderm, as well as the blastoderm.

### Highlighted Achievements

-   We developed an approach to ranking targets of a transcription
    factor through a linear differential models of transcription
    and translation. (see DISIMRANK software below, this [PNAS
    paper](#Honkela:modelbased10) and [this Bioconductor
    package](http://www.bioconductor.org/packages/2.6/bioc/html/tigre.html)).
-   We provided software implementations of our algorithms for linear
    response through [Bioconductor](http://www.bioconductor.org) as the
    TIGRE package.
-   We developed an approach to inferring protein concentration given
    the gene expression of known targets in a single input motif. (see
    GPSIM software below, this [NIPS
    paper](#Lawrence:transcriptionalGP06) and this [ECCB
    paper](#Gao:latent08)).
-   We developed a range of approaches for efficient computation in
    multiple-output Gaussian process models. The first relied on
    conditional independence assumptions (see this [NIPS
    paper](#Alvarez:convolved08) and this [JMLR
    paper](#Alvarez:computationally11)).
-   We pioneered a new class of approximation techniques for Gaussian
    processes in general based on a variational approximation to
    the posterior. We showed how this could be done for single output
    Gaussian processes with a NIPS paper and how the approach could be
    extended to multiple output Gaussian processes with an [AISTATS
    paper](#Alvarez:efficient10).
-   For non-linear response models we showed how sampling can be done
    efficiently using Gaussian processes even when the posterior over
    the GP is strongly correlated (see this [NIPS
    paper](#Titsias:efficient08) and this [book
    chapter](#Titsias:mcmcgp11))
-   With collaborators we composed a [collected
    volume](#Lawrence:licsb10) of papers in this area.
-   We were invited to contribute to two further collected volumes, one
    on Bayesian inference in time series models and the other is the
    imminent "Handbook of Systems Biology" edited by Mark Girolami and
    Michael Stumpf and soon to be published by Springer.
-   We organized four workshops, three in a new series "Learning and
    Inference in Computational Systems Biology" and one in "Machine
    Learning in Systems Biology".
-   The EPSRC funding covered a post-doctoral researcher in Manchester
    and a year's post-doctoral research in Nottingham. This was
    augmented by a visitor from Finland, funded by the EU under the FP7
    PASCAL2 Network of Excellence and a PhD student funded by the School
    of Computer Science at the University of Manchester.
-   Three follow on grants have so far been awarded which depend in some
    part the ideas developed in this project. Two from the BBSRC (Grant
    numbers BB/H018123/2 and BB/I004769/2, the second of which is a
    Europe-wide consortium under the ERASysBio Plus scheme) and one from
    the EU under FP7: "BioPreDyn-From Data to Models: New Bioinformatics
    Methods and Tools for Data-Driven Predictive Dynamic Modelling in
    Biotechnological Applications".

The project is sponsored by [EPSRC Project Ref EP/F005687/1](http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/F005687/1) and is a collaboration with [Dr Nick Monk](http://www.maths.nottingham.ac.uk/personal/nm/) of University of Nottingham, [Dr Johannes Jaeger](http://www.crg.es/johannes_jaeger) of CRG and [Dr Antti Honkela](http://www.cis.hut.fi/ahonkela/) of Helsinki University of Technology (visitor and collaborator).

<a name="personnel"></a>

## Personnel from ML@SITraN

- [Michalis Titsias](http://www.aueb.gr/users/mtitsias/) Post-doctoral research assistant

- [Mauricio Alvarez](https://sites.google.com/site/maalvarezl/) PhD student



<a name="software"></a>

## Software

The following software has been made available either wholly or partly as a result of work on this project:- [gpsim](http://inverseprobability.com/gpsim/) GPSIM: Gaussian Process Modelling of single input module motif networks.

- [multigp](http://sheffieldml.github.io/multigp) MULTIGP: Modelling multiple outputs with Gaussian processes (will eventually supercede the gpsim toolbox).

- [disimrank](http://sheffieldml.github.io/disimrank) DISIMRANK: Ranking potential targets using a driven input single input model motif.

<a name="publications"></a>

## Publications

The following conference publications were made associated with this project.

<span class="author">M. A. Álvarez, D. Luengo, M. K. Titsias and N. D.
Lawrence. </span> (2010) <span class="papertitle">"Efficient multioutput
Gaussian processes through variational inducing kernels"</span> in Y. W.
Teh and D. M. Titterington (eds) <span class="journal">Proceedings of
the Thirteenth International Workshop on Artificial Intelligence and
Statistics</span>, JMLR W&CP 9, Chia Laguna Resort, Sardinia, Italy, pp
25--32.
\[[Software](https://github.com/SheffieldML/multigp%20)\]\[[PDF](http://jmlr.csail.mit.edu/proceedings/papers/v9/alvarez10a/alvarez10a.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Efficient+Multioutput+Gaussian+Processes+through+Variational+Inducing+Kernels+&btnG=Search)\]

#### Abstract

Interest in multioutput kernel methods is increasing, whether under the
guise of multitask learning, multisensor networks or structured output
data. From the Gaussian process perspective a multioutput Mercer kernel
is a covariance function over correlated output functions. One way of
constructing such kernels is based on convolution processes (CP). A key
problem for this approach is efficient inference. Álvarez and Lawrence
[\[Alvarez:convolved08\]](/~neil/cgi-bin/publications/bibpage.cgi?keyName=Alvarez:convolved08&printAbstract=1)
recently presented a sparse approximation for CPs that enabled efficient
inference. In this paper, we extend this work in two directions: we
introduce the concept of variational inducing functions to handle
potential non-smooth functions involved in the kernel CP construction
and we consider an alternative approach to approximate inference based
on variational methods, extending the work by Titsias
[\[Titsias:variational09\]](/~neil/cgi-bin/publications/bibpage.cgi?keyName=Titsias:variational09&printAbstract=1)
to the multiple output case. We demonstrate our approaches on prediction
of school marks, compiler performance and financial time series.


<span class="author">M. A. Álvarez, D. Luengo and N. D. Lawrence.
</span> (2009) <span class="papertitle">"Latent force models"</span> in
D. van Dyk and M. Welling (eds) <span class="journal">Proceedings of the
Twelfth International Workshop on Artificial Intelligence and
Statistics</span>, JMLR W&CP 5, Clearwater Beach, FL, pp 9--16.
\[[Software](https://github.com/SheffieldML/multigp%20)\]\[[PDF](http://jmlr.csail.mit.edu/proceedings/papers/v5/alvarez09a/alvarez09a.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Latent+Force+Models+&btnG=Search)\]

#### Abstract

Purely data driven approaches for machine learning present difficulties
when data is scarce relative to the complexity of the model or when the
model is forced to extrapolate. On the other hand, purely mechanistic
approaches need to identify and specify all the interactions in the
problem at hand (which may not be feasible) and still leave the issue of
how to parameterize the system. In this paper, we present a hybrid
approach using Gaussian processes and differential equations to combine
data driven modeling with a physical model of the system. We show how
different, physically-inspired, kernel functions can be developed
through sensible, simple, mechanistic assumptions about the underlying
system. The versatility of our approach is illustrated with three case
studies from computational biology, motion capture and geostatistics.


<span class="author">M. K. Titsias</span> (2009) <span
class="papertitle">"Variational learning of inducing variables in sparse
Gaussian processes"</span> in D. van Dyk and M. Welling (eds) <span
class="journal">Proceedings of the Twelfth International Workshop on
Artificial Intelligence and Statistics</span>, JMLR W&CP 5, Clearwater
Beach, FL, pp 567--574. \[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Variational+Learning+of+Inducing+Variables+in+Sparse+Gaussian+Processes+&btnG=Search)\]


<span class="author">M. A. Álvarez and N. D. Lawrence. </span> (2009)
<span class="papertitle">"Sparse convolved Gaussian processes for
multi-output regression"</span> in D. Koller, D. Schuurmans, Y. Bengio
and L. Bottou (eds) <span class="journal">NIPS</span>, MIT Press,
Cambridge, MA, pp 57--64.
\[[Software](https://github.com/SheffieldML/multigp/%20)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/spmulti.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Sparse+Convolved+Gaussian+Processes+for+Multi-output+Regression+&btnG=Search)\]

#### Abstract

We present a sparse approximation approach for dependent output Gaussian
processes (GP). Employing a latent function framework, we apply the
convolution process formalism to establish dependencies between output
variables, where each latent function is represented as a GP. Based on
these latent functions, we establish an approximation scheme using a
conditional independence assumption between the output processes,
leading to an approximation of the full covariance which is determined
by the locations at which the latent functions are evaluated. We show
results of the proposed methodology for synthetic data and real world
applications on pollution prediction and a sensor network.


<span class="author">M. K. Titsias, N. D. Lawrence and M. Rattray.
</span> (2009) <span class="papertitle">"Efficient sampling for Gaussian
process inference using control variables"</span> in D. Koller, D.
Schuurmans, Y. Bengio and L. Bottou (eds) <span
class="journal">NIPS</span>, MIT Press, Cambridge, MA, pp 1681--1688.
\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/nipsSamGP08.pdf},)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Efficient+Sampling+for+Gaussian+Process+Inference+using+Control+Variables+&btnG=Search)\]

#### Abstract

Sampling functions in Gaussian process (GP) models is challenging
because of the highly correlated posterior distribution. We describe an
efficient Markov chain Monte Carlo algorithm for sampling from the
posterior process of the GP model. This algorithm uses control variables
which are auxiliary function values that provide a low dimensional
representation of the function. At each iteration, the algorithm
proposes new values for the control variables and generates the function
from the conditional GP prior. The control variable input locations are
found by continuously minimizing an objective function. We demonstrate
the algorithm on regression and classification problems and we use it to
estimate the parameters of a differential equation model of gene
regulation.


<span class="author">N. D. Lawrence, G. Sanguinetti and M. Rattray.
</span> (2007) <span class="papertitle">"Modelling transcriptional
regulation using Gaussian processes"</span> in B. Schölkopf, J. C. Platt
and T. Hofmann (eds) <span class="journal">NIPS</span>, MIT Press,
Cambridge, MA, pp 785--792.
\[[Errata](./bibpage.cgi?keyName=Lawrence:transcriptionalGP06&printErrata=1)\]\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/gpsim/%20)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/gpsim.ps.gz)\]\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/gpsim.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Modelling+transcriptional+regulation+using+Gaussian+Processes+&btnG=Search)\]

#### Abstract

Modelling the dynamics of transcriptional processes in the cell requires
the knowledge of a number of key biological quantities. While some of
them are relatively easy to measure, such as mRNA decay rates and mRNA
abundance levels, it is still very hard to measure the active
concentration levels of the transcription factor proteins that drive the
process and the sensitivity of target genes to these concentrations. In
this paper we show how these quantities for a given transcription factor
can be inferred from gene expression levels of a set of known target
genes. We treat the protein concentration as a latent function with a
Gaussian Process prior, and include the sensitivities, mRNA decay rates
and baseline expression levels as hyperparameters. We apply this
procedure to a human leukemia dataset, focusing on the tumour repressor
p53 and obtaining results in good accordance with recent biological
studies.


The following books were published as part of this project.

N. D. Lawrence, M. Girolami, M. Rattray and G. Sanguinetti (eds) (2010)
<span class="papertitle">"Learning and inference in computational
systems biology"</span>, MIT Press, Cambridge, MA.

#### Synopsis

Computational systems biology aims to develop algorithms that uncover
the structure and parameterization of the underlying mechanistic
model—in other words, to answer specific questions about the underlying
mechanisms of a biological system—in a process that can be thought of as
learning or inference. This volume offers state-of-the-art perspectives
from computational biology, statistics, modeling, and machine learning
on new methodologies for learning and inference in biological networks.
The chapters offer practical approaches to biological inference problems
ranging from genome-wide inference of genetic regulation to
pathway-specific studies. Both deterministic models (based on ordinary
differential equations) and stochastic models (which anticipate the
increasing availability of data from small populations of cells) are
considered. Several chapters emphasize Bayesian inference, so the
editors have included an introduction to the philosophy of the Bayesian
approach and an overview of current work on Bayesian inference. Taken
together, the methods discussed by the experts in Learning and Inference
in Computational Systems Biology provide a foundation upon which the
next decade of research in systems biology can be built.


<span class="author">M. A. Álvarez and N. D. Lawrence. </span> (2011)
<span class="papertitle">"Computationally efficient convolved multiple
output Gaussian processes"</span> in <span class="journal">Journal of
Machine Learning Research</span> 12, pp 1425--1466
\[[Software](https://github.com/SheffieldML/multigp%20)\]\[[PDF](http://www.jmlr.org/papers/volume12/alvarez11a/alvarez11a.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Computationally+Efficient+Convolved+Multiple+Output+Gaussian+Processes+&btnG=Search)\]

#### Abstract

Recently there has been an increasing interest in regression methods
that deal with multiple outputs. This has been motivated partly by
frameworks like multitask learning, multisensor networks or structured
output data. From a Gaussian processes perspective, the problem reduces
to specifying an appropriate covariance function that, whilst being
positive semi-definite, captures the dependencies between all the data
points and across all the outputs. One approach to account for
non-trivial correlations between outputs employs convolution processes.
Under a latent function interpretation of the convolution transform we
establish dependencies between output variables. The main drawbacks of
this approach are the associated computational and storage demands. In
this paper we address these issues. We present different efficient
approximations for dependent output Gaussian processes constructed
through the convolution formalism. We exploit the conditional
independencies present naturally in the model. This leads to a form of
the covariance similar in spirit to the so called PITC and FITC
approximations for a single output. We show experimental results with
synthetic and real data, in particular, we show results in school exams
score prediction, pollution prediction and gene expression data


<span class="author">A. Honkela, C. Girardot, E. H. Gustafson, Y.a.H.
Liu, E. E. M. Furlong, N. D. Lawrence and M. Rattray. </span> (2010)
<span class="papertitle">"Model-based method for transcription factor
target identification with limited data"</span> in <span
class="journal">Proc. Natl. Acad. Sci. USA</span> 107 (17), pp
7793--7798
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/disimrank%20)\]\[[DOI](http://dx.doi.org/10.1073/pnas.0914285107)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Model-based+Method+for+Transcription+Factor+Target+Identification+with+Limited+Data+&btnG=Search)\]

#### Abstract

We present a computational method for identifying potential targets of a
transcription factor (TF) using wild-type gene expression time series
data. For each putative target gene we fit a simple differential
equation model of transcriptional regulation, and the model likelihood
serves as a score to rank targets. The expression profile of the TF is
modeled as a sample from a Gaussian process prior distribution that is
integrated out using a nonparametric Bayesian procedure. This results in
a parsimonious model with relatively few parameters that can be applied
to short time series datasets without noticeable overfitting. We assess
our method using genome-wide chromatin immunoprecipitation (ChIP-chip)
and loss-of-function mutant expression data for two TFs, Twist, and
Mef2, controlling mesoderm development in Drosophila. Lists of
top-ranked genes identified by our method are significantly enriched for
genes close to bound regions identified in the ChIP-chip data and for
genes that are differentially expressed in loss-of-function mutants.
Targets of Twist display diverse expression profiles, and in this case a
model-based approach performs significantly better than scoring based on
correlation with TF expression. Our approach is found to be comparable
or superior to ranking based on mutant differential expression scores.
Also, we show how integrating complementary wild-type spatial expression
data can further improve target ranking performance.


<span class="author">P. Gao, A. Honkela, M. Rattray and N. D. Lawrence.
</span> (2008) <span class="papertitle">"Gaussian process modelling of
latent chemical species: applications to inferring transcription factor
activities"</span> in <span class="journal">Bioinformatics</span> 24, pp
i70--i75
\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/gpsim/%20)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/24/16/i70.pdf?ijkey=FauSn114lAUC1Ey&keytype=ref)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btn278)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Gaussian+Process+Modelling+of+Latent+Chemical+Species:+Applications+to+Inferring+Transcription+Factor+Activities+&btnG=Search)\]

#### Abstract

**Motivation:** Inference of *latent chemical species* in biochemical
interaction networks is a key problem in estimation of the structure and
parameters of the genetic, metabolic and protein interaction networks
that underpin all biological processes. We present a framework for
Bayesian marginalisation of these latent chemical species through
Gaussian process priors.\
\
 **Results:** We demonstrate our general approach on three different
biological examples of single input motifs, including both activation
and repression of transcription. We focus in particular on the problem
of inferring transcription factor activity when the concentration of
active protein cannot easily be measured. We show how the uncertainty in
the inferred transcription factor activity can be integrated out in
order to derive a likelihood function that can be used for the
estimation of regulatory model parameters. An advantage of our approach
is that we avoid the use of a coarse-grained discretization of
continuous-time functions, which would lead to a large number of
additional parameters to be estimated. We develop efficient exact and
approximate inference schemes, which are much more efficient than
competing sampling-based schemes and therefore provide us with a
practical toolkit for model-based inference.\
\
 **Availability:** The software and data for recreating all the
experiments in this paper is available in MATLAB from
<http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/gpsim>\
\
 **Contact:** Neil Lawrence


The following edited chapters were published as part of this project.

<span class="author">N. D. Lawrence</span> (2010) <span
class="papertitle">"Introduction to learning and inference in
computational systems biology"</span> in N. D. Lawrence, M. Girolami, M.
Rattray and G. Sanguinetti (eds) <span class="journal">Learning and
Inference in Computational Systems Biology</span>, MIT Press, Cambridge,
MA. \[[MIT Press
Site](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=12092)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Introduction+to+Learning+and+Inference+in+Computational+Systems+Biology+&btnG=Search)\]

#### Abstract

Computational systems biology aims to develop algorithms that uncover
the structure and parameterization of the underlying mechanistic
model—in other words, to answer specific questions about the underlying
mechanisms of a biological system—in a process that can be thought of as
learning or inference. This volume offers state-of-the-art perspectives
from computational biology, statistics, modeling, and machine learning
on new methodologies for learning and inference in biological networks.
The chapters offer practical approaches to biological inference problems
ranging from genome-wide inference of genetic regulation to
pathway-specific studies. Both deterministic models (based on ordinary
differential equations) and stochastic models (which anticipate the
increasing availability of data from small populations of cells) are
considered. Several chapters emphasize Bayesian inference, so the
editors have included an introduction to the philosophy of the Bayesian
approach and an overview of current work on Bayesian inference. Taken
together, the methods discussed by the experts in Learning and Inference
in Computational Systems Biology provide a foundation upon which the
next decade of research in systems biology can be built.


<span class="author">N. D. Lawrence and M. Rattray. </span> (2010) <span
class="papertitle">"A brief introduction to Bayesian inference"</span>
in N. D. Lawrence, M. Girolami, M. Rattray and G. Sanguinetti (eds)
<span class="journal">Learning and Inference in Computational Systems
Biology</span>, MIT Press, Cambridge, MA. \[[MIT Press
Site](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=12092)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=A+Brief+Introduction+to+Bayesian+Inference+&btnG=Search)\]

#### Abstract

Computational systems biology aims to develop algorithms that uncover
the structure and parameterization of the underlying mechanistic
model—in other words, to answer specific questions about the underlying
mechanisms of a biological system—in a process that can be thought of as
learning or inference. This volume offers state-of-the-art perspectives
from computational biology, statistics, modeling, and machine learning
on new methodologies for learning and inference in biological networks.
The chapters offer practical approaches to biological inference problems
ranging from genome-wide inference of genetic regulation to
pathway-specific studies. Both deterministic models (based on ordinary
differential equations) and stochastic models (which anticipate the
increasing availability of data from small populations of cells) are
considered. Several chapters emphasize Bayesian inference, so the
editors have included an introduction to the philosophy of the Bayesian
approach and an overview of current work on Bayesian inference. Taken
together, the methods discussed by the experts in Learning and Inference
in Computational Systems Biology provide a foundation upon which the
next decade of research in systems biology can be built.


<span class="author">N. D. Lawrence, M. Rattray, P. Gao and M. K.
Titsias. </span> (2010) <span class="papertitle">"Gaussian processes for
missing species in biochemical systems"</span> in N. D. Lawrence, M.
Girolami, M. Rattray and G. Sanguinetti (eds) <span
class="journal">Learning and Inference in Computational Systems
Biology</span>, MIT Press, Cambridge, MA.
\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=18689843&dopt=Citation)\]\[[MIT
Press
Site](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=12092)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Gaussian+Processes+for+Missing+Species+in+Biochemical+Systems+&btnG=Search)\]

#### Abstract

Computational systems biology aims to develop algorithms that uncover
the structure and parameterization of the underlying mechanistic
model—in other words, to answer specific questions about the underlying
mechanisms of a biological system—in a process that can be thought of as
learning or inference. This volume offers state-of-the-art perspectives
from computational biology, statistics, modeling, and machine learning
on new methodologies for learning and inference in biological networks.
The chapters offer practical approaches to biological inference problems
ranging from genome-wide inference of genetic regulation to
pathway-specific studies. Both deterministic models (based on ordinary
differential equations) and stochastic models (which anticipate the
increasing availability of data from small populations of cells) are
considered. Several chapters emphasize Bayesian inference, so the
editors have included an introduction to the philosophy of the Bayesian
approach and an overview of current work on Bayesian inference. Taken
together, the methods discussed by the experts in Learning and Inference
in Computational Systems Biology provide a foundation upon which the
next decade of research in systems biology can be built.


<span class="author">M. K. Titsias, M. Rattray and N. D. Lawrence.
</span> (2011) <span class="papertitle">"Markov chain Monte Carlo
algorithms for Gaussian processes"</span> in D. Barber, A. T. Cemgil and
S. Chiappa (eds) <span class="journal">Bayesian Time Series
Models</span>, Cambridge University Press, . \[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Markov+chain+Monte+Carlo+algorithms+for+Gaussian+processes+&btnG=Search)\]

#### Abstract

\`What's going to happen next?' Time series data hold the answers, and
Bayesian methods represent the cutting edge in learning what they have
to say. This ambitious book is the first unified treatment of the
emerging knowledge-base in Bayesian time series techniques. Exploiting
the unifying framework of probabilistic graphical models, the book
covers approximation schemes, both Monte Carlo and deterministic, and
introduces switching, multi-object, non-parametric and agent-based
models in a variety of application environments. It demonstrates that
the basic framework supports the rapid creation of models tailored to
specific applications and gives insight into the computational
complexity of their implementation. The authors span traditional
disciplines such as statistics and engineering and the more recently
established areas of machine learning and pattern recognition. Readers
with a basic understanding of applied probability, but no experience
with time series analysis, are guided from fundamental concepts to the
state-of-the-art in research and practice.


The following publications have provided background to our work in this project.

<span class="author">G. Della Gatta, M. Bansal, A. A.i.Impiombato, D.
Antonini, C. Missero and D. d. Bernardo. </span> (2008) <span
class="papertitle">"Direct targets of the trp63 transcription factor
revealed by a combination of gene expression profiling and reverse
engineering"</span> in <span class="journal">Genome Research</span> 18
(6), pp 939--948
\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=18441228&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1101/gr.073601.107)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Direct+Targets+of+the+TRP63+transcription+Factor+Revealed+by+a+Combination+of+Gene+Expression+Profiling+and+Reverse+Engineering+&btnG=Search)\]

#### Abstract

Genome-wide identification of bona-fide targets of transcription factors
in mammalian cells is still a challenge. We present a novel integrated
computational and experimental approach to identify direct targets of a
transcription factor. This consists of measuring time-course (dynamic)
gene expression profiles upon perturbation of the transcription factor
under study, and in applying a novel "reverse-engineering" algorithm
(TSNI) to rank genes according to their probability of being direct
targets. Using primary keratinocytes as a model system, we identified
novel transcriptional target genes of TRP63, a crucial regulator of skin
development. TSNI-predicted TRP63 target genes were validated by Trp63
knockdown and by ChIP-chip to identify TRP63-bound regions in vivo. Our
study revealed that short sampling times, in the order of minutes, are
needed to capture the dynamics of gene expression in mammalian cells. We
show that TRP63 transiently regulates a subset of its direct targets,
thus highlighting the importance of considering temporal dynamics when
identifying transcriptional targets. Using this approach, we uncovered a
previously unsuspected transient regulation of the AP-1 complex by TRP63
through direct regulation of a subset of AP-1 components. The integrated
experimental and computational approach described here is readily
applicable to other transcription factors in mammalian systems and is
complementary to genome-wide identification of transcription-factor
binding sites.


<span class="author">U. Alon</span> (2006) <span class="papertitle">"An
introduction to systems biology: design principles of biological
circuits"</span>, Chapman and Hall/CRC, London.


<span class="author">G. Sanguinetti, M. Rattray and N. D. Lawrence.
</span> (2006) <span class="papertitle">"A probabilistic dynamical model
for quantitative inference of the regulatory mechanism of
transcription"</span> in <span class="journal">Bioinformatics</span> 22
(14), pp 1753--1759
\[[Software](https://github.com/SheffieldML/chipdyno/%20)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/22/14/1753)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16632490&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btl154)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=A+probabilistic+dynamical+model+for+quantitative+inference+of+the+regulatory+mechanism+of+transcription+&btnG=Search)\]

#### Abstract

**Motivation:** Quantitative estimation of the regulatory relationship
between transcription factors and genes is a fundamental stepping stone
when trying to develop models of cellular processes. This task, however,
is difficult for a number of reasons: transcription factors' expression
levels are often low and noisy, and many transcription factors are
post-transcriptionally regulated. It is therefore useful to infer the
activity of the transcription factors from the expression levels of
their target genes.\
\
 **Results:** We introduce a novel probabilistic model to infer
transcription factor activities from microarray data when the structure
of the regulatory network is known. The model is based on regression,
retaining the computational efficiency to allow genome-wide
investigation, but is rendered more flexible by sampling regression
coefficients independently for each gene. This allows us to determine
the strength with which a transcription factor regulates each of its
target genes, therefore providing a quantitative description of the
transcriptional regulatory network. The probabilistic nature of the
model also means that we can associate credibility intervals to our
estimates of the activities. We demonstrate our model on two yeast data
sets. In both cases the network structure was obtained using Chromatine
Immunoprecipitation data. We show how predictions from our model are
consistent with the underlying biology and offer novel quantitative
insights into the regulatory structure of the yeast cell.\
\
 **Availability:** MATLAB code is available from
<http://umber.sbs.man.ac.uk/resources/puma>.


<span class="author">C. Sabatti and G. M. James. </span> (2006) <span
class="papertitle">"Bayesian sparse hidden components analysis for
transcription regulation networks"</span> in <span
class="journal">Bioinformatics</span> 22 (6), pp 739--746
\[[Software](http://www.genetics.ucla.edu/labs/sabatti/software.html%20)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Bayesian+Sparse+Hidden+Components+Analysis+for+Transcription+Regulation+Networks+&btnG=Search)\]

#### Abstract

**Motivation**: In systems like *Escherichia Coli*, the abundance of
sequence information, gene expression array studies and small scale
experiments allows one to reconstruct the regulatory network and to
quantify the effects of transcription factors on gene expression.
However, this goal can only be achieved if all information sources are
used in concert.\
\
 **Results**: Our method integrates literature information, DNA
sequences and expression arrays. A set of relevant transcription factors
is defined on the basis of literature. Sequence data are used to
identify potential target genes and the results are used to define a
prior distribution on the topology of the regulatory network. A Bayesian
hidden component model for the expression array data allows us to
identify which of the potential binding sites are actually used by the
regulatory proteins in the studied cell conditions, the strength of
their control, and their activation profile in a series of experiments.
We apply our methodology to 35 expression studies in *E.Coli* with
convincing results.\
\
 **Availability**:
[www.genetics.ucla.edu/labs/sabatti/software.html](www.genetics.ucla.edu/labs/sabatti/software.html)\
\
 **Supplementary information**: The supplementary material are available
at Bioinformatics online.\
\
 **Contact**: csabatti@mednet.ucla.edu


<span class="author">G. Sanguinetti, N. D. Lawrence and M. Rattray.
</span> (2006) <span class="papertitle">"Probabilistic inference of
transcription factor concentrations and gene-specific regulatory
activities"</span> in <span class="journal">Bioinformatics</span> 22
(22), pp 2275--2281
\[[Errata](./bibpage.cgi?keyName=Sanguinetti:chipvar06&printErrata=1)\]\[[Software](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/chipvar/%20)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/btl473v1)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16966362&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btl473)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Probabilistic+inference+of+transcription+factor+concentrations+and+gene-specific+regulatory+activities+&btnG=Search)\]

#### Abstract

**Motivation**: Quantitative estimation of the regulatory relationship
between transcription factors and genes is a fundamental stepping stone
when trying to develop models of cellular processes. Recent experimental
high-throughput techniques such as Chromatine Immunoprecipitation
provide important information about the architecture of the regulatory
networks in the cell. However, it is very difficult to measure the
concentration levels of transcription factor proteins and determine
their regulatory effect on gene transcription. It is therefore an
important computational challenge to infer these quantities using gene
expression data and network architecture data.\
\
 **Results**: We develop a probabilistic state space model that allows
genome-wide inference of both transcription factor protein
concentrations and their effect on the transcription rates of each
target gene from microarray data. We use variational inference
techniques to learn the model parameters and perform posterior inference
of protein concentrations and regulatory strengths. The probabilistic
nature of the model also means that we can associate credibility
intervals to our estimates, as well as providing a tool to detect which
binding events lead to significant regulation. We demonstrate our model
on artificial data and on two yeast data sets in which the network
structure has previously been obtained using Chromatine
Immunoprecipitation data. Predictions from our model are consistent with
the underlying biology and offer novel quantitative insights into the
regulatory structure of the yeast cell.\
\
 **Availability**: MATLAB code is available from
<http://umber.sbs.man.ac.uk/resources/puma>.


<span class="author">I. Nachman, A. Regev and N. Friedman. </span>
(2004) <span class="papertitle">"Inferring quantitative models of
regulatory networks from expression data"</span> in <span
class="journal">Bioinformatics</span> 20 (Suppl. 1), pp 248--256
\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Inferring+quantitative+models+of+regulatory+networks+from+expression+data+&btnG=Search)\]

#### Abstract

**Motivation:** Genetic networks regulate key processes in living cells.
Various methods have been suggested to reconstruct network architecture
from gene expression data. However, most approaches are based on
qualitative models that provide only rough approximations of the
underlying events, and lack the quantitative aspects that are critical
for understanding the proper function of biomolecular systems.\
\
 **Results:** We present fine-grained dynamical models of gene
transcription and develop methods for reconstructing them from gene
expression data within the framework of a generative probabilistic
model. Unlike previous works, we employ quantitative transcription
rates, and simultaneously estimate both the kinetic parameters that
govern these rates, and the activity levels of unobserved regulators
that control them. We apply our approach to expression data sets from
yeast and show that we can learn the unknown regulator activity
profiles, as well as the binding affinity parameters.We also introduce a
novel structure learning algorithm, and demonstrate its power to
accurately reconstruct the regulatory network from those data sets.\
\
 **Keywords:** transcription regulation, parameter learning, structure
learning, regulatory networks\
\
 **Contact:** nir@cs.huji.ac.il



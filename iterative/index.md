---
layout: default
title: "ITERATIVE"
---
# ITERATIVE Project

## Overview

Gene regulatory networks (GRNs) determine the developmental program of organisms by controlling the dynamics of gene expression. Comprehensive GRN models are only available for the most experimentally tractable model organisms. Inferring GRN models in more complex organisms is hugely challenging because the availability of informative experimental perturbations is limited. Moreover, computational approaches to GRN inference assume the availability of well sampled expression data that are impractical to collect for most developmental systems. We propose an iterative pipeline of modelling and experiment to construct GRN models by integrating expression data with ChIP-seq data. Our methodology builds on a Gaussian process inference approach developed by applicants Rattray and Lawrence for inference in driven differential equation systems. We will integrate ChIP-seq experiments for the top-level transcription factors in the GRN with expression data (microarray and in situ hybridization from wild-type and mutant embryos) to determine a confident network scaffold. We will then construct a weighted ensemble of GRN models consistent with this scaffold using Bayesian methods. The ensemble will be iteratively refined using the principles of Bayesian experimental design to select the most informative additional ChIP-seq and in situ hybridization experiments. Our methodology will be used to model the GRN controlling an important developmental system in vertebrate embryogenesis, the second branchial arch (IIBA). The GRN that mediates IIBA development is controlled by one of the Hox transcription factors, Hoxa2. Applicants Bobola and Mankoo have carried out seminal work on Hoxa2 and Meox1, the key transcription factors in this system, and are therefore uniquely well placed to generate experimental data for modelling this system. Uncovering the principles underlying this GRN will help us understand other systems controlled by Hox proteins in vertebrate embryogenesis.

The behaviour of biological systems is the result of multiple regulatory interactions. Gene regulatory networks (GRNs) are the representation of these complex molecular interactions. They help us to understand how relationships between molecules dictate cell behaviour and are particularly useful to understand the complex dynamical processes driving animal development. The nodes in a GRN represent genes. Links between genes determine which gene products (proteins) regulate which other genes. In this project we focus on transcriptional regulation. This control mechanism regulates which genes are transcribed and expressed in the cell (and eventually which proteins are synthesized). The gene products that regulate transcription are a class of proteins called transcription factors. Transcription factors bind the DNA of target genes and influence the rate at which the target genes are transcribed. Mathematical models can describe how the rate of target gene transcription is affected when transcription factors bind to the DNA, and are useful to understand how cellular-scale behaviours arise from molecular actions. In this project we aim to develop computational methods able to construct GRN models using experimental data that describe gene expression and experimental data that describe the location of bound transcription factor proteins in DNA. An important aspect of the project is the development of a methodology capable of iteratively improving the GRN model by designing the most informative and effective sequence of experiments to be performed. This is particularly important since the experiments to locate binding of transcription factors to DNA are time-consuming and expensive and care should be taken to choose the most useful experiment at each stage. The methodology developed will be used to construct the GRN controlling the development of the second branchial arch (IIBA) in mouse. Branchial arches are transient structures of all vertebrate embryos that will eventually contribute to the face and the neck. Development of the IIBA is controlled by Hoxa2, a member of the large family of Hox transcription factors (TF). Hox TFs regulate morphogenesis along the head-tail axis of all animals with bilateral symmetry, but their mechanism of action is mostly unknown in vertebrates. Uncovering the principles underlying the GRN responsible for IIBA development will help us to understand the function of many other systems that are controlled by Hox proteins in vertebrate embryogenesis.
The project is sponsored by [BBSRC Project Ref BB/H018123/2](http://www.bbsrc.ac.uk/PA/grants/AwardDetails.aspx?FundingReference=BB%2fH018123%2f2) and is a collaboration with [Magnus Rattray](http://www.ls.manchester.ac.uk/people/profile/?personid=10584) of University of Manchester and [Nicoletta Bobola](http://www.dentistry.manchester.ac.uk/staff/150829) of University of Manchester.

<a name="personnel"></a>
## Personnel from ML@SITraN

- [James Hensman](http://chicas.lancaster-university.uk/people/hensman.html) Post-doctoral research assistant



<a name="software"></a>
## Software

The following software has been made available either wholly or partly as a result of work on this project:- [gpsim](http://sheffieldml.github.io/gpsim) Gaussian Process Modelling of single input module motif networks.

- [multigp](http://sheffieldml.github.io/multigp) Modelling multiple outputs with Gaussian processes (will eventually supercede the gpsim toolbox).

<a name="publications"></a>
## Publications

The following conference publications were made associated with this project.

<span class="author">J. Hensman, M. Rattray and N. D. Lawrence. </span>
(2012) <span class="papertitle">"Fast variational inference in the
conjugate exponential family"</span> in P. L. Bartlett, F. C. N.
Pereira, C. J. C. Burges, L éo. Bottou and K. Q. Weinberger (eds) <span
class="journal">NIPS</span>, .
\[[PDF](http://books.nips.cc/papers/files/nips25/NIPS2012_1314.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Fast+variational+inference+in+the+Conjugate+Exponential+family+&btnG=Search)\]


<span class="author">J. Hensman, N. Fusi and N. D. Lawrence. </span>
(2013) <span class="papertitle">"Gaussian processes for big data"</span>
in A. Nicholson and P. Smyth (eds) <span class="journal">Uncertainty in
Artificial Intelligence</span>, AUAI Press, .
\[[PDF](http://auai.org/uai2013/prints/papers/244.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Gaussian+Processes+for+Big+Data+&btnG=Search)\]


<span class="author">J. Hensman, M. Rattray and N. D. Lawrence. </span>
(2014) <span class="papertitle">"Fast nonparametric clustering of
structured time-series"</span> in <span class="journal">IEEE
Transactions on Pattern Analysis and Machine Intelligence</span>
\[[DOI](http://dx.doi.org/10.1109/TPAMI.2014.2318711)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Fast+nonparametric+clustering+of+structured+time-series+&btnG=Search)\]

#### Abstract

In this publication, we combine two Bayesian nonparametric models: the
Gaussian Process (GP) and the Dirichlet Process (DP). Our innovation in
the GP model is to introduce a variation on the GP prior which enables
us to model structured time-series data, i.e. data containing groups
where we wish to model inter- and intra-group variability. Our
innovation in the DP model is an implementation of a new fast collapsed
variational inference procedure which enables us to optimize our
variational approximation significantly faster than standard VB
approaches. In a biological time series application we show how our
model better captures salient features of the data, leading to better
consistency with existing biological classifications, while the
associated inference algorithm provides a significant speed-up over
EM-based variational inference.


<span class="author">J. Hensman, N. D. Lawrence and M. Rattray. </span>
(2013) <span class="papertitle">"Hierarchical Bayesian modelling of gene
expression time series across irregularly sampled replicates and
clusters"</span> in <span class="journal">BMC Bioinformatics</span> 14
(252) \[[DOI](http://dx.doi.org/doi:10.1186/1471-2105-14-252)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Hierarchical+Bayesian+modelling+of+gene+expression+time+series+across+irregularly+sampled+replicates+and+clusters+&btnG=Search)\]

#### Abstract

\\textbf{Background}\
\
Time course data from microarrays and high-throughput sequencing
experiments require simple, computationally efficient and powerful
statistical models to extract meaningful biological signal, and for
tasks such as data fusion and clustering. Existing methodologies fail to
capture either the temporal or replicated nature of the experiments, and
often impose constraints on the data collection process, such as
regularly spaced samples, or similar sampling schema across
replications.\
\
\\textbf{Results}\
\
We propose hierarchical Gaussian processes as a general model of gene
expression time-series, with application to a variety of problems. In
particular, we illustrate the method's capacity for missing data
imputation, data fusion and clustering.The method can impute data which
is missing both systematically and at random: in a hold-out test on real
data, performance is significantly better than commonly used imputation
methods. The method's ability to model inter- and intra-cluster variance
leads to more biologically meaningful clusters. The approach removes the
necessity for evenly spaced samples, an advantage illustrated on a
developmental Drosophila dataset with irregular replications.\
\
\\textbf{Conclusion}\
\
The hierarchical Gaussian process model provides an excellent
statistical basis for several gene-expression time-series tasks. It has
only a few additional parameters over a regular GP, has negligible
additional complexity, is easily implemented and can be integrated into
several existing algorithms. Our experiments were implemented in python,
and are available from the authors' website:
<http://staffwww.dcs.shef.ac.uk/people/J.Hensman/>.


<span class="author">I. J. Donaldson, S. Amin, J. J. Hensman, E.
Kutejova, M. Rattray, N. D. Lawrence, A. Hayes, C. M. Ward and N.
Bobola. </span> (2012) <span class="papertitle">"Genome-wide occupancy
links hoxa2 to wnt-*\\beta*-catenin signaling in mouse embryonic
development"</span> in <span class="journal">Nucleaic Acids
Research</span> 40 (9), pp 3390--4001
\[[DOI](http://dx.doi.org/10.1093/nar/gkr1240)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Genome-wide+occupancy+links+Hoxa2+to+Wnt-\beta-catenin+signaling+in+mouse+embryonic+development+&btnG=Search)\]

#### Abstract

The regulation of gene expression is central to developmental programs
and largely depends on the binding of sequence-specific transcription
factors with cis-regulatory elements in the genome. Hox transcription
factors specify the spatial coordinates of the body axis in all animals
with bilateral symmetry, but a detailed knowledge of their molecular
function in instructing cell fates is lacking. Here, we used chromatin
immunoprecipitation with massively parallel sequencing (ChIP-seq) to
identify Hoxa2 genomic locations in a time and space when it is actively
instructing embryonic development in mouse. Our data reveals that Hoxa2
has large genome coverage and potentially regulates thousands of genes.
Sequence analysis of Hoxa2-bound regions identifies high occurrence of
two main classes of motifs, corresponding to Hox and Pbx-Hox recognition
sequences. Examination of the binding targets of Hoxa2 faithfully
captures the processes regulated by Hoxa2 during embryonic development;
in addition, it uncovers a large cluster of potential targets involved
in the Wnt-signaling pathway. In vivo examination of canonical
Wnt-*\\beta*-catenin signaling reveals activity specifically in Hoxa2
domain of expression, and this is undetectable in Hoxa2 mutant embryos.
The comprehensive mapping of Hoxa2-binding sites provides a framework to
study Hox regulatory networks in vertebrate developmental processes.


The following publications have provided background to our work in this project.

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



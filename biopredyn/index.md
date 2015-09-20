---
layout: default
title: "BioPreDyn"
---
# BioPreDyn Project

## Overview

Currently, biologists are collecting enormous amounts of 'omics' data in a vast number of different databases. There is a great need for the integration and exploitation of these data sets to gain biological insight. This can only be achieved through the development of methods for rigorous and systematic data-driven model building, model validation, and analysis, which can handle this level of complexity.

Such methods are currently being developed by a number of academic research groups, but their wider application — especially in an industrial biotechnology context — is seriously hampered by the lack of standardisation and powerful, easy-to-use, reliable software tools.

This project aims at resolving this issue, by bringing together academic labs that manage large databases and develop cutting-edge model-building, analysis, and optimisation algorithms with small- and medium-sized enterprises that can implement these tools in a consistent, well-supported software framework and apply them to relevant biotechnological applications. Such collaboration between algorithm developers and biotechnology companies will facilitate the transfer of information and code from an academic setting to commercial applications, and will thereby strengthen European competitiveness in the fields of systems biology and biotechnological production processes based on engineered biological systems.
The project is sponsored by [EU FP7-KBBE Project Ref 289434](http://cordis.europa.eu/search/index.cfm?fuseaction=proj.document&PJ_RCN=12267363) and is a collaboration with [Johannes Jaeger](http://pasteur.crg.es/portal/page/portal/Internet/02_Research/01_Programmes/06_Systems_Biology/06_CompAnalysisDevSystems) of Fundacio Privada Centre De Regulacio Genomica, [Magnus Rattray](http://www.ls.manchester.ac.uk/people/profile/?personid=10584) of University of Manchester, [Julio Banga](http://www.iim.csic.es/~julio/) of Agencia Estatal Consejo Superior De Investigaciones Cientificas, [Julio Saez Rodriguez](http://www.ebi.ac.uk/research/saez-rodriguez) of European Molecular Biology Laboratory (European Bioinformatics Institute), [Jaap Kaandorp](http://staff.science.uva.nl/~jaapk/) of Universiteit Van Amsterdam, [Joke Blom](http://www.cwi.nl/people/601) of Stichting Centrum Voor Wiskunde, [Diego di Bernardo](http://dibernardo.tigem.it/wiki/index.php/Main_Page) of Fondazione Telethon, [Pedro Mendes](http://www.manchester.ac.uk/research/Pedro.mendes/) of The University of Manchester, [Eric Boix](http://www.thecosmocompany.com/) of The Cosmo Company, [Klaus Mauch](http://www.insilico-biotechnology.com/people) of Insilico Biotechnology and [Jean-Marie Mouillon](http://www.fluxome.com/company/organization/leadership-team.aspx) of Fluxome Sciences A/S.

<a name="personnel"></a>

## Personnel from ML@SITraN

- [Mu Niu](http://www.gla.ac.uk/schools/mathematicsstatistics/staff/muniu/) Post-doctoral research assistant

- [Nicolas Durrande](https://sites.google.com/site/nicolasdurrandehomepage/) Post-doctoral research assistant

- [Jie Gao]() Post-doctoral research assistant



<a name="software"></a>

## Software

The following software has been made available either wholly or partly as a result of work on this project:- [GPy](http://sheffieldml.github.io/GPy/) The GPy Gaussian process framework in Python (implements much of the MATLAB functionality in Python)

- [vargplvm](http://sheffieldml.github.io/vargplvm/) R and MATLAB Implementations of the Bayesian GP-LVM

- [gpsim](http://sheffieldml.github.io/gpsim/) GPSIM: Gaussian Process Modelling of single input module motif networks.

- [multigp](http://sheffieldml.github.io/multigp/) MULTIGP: Modelling multiple outputs with Gaussian processes.

- [disimrank](http://sheffieldml.github.io/disimrank/) DISIMRANK: Ranking potential targets using a driven input single input model motif.

- [vargplvm](http://sheffieldml.github.io/vargplvm/) VARGPLVM: Bayesian GPLVM Software.

<a name="publications"></a>

## Publications

The following conference publications were made associated with this project.

<span class="author">J. Hensman, M. Zwiessele and N. D. Lawrence.
</span> (2014) <span class="papertitle">"Tilted variational
Bayes"</span> in S. Kaski and J. Corander (eds) <span
class="journal">Proceedings of the Seventeenth International Workshop on
Artificial Intelligence and Statistics</span>, JMLR W&CP 33, Iceland, pp
. \[[Software](https://github.com/SheffieldML/GPy%20)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Tilted+Variational+Bayes+&btnG=Search)\]

#### Abstract

We present a novel method for approximate inference. Using some of the
constructs from expectation propagation (EP), we derive a lower bound of
the marginal likelihood in a similar fashion to variational Bayes (VB).
The method combines some of the benefits of VB and EP: it can be used
with light-tailed likelihoods (where traditional VB fails), and it
provides a lower bound on the marginal likelihood. We apply the method
to Gaussian process classification, a situation where the
Kullback-Leibler divergence minimized in traditional VB can be infinite,
and to robust Gaussian process regression, where the inference process
is dramatically simplified in comparison to EP.\
\
Code to reproduce all the experiments can be found at
[github.com/SheffieldML/TVB](github.com/SheffieldML/TVB).


<span class="author">R. Andrade-Pacheco, J. Hensman and N. D. Lawrence.
</span> (2014) <span class="papertitle">"Hybrid
discriminative-generative approaches with Gaussian processes"</span> in
S. Kaski and J. Corander (eds) <span class="journal">Proceedings of the
Seventeenth International Workshop on Artificial Intelligence and
Statistics</span>, JMLR W&CP 33, Iceland, pp .
\[[Software](https://github.com/SheffieldML/GPy%20)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Hybrid+Discriminative-Generative+Approaches+with+Gaussian+Processes+&btnG=Search)\]

#### Abstract

Machine learning practitioners are often faced with a choice between a
discriminative and a generative approach to modelling. Here, we present
a model based on a hybrid approach that breaks down some of the barriers
between the discriminative and generative points of view, allowing
continuous dimensionality reduction of hybrid discrete-continous data,
discriminative classification with missing inputs and manifold learning
informed by class labels.





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



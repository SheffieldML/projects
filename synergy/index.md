---
layout: default
title: "SYNERGY"
---
# SYNERGY Project

## Overview

Nuclear receptors (NRs) are key factors regulating fundamental cell fate
decisions during organogenesis, growth, homeostatic tissue maintenance
and renewal. Through influencing the expression of genes within complex
regulatory networks, NRs affect a diverse spectrum of physiological and
pathological processes, including differentiation, cellular homeostasis,
cancer and metabolic diseases. Prime examples are estrogen-dependent
breast cancer and androgen-dependent prostate cancer.

Transcription of NR-regulated genes is a complex, tightly regulated
process where distinct NRs, in conjunction with other transcription
factors (TFs), the basal transcription machinery and covalent
modifications to chromatin, collectively act to regulate gene
expression. The major objectives of SYNERGY (Systems approach to gene
regulation biology through nuclear receptors) are to characterize the
roles of four nuclear receptors (NRs), RNA polymerase II and four
histone marks in tumor cells and in normal breast and prostate cells. We
will determine NR binding through ChIP-seq; gene expression with RNA-seq
and place these datasets in context with DNA methylation and histone
marks at multiple time points. These measurements will provide unique
temporal datasets that will be used to design and implement
computational methods to (i) identify genes regulated by NRs, (ii) infer
the mechanisms of NR-triggered gene regulation, and (iii) identify
pathways, biological processes and gene regulatory networks that the
NR-responsive genes are involved in.

SYNERGY is built upon interactive cycles between experimental (Henk
Stunnenberg, Olli A. Jänne, George Reid) and modeling oriented (Sampsa
Hautaniemi, Magnus Rattray, Neil Lawrence, Antti Honkela, Genomatix
Ltd.) groups. The models will be extensively validated during the
project, and the predictions emerging from the models will be used to
direct experiments that lead to more comprehensive understanding of gene
regulation.
The project is sponsored by [ERA-NET Project Ref ERASysBio](http://www.erasysbio.net/index.php?index=271) and is a collaboration with [Prof Magnus Rattray](http://www.ls.manchester.ac.uk/people/profile/?personid=10584) of University of Manchester, [Dr Antti Honkela](http://www.hiit.fi/u/ahonkela/) of University of Helsinki, [Dr Jaako Peltonen](http://users.ics.aalto.fi/jtpelto/) of Aalto University, [Prof Henk Stunnenberg](http://www.ncmls.eu/people/stunnenberg/) of Nijmegen Centre for Molecular Life Sciences, [Dr Sampsa Hautaniemi](http://www.helsinki.fi/~shautani/) of University of Helsinki, [Dr George Reid](http://www.embl.de/~reid/) of DKFZ Heidelberg, [Prof Olli A. Janne](http://www.helsinki.fi/science/arlab/) of University of Helsinki and [Dr Martin Seifert](http://www.genomatix.de/) of Genomatix Software.

<a name="personnel"></a>

## Personnel from ML@SITraN

- [Ciira Maina](https://sites.google.com/site/cwamainadekut/) post-doctoral research assistant



<a name="software"></a>

## Software

The following software has been made available either wholly or partly as a result of work on this project:

- [GPy](https://github.com/SheffieldML/GPy) GPy: Gaussian process modelling framework in Python

- [gpsim](http://inverseprobability.com/gpsim/) GPSIM: Gaussian Process Modelling of single input module motif networks.

- [multigp](http://github.com/SheffieldML/multigp/) MULTIGP: Modelling multiple outputs with Gaussian processes (will eventually supercede the gpsim toolbox).

- [disimrank](http://github.com/SheffieldML/disimrank/) DISIMRANK: Ranking potential targets using a driven input single input model motif.

<a name="publications"></a>

## Publications

<span class="author">A. Honkela, J. Peltonen, H. Topa, I. Charapitsa, F.
Matarese, K. Grote, H. G. Stunnenberg, G. Reid, N. D. Lawrence and M.
Rattray. </span> (2015) <span class="papertitle">"Genome-wide modeling
of transcription kinetics reveals patterns of rna production
delays"</span> in <span class="journal">Proc. Natl. Acad. Sci.
USA</span> In press \[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Genome-wide+modeling+of+transcription+kinetics+reveals+patterns+of+RNA+production+delays+&btnG=Search)\]

#### Abstract

Genes with similar transcriptional activation kinetics can display very
different temporal mRNA profiles because of differences in transcrip
tion time, degradation rate, and RNA-processing kinetics. Recent studies
have shown that a splicing-associated RNA production delay can be
significant. To investigate this issue more generally, it is useful to
develop methods applicable to genome-wide datasets. We introduce a joint
model of transcriptional activation and mRNA accumulation that can be
used for inference of transcription rate, RNA production delay, and
degradation rate given data from high-throughput sequencing time course
experiments. We combine a mechanistic differential equation model with a
nonparametric statistical modeling approach allowing us to capture a
broad range of activation kinetics, and we use Bayesian parameter
estimation to quantify the uncertainty in estimates of the kinetic
parameters. We apply the model to data from estrogen receptor α
activation in the MCF-7 breast cancer cell line. We use RNA polymerase
II ChIP-Seq time course data to characterize transcriptional activation
and mRNA-Seq time course data to quantify mature transcripts. We find
that 11% of genes with a good signal in the data display a delay of more
than 20 min between completing transcription and mature mRNA production.
The genes displaying these long delays are significantly more likely to
be short. We also find a statistical association between high delay and
late intron retention in pre-mRNA data, indicating significant
splicing-associated production delays in many genes.


<span class="author">C. w. Maina, A. Honkela, F. Matarese, K. Grote, H.
G. Stunnenberg, G. Reid, N. D. Lawrence and M. Rattray. </span> (2014)
<span class="papertitle">"Inference of rna polymerase ii transcription
dynamics from chromatin immunoprecipitation time course data"</span> in
<span class="journal">PLoS Computat Biol</span> 10 (5), pp e1003598
\[[DOI](http://dx.doi.org/10.1371/journal.pcbi.1003598)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Inference+of+RNA+Polymerase+II+Transcription+Dynamics+from+Chromatin+Immunoprecipitation+Time+Course+Data+&btnG=Search)\]


<span class="author">M. K. Titsias, A. Honkela, N. D. Lawrence and M.
Rattray. </span> (2012) <span class="papertitle">"Identifying targets of
multiple co-regulated transcription factors from expression time-series
by Bayesian model comparison"</span> in <span class="journal">BMC
Systems Biology</span> 6 (53)
\[[DOI](http://dx.doi.org/10.1186/1752-0509-6-53)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Identifying+Targets+of+Multiple+Co-regulated+Transcription+Factors+from+Expression+Time-series+by+Bayesian+Model+Comparison+&btnG=Search)\]

#### Abstract

\\textbf{Background}\
\
 Complete transcriptional regulatory network inference is a huge
challenge because of the complexity of the network and sparsity of
available data. One approach to make it more manageable is to focus on
the inference of context-speciﬁc networks involving a few interacting
transcription factors (TFs) and all of their target genes.
\\textbf{Results}\
\
 We present a computational framework for Bayesian statistical inference
of target genes of multiple interacting TFs from high-throughput gene
expression time-series data. We use ordinary differential equation
models that describe transcription of target genes taking into account
combinatorial regulation. The method consists of a training and a
prediction phase. During the training phase we infer the unobserved TF
protein concentrations on a subnetwork of approximately known regulatory
structure. During the prediction phase we apply Bayesian model selection
on a genome-wide scale and score all alternative regulatory structures
for each target gene. We use our methodology to identify targets of ﬁve
TFs regulating Drosophila melanogaster mesoderm development. We ﬁnd that
conﬁdent predicted links between TFs and targets are signiﬁcantly
enriched for supporting ChIP-chip binding events and annotated TF-gene
interations. Our method statistically signiﬁcantly outperforms existing
alternatives. \\textbf{Conclusions}\
\
 Our results show that it is possible to infer regulatory links between
multiple interacting TFs and their target genes even from a single
relatively short time series and in presence of unmodelled confounders
and unreliable prior knowledge on training network connectivity.
Introducing data from several different experimental perturbations
signiﬁcantly increases the accuracy.


<span class="author">P. Glaus, A. Honkela and M. Rattray. </span> (2012)
<span class="papertitle">"Identifying differentially expressed
transcripts from rna-seq data with biological variation"</span> in <span
class="journal">Bioinformatics</span> 28 (13), pp 1721--1728
\[[PDF](http://bioinformatics.oxfordjournals.org/content/28/13/1721.full.pdf+html)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/bts260)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Identifying+differentially+expressed+transcripts+from+RNA-seq+data+with+biological+variation+&btnG=Search)\]

#### Abstract

\\textbf{Motivation}: High-throughput sequencing enables expression
analysis at the level of individual transcripts. The analysis of
transcriptome expression levels and differential expression (DE)
estimation requires a probabilistic approach to properly account for
ambiguity caused by shared exons and finite read sampling as well as the
intrinsic biological variance of transcript expression.\
\
\\textbf{Results:} We present Bayesian inference of transcripts from
sequencing data (BitSeq), a Bayesian approach for estimation of
transcript expression level from RNA-seq experiments. Inferred relative
expression is represented by Markov chain Monte Carlo samples from the
posterior probability distribution of a generative model of the read
data. We propose a novel method for DE analysis across replicates which
propagates uncertainty from the sample-level model while modelling
biological variance using an expression-level-dependent prior. We
demonstrate the advantages of our method using simulated data as well as
an RNA-seq dataset with technical and biological replication for both
studied conditions.\
\
\\textbf{Availability:} The implementation of the transcriptome
expression estimation and differential expression analysis, BitSeq, has
been written in C++ and Python. The software is available online from
http://code.google.com/p/bitseq/, version 0.4 was used for generating
results presented in this article.\
\
\\\\textbf{Contact:} glaus@cs.man.ac.uk, antti.honkela@hiit.fi or
m.rattray@sheffield.ac.uk


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



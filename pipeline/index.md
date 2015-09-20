<div id="inner">

PUMA: Improved processing of microarray data with probabilistic models
======================================================================

Overview
--------

### Investigators: Neil Lawrence and Magnus Rattray

Affymetrix Genechip arrays are currently the most widely used microarray
technology. In this project we use probabilistic methods to propagate
the uncertainty of gene expression levels from probe-level analysis of
Affymetrix microarray data to the higher level of gene expression data
analysis. The focus of the project is twofold: developing tractable
probabilistic models for microarray data, allowing reliable estimates of
the experimental noise associated with each gene and experiment. At a
higher level, we aim to produce algorithms and software for data
analysis (such as PCA, clustering, etc..) that uses the information
obtained in the probe-level analysis. This can greatly improve the
accuracy of methods, allow the biologist to obtain uncertainty levels on
the final outcome of the analysis, and hopefully it should give a
principled way to automate many of the heuristic procedures currently
used in microarray data analysis. There is another [project web
page](http://umber.sbs.man.ac.uk/resources/puma/) at Manchester.

The following was achieved under this project:

-   We have made available a software package that implements our
    approaches through bioconductor (see this [application
    note](#Pearson:puma09)).
-   We have an approach for analysing multiple Affymetrix chips which
    gives an estimate of the uncertainty (see mmgMOS package below this
    [Bioinformatics paper](#Liu:tractable04)).
-   We make use of the variances to estimate the probability of one gene
    being more expressed than another (see PPLR software package below).
-   We have modified principal component analysis to take account of the
    uncertainty in the model (see NPPCA package below and this
    [Bioinformatics paper](#Sanguinetti:accounting05).)
-   We have an approach to inferring the activity of transcription
    networks given expression data and a matrix of
    assumed connectivities. (see CHIPDYNO software below and this
    [Bioinformatics paper](#Sanguinetti:chipdyno06)).
-   We have an approach to inferring protein concentration given the
    gene expression of known targets in a single input motif. (see GPSIM
    software below, this [NIPS paper](#Lawrence:transcriptionalGP06) and
    this [ECCB paper](#Gao:latent08)). This is being built on in the
    TIGRA project.
-   Also related is the VIS package for extracting uncertainty from cDNA
    arrays (see VIS software package below and this [Bioinformatics
    paper](#Lawrence:variability03)).

The project is sponsored by [BBSRC Grant No
BBS/B/0076X](http://www.bbsrc.ac.uk) and is a collaboration with [Dr
Marta Milo](http://www.shef.ac.uk/bms/research/milo/) of Wellcome Trust
Fellow at University of Sheffield, [Dr Xuejun
Liu](http://parnec.nuaa.edu.cn/liux/) of Nanjing University of
Aeronautics & Astronautics (former PhD student), [Dr Guido
Sanguinetti](http://www.dcs.shef.ac.uk/~guido) of University of
Sheffield (former post-doc) and [Dr Antti
Honkela](http://www.cis.hut.fi/ahonkela/) of Helsinki University of
Technology (visitor and collaborator).

Personnel in the Project
------------------------

-  [Pei Gao](http://www.dcs.sheffield.ac.uk/cgi-bin/makeperson?gaop), Post-doctorate Researcher
-  [Richard Pearson](http://www.dcs.sheffield.ac.uk/cgi-bin/makeperson?pearsonr), PhD Student

Software
--------

The following software has been made available either wholly or partly
as a result of work on this project:

-  [NPPCA: Probabilistic PCA that deals with different variances associated with each element of the data.](http://inverseprobability.com/nppca)
-  [CHIPDYNO: Inference of transcription factor activities from microarray data and network connectivity data.](http://inverseprobability.com/chipdyno)
-  [CHIPVAR: Variational inference of transcription factor concentrations and actions on target genes from microarray data and network connectivity data.](http://inverseprobability.com/chipvar)
-  [mmgMOS: Modified multi-array gMOS algorithm for extracting uncertainties from Affymetrix slides.](http://www.bioinf.manchester.ac.uk/resources/puma/mmgmos/mmgmos.html)
-  [PPLR: Detecting up regulated genes by using variances and looking at the probability of a positive log ratio.](http://www.bioinf.manchester.ac.uk/resources/puma/pplr/pplr.html)
-  [PUMA: A Bioconductor package that inmplements mmgMOS](http://www.bioinf.manchester.ac.uk/resources/puma/puma/puma.html)
-  [GPSIM: Gaussian Process Modelling of Single Input Motif networks.](http://inverseprobability.com/gpsim)

Publications
------------

The following publications have provided background to our work in this
project.

### Review Paper

<span class="author">M. Rattray, X. Liu, G. Sanguinetti, M. Milo and N.
D. Lawrence. </span> (2006) <span class="papertitle">"Propagating
uncertainty in microarray data analysis"</span> in <span
class="journal">Briefings in Bioinformatics</span> 7 (1), pp 37--47
\[[Errata](http://ml.sheffield.ac.uk/~neil/cgi-bin/bibpage.cgi?keyName=Rattray:propagating06&printErrata=1)\]\[[PDF](http://bib.oxfordjournals.org/cgi/reprint/7/1/37)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16761363&dopt=Citation)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Propagating+Uncertainty+in+Microarray+Data+Analysis+&btnG=Search)\]
#### Abstract

Microarray technology is associated with many sources of experimental
uncertainty. In this review we discuss a number of approaches for
dealing with this uncertainty in the processing of data from microarray
experiments. We focus here on the analysis of high-density
oligonucleotide arrays, such as the popular Affymetrix GeneChip® array,
which contain multiple probes for each target. This set of probes can be
used to determine an estimate for the target concentration and can also
be used to determine the experimental uncertainty associated with this
measurement. This measurement uncertainty can then be propagated through
the downstream analysis using probabilistic methods. We give examples
showing how these credibility intervals can be used to help identify
differential expression, to combine information from replicated
experiments and to improve the performance of principal component
analysis.

------------------------------------------------------------------------

### Journal Papers

<span class="author">R. D. Pearson, X. Liu, G. Sanguinetti, M. Milo, N.
D. Lawrence and M. Rattray. </span> (2009) <span
class="papertitle">"Puma: a Bioconductor package for propagating
uncertainty in microarray analysis"</span> in <span class="journal">BMC
Bioinformatics</span> 10 (211)
\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=19589155&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1186/1471-2105-10-211)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=puma:+a+Bioconductor+package+for+Propagating+Uncertainty+in+Microarray+Analysis+&btnG=Search)\]
#### Abstract

**Background**\
\
 Most analyses of microarray data are based on point estimates of
expression levels and ignore the uncertainty of such estimates. By
determining uncertainties from Affymetrix GeneChip data and propagating
these uncertainties to downstream analyses it has been shown that we can
improve results of differential expression detection, principal
component analysis and clustering. Previously, implementations of these
uncertainty propagation methods have only been available as separate
packages, written in different languages. Previous implementations have
also suffered from being very costly to compute, and in the case of
differential expression detection, have been limited in the experimental
designs to which they can be applied.\
\
 **Results**\
\
 puma is a Bioconductor package incorporating a suite of analysis
methods for use on Affymetrix GeneChip data. puma extends the
differential expression detection methods of previous work from the
2-class case to the multi-factorial case. puma can be used to
automatically create design and contrast matrices for typical
experimental designs, which can be used both within the package itself
but also in other Bioconductor packages. The implementation of
differential expression detection methods has been parallelised leading
to significant decreases in processing time on a range of computer
architectures. puma incorporates the first R implementation of an
uncertainty propagation version of principal component analysis, and an
implementation of a clustering method based on uncertainty propagation.
All of these techniques are brought together in a single, easy-to-use
package with clear, task-based documentation.\
\
 **Conclusions**\
\
 For the first time, the puma package makes a suite of uncertainty
propagation methods available to a general audience. These methods can
be used to improve results from more traditional analyses of microarray
data. puma also offers improvements in terms of scope and speed of
execution over previously available methods. puma is recommended for
anyone working with the Affymetrix GeneChip platform for gene expression
analysis and can also be applied more generally.

------------------------------------------------------------------------

<span class="author">P. Gao, A. Honkela, M. Rattray and N. D. Lawrence.
</span> (2008) <span class="papertitle">"Gaussian process modelling of
latent chemical species: applications to inferring transcription factor
activities"</span> in <span class="journal">Bioinformatics</span> 24, pp
i70--i75
\[[Software](http://inverseprobability.com/gpsim/)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/24/16/i70.pdf?ijkey=FauSn114lAUC1Ey&keytype=ref)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btn278)\]\[[Google
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
<http://inverseprobability.com/gpsim>\
\
 **Contact:** Neil Lawrence

------------------------------------------------------------------------

<span class="author">G. Sanguinetti, N. D. Lawrence and M. Rattray.
</span> (2006) <span class="papertitle">"Probabilistic inference of
transcription factor concentrations and gene-specific regulatory
activities"</span> in <span class="journal">Bioinformatics</span> 22
(22), pp 2275--2281
\[[Errata](http://ml.sheffield.ac.uk/~neil/cgi-bin/bibpage.cgi?keyName=Sanguinetti:chipvar06&printErrata=1)\]\[[Software](http://inverseprobability.com/chipvar/)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/btl473v1)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16966362&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btl473)\]\[[Google
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

------------------------------------------------------------------------

<span class="author">X. Liu, M. Milo, N. D. Lawrence and M. Rattray.
</span> (2006) <span class="papertitle">"Probe-level measurement error
improves accuracy in detecting differential gene expression"</span> in
<span class="journal">Bioinformatics</span> 22 (17), pp 2107--2113
\[[Errata](http://ml.sheffield.ac.uk/~neil/cgi-bin/bibpage.cgi?keyName=Liu:variances06&printErrata=1)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/btl361v1.pdf)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16820429&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btl361)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Probe-level+Measurement+Error+Improves+Accuracy+in+Detecting+Differential+Gene+Expression+&btnG=Search)\]
#### Abstract

**Motivation:** Finding differentially expressed genes is a fundamental
objective of a microarray experiment. Numerous methods have been
proposed to perform this task. Existing methods are based on point
estimates of gene expression level obtained from each microarray
experiment. This approach discards potentially useful information about
measurement error that can be obtained from an appropriate probe-level
analysis. Probabilistic probe-level models can be used to measure gene
expression and also provide a level of uncertainty in this measurement.
This probe-level variance provides useful information which can help in
the identification of differentially expressed genes.\
\
 **Results:** We propose a Bayesian method to include probe-level
variances into the detection of differentially expressed genes from
replicated experiments. A variational approximation is used for effcient
parameter estimation. We compare this approximation with MAP and MCMC
parameter estimation in terms of computational effciency and accuracy.
The method is used to calculate the probability of positive log-ratio
(PPLR) of expression levels between conditions. Using the measurements
from a recently developed Affymetrix probe-level model, multi-mgMOS, we
test PPLR on a spike-in data set and a mouse time-course data set.
Results show that the inclusion of probelevel measurement error improves
accuracy in detecting differential gene expression.\
\
 **Availability:** The methods described in this paper have been
implemented in an R package *pplr* that is currently available from
<http://umber.sbs.man.ac.uk/resources/puma>.\
\
 **Contact:** Magnus Rattray

------------------------------------------------------------------------

<span class="author">G. Sanguinetti, M. Rattray and N. D. Lawrence.
</span> (2006) <span class="papertitle">"A probabilistic dynamical model
for quantitative inference of the regulatory mechanism of
transcription"</span> in <span class="journal">Bioinformatics</span> 22
(14), pp 1753--1759
\[[Software](http://inverseprobability.com/chipdyno/)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/22/14/1753)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16632490&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btl154)\]\[[Google
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

------------------------------------------------------------------------

<span class="author">X. Liu, M. Milo, N. D. Lawrence and M. Rattray.
</span> (2005) <span class="papertitle">"A tractable probabilistic model
for Affymetrix probe-level analysis across multiple chips"</span> in
<span class="journal">Bioinformatics</span> 21 (18), pp 3637--3644
\[[Software](http://www.bioconductor.org/packages/2.0/bioc/html/puma.html)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/21/18/3637)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16020470&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/bti583)\]\[[Advance
Access](http://bioinformatics.oxfordjournals.org/cgi/content/abstract/bti583?ijkey=NwpQ2i5ZVAlgBwj&keytype=ref)\]\[[Pre-print
PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/multigmos.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=A+Tractable+Probabilistic+Model+for+Affymetrix+Probe-level+Analysis+across+Multiple+Chips+&btnG=Search)\]
#### Abstract

**Motivation:** Affymetrix GeneChip arrays are currently the most widely
used microarray technology. Many summarisation methods have been
developed to provide gene expression levels from Affymetrix probe-level
data. Most of the currently popular methods do not provide a measure of
uncertainty for the expression level of each gene. The use of
probabilistic models can overcome this limitation. A full hierarchical
Bayesian approach requires the use of computationally intensive MCMC
methods that are impractical for large data sets. An alternative
computationally efficient probabilistic model, mgMOS, uses Gamma
distributions to model specific and non-specific binding with a latent
variable to capture variations in probe affinity. Although promising,
the main limitations of this model are that it does not use information
from multiple chips and that it does not account for specific binding to
the mismatch (MM) probes.\
\
 **Results:** We extend mgMOS to model the binding affinity of
probe-pairs across multiple chips and to capture the effect of specific
binding to MM probes. The new model, multi-mgMOS, provides improved
accuracy, as demonstrated on some bench-mark data sets and a real
time-course data set, and is much more computationally efficient than a
competing hierarchical Bayesian approach that requires MCMC sampling. We
demonstrate how the probabilistic model can be used to estimate
credibility intervals for expression levels and their log-ratios between
conditions.\
\
 **Availability:** Both mgMOS and the new model multi-mgMOS have been
implemented in an R package that is currently available from
<http://umber.sbs.man.ac.uk/resources/puma>.

------------------------------------------------------------------------

<span class="author">G. Sanguinetti, M. Milo, M. Rattray and N. D.
Lawrence. </span> (2005) <span class="papertitle">"Accounting for
probe-level noise in principal component analysis of microarray
data"</span> in <span class="journal">Bionformatics</span> 21 (19), pp
3748--3754
\[[Software](http://inverseprobability.com/nppca/)\]\[[PDF](http://bioinformatics.oxfordjournals.org/cgi/reprint/21/19/3748)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=16091409&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/bti617)\]\[[Advance
Access](http://bioinformatics.oxfordjournals.org/cgi/reprint/bti617?ijkey=2Elnob2I7AyTWIM&keytype=ref)\]\[[Pre-print
PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/nppca.pdf)\]\[[Bioinformatics
Abstract](http://bioinformatics.oxfordjournals.org/cgi/content/abstract/21/19/3748)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Accounting+for+Probe-level+Noise+in+Principal+Component+Analysis+of+Microarray+Data+&btnG=Search)\]
#### Abstract

**Motivation:** Principal Component Analysis (PCA) is one of the most
popular dimensionality reduction techniques for the analysis of
high-dimensional datasets. However, in its standard form, it does not
take into account any error measures associated with the data points
beyond a standard spherical noise. This indiscriminate nature provides
one of its main weaknesses when applied to biological data with
inherently large variability, such as expression levels measured with
microarrays. Methods now exist for extracting credibility intervals from
the probe-level analysis of cDNA and oligonucleotide microarray
experiments. These credibility intervals are gene and experiment
specific, and can be propagated through an appropriate probabilistic
downstream analysis.\
\
 **Results:** We propose a new model-based approach to PCA that takes
into account the variances associated with each gene in each experiment.
We develop an efficient EM-algorithm to estimate the parameters of our
new model. The model provides significantly better results than standard
PCA, while remaining computationally reasonable. We show how the model
can be used to 'denoise' a microarray dataset leading to improved
expression profiles and tighter clustering across profiles. The
probabilistic nature of the model means that the correct number of
principal components is automatically obtained.\
\
 **Availability:** The software used in the paper is available from
<http://www.bioinf.manchester.ac.uk/resources/puma>. The microarray data
are deposited in the NCBI database.

------------------------------------------------------------------------

<span class="author">M. Milo, A. Fazeli, M. Niranjan and N. D. Lawrence.
</span> (2003) <span class="papertitle">"A probabilistic model for the
extraction of expression levels from oligonucleotide arrays"</span> in
<span class="journal">Biochemical Transations</span> 31 (6), pp
1510--1512
\[[PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/probabilisticOligo.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=A+Probabilistic+Model+for+the+Extraction+of+Expression+Levels+from+Oligonucleotide+Arrays+&btnG=Search)\]
#### Abstract

In this work we present a probabilistic model to estimate summaries of
Affymetrix GeneChip probe level data. Comparisons with two different
models were made both on a publicly available dataset and on a study
performed in our laboratory, showing that our model performs better for
consistency of fold change.

------------------------------------------------------------------------

<span class="author">N. D. Lawrence, M. Milo, M. Niranjan, P. Rashbass
and S. Soullier. </span> (2004) <span class="papertitle">"Reducing the
variability in cDNA microarray image processing by Bayesian
inference"</span> in <span class="journal">Bioinformatics</span> 20 (4),
pp 518--526
\[[Software](http://inverseprobability.com/vis/)\]\[[Gzipped
Postscript](ftp://ftp.dcs.shef.ac.uk/home/neil/microarrayImage.ps.gz)\]\[[Pubmed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=14990447&dopt=Citation)\]\[[DOI](http://dx.doi.org/10.1093/bioinformatics/btg438)\]\[[Pre-print
PDF](ftp://ftp.dcs.shef.ac.uk/home/neil/microarrayImage.pdf)\]\[[Google
Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Reducing+the+Variability+in+cDNA+Microarray+Image+Processing+by+Bayesian+Inference+&btnG=Search)\]
#### Abstract

**Motivation:** Gene expression levels are obtained from microarray
experiments through the extraction of pixel intensities from a scanned
image of the slide. It is widely acknowledged that variabilities can
occur in expression levels extracted from the same images by different
users with the same software packages. These inconsistencies arise due
to differences in the refinement of the placement of the microarray
\`grids'. We introduce a novel automated approach to the refinement of
grid placements that is based upon the use of Bayesian inference for
determining the size, shape and positioning of the microarray \`spots',
capturing uncertainty that can be passed to downstream analysis.\
\
 **Results:** Our experiments demonstrate that variability between users
can be significantly reduced using the approach. The automated nature of
the approach also saves hours of researchers' time normally spent in
refining the grid placement.\
\
 **Availability:** A MATLAB implementation of the algorithm and an image
of the slide used in our experiments, as well as the code necessary to
recreate them are available for non-commercial use from
<http://www.dcs.shef.ac.uk/~neil/vis>.

------------------------------------------------------------------------

### Conference Papers

<span class="author">G. Sanguinetti, M. Rattray and N. D. Lawrence.
</span> (2006) <span class="papertitle">"Identifying submodules of
cellular regulatory networks"</span> in <span
class="journal">International Conference on Computational Methods in
Systems Biology</span>, Springer-Verlag, .
\[[DOI](http://dx.doi.org/10.1007/11885191_11)\]\[[Google Scholar
Search](http://scholar.google.com/scholar?hl-en&lr=&q=Identifying+submodules+of+cellular+regulatory+networks+&btnG=Search)\]
#### Abstract

Recent high throughput techniques in molecular biology have brought
about the possibility of directly identifying the architecture of
regulatory networks on a genome-wide scale. However, the computational
task of estimating fine-grained models on a genome-wide scale is
daunting. Therefore, it is of great importance to be able to reliably
identify submodules of the network that can be effectively modelled as
independent subunits. In this paper we present a procedure to obtain
submodules of a cellular network by using information from
gene-expression measurements. We integrate network architecture data
with genome-wide gene expression measurements in order to determine
which regulatory relations are actually confirmed by the expression
data. We then use this information to obtain non-trivial submodules of
the regulatory network using two distinct algorithms, a naive exhaustive
algorithm and a spectral algorithm based on the eigendecomposition of an
affinity matrix. We test our method on two yeast biological data sets,
using regulatory information obtained from chromatin
immunoprecipitation.

------------------------------------------------------------------------

<span class="author">N. D. Lawrence, G. Sanguinetti and M. Rattray.
</span> (2007) <span class="papertitle">"Modelling transcriptional
regulation using Gaussian processes"</span> in B. Schölkopf, J. C. Platt
and T. Hofmann (eds) <span class="journal">Advances in Neural
Information Processing Systems</span>, MIT Press, Cambridge, MA, pp
785--792.
\[[Errata](http://ml.sheffield.ac.uk/~neil/cgi-bin/bibpage.cgi?keyName=Lawrence:transcriptionalGP06&printErrata=1)\]\[[Software](http://inverseprobability.com/gpsim/)\]\[[Gzipped
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

------------------------------------------------------------------------

This document last modified

</div>

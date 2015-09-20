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


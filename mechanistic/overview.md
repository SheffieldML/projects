Machine learning has had wide success in application over the last
decade, with significant contributions in classification, probabilistic
modelling and analysis of structured data. Over the next decade we
expect significant progress in applying these machine learning models to
very large data sets (on the order of millions or billions of examples,
*e.g.* web based corpora). Improving the scalability of machine learning
methods is a very active area of research (see, *e.g.*, this
[book](#Bottou:lskm07)). We think of these methods as *large data
learning*. These methods will prove to be very valuable, but in this
work we will be focussing on the other end of the spectrum. In
particular, we will be looking at *small data learning*, by which we
mean data sets which are small *relative* to the complexity of the
system from which they are derived. Examples of this type of data
include:

-   human motion data --- whilst a large amount of motion capture data
    is available (millions of frames), the total amount of data relative
    to the number of possible \`natural' human motions is small.
-   Systems biology measurements --- high throughput genetic
    technologies allow us to measure many thousands of chemical
    species simultaneously. A major task of systems biology can be
    characterised as "system identification" --- or from the machine
    learning perspective "model selection". However, the sample rate of
    the data is typically much smaller than is used in classical systems
    identification (a typical experiment would be one sample an hour for
    twelve hours, or one sample a day for two weeks). The situation is
    further complicated by the relative difficulty of making fine system
    disturbances to better characterise system behaviour.
-   Computational Health Informatics --- the increasing availability of
    high resolution single nucleotype polymorphism (SNP) arrays for
    assessing the genetic background of populations, in common with the
    availability of environmental information in a range of disease
    studies (in Manchester we have access to studies on asthma
    and diabetes) should allow resolution of the confounding
    genetic/environmental causes of disease. However, disease mechanisms
    can be highly complex and data sets typically might include over a
    thousand features for each subject for a total of only 500 subjects.

These data are representative of a growing number of application areas
where the number of features is large (high dimensional data) and the
number of data points is relatively small. Additionally, for example in
the case of the medical and computational health applications, there may
be many additional variables that effect the system but are unobserved.

This type of data is sometimes known in statistics as large *p* small
*n*, where *p* represents the dimensionality of the feature space and
*n* the number of data points.In this domain there are two key problems
with purely data driven approaches. Firstly, if data is scarce relative
to the complexity of the model we may be unable to make accurate
predictions on test data. The second problem also applies for larger
*n*. When a model is forced to extrapolate, *i.e.* make predictions in a
regime in which data has not yet been seen, the absence of a sensible
physical foundation for a system can lead to poor performance. One major
advantage of dealing with a physically well characterised system is that
it enables accurate prediction even in regions where there may be no
available training data, for example Pioneer space probes have been able
to enter different extra terrestrial orbits despite the absence of data
for these orbits.}

Turning to a purely mechanistic approach does leaves us with a different
set of problems. In particular, accurate description of a complex system
through a mechanistic modelling paradigm such as differential equations
can lead to an extremely complex model. Identifying and specifying all
the interactions may not be feasible and we are still faced with the
problem of how to parameterise the system.

In this project we advocate an alternative approach. We will augment
traditional machine learning approaches with mechanistic systems models.
Our main algorithmic tool will be the Gaussian process, and the focus of
our mechanistic models will be differential equations. We will refer to
the resulting models as *convolution processes*. Rather than relying on
an exclusively mechanistic or data driven approach we propose a hybrid
system which involves a (typically overly simplistic) mechanistic model
of the system which can easily be augmented through machine learning
techniques.

Progress so far is:

-   We have a suite of methods for improving the efficiency of
    Convolutional Gaussian Processes (see this [NIPS
    Paper](#Alvarez:convolved08) and the MULTIGP software below. Two
    further publications are expected soon)
-   We have shown how latent force models can be applied in first order,
    second order and spatial differential equations using applications
    in computational biology, finance and geostatistics (see this
    [AISTATS Paper](#Alvarez:lfm09)).


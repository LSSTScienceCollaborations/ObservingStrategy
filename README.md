# Science-Driven Optimization of the LSST Observing Strategy

Welcome to the online community thinking about LSST survey strategy ("cadence"), with quantifications via the Metric Analysis Framework.

We are writing a white paper on this topic, primarily composed of a set of individual science cases that are either very important, and somehow stress the observing strategy, and describing how we expect them to be sensitive to LSST observing strategy. MAF metric calculations are then being designed and implemented: these form the quantitative backbone of the document. You may have heard of the coming  "Cadence Wars" - this white paper represents the "Cadence Diplomacy" that will allow us, as a community, to avoid, or at least manage, that conflict. We welcome contributions from all around the LSST Science community.

<!--
* **[Read the current draft of the white paper](http://www.slac.stanford.edu/~digel/ObservingStrategy/whitepaper/LSST_Observing_Strategy_White_Paper.pdf)** (automatically generated PDF, updated every hour, in principle - [log file is here](http://www.slac.stanford.edu/~digel/ObservingStrategy/whitepaper/LSST_Observing_Strategy_White_Paper.log)) -->

* **[Read the current draft of the white paper](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/pdf/whitepaper/LSST_Observing_Strategy_White_Paper.pdf
)** (automatically generated PDF, rebuilt every time the `master` branch is updated)
[![Build Status](https://travis-ci.org/LSSTScienceCollaborations/ObservingStrategy.svg?branch=master)](https://travis-ci.org/LSSTScienceCollaborations/ObservingStrategy)

* **[Download v1.0 of the white paper](https://github.com/LSSTScienceCollaborations/ObservingStrategy/raw/master/whitepaper/releases/LSST_Observing_Strategy_White_Paper_v1.0.pdf)** This is the initial arxiv version, visible at https://arxiv.org/abs/1708.04058

* **[Join the conversation about this project at its issues list](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues)**

* **[Gauge the project's activity level](https://github.com/LSSTScienceCollaborations/ObservingStrategy/pulse/halfweekly)**

* **[Suggest a new `OpSim` experiment](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/README.md)**

* **[Suggest some interesting commissioning observations](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/commissioning/README.md)**


#### Shortcuts

* Guidelines for how to get involved are [in the introduction of the white paper itself, in Section 1.4](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/whitepaper/preface.tex)
* For help getting started with git and GitHub, see this [handy guide](https://github.com/drphilmarshall/GettingStarted#top).
* Shortened URL for this repository (for passing around): [http://ls.st/o5k](http://ls.st/o5k)
* Community-contributed MAF metric code at the [`sims_maf_contrib` repository](https://github.com/LSST-nonproject/sims_maf_contrib/wiki)

<!-- Old workshop links:
## The 2015 MAF Workshop, Bremerton
*August 19-21, 2015.*
* [Meeting website](http://lsstsciencecollaborations.github.io/ObservingStrategy/)
* [List of registered attendees](https://project.lsst.org/meetings/lsst2015/cadence-registrations)
* [Hack session products](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues?utf8=%E2%9C%93&q=label%3A%22Hack+Day!%22+)
* [Feedback form](http://goo.gl/forms/xmVBIWynm4)
## Face-to-Face White Paper Workshop, Tucscon
*November 19-20, 2015.*
* [Program](workshop/Tucson2015.md)
End of old workshop links -->

## Contacts

This effort is being coordinated by [Zeljko Ivezic](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/new?body=@ivezic) and [Beth Willman](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/new?body=@bethwillman), while [Phil Marshall](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/new?body=@drphilmarshall) is the white paper's editor-in-chief. Any of them can propagate your privately-communicated concerns into a redacted issue on this repository. Contributions are very welcome from all round the LSST science collaborations, and beyond. Perhaps we are missing a science case? Or an idea for how to perturb the observing strategy? We'd like to hear from you! Please send all your feedback to [this repo's issues](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues).

All white paper content is Copyright 2015, 2016, 2017 The Authors. If you make use of the ideas and results in the white paper in your research, please cite it as **"(LSST Science Collaborations 2017)"**, and provide the URL of this repository: https://github.com/LSSTScienceCollaborations/ObservingStrategy. The BibTeX entry for the white paper is below.  Thanks!

```
@ARTICLE{LSSTObservingStrategyWhitePaper,
   author = {{LSST Science Collaborations} and {Marshall}, P. and {Anguita}, T. and 
	{Bianco}, F.~B. and {Bellm}, E.~C. and {Brandt}, N. and {Clarkson}, W. and 
	{Connolly}, A. and {Gawiser}, E. and {Ivezic}, Z. and {Jones}, L. and 
	{Lochner}, M. and {Lund}, M.~B. and {Mahabal}, A. and {Nidever}, D. and 
	{Olsen}, K. and {Ridgway}, S. and {Rhodes}, J. and {Shemmer}, O. and 
	{Trilling}, D. and {Vivas}, K. and {Walkowicz}, L. and {Willman}, B. and 
	{Yoachim}, P. and {Anderson}, S. and {Antilogus}, P. and {Angus}, R. and 
	{Arcavi}, I. and {Awan}, H. and {Biswas}, R. and {Bell}, K.~J. and 
	{Bennett}, D. and {Britt}, C. and {Buzasi}, D. and {Casetti-Dinescu}, D.~I. and 
	{Chomiuk}, L. and {Claver}, C. and {Cook}, K. and {Davenport}, J. and 
	{Debattista}, V. and {Digel}, S. and {Doctor}, Z. and {Firth}, R.~E. and 
	{Foley}, R. and {Fong}, W.-f. and {Galbany}, L. and {Giampapa}, M. and 
	{Gizis}, J.~E. and {Graham}, M.~L. and {Grillmair}, C. and {Gris}, P. and 
	{Haiman}, Z. and {Hartigan}, P. and {Hawley}, S. and {Hlozek}, R. and 
	{Jha}, S.~W. and {Johns-Krull}, C. and {Kanbur}, S. and {Kalogera}, V. and 
	{Kashyap}, V. and {Kasliwal}, V. and {Kessler}, R. and {Kim}, A. and 
	{Kurczynski}, P. and {Lahav}, O. and {Liu}, M.~C. and {Malz}, A. and 
	{Margutti}, R. and {Matheson}, T. and {McEwen}, J.~D. and {McGehee}, P. and 
	{Meibom}, S. and {Meyers}, J. and {Monet}, D. and {Neilsen}, E. and 
	{Newman}, J. and {O'Dowd}, M. and {Peiris}, H.~V. and {Penny}, M.~T. and 
	{Peters}, C. and {Poleski}, R. and {Ponder}, K. and {Richards}, G. and 
	{Rho}, J. and {Rubin}, D. and {Schmidt}, S. and {Schuhmann}, R.~L. and 
	{Shporer}, A. and {Slater}, C. and {Smith}, N. and {Soares-Santos}, M. and 
	{Stassun}, K. and {Strader}, J. and {Strauss}, M. and {Street}, R. and 
	{Stubbs}, C. and {Sullivan}, M. and {Szkody}, P. and {Trimble}, V. and 
	{Tyson}, T. and {de Val-Borro}, M. and {Valenti}, S. and {Wagoner}, R. and 
	{Wood-Vasey}, W.~M. and {Zauderer}, B.~A.},
    title = "{Science-Driven Optimization of the LSST Observing Strategy}",
  journal = {ArXiv e-prints},
archivePrefix = "arXiv",
   eprint = {1708.04058},
 primaryClass = "astro-ph.IM",
 keywords = {Astrophysics - Instrumentation and Methods for Astrophysics, Astrophysics - Cosmology and Nongalactic Astrophysics, Astrophysics - Earth and Planetary Astrophysics, Astrophysics - Astrophysics of Galaxies, Astrophysics - Solar and Stellar Astrophysics},
     year = 2017,
    month = aug,
      doi = {10.5281/zenodo.842712},
      url = {https://doi.org/10.5281/zenodo.842712}
   adsurl = {http://adsabs.harvard.edu/abs/2017arXiv170804058L},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

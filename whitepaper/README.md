# Science-driven Optimization of the LSST Observing Strategy

A community white paper about LSST observing strategy, with quantifications via the the Metric Analysis Framework.

## Overview

* [Document Layout](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/whitepaper/notes/whitepaper-design.md)
* [Chapters and Sections ](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/whitepaper/notes/chapter-template.md)

## Instructions for Authors

From the command line, in the `whitepaper` directory, just hit

    make

If the document does not compile, and you cannot fix the problem, please submit the error message and your preliminary diagnosis as an [issue](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues).

The individual chapters and sections are stored in separate modular tex files, to enable us to be flexible about the document structure later. The main tex file is [`LSST_Observing_strategy_White_Paper.tex`](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/whitepaper/LSST_Observing_strategy_White_Paper.tex). Please browse this file to see which files host each chapter. The chapter files then bring in the content from the section files.

Section Leads: you will need to make sure that your section is correctly read into your chapter via an `\input` statement. Please see the [`cosmology.tex`](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/whitepaper/cosmology.tex) chapter and [`lenstimedelays.tex`](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/whitepaper/lenstimedelays.tex) section for an example. Also, please keep your section's header up to date, to make it easy for your co-authors to see what is in each file.

## How to contribute

We welcome contributions from all members of the LSST project and science community. If you would like to propose changes or additions to the white paper, please [fork](https://help.github.com/articles/fork-a-repo/) this repository, edit the text and submit a [pull request](https://help.github.com/articles/using-pull-requests/). The editors will then merge in your work, as appropriate. Thanks!

## License, credit etc

This paper contains research in progress. All content is Copyright 2015 The LSST Science Collaborations. If you would like to cite it, please do so as "(LSST Science Collaborations, in preparation)" and provide a footnote containing the [URL of this repository](https://github.com/LSSTScienceCollaborations/ObservingStrategy/). The latex code used here is distributed for you to use at your own risk under the MIT License.

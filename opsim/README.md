# Suggestions for New OpSim Runs

While we write down our science cases and code up their metrics and
Figures of Merit, we can also think about which `OpSim` experiments
we want to carry out, to explore the possibilities the LSST offers.

## Guidelines

The [LSST Observing Strategy White Paper](https://github.com/LSSTScienceCollaborations/ObservingStrategy/raw/master/whitepaper/LSST_Observing_Strategy_White_Paper.pdf) contains a chapter (2) listing the 2015 `OpSim` runs. The output databases from these
experiments are available for us to run our MAF metrics on. This chapter gives some initial feel for what is possible, and what has already been done. Our first task: read that chapter.

To suggest a new `OpSim` run, you will (of course) need to write a very short *proposal*. You can do this in a markdown file following [this template](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_Template.md) and check it into the `opsim` folder of this repository. Then, add it to the Table below, so everyone can see what you are suggesting and follow the link to your proposal.

NB. When proposing a "rolling cadence" experiment, you should try and use the terminology defined by Kem Cook and Steve Ridgeway in their OpSim development work. Please see [their notes on rolling cadence strategy (v1.4)](https://docs.google.com/document/d/1OifCjqPMa76ErewS1zfY2KYjx0dBaY4KmXXnN3wm1GY/edit?usp=sharing) for guidance.


## Proposed New OpSim Experiments

 **Name**              | **Proposer(s)**       | **Issue Thread**| **Description**
:----------------------|:----------------------|:----------------|:----------------:
 [No Extragalactic Visit Pairs](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_NoExtragalacticVisitPairs.md) | [Marshall](https://github.com/drphilmarshall) | [#66](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/66) | Dont observe in pairs of visits above the Galactic and Ecliptic planes
 [Target of Opportunity Observations](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_TOOObservations.md) | [Soares-Santos](https://github.com/soares-santos), [Bellm](https://github.com/soares-santos) | [#75](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/75) | simulate TOO Observations
 [Coordination with WFIRST](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_WFIRST.md) | [Gawiser](https://github.com/egawiser), [Rhodes](https://github.com/jasondrhodes) | [#114](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/114) | Add Special Survey to duplicate WFD observations of 2300 degrees during first 5 years 
NEO optimized runs | SS SC | [#120](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/120) | Find more and different NEOs
[Normal Plane](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_GP.md) | [Strader](https://github.com/caprastro) (for SMWLV) | [#162](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/162) | Do Galactic Plane with normal WFD cadence
 [New Observing Strategy of the Main Survey Optimized for SN Cosmology](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_SN.md) | [Jeonghee Rho ](https://github.com/jhrlsst), [SN Cosmology Team] | [#159](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/159) | Modified Rolling Cadence for densely populated SN light curves
 [...](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/) | [...](https://github.com/) | [...](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/)
Here's the [proposal template](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/opsim/Proposal_Template.md)
for you to copy and edit. Have fun!

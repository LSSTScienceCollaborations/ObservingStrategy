# Suggestions for Commissioning Observations

While we write down our science cases and code up their metrics and
Figures of Merit, we can also think about which kinds of observations or experiments 
we might want to do during commissioning to prepare for doing science when the full survey
starts.

## Guidelines

The [LSST Observing Strategy White Paper](https://github.com/LSSTScienceCollaborations/ObservingStrategy/raw/master/whitepaper/LSST_Observing_Strategy_White_Paper.pdf) contains an overview of LSST science programs that depend on the details of LSST's observing strategy.   This white paper presents a set of MAF based metrics for a variety of science programs.  Some of the science cases presented would benefit from early data during commissioning either to validate and refine algorithms, bootstrap algorithms to be used in the full survey or provide value added in the science of the full survey (e.g. filling in time sampling that the main survey won't do).

When considering a proposed observing run that would be done in commissioning, consider what could be done with the commissioning camera (ComCam - 3x3 4k x 4k CCDs in a single raft with 45 arcmin FOV) and what would need the full camera.  Think also about data that can be obtained in an hour, a night and/or a week or so. 

To suggest a new `Commissioning Observation or Experiment`, you will need to write a very short *proposal*. 

To create a new commissioning proposal:
- click the "Create New File" button above
- Give your new file a descriptive name that ends in ".md"
- paste the following lines into your new file
~~~~
# "Template"

A Proposed Commissioning Experiment.

*Proposer(s): Your Name Here*


## Proposed Commissioning Observation/Experiment

What observations or experimient during commissioning would be
beneficial for validating your algorithms and help bootstrap your science
in preparation for the full survey.


## Technical and/or Science Motivation

Write a few sentences about why you want to make these observations. Which
science projects will benefit and/or what technical aspect of the
project will benefit (e.g. algorithms or characterization), do you expect?
~~~~
- edit the file to reflect your proposal
- click "Propose new file" at the bottom of the page which will create a new branch that contains your new file
- click "Create new pull request" and submit this to the ObservingStrategy repo
- you can then add the proposal to the table below

Alternately you can download [this template](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/commissioning/commProp_Template.md) and check it into the `commissioning` folder of this repository. Then, add it to the Table below, so everyone can see what you are suggesting and follow the link to your proposal.


## Proposed New Commissioning Experiments



 **Name**              | **Proposer(s)**       | **Issue Thread**| **Description**
:----------------------|:----------------------|:----------------|:----------------:
 [1-Hour r-band Time Series](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/commissioning/commProp_r-band1hourtimeSeries.md) | [cclaver](https://github.com/cclaver) | [#69](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/69) | A continuous 1-hour sequence of 15-sec. exposures
 [...](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/issue64/opsim/) | [...](https://github.com/) | [...](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/)


Here's the [commissioning proposal template](https://github.com/LSSTScienceCollaborations/ObservingStrategy/blob/master/commissioning/commProp_Template.md)
for you to copy and edit. Have fun!

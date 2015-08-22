# "Target of Opportunity Observations"

A Proposed OpSim Experiment.

*Proposer(s): Marcelle Soares-Santos, Eric Neilsen, Eric Bellm*

*Issue thread: [#75](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/75)*

## Proposed Changes to the Observing Strategy

Up to a specified maximum number of times over the 10-year survey, after a
randomly-specified "trigger" time (which could be in daytime) 
strongly prioritize observations of a
specific field (or small number of fields, at most perhaps 10).  

A suggested observing sequence relevant for Advanced LIGO followup would be to
obtain images in i and z bands as soon as possible after the trigger time (T0),
with a two additional revisits in both i and z scheduled flexibly on something
like an every other night cadence after T0.

Other specific TOO science cases would have potentially different followup
strategies.  Tunable variables include:

   * number of triggers allowed
   * number of fields per trigger
   * number of revisits desired
   * time between revisits
   * filter choice
   * total integration time


## Science Motivation

External surveys may produce triggers (real-time event notifications) for which
LSST's wide field and deep imaging are required to identify an optical
counterpart.  In particular, Advanced LIGO locations are typically tens of
square degrees and the expected counterparts faint.  The ability to interrupt
LSST's normal schedule to make TOO observations can enable discovery of
scientifically valuable events not easily discovered by other facilities.
OpSim simulations can determine what number and type of TOO observations are
minimally disruptive to LSST's other science programs.

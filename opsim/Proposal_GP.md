# "Normal Galactic Plane"

A Proposed OpSim Experiment.

*Proposer(s): Jay Strader (for SMWLV)*

*Issue Thread: [#162](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/162)*


## Proposed Changes to the Observing Strategy

I propose an OpSim run in which the part of the Galactic Plane that falls within the normal WFD survey declination limits is observed with the standard WFD survey cadence. The current northern extension of the Plane coverage can be left at that for the existing special proposal 
(30 visits total per filter), though this deserves future consideration.

## Science Motivation

The current division between WFD and the special Galactic Plane proposal
is broadly motivated by the increased crowding and extinction toward
the Plane, but has not been justified in detail. Further, there are
a number of science programs that cannot be accomplished with the baseline special proposal coverage, including the characterization of certain classes of variable stars only found in these crowded regions, a microlensing survey for exoplanets and compact objects, and a three-dimensional dust map important for both Galactic and extragalactic science. These science cases will be laid out in more detail in the Observing Strategy white paper.

With this OpSim run, the difference with the baseline cadence can be determined and then this can be properly weighed against the science gain from the proposal.


## Implementation

A version of this has been produced using opsim v3.3.8 and is available from the links at
http://astro-lsst-01.astro.washington.edu:8080/ 
You can see that the galactic plane run is called 'astro_lsst_01_1004' (sorry for the terrible names). 
The sqlite link is
http://astro-lsst-01.astro.washington.edu:8080/db_gzip/astro_lsst_01_1004_sqlite.db.gz 
The standard MAF analyses for this run are also available at: 
http://astro-lsst-01.astro.washington.edu:8080/metricSelect?runId=3
and 
http://astro-lsst-01.astro.washington.edu:8080/metricSelect?runId=4

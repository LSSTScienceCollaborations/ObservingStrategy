# "Rolling Cadence Optimized for SN Cosmology"

A Proposed OpSim Experiment.

*Proposer(s): Jeonghee Rho and Supernova team (e.g. SN Cosmology)

*Issue Thread: [#159](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/159)*


## Proposed Changes to the Observing Strategy

We propose a new Observing Strategy of the main survey (the Universal Cadence area; WFD) in order to generate 3 times densely populated SN light curves in time (i.e. 3 times higher samples for a SN light curve). Our main goal is to obtain 7-10 epochs spread over 45 days per filter.
For simplicity, we assume the main survey will cover available sky (2293 fields) for 3 days (we divide the available sky into 3 separate Sectors, which would be called Sector 1 and 2 and 3. Each Sector of the sky corresponds to ~764 fields. The sum of Sector 1 and 2 and 3 is 2293 fields, a total number of LSST fields from the Universal Cadeance area. For a day, 1/3 of available sky would be observed. By changing the filter, every day, it will take 6 days to observe 6 filters for 1/3 of available sky. We repeat 9 times for the same Sector of sky, which will result in 54 visits (with 6 different filters) for the same Sector (1/3 of available sky). We repeat the same for the 2nd Sector of sky which takes another 54 days. Then we observe the 3rd Sector for another 54 days.

To visualize this idea, we list our proposed observing strategy day by day;
Day 1 : Filter 1 (for the 1st Sector), 
Day 2:  Filter 2 (for the 1st Sector),
Day 3:  Filter 3 (for the 1st Sector), 
Day 4:  Filter 4 (for the 1st Sector), 
Day 5:  Filter 5 (for the 1st Sector), and
Day 6:  Filter 6 (for the 1st Sector).
Repeat this sequence 9 times for the 1st Sector. This will generate 54 data points for 54 days for a supernova and
9 data points in average for each filter. This is approximately 3 times higher sample of data for 54 days than those from the Universal Cadence.
Observe the same sequences for the 2nd Sector (it takes 54 days) and then do the same for the 3rd Sector of sky (it takes another 54 days).
This summarizes overall idea, but since visible sky is slightly different every day and observation depends on the weather, an OpSim run is needed accounting for all of these factors (and maybe other factors that we haven't mentioned here). One may also consider to observe each Sector for 108 days (2x54 days) instead of 54 days; this may allow us to discover a higher number of SNe in stead of for 54 days. Our suggestion is mainly for the sky of Galactic latitude greater than 30 degree (|l| > 30) since it would be hard to discover SNe at the Galactic plane.


## Science Motivation
The main survey is important for discoveries of supernovae (SNe) at a redshift range of 0.1- 1. This observation is critical to constrain osmological parameters from supernovae. In order to identify a variable source as a SN and to distinguish the source as a Type Ia SN,
we need 7-10 epochs spread over 45 days or so for each filter based on past experience. Universal survey of the baseline plan provides 6 filter data for approximately 18 days (assuming a survey with a filter can be done for 3 days).  This provides
15 data points over 45 days and 2.5 data points in average for each filter. Our analysis of OpSim run (baseline observing strategy) output shows the light curves of SNe from the OpSim data are insufficient not only to identify the source as a SN and but also to classify the SN if the SN is type Ia or II (or Ib, Ic). Our proposed observing strategy is critical
to improve the quality of SN light curves. The light curves will have at least 3 times densely populated data points in time. 

This strategy may allow us to keep "Uniformity" of the LSST main survey and yet it might be able to improve the quality of the data because newly suggested observing strategy can produce a lower airmass in average than that from the Universal Cadence. 

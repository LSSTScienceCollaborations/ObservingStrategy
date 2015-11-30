# "New Observing Strategy of the Main Survey Optimized for SN Cosmology"

A Proposed OpSim Experiment.

*Proposer(s): Jeonghee Rho and SN Cosmology team

*Issue Thread: [#159](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/159)*


## Proposed Changes to the Observing Strategy

We propose a new Observing Strategy of the main survery in order to generate densely populated SN light curves (3 times more densely populated data acquisition in time). 
For simplicity, we assume the LSST main survey will cover the entire LSST fields for 3 days (we divide the entire LSST fields into 3 separate fields, which would be called Field 1 and 2 and 3. The sum of Field 1 and 2 and 3 is the LSST entire fields) . For a day, 1/3 of the LSST entire field would be observed. By changing the filter, every day, LSST can observe 6 filters for 1/3 of the LSST entire fields. We repeat 9 times for the same field, which will result in 54 visits (with 6 different filters) for the same field (1/3 of the LSST entire fields). We repeat the same for Field 2 which takes another 54 days. Then observe Field 3 for another 54 days.
To visualize this idea, I list proposed observing strategy day by day;
Day 1 : Filter 1 (for Field 1), 
Day 2:  Filter 2 (for Field 1),
Day 3:  Filter 3 (for Field 1), 
Day 4:  Filter 4 (for Field 1), 
Day 5:  Filter 5 (for Field 1), and
Day 6:  Filter 6 (for Field 1).
Repeat this sequence 9 times for the Field 1. This will generate 54 data points for 54 days for a supernova and
average 9 data points for each filter. 
Observe the same sequences for Field 2 (it takes 54 days) and then do the same for Field 3 (it takes another 54 days).
This summarizes overall idea, but since the visible sky is different every day and the observation depends on the weather, an opsim run is needed accounting for all of these factors (and maybe others that we haven't mentioned here).


## Science Motivation
The main survey is important for discoveries of supernovae (SNe) for the redshift range of 0.1- 1 which is critical to constraint 
SN cosmological parameters. In order to identify a variable source as a SN and to distinguish the source as a Type Ia SN,
we need 7-10 epochs spread over 45 days or so for each filter based on past experience. Universal survey of the baseline plan provides 6 filter data for approximately 18 days (assuming a survey with a filter can be done for 3 days).  This provides
15 data points over 45 days and 2.5 data points in average for each filter. Our analysis of OpSim run (baseline observing strategy) output shows the light curves of SNe from the OpSim data are insufficient not only to identify the source as a SN and but also to classify the SN if the SN is type Ia or II (or Ib, Ic). Our proposed observing strategy is critical
to improve the quality of SN light curves. The light curves will have at least 3 times densely populated data points in time. 

This strategy may allow us to keep "Uniformity" of the LSST main survery and yet it might be able to improve the quality of the data because newly suggested observing strategy can produce lower airmass in average. 

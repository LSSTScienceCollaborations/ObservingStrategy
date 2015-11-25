# "New Observing Strategy of the Main Survey Optimized for SN Cosmology "

A Proposed OpSim Experiment.

*Proposer(s): Jeonghee Rho and SN Cosmology team

*Issue Thread: [#159](https://github.com/LSSTScienceCollaborations/ObservingStrategy/issues/159)*


## Proposed Changes to the Observing Strategy

We propose new Observing Strategy of the main survery in order to generate densely populated SN light curves (3 times more densely populated data acquisition in time). Our goal is to obtain LSST data points (from the main survey)
For simplicity, we assume the LSST main survey will cover the entire LSST fields for 3 days (we divide the entire LSST fields into 3 separate fields, which would be called Field 1 and 2 and 3. The sum of Field 1 and 2 and 3 is the LSST entire fields) . For a day, 1/3 of the LSST entire field would be observed. By changing the filter, every day, LSST can observe 6 filters for 1/3 of the LSST entire fields. We repeat 9 times for the same field, which will result in 54 visits (with 6 different filters) for the same field (1/3 of the LSST entire fields). We repeat the same for Field 2 which takes another 54 days. Then observe Field 3 for another 54 days.
To visualize this idea, I list proposed observing strategy day by day.
Day 1 : Filter 1 (for Field 1)
Day 2:  Filter 2 (for Field 1)
Day 3:  Filter 3 (for Field 1)
Day 4:  Filter 4 (for Field 1)
Day 5:  Filter 5 (for Field 1)
Day 6:  Filter 6 (for Field 1)
Repeat this sequence for 9 times for the Field 1. This will generate 54 data points for 54 days for a supernova and
average 9 data points for each filter. 
Observe the same sequences for Field 2 (it takes 54 days) and then do the same for Field 3 (it takes another 54 days).
This is overall idea and since the visible sky is different every day and the observation depends on the weather, an opsim run is needed accounting for all of these factors (and others that we haven't included here).


## Science Motivation
We aim to obtain 7-10 epochs spread over 45 days or so for each filter. 

Write a few sentences about why you want to make this change. Which
science projects will benefit, do you expect?

This strategy allows us to keep "Uniformity" of the LSST main survery and yet it can improve the quality of the data with smaller averge airmass.

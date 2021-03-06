
# coding: utf-8

# # Comparing MAREDAT estimates to remote sensing measurements
# As a consistency check for the estimates in the MAREDAT database, we calculate the total biomass of phytoplankton, and compare it to estimates of the total biomass of phytoplankton from remote sensing measurements.
# 
# The groups of phytoplankton for which we estimate the total biomass are picophytoplankton, diatoms and *Phaeocystis*. Our best estimates for the total biomass of these groups based on data from the MAREDAT database are 0.42, 0.3 and 0.27 Gt C, respectively (for more details on our estimates, see the marine protist section in the Supplementary Information). To estimate the total biomass of phytoplankton, we sum up our estimates for the biomass of all the phytoplankton groups:

# In[1]:

# The estimates of the total biomass of the different phyotplankton groups, based on the MAREDAT database
picophyoto_biomass = 0.42e15
diatom_biomass = 0.3e15
phaeocystis_biomass = 0.27e15

# Calculate our best estimate of the total biomass of phytoplankton based on the MAREDAT database
phyoplankton_biomass = picophyoto_biomass + diatom_biomass + phaeocystis_biomass

print('Our best estimate of the total biomass of phytoplankton based on the MAREDAT database is ≈%.0f Gt C' %(phyoplankton_biomass/1e15))


# We compate this estimate with the estimates of the total biomass of phytoplankton made by [Antonine et al.](http://dx.doi.org/10.1029/95GB02832) and [Behrenfeld & Falkowski](http://dx.doi.org/10.4319/lo.1997.42.1.0001). Antonine et al. and Behrenfeld & Falkowski use remote sensing data to estimate ≈0.3-0.75 Gt C of phytoplankton. This means that our estimate based on the MAREDAT databased is 1.3-3-fold higher than the estimate based on remote sensing.

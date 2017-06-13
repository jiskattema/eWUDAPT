Title: Output description
Date: 2017-06-12 10:20
Category: Output
save_as: output.html

# Requested output

We ask for a NetCdf file which contains:

* surface variables

* profiles of state variables at full levels

* profiles of fluxes on half levels 

* profiles of soil parameters

* profiles of forcings as prescribed for this case at model levels

* profiles of the initial state as prescribed for this case

All data should be given as 10-min averages.

# Filename

The filename should be composed as:
```gabls_urban_scm_<institute>_<model>_<ver>.nc```
where:

* *institute* name or acronym of your institute 

* *model* acronym of your model 

* *phase* phase of the experiment (0 or 1)

* *stage* stage of the experiment (1-3)

* *ver* two digit version number of your submission prepended with a *v* (v01, v10, v11, etc)
 
example:
```gabls_urban_scm_wur_wrf_0_1_v03.nc```

# Global attributes

All relevant meta information should be added to the file as global attributes.
This should include:

## General

- reference to the model

- contact person.

- type of model where the SCM is derived from (climate model, mesoscale weather prediction model, regional model) ?

- time step

## Surface scheme properties

Describe the level op complexity of the urban canopy scheme.
Is there a tile approach?

## Turbulence scheme

Turbulence scheme  (e.g., K profile, TKE-l, ...)
Formulation of eddy diffusivity K.
For E-l and Louis-type scheme: give formulation length scale.
For K-profile: how is this  profile determined ? (e.g., based on Richardson, Brunt-Vaisala frequency (N^2),  Parcel method, other.


## Initial profiles

Include the initial profiles in the mean state section as the first time step at 0 seconds.
Here we assume that the model is in eta coordinates and has a specific structure in the use of full levels and half level.
If your model differs in this respect please adapt the output to fit with your model.

# Sign convention

Surface energy fluxes (shf, lhf, g, qf) are positive when directed away from the surface.
Surface radiation fluxes (qdw, qup, ldw, lup) are positive.

# NetCdf dimensions and variables

Variables and dimensions should have the names as specified below (all lower case).
Use the unlimited option for the "time" dimension or at least be sure that "time" is the slowest varying dimension in two dimensional variables.
Each variable should have an attribute "units" with the unit prescribed as below.
Each variable should have an attribute "long_name" which explains the meaning of the variable.
The exact formulation is free, but could be taken from the description below.
If a variable is not available for your model, use the attribute ```_FillValue``` to prescribe the numerical value that defines not available.
All physical variables should be of type float.

## Dimensions

|Name| Description            |
|----|------------------------|
|time| number of output times |
|levf| number of full levels  |
|levh| number of half levels  |
|levs| number of soil levels  |

TODO: variables corresponding to the dimenension (netcdf requirement) and further grid description (eta levels)

 {time} seconds since 2006-07-01 12:00:00 [s]
 {afull}
 {bfull}
 {ahalf}
 {bhalf}

## Variables

### Time series output {time}

 {ldw} long wave downward radiation at surface [W/m2]
 {lup} long wave upward radiation at surface [W/m2]
 {qdw} short wave downward radiation at surface [W/m2]
 {qup} short wave upward radiation at surface [W/m2]
 {tsk} temperature skin layer [W/m2]
 {g} soil heat flux [W/m2]
 {shf} sensible heat flux [W/m2]
 {lhf} latent heat flux [W/m2]
 {qf} anthropogenic heat flux [W/m2]
 {ustar} friction velocity [m/s]
 {hpbl} boundary layer height [m]
 {t2m} 2m temperature [K]
 {q2m} 2m specific humidity [kg/kg]
 {u10m} 10m u-component wind [m/s]
 {v10m} 10m v-component wind [m/s]
 {cc} cloud cover fraction [0 1]

### Mean state {time} {levf}

 {zf} height of full level [m]
 {pf} pressure at full level [Pa]
 {t} temperature [K]
 {th} potential temperature [K]
 {q} specific humidity [kg/kg]
 {u} zonal component wind [m/s]
 {v} meridional component wind [m/s]

### Prescribed forcings {time} ({levf} or {levh})

 {ugeo} u-component geostrophic wind [m/s]
 {vgeo} v-component geostrophic wind [m/s] 
 {dudt_ls} u-component momentum advection [m/s/s]
 {dvdt_ls} v-component momentum advection [m/s/s]
 {dtdt_ls} temperature advection [K/s]
 {dqdt_ls} moisture advection [kg/kg/s]
 {ome} vertical movement [Pa/s]

### Fluxes {time} {levh}

 {zh} height of half level [m]
 {ph} pressure at half level [Pa]
 {wt} vertical temperature flux [Km/s]
 {wq} vertical moisture flux [kg/kg m/s]
 {uw} vertical flux u-component momentum [m2/s2]
 {vw} vertical flux v-component momentum [m2/s2]
 {Km} eddy diffusivity momentum [m2/s]
 {Kh} eddy diffusivity heat [m2/s]
 {TKE} turbulent kinetic energy [m^2/s^2]
 {shear} shear production [m2/s3]
 {buoy} buoyancy production [m2/s3]
 {trans} total transport [m2/s3]
 {dissi} dissipation [m2/s3]

### Soil variables {time} {levs}

 {zs} height of soil level [m]
 {ts} soil temperature [K]
 {ths} soil water content [m3/m3]

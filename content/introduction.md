Title: Introduction
Date: 2017-06-12 10:20
Category: General
save_as: introduction.html

# Context

Urban areas are characterized by a clearly different meteorology than rural areas.
With the refinement of the resolution of numerical weather prediction models, the consideration of the surface energy balance of urban areas require a specific representation to account for radiative  trapping,  urban  vegetation,  anthropogenic  heat  flux,  heat  storage  in  the  urban fabric.
Many urban canopy models of different complexity have been developed in the last decades.
Grimmond et al (2010, 2011) compared a myriad of the models on the performance of the surface energy balance, and identified a ranking in the essentials of processes to be represented  and  parameter  space.
In  that  particular  study  the  models  were  driven  by observations taken above the canopy, which is a state of the art method to evaluate land surface models.
However, in the real world, these urban canopy schemes are operating in conjunction with boundary-layer schemes that are responsible for transport of heat, moisture and  momentum  from  the  surface  through  the  lower  atmosphere,  as  well  as  with  the  free atmosphere due to entrainment.
This coupling leads to feedbacks and dependencies on the schemes that have so far not been quantified.
Here we propose a modelling experiment in which we further evaluate the modelling infrastructure for the urban boundary layer coupled to the urban land surface.

This modelling exercise specifically aims to:

* Evaluate  single-column  models  coupled  to  the  urban  surface  for  the  urban environment against field observations at the surface as well and in the PBL. 

* Identify key strengths and weaknesses in these model approaches. 

* Identify feedbacks and their strengths between urban canopy schemes and boundary-layer scheme. 

* Provide a benchmark case study for later use in the community.  
 
In this sense the proposed work build upon earlier experiments in the GABLS (Holtslag et al, 2013) and DICE (Best and Lock, 2016) communities. 
 
# Case selection 

Since  this  will  be  the  first  model  comparison  study  for  urban  areas,  we  propose  to  start relatively simple and search for a clear-sky period with relatively low winds (geowind < 5 m/s) for a period of 48-72 h.
In general vertical information of the structure of the atmosphere is scarce  from  observations,  though  for  London  (Bohnenstengel  et  al  2013)  a  wide  suite  of observations is at hand.
Therefore we propose to select a case study for London. 

# Workflow 

Since the setup of such a case study is not a trivial thing to do, we propose to perform the intercomparison in two phases.
Phase 0 covers the time available at the eWUDAPT workshop in which the participants thoroughly prepare the intercomparison and analyse pro and cons of the setups.
In phase 1 the single column model intercomparison is being released to the whole research community, and results will be discussed at later workshops (e.g. during ICUC-2018).
Moreover, each phase will cover multiple stages.

 * Stage 1: In this stage only the urban land surface schemes will be evaluated, analogous to PILPS-urban.
   Urban  morphological  parameters  will  be  provided  by  WG1  in  the eWUDAPT workshop and formulated in terms of local climate zones.
 
 * Stage 2: In this stage the same urban morphological parameters will be provided as in stage 1, but now to the single column model will be run.
   In this way one can identify the model behaviour of the land surface scheme in connection to the PBL scheme.
 
 * Stage 3: In this stage modellers are asked to apply their default model settings for the urban scheme.
   This allows for model evaluation against real world observations.
   For phase 1 identical steps will be undertaken, but for the whole community.

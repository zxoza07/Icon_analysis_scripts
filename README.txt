This repo is collection of .ipynb-Plot routines to analyze data from icon-paleo simulations. 
There is a LIG a PI and a LIG.ghg simulation, which is analyzed.
Often plotting the Anomaly between LIG and PI regarding sea_ice_fraction or Temperature.


Here a short description of files:


Important Plot routines:

Standard_notebook.ipynb:
    Default notebook template if you want to make new plot routines

Worldmap_Temp_Anomalies.ipynb
    Gives Temperature Anomaly for Annual, July and January between LIG & PI
    for whole Worldmap and Polar Regions. 
    
sif_buildup.ipynb:
    Same but for Sea_Ice_fraction
    Gives Sea Ice_Fraction Anomaly for Annual, July and January between LIG & PI
    for Polar Regions 
    but build up plot step by step
    at the end there is also a comparison to Kiras Plot, in the end the actual reason
    is that at Kiras Plot the annotation is mixed up (Like the "July" sea ice is actually from January)
    
GMST.ipynb:
    Plots GMST of time for PI, LIG and LIG_ghg

Arctic.ipynb:
    Plots NH from 45°-90° temperature and sea_ice_fraction over time for PI, LIG and LIG_ghg
    
    
    
    
    
    
    
Not so important plot routines:

Worldmap_sif_Anomalies.ipynb:
    failed plots of sif worldmaps, use sif_buildup instead !!!!!

sif_Kiras_Data_buildup.ipynb:
    Same as sif_buildup.ipynb but with Kira's differently remapped data
    Result  ==> not much difference from my data, Kiras remapping does not obstruct the data
    just the resolution is higher (which "pretends" a unrealistically high resolution)
    
    
sif_mine_vs_Kiras_Data_comparison.ipynb:
    Here I explicitly derive the difference between my and Kiras differntly remapped data
    result ==> not much difference from my data, Kiras remapping does not obstruct the data
    
    
    
Other stuff:
plot_settings.py
    Here the rc_Params for all plots are set. (font sizes etc.)
    Change something here and all the plots will look different.
                    
sim=TitanSimulation(overwrite_output=True)

sim.setGIS(
    gis_format='GIS_GRASS', 
    gis_main='../dem',
    gis_sub='oak_sy',
    gis_mapset='PERMANENT',
    gis_map='Oak_Sy'
)

sim.setScale(
    length_scale=1.0,
    gravity_scale=1.0,
)

sim.setNumProp(
    AMR=False,
    number_of_cells_across_axis=2,
    order='First',
    geoflow_tiny=0.0001
)
sim.setMatModel(
    model='TwoPhases-Pitman-Le',
    int_frict=22.0,
    bed_frict=15.0
)
sim.addPile(
    pile_type='Cylinder',
    height=3.0,
    center=[260855,3818811],
    radii=[10.0, 10.0],
    orientation=0.0,
    Vmagnitude=0.0,
    Vdirection=0.0,
    vol_fract=0.7,
)
'''
sim.addPile(
    pile_type='Cylinder',
    height=5.0,
    center=[260871,3818475],
    radii=[55.0, 55.0],
    orientation=0.0,
    Vmagnitude=0.0,
    Vdirection=0.0,
    vol_fract=0.7,
)
'''

sim.setTimeProps(
    #max_iter=1000,
    max_time=3610
)

sim.setTimeSeriesOutput(
    vizoutput=('xdmf'),
    dtime=600.0,
)

sim.setOutlineProps(
    output_prefix='',
    enabled=True,
    max_linear_size=2500,
    init_size='DEM' #default AMR
)

#start simulation
sim.run()

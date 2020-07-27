# MIRI-asteroid-detection

Code to extract a fixed source of light out of a moving one. Meant to allow for seredipitous asteroid detection using the Mid-infrared Instrument (MIRI) on board of the James Webb Space Telescope (JWST). JWST's data-reduction pipeline (specifically the Ramps-to-Slopes stage) will reject any moving source as an artefact, hence the need to collapse any source of interest before processing.

Run move_source_code.py in order to collapse the source. The dq_init step of the pipeline is meant to be run first and separately. Then run change_pixeldq.py to manipulate the PIXELDQ array as needed, and then the rest of the pipeline, skipping dq_init and refpix. Instructions on running the pipeline found here: https://paddykavanagh.github.io/Introduction.html (last visited on 27/07/2020). MIRISim example input files for asteroid (2006 QG93) and example image also included.  

Developed as part of my first year's research project, MSc in Astronomy, Leiden University.

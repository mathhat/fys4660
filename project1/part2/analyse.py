# analyse.py
from ovito.io import import_file
from ovito.modifiers import *
from matplotlib.pyplot import *
'''
filename = "dump.xyz"
pipeline = import_file(filename, multiple_frames=True)

myComputePropertyModifier =ComputePropertyModifier(
                            output_property="Velocity Magnitude",
                            expressions=["sqrt( Velocity.X^2+Velocity.Y^2+Velocity.Z^2)"])

pipeline.modifiers.append(myComputePropertyModifier)

myHistogramModifier = HistogramModifier(
                        property="Velocity Magnitude", 
                        bin_count=100, 
                        fix_xrange=True, 
                        xrange_end=10)
#pipeline.modifiers.append(myHistogramModifier)
'''

import numpy

# Load a particle dataset, apply modifier, and evaluate data pipeline.
node = import_file("dump_0.xyz")
modifier = CoordinationNumberModifier(cutoff = 100.0, number_of_bins = 1000)
node.modifiers.append(modifier)
node.compute()

# Export the computed RDF data to a text file.
#numpy.savetxt("output_rdf.txt", modifier.rdf)


node.add_to_scene()

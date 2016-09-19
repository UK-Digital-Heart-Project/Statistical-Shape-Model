#!/usr/bin/python
# Reconstruct the shape at a certain standard deviation from the mean shape model

import vtk, numpy as np

# Specify the anatomical structure
which_shape  = 'LV'  # LV, RV or Both
which_mode   = 0     # 0 corresponds to the 1st PC
how_much_std = 3     # 3 standard deviation

# Read the mean shape
reader = vtk.vtkPolyDataReader()
mean_shape = '{0}_ED_mean.vtk'.format(which_shape)
reader.SetFileName(mean_shape)
reader.Update()
polydata = reader.GetOutput()
points = polydata.GetPoints()
n_points = points.GetNumberOfPoints()

# Read the principal component and variance
pc = np.genfromtxt('LV_ED_pc_100_modes.csv.gz', delimiter=',')
variance = np.genfromtxt('LV_ED_var_100_modes.csv.gz', delimiter=',')

pc_i = pc[:, which_mode]
pc_i = np.reshape(pc_i, (n_points, 3))
std = np.sqrt(variance[which_mode])

# Compute the varying shape
for j in range(0, n_points):
    p = points.GetPoint(j)
    p += how_much_std * std * pc_i[j]
    points.SetPoint(j, p)

# Write the shape
writer = vtk.vtkPolyDataWriter()
writer.SetInputData(polydata)
writer.SetFileName('LV_ED_mode{0}_{1}std.vtk'.format(which_mode + 1, how_much_std))
writer.Write()

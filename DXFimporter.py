#!/usr/bin/env python2.7
import sys
import os, os.path, glob
sys.path.append(#~~~'IronPython Folder Path'~~~)
sys.path.append(#~~~'IronPython Rhinoscript Folder Path'~~~)
import rhinoscriptsyntax as rs

# Opens text file containing strings of all DXF files + absolute folder path
DXF_ext_file = open(#~~~'DXF files reference text file path'~~~)
DXF_files = DXF_ext_file.read()
DXF_files = DXF_files.splitlines()
transx = []
tx = []
trans_list= []
total = 0
curve_objs = []

# Loops over DXF files importing every file, joining curves and naming per dxf file
for i in range(len(DXF_files)-1):

    cmd="_-Import " + "\"" + DXF_files[0] + DXF_files[i+1] + "\"" + " _Enter"
    rs.Command(cmd)
    objs = rs.SelectedObjects()
    curve_objs = []

    # filter out non-curve objects & delete
    for k in range(len(objs)):
        if rs.IsCurve(objs[k]):
            curve_objs.append(objs[k])
        else:
            rs.DeleteObject(objs[k])

    curveID = rs.JoinCurves(curve_objs, True)
    objname = rs.ObjectName(curveID, DXF_files[i+1])
    bbox = rs.BoundingBox(curveID)
    for j in range (2):
        transvals = str(bbox[j])
        trans_list = transvals.split(",")
        transx.append(trans_list[0])

    tx.append(float(transx[i*2+1]) - float(transx[i*2]))
    if i > 0:
        xval = tx[i-1] + 100
        total = total + xval

    matrix = rs.XformTranslation([total,0,0])
    translation = rs.TransformObject(curveID, matrix)




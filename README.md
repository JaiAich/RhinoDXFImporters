Python script files to automate the import of multiple individual .dxf CAD drawing files into a single .3dm
Rhino file.

Requires IronPython, Python 3 and Rhinoceros 5.

The program DXFimporter.py is called by BatchDXFImporter.py which loops over every file within a user selected 
directory importing each one.

The DXF curves themselves are named using the DXF file name itself specific to each file.

Local file paths need changing - indicated by ~~~...~~~ each side of path.

BatchDXFImporter handles the looping through every file with windows commands.
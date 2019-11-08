# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def ww():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    odb = session.odbs['D:/ry/RUOSTE/40-5/R-40-5-1,14.odb']
    session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
        NODAL, ((COMPONENT, 'RF1'), (COMPONENT, 'RF2'), (COMPONENT, 'RF3'), )), 
        ), nodeSets=('REFMACRO1', 'REFMACRO2', 'REFMACRO3', ))


def ee():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    abq_ExcelUtilities.excelUtilities.XYtoExcel(
        xyDataNames='RF:RF1 PI: ASSEMBLY N: 1,RF:RF2 PI: ASSEMBLY N: 2,RF:RF3 PI: ASSEMBLY N: 3', 
        trueName='')


def rr():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    del session.xyDataObjects['RF:RF1 PI: ASSEMBLY N: 1']
    del session.xyDataObjects['RF:RF1 PI: ASSEMBLY N: 2']
    del session.xyDataObjects['RF:RF1 PI: ASSEMBLY N: 3']
    del session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 1']
    del session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 2']
    del session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 3']
    del session.xyDataObjects['RF:RF3 PI: ASSEMBLY N: 1']
    del session.xyDataObjects['RF:RF3 PI: ASSEMBLY N: 2']
    del session.xyDataObjects['RF:RF3 PI: ASSEMBLY N: 3']



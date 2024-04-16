import numpy as np
import scipy.signal


#########################################################
#BUILDS THE ARRAYS WITH PERCENT CHANCE OF DAMAGE OUTCOME#
#########################################################

def build_arrDDC(DDF, ND):
    if ND == 1:
        arrDDC = np.empty(DDF)
        arrDDC.fill(1/DDF)
    elif ND == 2:
        arrDD1 = np.empty(DDF)
        arrDD1.fill(1)
        arrDD2 = arrDD1
        arrDDC = scipy.signal.fftconvolve(arrDD1,arrDD2)/(np.size(arrDD1)*np.size(arrDD2))
    return(arrDDC)

##################################################
#BUILDS THE ARRAY WITH THE POSSIBLE DAMAGE VALUES#
##################################################

def build_arrDV(DDF, ND):
    if ND == 1:
        arrDV = np.empty(DDF)
        for i in range(0,len(arrDV)):
            arrDV[i] = i+1
    elif ND == 2:
        arrDV = np.empty(2*DDF-1)
        for i in range(0,len(arrDV)):
            arrDV[i] = i+2
    return(arrDV)

################################################
#CALCULATE THE EXPECTATION VALUE OF DAMAGE DICE#
################################################

def calc_EDV(DDF, ND, AM):
    EDV = 0.
    arrDV = build_arrDV(DDF,ND)
    arrDDC = build_arrDDC(DDF,ND)
    for i in range(0,len(arrDDC)):
        EDV = EDV + arrDDC[i]*arrDV[i]
    EDV = EDV + AM
    EDV = EDV + EDV*0.05
    return(EDV)

#########################################################################
#CALCULATE THE CHANCE TO HIT GIVEN ARMOR CLASS, ATTACK MOD, AND PROF MOD#
#########################################################################

def calc_CtH(AC, AM, PM):
    EAC = AC - AM - PM
    if EAC < 2:
        EAC = 2
    elif EAC > 20:
        EAC = 20
    CtH = (20 - (EAC-1))*0.05
    return(CtH)

#########################
#CALCULATE EFFECTIVE DPR#
#########################

def calc_EDPR(AC, AM, PM, Sharp, Steady, nAtk, nFaces, nDice):
    DM = AM

    if Sharp:
        AM = AM - 5
        DM = DM + 10

    if Steady:
        AM = AM + 5
        nAtk = nAtk/2

    CtH = calc_CtH(AC, AM, PM)
    EDV = calc_EDV(nFaces, nDice, DM)
    EDPR = (EDV * nAtk) * CtH
    return(EDPR)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on 十二月 11, 2019, at 20:41
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'ppp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\TAIIC\\psychopy测试\\2\\ppp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='脑机接口\n\n视觉刺激实验\n\n按"空格"继续\n\n可随时按"ESC"退出',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
# instr Begin Experiment
import numpy as np

Freq = np.array([8.00, 14.00, 10.00, 11.00, 12.00, 13.00, 9.00, 15.00])
Phas = np.array([1.05,  0.10,  0.35,  1.40,  0.45, 0.70,  1.75,  0.80])

varpy = [600,90]

x0 = 1020*0/3 - 510
x1 = 1020*1/3 - 510
x2 = 1020*2/3 - 510
x3 = 1020*3/3 - 510

y0 = 1020*0/3 - 510
y1 = 1020*1/3 - 510
y2 = 1020*2/3 - 510
y3 = 1020*3/3 - 510

mylocation = [
[(x0+x1)/2,(y2+y3)/2],
[(x1+x2)/2,(y2+y3)/2],
[(x2+x3)/2,(y2+y3)/2],

[(x0+x1)/2,(y1+y2)/2],
[(x1+x2)/2,(y1+y2)/2],
[(x2+x3)/2,(y1+y2)/2],

[(x0+x1)/2,(y0+y1)/2],
[(x1+x2)/2,(y0+y1)/2],
[(x2+x3)/2,(y0+y1)/2]
]

size_w = 200
size_h = 200


# Initialize components for Routine "cue"
cueClock = core.Clock()
polygon_0 = visual.Rect(
    win=win, name='polygon_0',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_1 = visual.Rect(
    win=win, name='polygon_1',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_4 = visual.Rect(
    win=win, name='polygon_4',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon_6 = visual.Rect(
    win=win, name='polygon_6',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
polygon_7 = visual.Rect(
    win=win, name='polygon_7',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
polygon_8 = visual.Rect(
    win=win, name='polygon_8',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
loop_id = -1

# Initialize components for Routine "trial"
trialClock = core.Clock()
polygon_trial_0 = visual.Rect(
    win=win, name='polygon_trial_0',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_trial_1 = visual.Rect(
    win=win, name='polygon_trial_1',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_trial_2 = visual.Rect(
    win=win, name='polygon_trial_2',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_trial_3 = visual.Rect(
    win=win, name='polygon_trial_3',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_trial_4 = visual.Rect(
    win=win, name='polygon_trial_4',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon_trial_5 = visual.Rect(
    win=win, name='polygon_trial_5',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon_trial_6 = visual.Rect(
    win=win, name='polygon_trial_6',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
polygon_trial_7 = visual.Rect(
    win=win, name='polygon_trial_7',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
polygon_trial_8 = visual.Rect(
    win=win, name='polygon_trial_8',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
instrComponents = [text, key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cue"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    polygon_0.setPos((mylocation[0][0], mylocation[0][1]))
    polygon_0.setSize((size_w, size_h))
    polygon_1.setPos((mylocation[1][0], mylocation[1][1]))
    polygon_1.setSize((size_w, size_h))
    polygon_2.setPos((mylocation[2][0],mylocation[2][1]))
    polygon_2.setSize((size_w,size_h))
    polygon_3.setPos((mylocation[3][0],mylocation[3][1]))
    polygon_3.setSize((size_w,size_h))
    polygon_4.setPos((mylocation[4][0], mylocation[4][1]))
    polygon_4.setSize((5, 5))
    polygon_5.setPos((mylocation[5][0], mylocation[5][1]))
    polygon_5.setSize((size_w, size_h))
    polygon_6.setPos((mylocation[6][0], mylocation[6][1]))
    polygon_6.setSize((size_w, size_h))
    polygon_7.setPos((mylocation[7][0], mylocation[7][1]))
    polygon_7.setSize((size_w, size_h))
    polygon_8.setPos((mylocation[8][0], mylocation[8][1]))
    polygon_8.setSize((size_w, size_h))
    
    
    # peiyu code cue
    selecList = [polygon_0, polygon_1, polygon_2, polygon_3, polygon_5, polygon_6, polygon_7, polygon_8]
    selecList[ loop_id    %8].setFillColor([1.000,1.000,1.000]) # rgb
    loop_id += 1
    selecList[ loop_id    %8].setFillColor([1.000,-1.000,-1.000]) # rgb
    
    
    # peiyu code cue End
    # keep track of which components have finished
    cueComponents = [polygon_0, polygon_1, polygon_2, polygon_3, polygon_4, polygon_5, polygon_6, polygon_7, polygon_8]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_0* updates
        if polygon_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_0.frameNStart = frameN  # exact frame index
            polygon_0.tStart = t  # local t and not account for scr refresh
            polygon_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_0, 'tStartRefresh')  # time at next scr refresh
            polygon_0.setAutoDraw(True)
        if polygon_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_0.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_0.tStop = t  # not accounting for scr refresh
                polygon_0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_0, 'tStopRefresh')  # time at next scr refresh
                polygon_0.setAutoDraw(False)
        
        # *polygon_1* updates
        if polygon_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_1.frameNStart = frameN  # exact frame index
            polygon_1.tStart = t  # local t and not account for scr refresh
            polygon_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_1, 'tStartRefresh')  # time at next scr refresh
            polygon_1.setAutoDraw(True)
        if polygon_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_1.tStop = t  # not accounting for scr refresh
                polygon_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_1, 'tStopRefresh')  # time at next scr refresh
                polygon_1.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        if polygon_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
                polygon_5.setAutoDraw(False)
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(False)
        
        # *polygon_7* updates
        if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            polygon_7.setAutoDraw(True)
        if polygon_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_7.tStop = t  # not accounting for scr refresh
                polygon_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_7, 'tStopRefresh')  # time at next scr refresh
                polygon_7.setAutoDraw(False)
        
        # *polygon_8* updates
        if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.tStart = t  # local t and not account for scr refresh
            polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            polygon_8.setAutoDraw(True)
        if polygon_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon_8.tStop = t  # not accounting for scr refresh
                polygon_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_8, 'tStopRefresh')  # time at next scr refresh
                polygon_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_0.started', polygon_0.tStartRefresh)
    trials.addData('polygon_0.stopped', polygon_0.tStopRefresh)
    trials.addData('polygon_1.started', polygon_1.tStartRefresh)
    trials.addData('polygon_1.stopped', polygon_1.tStopRefresh)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    trials.addData('polygon_3.started', polygon_3.tStartRefresh)
    trials.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    trials.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    trials.addData('polygon_6.started', polygon_6.tStartRefresh)
    trials.addData('polygon_6.stopped', polygon_6.tStopRefresh)
    trials.addData('polygon_7.started', polygon_7.tStartRefresh)
    trials.addData('polygon_7.stopped', polygon_7.tStopRefresh)
    trials.addData('polygon_8.started', polygon_8.tStartRefresh)
    trials.addData('polygon_8.stopped', polygon_8.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    polygon_trial_0.setPos((mylocation[0][0], mylocation[0][1]))
    polygon_trial_0.setSize((size_w, size_h))
    polygon_trial_1.setPos((mylocation[1][0], mylocation[1][1]))
    polygon_trial_1.setSize((size_w, size_h))
    polygon_trial_2.setPos((mylocation[2][0], mylocation[2][1]))
    polygon_trial_2.setSize((size_w,size_h))
    polygon_trial_3.setPos((mylocation[3][0], mylocation[3][1]))
    polygon_trial_3.setSize((size_w,size_h))
    polygon_trial_4.setPos((mylocation[4][0], mylocation[4][1]))
    polygon_trial_4.setSize((5,5))
    polygon_trial_5.setPos((mylocation[5][0], mylocation[5][1]))
    polygon_trial_5.setSize((size_w,size_h))
    polygon_trial_6.setPos((mylocation[6][0], mylocation[6][1]))
    polygon_trial_6.setSize((size_w,size_h))
    polygon_trial_7.setPos((mylocation[7][0], mylocation[7][1]))
    polygon_trial_7.setSize((size_w,size_h))
    polygon_trial_7.setFillColor([1,1,1])
    polygon_trial_8.setPos((mylocation[8][0], mylocation[8][1]))
    polygon_trial_8.setSize((size_w,size_h))
    trial_dura = 2
    
    seleclist2 = [polygon_trial_0, polygon_trial_1, polygon_trial_2, polygon_trial_3, polygon_trial_5, polygon_trial_6, polygon_trial_7, polygon_trial_8]
    # keep track of which components have finished
    trialComponents = [polygon_trial_0, polygon_trial_1, polygon_trial_2, polygon_trial_3, polygon_trial_4, polygon_trial_5, polygon_trial_6, polygon_trial_7, polygon_trial_8]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_trial_0* updates
        if polygon_trial_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_0.frameNStart = frameN  # exact frame index
            polygon_trial_0.tStart = t  # local t and not account for scr refresh
            polygon_trial_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_0, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_0.setAutoDraw(True)
        if polygon_trial_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_0.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_0.tStop = t  # not accounting for scr refresh
                polygon_trial_0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_0, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_0.setAutoDraw(False)
        if polygon_trial_0.status == STARTED:  # only update if drawing
            polygon_trial_0.setFillColor([1,1,1], log=False)
        
        # *polygon_trial_1* updates
        if polygon_trial_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_1.frameNStart = frameN  # exact frame index
            polygon_trial_1.tStart = t  # local t and not account for scr refresh
            polygon_trial_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_1, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_1.setAutoDraw(True)
        if polygon_trial_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_1.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_1.tStop = t  # not accounting for scr refresh
                polygon_trial_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_1, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_1.setAutoDraw(False)
        if polygon_trial_1.status == STARTED:  # only update if drawing
            polygon_trial_1.setFillColor([1,1,1], log=False)
        
        # *polygon_trial_2* updates
        if polygon_trial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_2.frameNStart = frameN  # exact frame index
            polygon_trial_2.tStart = t  # local t and not account for scr refresh
            polygon_trial_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_2, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_2.setAutoDraw(True)
        if polygon_trial_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_2.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_2.tStop = t  # not accounting for scr refresh
                polygon_trial_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_2, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_2.setAutoDraw(False)
        if polygon_trial_2.status == STARTED:  # only update if drawing
            polygon_trial_2.setFillColor([1,1,1], log=False)
        
        # *polygon_trial_3* updates
        if polygon_trial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_3.frameNStart = frameN  # exact frame index
            polygon_trial_3.tStart = t  # local t and not account for scr refresh
            polygon_trial_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_3, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_3.setAutoDraw(True)
        if polygon_trial_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_3.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_3.tStop = t  # not accounting for scr refresh
                polygon_trial_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_3, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_3.setAutoDraw(False)
        if polygon_trial_3.status == STARTED:  # only update if drawing
            polygon_trial_3.setFillColor([1,1,1], log=False)
        
        # *polygon_trial_4* updates
        if polygon_trial_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_4.frameNStart = frameN  # exact frame index
            polygon_trial_4.tStart = t  # local t and not account for scr refresh
            polygon_trial_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_4, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_4.setAutoDraw(True)
        if polygon_trial_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_4.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_4.tStop = t  # not accounting for scr refresh
                polygon_trial_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_4, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_4.setAutoDraw(False)
        
        # *polygon_trial_5* updates
        if polygon_trial_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_5.frameNStart = frameN  # exact frame index
            polygon_trial_5.tStart = t  # local t and not account for scr refresh
            polygon_trial_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_5, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_5.setAutoDraw(True)
        if polygon_trial_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_5.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_5.tStop = t  # not accounting for scr refresh
                polygon_trial_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_5, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_5.setAutoDraw(False)
        if polygon_trial_5.status == STARTED:  # only update if drawing
            polygon_trial_5.setFillColor([1,1,1], log=False)
        
        # *polygon_trial_6* updates
        if polygon_trial_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_6.frameNStart = frameN  # exact frame index
            polygon_trial_6.tStart = t  # local t and not account for scr refresh
            polygon_trial_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_6, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_6.setAutoDraw(True)
        if polygon_trial_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_6.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_6.tStop = t  # not accounting for scr refresh
                polygon_trial_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_6, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_6.setAutoDraw(False)
        if polygon_trial_6.status == STARTED:  # only update if drawing
            polygon_trial_6.setFillColor([1,1,1], log=False)
        
        # *polygon_trial_7* updates
        if polygon_trial_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_7.frameNStart = frameN  # exact frame index
            polygon_trial_7.tStart = t  # local t and not account for scr refresh
            polygon_trial_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_7, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_7.setAutoDraw(True)
        if polygon_trial_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_7.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_7.tStop = t  # not accounting for scr refresh
                polygon_trial_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_7, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_7.setAutoDraw(False)
        
        # *polygon_trial_8* updates
        if polygon_trial_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_8.frameNStart = frameN  # exact frame index
            polygon_trial_8.tStart = t  # local t and not account for scr refresh
            polygon_trial_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_8, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_8.setAutoDraw(True)
        if polygon_trial_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_8.tStartRefresh + trial_dura-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_8.tStop = t  # not accounting for scr refresh
                polygon_trial_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_8, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_8.setAutoDraw(False)
        if polygon_trial_8.status == STARTED:  # only update if drawing
            polygon_trial_8.setFillColor([1,1,1], log=False)
        # peiyu code
        #f1 = 5
        #phi1 = 0
        #amp1 = (sin(2*pi*f1*frameN/60) - 0.5)*2
        #f2 = 20
        #phi2 = 0
        #amp2 = (sin(2 * pi * f2 * frameN / 60) - 0.5) * 2
        #polygon.setFillColor([amp1, amp1, amp1])
        #polygon_2.setFillColor([amp2, amp2, amp2])
        
        
        Amp = (sin(2*pi*Freq*frameN/60  + Phas) - 0.5)*2
        
        print(Amp)
        
        for idx in range(8):
            seleclist2[idx].setFillColor([Amp[i]])
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_trial_0.started', polygon_trial_0.tStartRefresh)
    trials.addData('polygon_trial_0.stopped', polygon_trial_0.tStopRefresh)
    trials.addData('polygon_trial_1.started', polygon_trial_1.tStartRefresh)
    trials.addData('polygon_trial_1.stopped', polygon_trial_1.tStopRefresh)
    trials.addData('polygon_trial_2.started', polygon_trial_2.tStartRefresh)
    trials.addData('polygon_trial_2.stopped', polygon_trial_2.tStopRefresh)
    trials.addData('polygon_trial_3.started', polygon_trial_3.tStartRefresh)
    trials.addData('polygon_trial_3.stopped', polygon_trial_3.tStopRefresh)
    trials.addData('polygon_trial_4.started', polygon_trial_4.tStartRefresh)
    trials.addData('polygon_trial_4.stopped', polygon_trial_4.tStopRefresh)
    trials.addData('polygon_trial_5.started', polygon_trial_5.tStartRefresh)
    trials.addData('polygon_trial_5.stopped', polygon_trial_5.tStopRefresh)
    trials.addData('polygon_trial_6.started', polygon_trial_6.tStartRefresh)
    trials.addData('polygon_trial_6.stopped', polygon_trial_6.tStopRefresh)
    trials.addData('polygon_trial_7.started', polygon_trial_7.tStartRefresh)
    trials.addData('polygon_trial_7.stopped', polygon_trial_7.tStopRefresh)
    trials.addData('polygon_trial_8.started', polygon_trial_8.tStartRefresh)
    trials.addData('polygon_trial_8.stopped', polygon_trial_8.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

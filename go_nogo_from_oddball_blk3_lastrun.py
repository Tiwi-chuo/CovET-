#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on 11月 06, 2025, at 18:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Calibration
import os
from psychopy import visual, monitors
import numpy as np
import matplotlib.pyplot as plt
from titta import Titta, helpers_tobii as helpers
import h5py
import shutil
import pandas as pd
from titta import Titta
# Run 'Before Experiment' code from code_go
from psychopy import visual
import random
# + numpy
import numpy as np
import pandas as pd
from PIL import Image

# Run 'Before Experiment' code from code_nogo
from psychopy import visual
import random
# + numpy
import numpy as np
import pandas as pd
from PIL import Image

# Run 'Before Experiment' code from code_go
from psychopy import visual
import random
# + numpy
import numpy as np
import pandas as pd
from PIL import Image

# Run 'Before Experiment' code from code_nogo
from psychopy import visual
import random
# + numpy
import numpy as np
import pandas as pd
from PIL import Image

# Run 'Before Experiment' code from code_go
from psychopy import visual
import random
# + numpy
import numpy as np
import pandas as pd
from PIL import Image

# Run 'Before Experiment' code from code_nogo
from psychopy import visual
import random
# + numpy
import numpy as np
import pandas as pd
from PIL import Image

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'go_nogo'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'eyetracker': 'Tobii Pro Spectrum',
    'dummymode': False,
    'f/m': 'f',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\pussycat\\Danlab Dropbox\\eyetracking\\covet\\Experiment_tiwii\\exp1\\go_nogo_from_oddball_blk3_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='ptb')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='PsychToolbox')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "ET_Setup" ---
    # Run 'Begin Experiment' code from Calibration
    et_name = expInfo['eyetracker']
    settings = Titta.get_defaults(et_name)
    settings.FILENAME = expInfo['participant']
    
    # Export dir
    
    et_out_dir = 'et_data'
    if not os.path.exists(et_out_dir):
        os.mkdir(et_out_dir)
    settings.DATA_STORAGE_PATH = et_out_dir
    
    # Sampling freq.
    
    if settings.eye_tracker_name == "Tobii Pro Fusion":
        settings.SAMPLING_RATE = 250
    if settings.eye_tracker_name == "Tobii Pro Spectrum":
        settings.SAMPLING_RATE = 1200
    
    # Connect to eye tracker
    
    tracker = Titta.Connect(settings)
    
    # Dummy mode
    if expInfo['dummymode']:
        tracker.set_dummy_mode()
    tracker.init()
    # Calibrate
    
    tracker.calibrate(win)
    tracker.start_recording(gaze=True)
    
    
    # --- Initialize components for Routine "intro_exp_gonogo" ---
    intro_gonogo_key = keyboard.Keyboard()
    Intro_gonogo = visual.TextStim(win=win, name='Intro_gonogo',
        text='これから認知課題を実施します。\n準備ができたらSpaceキーを押してください。',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "intro_go_1" ---
    intro_text_go_1 = visual.TextStim(win=win, name='intro_text_go_1',
        text='画面にロゴ画像が表示されたら\nSPACEキーを押してください。\nできる限り早く正確に回答してください。',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introLoop_key_go_1 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Go" ---
    # Run 'Begin Experiment' code from code_go
    correct_counter=0
    
    fixation_cross_trial_go = visual.ShapeStim(
        win=win, name='fixation_cross_trial_go', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    images_go = visual.ImageStim(
        win=win,
        name='images_go', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    trial_key_go = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "intro_gonogo_1" ---
    intro_text_nogo_1 = visual.TextStim(win=win, name='intro_text_nogo_1',
        text='画面に以下のロゴ画像が表示されたら\nSPACEキーを押さないでください。\nそれ以外のロゴ画像が表示されたら\nSPACEキーを押してください。\nできる限り早く正確に回答してください。',
        font='Open Sans',
        pos=(0, 0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introLoop_key_nogo_1 = keyboard.Keyboard()
    intro_targetimg_nogo_1 = visual.ImageStim(
        win=win,
        name='intro_targetimg_nogo_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Go_Nogo" ---
    # Run 'Begin Experiment' code from code_nogo
    correct_counter=0
    
    fixation_cross_trial_nogo = visual.ShapeStim(
        win=win, name='fixation_cross_trial_nogo', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    images_nogo = visual.ImageStim(
        win=win,
        name='images_nogo', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    trial_key_nogo = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "intro_go_2" ---
    intro_text_go_2 = visual.TextStim(win=win, name='intro_text_go_2',
        text='画面にロゴ画像が表示されたら\nSPACEキーを押してください。\nできる限り早く正確に回答してください。',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introLoop_key_go_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Go" ---
    # Run 'Begin Experiment' code from code_go
    correct_counter=0
    
    fixation_cross_trial_go = visual.ShapeStim(
        win=win, name='fixation_cross_trial_go', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    images_go = visual.ImageStim(
        win=win,
        name='images_go', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    trial_key_go = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "intro_gonogo_2" ---
    intro_text_nogo_2 = visual.TextStim(win=win, name='intro_text_nogo_2',
        text='画面に以下のロゴ画像が表示されたら\nSPACEキーを押さないでください。\nそれ以外のロゴ画像が表示されたら\nSPACEキーを押してください。\nできる限り早く正確に回答してください。',
        font='Open Sans',
        pos=(0, 0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introLoop_key_nogo_2 = keyboard.Keyboard()
    intro_tagetimg_nogo_2 = visual.ImageStim(
        win=win,
        name='intro_tagetimg_nogo_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Go_Nogo" ---
    # Run 'Begin Experiment' code from code_nogo
    correct_counter=0
    
    fixation_cross_trial_nogo = visual.ShapeStim(
        win=win, name='fixation_cross_trial_nogo', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    images_nogo = visual.ImageStim(
        win=win,
        name='images_nogo', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    trial_key_nogo = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "intro_go_3" ---
    intro_text_go_3 = visual.TextStim(win=win, name='intro_text_go_3',
        text='画面にロゴ画像が表示されたら\nSPACEキーを押してください。\nできる限り早く正確に回答してください。',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introLoop_key_go_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Go" ---
    # Run 'Begin Experiment' code from code_go
    correct_counter=0
    
    fixation_cross_trial_go = visual.ShapeStim(
        win=win, name='fixation_cross_trial_go', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    images_go = visual.ImageStim(
        win=win,
        name='images_go', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    trial_key_go = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "intro_gonogo_3" ---
    intro_text_nogo_3 = visual.TextStim(win=win, name='intro_text_nogo_3',
        text='画面に以下のロゴ画像が表示されたら\nSPACEキーを押さないでください。\nそれ以外のロゴ画像が表示されたら\nSPACEキーを押してください。\nできる限り早く正確に回答してください。',
        font='Open Sans',
        pos=(0, 0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introLoop_key_nogo_3 = keyboard.Keyboard()
    intro_tagetimg_nogo_3 = visual.ImageStim(
        win=win,
        name='intro_tagetimg_nogo_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Go_Nogo" ---
    # Run 'Begin Experiment' code from code_nogo
    correct_counter=0
    
    fixation_cross_trial_nogo = visual.ShapeStim(
        win=win, name='fixation_cross_trial_nogo', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    images_nogo = visual.ImageStim(
        win=win,
        name='images_nogo', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    trial_key_nogo = keyboard.Keyboard()
    
    # --- Initialize components for Routine "rest" ---
    fixation_cross = visual.ShapeStim(
        win=win, name='fixation_cross', vertices='cross',units='pix', 
        size=(60, 60),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "finished" ---
    text = visual.TextStim(win=win, name='text',
        text='finish',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "ET_Setup" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ET_Setup.started', globalClock.getTime())
    # keep track of which components have finished
    ET_SetupComponents = []
    for thisComponent in ET_SetupComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ET_Setup" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ET_SetupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ET_Setup" ---
    for thisComponent in ET_SetupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ET_Setup.stopped', globalClock.getTime())
    # the Routine "ET_Setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "intro_exp_gonogo" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('intro_exp_gonogo.started', globalClock.getTime())
    intro_gonogo_key.keys = []
    intro_gonogo_key.rt = []
    _intro_gonogo_key_allKeys = []
    # keep track of which components have finished
    intro_exp_gonogoComponents = [intro_gonogo_key, Intro_gonogo]
    for thisComponent in intro_exp_gonogoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro_exp_gonogo" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_gonogo_key* updates
        waitOnFlip = False
        
        # if intro_gonogo_key is starting this frame...
        if intro_gonogo_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_gonogo_key.frameNStart = frameN  # exact frame index
            intro_gonogo_key.tStart = t  # local t and not account for scr refresh
            intro_gonogo_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_gonogo_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_gonogo_key.started')
            # update status
            intro_gonogo_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intro_gonogo_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intro_gonogo_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intro_gonogo_key.status == STARTED and not waitOnFlip:
            theseKeys = intro_gonogo_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro_gonogo_key_allKeys.extend(theseKeys)
            if len(_intro_gonogo_key_allKeys):
                intro_gonogo_key.keys = _intro_gonogo_key_allKeys[0].name  # just the first key pressed
                intro_gonogo_key.rt = _intro_gonogo_key_allKeys[0].rt
                intro_gonogo_key.duration = _intro_gonogo_key_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Intro_gonogo* updates
        
        # if Intro_gonogo is starting this frame...
        if Intro_gonogo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Intro_gonogo.frameNStart = frameN  # exact frame index
            Intro_gonogo.tStart = t  # local t and not account for scr refresh
            Intro_gonogo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Intro_gonogo, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Intro_gonogo.started')
            # update status
            Intro_gonogo.status = STARTED
            Intro_gonogo.setAutoDraw(True)
        
        # if Intro_gonogo is active this frame...
        if Intro_gonogo.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_exp_gonogoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro_exp_gonogo" ---
    for thisComponent in intro_exp_gonogoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('intro_exp_gonogo.stopped', globalClock.getTime())
    # check responses
    if intro_gonogo_key.keys in ['', [], None]:  # No response was made
        intro_gonogo_key.keys = None
    thisExp.addData('intro_gonogo_key.keys',intro_gonogo_key.keys)
    if intro_gonogo_key.keys != None:  # we had a response
        thisExp.addData('intro_gonogo_key.rt', intro_gonogo_key.rt)
        thisExp.addData('intro_gonogo_key.duration', intro_gonogo_key.duration)
    thisExp.nextEntry()
    # the Routine "intro_exp_gonogo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    exp_trails = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/targetimg.csv"),
        seed=None, name='exp_trails')
    thisExp.addLoop(exp_trails)  # add the loop to the experiment
    thisExp_trail = exp_trails.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp_trail.rgb)
    if thisExp_trail != None:
        for paramName in thisExp_trail:
            globals()[paramName] = thisExp_trail[paramName]
    
    for thisExp_trail in exp_trails:
        currentLoop = exp_trails
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisExp_trail.rgb)
        if thisExp_trail != None:
            for paramName in thisExp_trail:
                globals()[paramName] = thisExp_trail[paramName]
        
        # set up handler to look after randomisation of conditions etc
        go_gonogo_1 = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='go_gonogo_1')
        thisExp.addLoop(go_gonogo_1)  # add the loop to the experiment
        thisGo_gonogo_1 = go_gonogo_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisGo_gonogo_1.rgb)
        if thisGo_gonogo_1 != None:
            for paramName in thisGo_gonogo_1:
                globals()[paramName] = thisGo_gonogo_1[paramName]
        
        for thisGo_gonogo_1 in go_gonogo_1:
            currentLoop = go_gonogo_1
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisGo_gonogo_1.rgb)
            if thisGo_gonogo_1 != None:
                for paramName in thisGo_gonogo_1:
                    globals()[paramName] = thisGo_gonogo_1[paramName]
            
            # --- Prepare to start Routine "intro_go_1" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_go_1.started', globalClock.getTime())
            introLoop_key_go_1.keys = []
            introLoop_key_go_1.rt = []
            _introLoop_key_go_1_allKeys = []
            # keep track of which components have finished
            intro_go_1Components = [intro_text_go_1, introLoop_key_go_1]
            for thisComponent in intro_go_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "intro_go_1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *intro_text_go_1* updates
                
                # if intro_text_go_1 is starting this frame...
                if intro_text_go_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_text_go_1.frameNStart = frameN  # exact frame index
                    intro_text_go_1.tStart = t  # local t and not account for scr refresh
                    intro_text_go_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_text_go_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_text_go_1.started')
                    # update status
                    intro_text_go_1.status = STARTED
                    intro_text_go_1.setAutoDraw(True)
                
                # if intro_text_go_1 is active this frame...
                if intro_text_go_1.status == STARTED:
                    # update params
                    pass
                
                # *introLoop_key_go_1* updates
                waitOnFlip = False
                
                # if introLoop_key_go_1 is starting this frame...
                if introLoop_key_go_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    introLoop_key_go_1.frameNStart = frameN  # exact frame index
                    introLoop_key_go_1.tStart = t  # local t and not account for scr refresh
                    introLoop_key_go_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(introLoop_key_go_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'introLoop_key_go_1.started')
                    # update status
                    introLoop_key_go_1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(introLoop_key_go_1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(introLoop_key_go_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if introLoop_key_go_1.status == STARTED and not waitOnFlip:
                    theseKeys = introLoop_key_go_1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _introLoop_key_go_1_allKeys.extend(theseKeys)
                    if len(_introLoop_key_go_1_allKeys):
                        introLoop_key_go_1.keys = _introLoop_key_go_1_allKeys[0].name  # just the first key pressed
                        introLoop_key_go_1.rt = _introLoop_key_go_1_allKeys[0].rt
                        introLoop_key_go_1.duration = _introLoop_key_go_1_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_go_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "intro_go_1" ---
            for thisComponent in intro_go_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('intro_go_1.stopped', globalClock.getTime())
            # check responses
            if introLoop_key_go_1.keys in ['', [], None]:  # No response was made
                introLoop_key_go_1.keys = None
            go_gonogo_1.addData('introLoop_key_go_1.keys',introLoop_key_go_1.keys)
            if introLoop_key_go_1.keys != None:  # we had a response
                go_gonogo_1.addData('introLoop_key_go_1.rt', introLoop_key_go_1.rt)
                go_gonogo_1.addData('introLoop_key_go_1.duration', introLoop_key_go_1.duration)
            # the Routine "intro_go_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_go_1 = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/dummy_block_1.csv"),
                seed=None, name='trials_go_1')
            thisExp.addLoop(trials_go_1)  # add the loop to the experiment
            thisTrials_go_1 = trials_go_1.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_go_1.rgb)
            if thisTrials_go_1 != None:
                for paramName in thisTrials_go_1:
                    globals()[paramName] = thisTrials_go_1[paramName]
            
            for thisTrials_go_1 in trials_go_1:
                currentLoop = trials_go_1
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_go_1.rgb)
                if thisTrials_go_1 != None:
                    for paramName in thisTrials_go_1:
                        globals()[paramName] = thisTrials_go_1[paramName]
                
                # --- Prepare to start Routine "Go" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Go.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_go
                key_name = "nan"
                # covet study said 1+-0.03s is fixation-cross time
                randDuration = np.random.normal(10, 0.3) / 10
                randDuration = randDuration + 1.00
                images_go.setImage(image)
                trial_key_go.keys = []
                trial_key_go.rt = []
                _trial_key_go_allKeys = []
                # Run 'Begin Routine' code from ET_go
                # tracker.send_message('_'.join(['onset', Name.jpg_Counter"]))
                
                file_name = os.path.basename(image)
                tracker.send_message('_'.join(['onset', f"{str(file_name)}"]))
                # keep track of which components have finished
                GoComponents = [fixation_cross_trial_go, images_go, trial_key_go]
                for thisComponent in GoComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Go" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_trial_go* updates
                    
                    # if fixation_cross_trial_go is starting this frame...
                    if fixation_cross_trial_go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_trial_go.frameNStart = frameN  # exact frame index
                        fixation_cross_trial_go.tStart = t  # local t and not account for scr refresh
                        fixation_cross_trial_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_trial_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_trial_go.started')
                        # update status
                        fixation_cross_trial_go.status = STARTED
                        fixation_cross_trial_go.setAutoDraw(True)
                    
                    # if fixation_cross_trial_go is active this frame...
                    if fixation_cross_trial_go.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_trial_go is stopping this frame...
                    if fixation_cross_trial_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_trial_go.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_trial_go.tStop = t  # not accounting for scr refresh
                            fixation_cross_trial_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_trial_go.stopped')
                            # update status
                            fixation_cross_trial_go.status = FINISHED
                            fixation_cross_trial_go.setAutoDraw(False)
                    
                    # *images_go* updates
                    
                    # if images_go is starting this frame...
                    if images_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        images_go.frameNStart = frameN  # exact frame index
                        images_go.tStart = t  # local t and not account for scr refresh
                        images_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(images_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'images_go.started')
                        # update status
                        images_go.status = STARTED
                        images_go.setAutoDraw(True)
                    
                    # if images_go is active this frame...
                    if images_go.status == STARTED:
                        # update params
                        pass
                    
                    # if images_go is stopping this frame...
                    if images_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > images_go.tStartRefresh + 0.8-frameTolerance:
                            # keep track of stop time/frame for later
                            images_go.tStop = t  # not accounting for scr refresh
                            images_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'images_go.stopped')
                            # update status
                            images_go.status = FINISHED
                            images_go.setAutoDraw(False)
                    
                    # *trial_key_go* updates
                    waitOnFlip = False
                    
                    # if trial_key_go is starting this frame...
                    if trial_key_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        trial_key_go.frameNStart = frameN  # exact frame index
                        trial_key_go.tStart = t  # local t and not account for scr refresh
                        trial_key_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trial_key_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trial_key_go.started')
                        # update status
                        trial_key_go.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trial_key_go.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trial_key_go.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if trial_key_go is stopping this frame...
                    if trial_key_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > trial_key_go.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            trial_key_go.tStop = t  # not accounting for scr refresh
                            trial_key_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_key_go.stopped')
                            # update status
                            trial_key_go.status = FINISHED
                            trial_key_go.status = FINISHED
                    if trial_key_go.status == STARTED and not waitOnFlip:
                        theseKeys = trial_key_go.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _trial_key_go_allKeys.extend(theseKeys)
                        if len(_trial_key_go_allKeys):
                            trial_key_go.keys = _trial_key_go_allKeys[0].name  # just the first key pressed
                            trial_key_go.rt = _trial_key_go_allKeys[0].rt
                            trial_key_go.duration = _trial_key_go_allKeys[0].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in GoComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Go" ---
                for thisComponent in GoComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Go.stopped', globalClock.getTime())
                # Run 'End Routine' code from code_go
                print(trial_key_go.time,istarget)
                
                if len(trial_key_go.keys)>0:
                    key_name = "space"
                
                if key_name =="space":
                    correct = 1
                else:
                    correct = 0
                
                correct_counter += correct
                
                thisExp.addData("correct", correct)
                # check responses
                if trial_key_go.keys in ['', [], None]:  # No response was made
                    trial_key_go.keys = None
                trials_go_1.addData('trial_key_go.keys',trial_key_go.keys)
                if trial_key_go.keys != None:  # we had a response
                    trials_go_1.addData('trial_key_go.rt', trial_key_go.rt)
                    trials_go_1.addData('trial_key_go.duration', trial_key_go.duration)
                # Run 'End Routine' code from ET_go
                tracker.send_message('_'.join(['offset', f"{str(file_name)}"]))
                # the Routine "Go" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'trials_go_1'
            
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # --- Prepare to start Routine "intro_gonogo_1" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_gonogo_1.started', globalClock.getTime())
            introLoop_key_nogo_1.keys = []
            introLoop_key_nogo_1.rt = []
            _introLoop_key_nogo_1_allKeys = []
            intro_targetimg_nogo_1.setImage(targetimg1)
            # keep track of which components have finished
            intro_gonogo_1Components = [intro_text_nogo_1, introLoop_key_nogo_1, intro_targetimg_nogo_1]
            for thisComponent in intro_gonogo_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "intro_gonogo_1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *intro_text_nogo_1* updates
                
                # if intro_text_nogo_1 is starting this frame...
                if intro_text_nogo_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_text_nogo_1.frameNStart = frameN  # exact frame index
                    intro_text_nogo_1.tStart = t  # local t and not account for scr refresh
                    intro_text_nogo_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_text_nogo_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_text_nogo_1.started')
                    # update status
                    intro_text_nogo_1.status = STARTED
                    intro_text_nogo_1.setAutoDraw(True)
                
                # if intro_text_nogo_1 is active this frame...
                if intro_text_nogo_1.status == STARTED:
                    # update params
                    pass
                
                # *introLoop_key_nogo_1* updates
                waitOnFlip = False
                
                # if introLoop_key_nogo_1 is starting this frame...
                if introLoop_key_nogo_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    introLoop_key_nogo_1.frameNStart = frameN  # exact frame index
                    introLoop_key_nogo_1.tStart = t  # local t and not account for scr refresh
                    introLoop_key_nogo_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(introLoop_key_nogo_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'introLoop_key_nogo_1.started')
                    # update status
                    introLoop_key_nogo_1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(introLoop_key_nogo_1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(introLoop_key_nogo_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if introLoop_key_nogo_1.status == STARTED and not waitOnFlip:
                    theseKeys = introLoop_key_nogo_1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _introLoop_key_nogo_1_allKeys.extend(theseKeys)
                    if len(_introLoop_key_nogo_1_allKeys):
                        introLoop_key_nogo_1.keys = _introLoop_key_nogo_1_allKeys[0].name  # just the first key pressed
                        introLoop_key_nogo_1.rt = _introLoop_key_nogo_1_allKeys[0].rt
                        introLoop_key_nogo_1.duration = _introLoop_key_nogo_1_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *intro_targetimg_nogo_1* updates
                
                # if intro_targetimg_nogo_1 is starting this frame...
                if intro_targetimg_nogo_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_targetimg_nogo_1.frameNStart = frameN  # exact frame index
                    intro_targetimg_nogo_1.tStart = t  # local t and not account for scr refresh
                    intro_targetimg_nogo_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_targetimg_nogo_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_targetimg_nogo_1.started')
                    # update status
                    intro_targetimg_nogo_1.status = STARTED
                    intro_targetimg_nogo_1.setAutoDraw(True)
                
                # if intro_targetimg_nogo_1 is active this frame...
                if intro_targetimg_nogo_1.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_gonogo_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "intro_gonogo_1" ---
            for thisComponent in intro_gonogo_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('intro_gonogo_1.stopped', globalClock.getTime())
            # check responses
            if introLoop_key_nogo_1.keys in ['', [], None]:  # No response was made
                introLoop_key_nogo_1.keys = None
            go_gonogo_1.addData('introLoop_key_nogo_1.keys',introLoop_key_nogo_1.keys)
            if introLoop_key_nogo_1.keys != None:  # we had a response
                go_gonogo_1.addData('introLoop_key_nogo_1.rt', introLoop_key_nogo_1.rt)
                go_gonogo_1.addData('introLoop_key_nogo_1.duration', introLoop_key_nogo_1.duration)
            # the Routine "intro_gonogo_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_nogo_1 = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/target_block_1.csv"),
                seed=None, name='trials_nogo_1')
            thisExp.addLoop(trials_nogo_1)  # add the loop to the experiment
            thisTrials_nogo_1 = trials_nogo_1.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_nogo_1.rgb)
            if thisTrials_nogo_1 != None:
                for paramName in thisTrials_nogo_1:
                    globals()[paramName] = thisTrials_nogo_1[paramName]
            
            for thisTrials_nogo_1 in trials_nogo_1:
                currentLoop = trials_nogo_1
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_nogo_1.rgb)
                if thisTrials_nogo_1 != None:
                    for paramName in thisTrials_nogo_1:
                        globals()[paramName] = thisTrials_nogo_1[paramName]
                
                # --- Prepare to start Routine "Go_Nogo" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Go_Nogo.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_nogo
                key_name = "nan"
                # covet study said 1+-0.03s is fixation-cross time
                randDuration = np.random.normal(10, 0.3) / 10
                randDuration = randDuration + 1.00
                images_nogo.setImage(image)
                trial_key_nogo.keys = []
                trial_key_nogo.rt = []
                _trial_key_nogo_allKeys = []
                # Run 'Begin Routine' code from ET_nogo
                # tracker.send_message('_'.join(['onset', Name.jpg_Counter"]))
                
                file_name = os.path.basename(image)
                tracker.send_message('_'.join(['onset', f"{str(file_name)}"]))
                # keep track of which components have finished
                Go_NogoComponents = [fixation_cross_trial_nogo, images_nogo, trial_key_nogo]
                for thisComponent in Go_NogoComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Go_Nogo" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_trial_nogo* updates
                    
                    # if fixation_cross_trial_nogo is starting this frame...
                    if fixation_cross_trial_nogo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_trial_nogo.frameNStart = frameN  # exact frame index
                        fixation_cross_trial_nogo.tStart = t  # local t and not account for scr refresh
                        fixation_cross_trial_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_trial_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_trial_nogo.started')
                        # update status
                        fixation_cross_trial_nogo.status = STARTED
                        fixation_cross_trial_nogo.setAutoDraw(True)
                    
                    # if fixation_cross_trial_nogo is active this frame...
                    if fixation_cross_trial_nogo.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_trial_nogo is stopping this frame...
                    if fixation_cross_trial_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_trial_nogo.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_trial_nogo.tStop = t  # not accounting for scr refresh
                            fixation_cross_trial_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_trial_nogo.stopped')
                            # update status
                            fixation_cross_trial_nogo.status = FINISHED
                            fixation_cross_trial_nogo.setAutoDraw(False)
                    
                    # *images_nogo* updates
                    
                    # if images_nogo is starting this frame...
                    if images_nogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        images_nogo.frameNStart = frameN  # exact frame index
                        images_nogo.tStart = t  # local t and not account for scr refresh
                        images_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(images_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'images_nogo.started')
                        # update status
                        images_nogo.status = STARTED
                        images_nogo.setAutoDraw(True)
                    
                    # if images_nogo is active this frame...
                    if images_nogo.status == STARTED:
                        # update params
                        pass
                    
                    # if images_nogo is stopping this frame...
                    if images_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > images_nogo.tStartRefresh + 0.8-frameTolerance:
                            # keep track of stop time/frame for later
                            images_nogo.tStop = t  # not accounting for scr refresh
                            images_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'images_nogo.stopped')
                            # update status
                            images_nogo.status = FINISHED
                            images_nogo.setAutoDraw(False)
                    
                    # *trial_key_nogo* updates
                    waitOnFlip = False
                    
                    # if trial_key_nogo is starting this frame...
                    if trial_key_nogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        trial_key_nogo.frameNStart = frameN  # exact frame index
                        trial_key_nogo.tStart = t  # local t and not account for scr refresh
                        trial_key_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trial_key_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trial_key_nogo.started')
                        # update status
                        trial_key_nogo.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trial_key_nogo.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trial_key_nogo.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if trial_key_nogo is stopping this frame...
                    if trial_key_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > trial_key_nogo.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            trial_key_nogo.tStop = t  # not accounting for scr refresh
                            trial_key_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_key_nogo.stopped')
                            # update status
                            trial_key_nogo.status = FINISHED
                            trial_key_nogo.status = FINISHED
                    if trial_key_nogo.status == STARTED and not waitOnFlip:
                        theseKeys = trial_key_nogo.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _trial_key_nogo_allKeys.extend(theseKeys)
                        if len(_trial_key_nogo_allKeys):
                            trial_key_nogo.keys = _trial_key_nogo_allKeys[0].name  # just the first key pressed
                            trial_key_nogo.rt = _trial_key_nogo_allKeys[0].rt
                            trial_key_nogo.duration = _trial_key_nogo_allKeys[0].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Go_NogoComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Go_Nogo" ---
                for thisComponent in Go_NogoComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Go_Nogo.stopped', globalClock.getTime())
                # Run 'End Routine' code from code_nogo
                print(trial_key_nogo.time,istarget)
                
                if len(trial_key_nogo.keys)>0:
                    key_name = "space"
                
                if (key_name == "nan" and istarget == 1) or (key_name == "space" and istarget == 0):
                    correct = 1
                else:
                    correct = 0
                
                correct_counter += correct
                
                thisExp.addData("correct", correct)
                # check responses
                if trial_key_nogo.keys in ['', [], None]:  # No response was made
                    trial_key_nogo.keys = None
                trials_nogo_1.addData('trial_key_nogo.keys',trial_key_nogo.keys)
                if trial_key_nogo.keys != None:  # we had a response
                    trials_nogo_1.addData('trial_key_nogo.rt', trial_key_nogo.rt)
                    trials_nogo_1.addData('trial_key_nogo.duration', trial_key_nogo.duration)
                # Run 'End Routine' code from ET_nogo
                tracker.send_message('_'.join(['offset', f"{str(file_name)}"]))
                # the Routine "Go_Nogo" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'trials_nogo_1'
            
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'go_gonogo_1'
        
        
        # set up handler to look after randomisation of conditions etc
        go_gonogo_2 = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='go_gonogo_2')
        thisExp.addLoop(go_gonogo_2)  # add the loop to the experiment
        thisGo_gonogo_2 = go_gonogo_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisGo_gonogo_2.rgb)
        if thisGo_gonogo_2 != None:
            for paramName in thisGo_gonogo_2:
                globals()[paramName] = thisGo_gonogo_2[paramName]
        
        for thisGo_gonogo_2 in go_gonogo_2:
            currentLoop = go_gonogo_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisGo_gonogo_2.rgb)
            if thisGo_gonogo_2 != None:
                for paramName in thisGo_gonogo_2:
                    globals()[paramName] = thisGo_gonogo_2[paramName]
            
            # --- Prepare to start Routine "intro_go_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_go_2.started', globalClock.getTime())
            introLoop_key_go_2.keys = []
            introLoop_key_go_2.rt = []
            _introLoop_key_go_2_allKeys = []
            # keep track of which components have finished
            intro_go_2Components = [intro_text_go_2, introLoop_key_go_2]
            for thisComponent in intro_go_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "intro_go_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *intro_text_go_2* updates
                
                # if intro_text_go_2 is starting this frame...
                if intro_text_go_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_text_go_2.frameNStart = frameN  # exact frame index
                    intro_text_go_2.tStart = t  # local t and not account for scr refresh
                    intro_text_go_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_text_go_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_text_go_2.started')
                    # update status
                    intro_text_go_2.status = STARTED
                    intro_text_go_2.setAutoDraw(True)
                
                # if intro_text_go_2 is active this frame...
                if intro_text_go_2.status == STARTED:
                    # update params
                    pass
                
                # *introLoop_key_go_2* updates
                waitOnFlip = False
                
                # if introLoop_key_go_2 is starting this frame...
                if introLoop_key_go_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    introLoop_key_go_2.frameNStart = frameN  # exact frame index
                    introLoop_key_go_2.tStart = t  # local t and not account for scr refresh
                    introLoop_key_go_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(introLoop_key_go_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'introLoop_key_go_2.started')
                    # update status
                    introLoop_key_go_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(introLoop_key_go_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(introLoop_key_go_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if introLoop_key_go_2.status == STARTED and not waitOnFlip:
                    theseKeys = introLoop_key_go_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _introLoop_key_go_2_allKeys.extend(theseKeys)
                    if len(_introLoop_key_go_2_allKeys):
                        introLoop_key_go_2.keys = _introLoop_key_go_2_allKeys[0].name  # just the first key pressed
                        introLoop_key_go_2.rt = _introLoop_key_go_2_allKeys[0].rt
                        introLoop_key_go_2.duration = _introLoop_key_go_2_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_go_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "intro_go_2" ---
            for thisComponent in intro_go_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('intro_go_2.stopped', globalClock.getTime())
            # check responses
            if introLoop_key_go_2.keys in ['', [], None]:  # No response was made
                introLoop_key_go_2.keys = None
            go_gonogo_2.addData('introLoop_key_go_2.keys',introLoop_key_go_2.keys)
            if introLoop_key_go_2.keys != None:  # we had a response
                go_gonogo_2.addData('introLoop_key_go_2.rt', introLoop_key_go_2.rt)
                go_gonogo_2.addData('introLoop_key_go_2.duration', introLoop_key_go_2.duration)
            # the Routine "intro_go_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_go_2 = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/dummy_block_2.csv"),
                seed=None, name='trials_go_2')
            thisExp.addLoop(trials_go_2)  # add the loop to the experiment
            thisTrials_go_2 = trials_go_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_go_2.rgb)
            if thisTrials_go_2 != None:
                for paramName in thisTrials_go_2:
                    globals()[paramName] = thisTrials_go_2[paramName]
            
            for thisTrials_go_2 in trials_go_2:
                currentLoop = trials_go_2
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_go_2.rgb)
                if thisTrials_go_2 != None:
                    for paramName in thisTrials_go_2:
                        globals()[paramName] = thisTrials_go_2[paramName]
                
                # --- Prepare to start Routine "Go" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Go.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_go
                key_name = "nan"
                # covet study said 1+-0.03s is fixation-cross time
                randDuration = np.random.normal(10, 0.3) / 10
                randDuration = randDuration + 1.00
                images_go.setImage(image)
                trial_key_go.keys = []
                trial_key_go.rt = []
                _trial_key_go_allKeys = []
                # Run 'Begin Routine' code from ET_go
                # tracker.send_message('_'.join(['onset', Name.jpg_Counter"]))
                
                file_name = os.path.basename(image)
                tracker.send_message('_'.join(['onset', f"{str(file_name)}"]))
                # keep track of which components have finished
                GoComponents = [fixation_cross_trial_go, images_go, trial_key_go]
                for thisComponent in GoComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Go" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_trial_go* updates
                    
                    # if fixation_cross_trial_go is starting this frame...
                    if fixation_cross_trial_go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_trial_go.frameNStart = frameN  # exact frame index
                        fixation_cross_trial_go.tStart = t  # local t and not account for scr refresh
                        fixation_cross_trial_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_trial_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_trial_go.started')
                        # update status
                        fixation_cross_trial_go.status = STARTED
                        fixation_cross_trial_go.setAutoDraw(True)
                    
                    # if fixation_cross_trial_go is active this frame...
                    if fixation_cross_trial_go.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_trial_go is stopping this frame...
                    if fixation_cross_trial_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_trial_go.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_trial_go.tStop = t  # not accounting for scr refresh
                            fixation_cross_trial_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_trial_go.stopped')
                            # update status
                            fixation_cross_trial_go.status = FINISHED
                            fixation_cross_trial_go.setAutoDraw(False)
                    
                    # *images_go* updates
                    
                    # if images_go is starting this frame...
                    if images_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        images_go.frameNStart = frameN  # exact frame index
                        images_go.tStart = t  # local t and not account for scr refresh
                        images_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(images_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'images_go.started')
                        # update status
                        images_go.status = STARTED
                        images_go.setAutoDraw(True)
                    
                    # if images_go is active this frame...
                    if images_go.status == STARTED:
                        # update params
                        pass
                    
                    # if images_go is stopping this frame...
                    if images_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > images_go.tStartRefresh + 0.8-frameTolerance:
                            # keep track of stop time/frame for later
                            images_go.tStop = t  # not accounting for scr refresh
                            images_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'images_go.stopped')
                            # update status
                            images_go.status = FINISHED
                            images_go.setAutoDraw(False)
                    
                    # *trial_key_go* updates
                    waitOnFlip = False
                    
                    # if trial_key_go is starting this frame...
                    if trial_key_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        trial_key_go.frameNStart = frameN  # exact frame index
                        trial_key_go.tStart = t  # local t and not account for scr refresh
                        trial_key_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trial_key_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trial_key_go.started')
                        # update status
                        trial_key_go.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trial_key_go.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trial_key_go.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if trial_key_go is stopping this frame...
                    if trial_key_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > trial_key_go.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            trial_key_go.tStop = t  # not accounting for scr refresh
                            trial_key_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_key_go.stopped')
                            # update status
                            trial_key_go.status = FINISHED
                            trial_key_go.status = FINISHED
                    if trial_key_go.status == STARTED and not waitOnFlip:
                        theseKeys = trial_key_go.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _trial_key_go_allKeys.extend(theseKeys)
                        if len(_trial_key_go_allKeys):
                            trial_key_go.keys = _trial_key_go_allKeys[0].name  # just the first key pressed
                            trial_key_go.rt = _trial_key_go_allKeys[0].rt
                            trial_key_go.duration = _trial_key_go_allKeys[0].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in GoComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Go" ---
                for thisComponent in GoComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Go.stopped', globalClock.getTime())
                # Run 'End Routine' code from code_go
                print(trial_key_go.time,istarget)
                
                if len(trial_key_go.keys)>0:
                    key_name = "space"
                
                if key_name =="space":
                    correct = 1
                else:
                    correct = 0
                
                correct_counter += correct
                
                thisExp.addData("correct", correct)
                # check responses
                if trial_key_go.keys in ['', [], None]:  # No response was made
                    trial_key_go.keys = None
                trials_go_2.addData('trial_key_go.keys',trial_key_go.keys)
                if trial_key_go.keys != None:  # we had a response
                    trials_go_2.addData('trial_key_go.rt', trial_key_go.rt)
                    trials_go_2.addData('trial_key_go.duration', trial_key_go.duration)
                # Run 'End Routine' code from ET_go
                tracker.send_message('_'.join(['offset', f"{str(file_name)}"]))
                # the Routine "Go" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'trials_go_2'
            
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # --- Prepare to start Routine "intro_gonogo_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_gonogo_2.started', globalClock.getTime())
            introLoop_key_nogo_2.keys = []
            introLoop_key_nogo_2.rt = []
            _introLoop_key_nogo_2_allKeys = []
            intro_tagetimg_nogo_2.setImage(targetimg2)
            # keep track of which components have finished
            intro_gonogo_2Components = [intro_text_nogo_2, introLoop_key_nogo_2, intro_tagetimg_nogo_2]
            for thisComponent in intro_gonogo_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "intro_gonogo_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *intro_text_nogo_2* updates
                
                # if intro_text_nogo_2 is starting this frame...
                if intro_text_nogo_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_text_nogo_2.frameNStart = frameN  # exact frame index
                    intro_text_nogo_2.tStart = t  # local t and not account for scr refresh
                    intro_text_nogo_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_text_nogo_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_text_nogo_2.started')
                    # update status
                    intro_text_nogo_2.status = STARTED
                    intro_text_nogo_2.setAutoDraw(True)
                
                # if intro_text_nogo_2 is active this frame...
                if intro_text_nogo_2.status == STARTED:
                    # update params
                    pass
                
                # *introLoop_key_nogo_2* updates
                waitOnFlip = False
                
                # if introLoop_key_nogo_2 is starting this frame...
                if introLoop_key_nogo_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    introLoop_key_nogo_2.frameNStart = frameN  # exact frame index
                    introLoop_key_nogo_2.tStart = t  # local t and not account for scr refresh
                    introLoop_key_nogo_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(introLoop_key_nogo_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'introLoop_key_nogo_2.started')
                    # update status
                    introLoop_key_nogo_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(introLoop_key_nogo_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(introLoop_key_nogo_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if introLoop_key_nogo_2.status == STARTED and not waitOnFlip:
                    theseKeys = introLoop_key_nogo_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _introLoop_key_nogo_2_allKeys.extend(theseKeys)
                    if len(_introLoop_key_nogo_2_allKeys):
                        introLoop_key_nogo_2.keys = _introLoop_key_nogo_2_allKeys[0].name  # just the first key pressed
                        introLoop_key_nogo_2.rt = _introLoop_key_nogo_2_allKeys[0].rt
                        introLoop_key_nogo_2.duration = _introLoop_key_nogo_2_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *intro_tagetimg_nogo_2* updates
                
                # if intro_tagetimg_nogo_2 is starting this frame...
                if intro_tagetimg_nogo_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_tagetimg_nogo_2.frameNStart = frameN  # exact frame index
                    intro_tagetimg_nogo_2.tStart = t  # local t and not account for scr refresh
                    intro_tagetimg_nogo_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_tagetimg_nogo_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_tagetimg_nogo_2.started')
                    # update status
                    intro_tagetimg_nogo_2.status = STARTED
                    intro_tagetimg_nogo_2.setAutoDraw(True)
                
                # if intro_tagetimg_nogo_2 is active this frame...
                if intro_tagetimg_nogo_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_gonogo_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "intro_gonogo_2" ---
            for thisComponent in intro_gonogo_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('intro_gonogo_2.stopped', globalClock.getTime())
            # check responses
            if introLoop_key_nogo_2.keys in ['', [], None]:  # No response was made
                introLoop_key_nogo_2.keys = None
            go_gonogo_2.addData('introLoop_key_nogo_2.keys',introLoop_key_nogo_2.keys)
            if introLoop_key_nogo_2.keys != None:  # we had a response
                go_gonogo_2.addData('introLoop_key_nogo_2.rt', introLoop_key_nogo_2.rt)
                go_gonogo_2.addData('introLoop_key_nogo_2.duration', introLoop_key_nogo_2.duration)
            # the Routine "intro_gonogo_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_nogo_2 = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/target_block_2.csv"),
                seed=None, name='trials_nogo_2')
            thisExp.addLoop(trials_nogo_2)  # add the loop to the experiment
            thisTrials_nogo_2 = trials_nogo_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_nogo_2.rgb)
            if thisTrials_nogo_2 != None:
                for paramName in thisTrials_nogo_2:
                    globals()[paramName] = thisTrials_nogo_2[paramName]
            
            for thisTrials_nogo_2 in trials_nogo_2:
                currentLoop = trials_nogo_2
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_nogo_2.rgb)
                if thisTrials_nogo_2 != None:
                    for paramName in thisTrials_nogo_2:
                        globals()[paramName] = thisTrials_nogo_2[paramName]
                
                # --- Prepare to start Routine "Go_Nogo" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Go_Nogo.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_nogo
                key_name = "nan"
                # covet study said 1+-0.03s is fixation-cross time
                randDuration = np.random.normal(10, 0.3) / 10
                randDuration = randDuration + 1.00
                images_nogo.setImage(image)
                trial_key_nogo.keys = []
                trial_key_nogo.rt = []
                _trial_key_nogo_allKeys = []
                # Run 'Begin Routine' code from ET_nogo
                # tracker.send_message('_'.join(['onset', Name.jpg_Counter"]))
                
                file_name = os.path.basename(image)
                tracker.send_message('_'.join(['onset', f"{str(file_name)}"]))
                # keep track of which components have finished
                Go_NogoComponents = [fixation_cross_trial_nogo, images_nogo, trial_key_nogo]
                for thisComponent in Go_NogoComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Go_Nogo" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_trial_nogo* updates
                    
                    # if fixation_cross_trial_nogo is starting this frame...
                    if fixation_cross_trial_nogo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_trial_nogo.frameNStart = frameN  # exact frame index
                        fixation_cross_trial_nogo.tStart = t  # local t and not account for scr refresh
                        fixation_cross_trial_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_trial_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_trial_nogo.started')
                        # update status
                        fixation_cross_trial_nogo.status = STARTED
                        fixation_cross_trial_nogo.setAutoDraw(True)
                    
                    # if fixation_cross_trial_nogo is active this frame...
                    if fixation_cross_trial_nogo.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_trial_nogo is stopping this frame...
                    if fixation_cross_trial_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_trial_nogo.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_trial_nogo.tStop = t  # not accounting for scr refresh
                            fixation_cross_trial_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_trial_nogo.stopped')
                            # update status
                            fixation_cross_trial_nogo.status = FINISHED
                            fixation_cross_trial_nogo.setAutoDraw(False)
                    
                    # *images_nogo* updates
                    
                    # if images_nogo is starting this frame...
                    if images_nogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        images_nogo.frameNStart = frameN  # exact frame index
                        images_nogo.tStart = t  # local t and not account for scr refresh
                        images_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(images_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'images_nogo.started')
                        # update status
                        images_nogo.status = STARTED
                        images_nogo.setAutoDraw(True)
                    
                    # if images_nogo is active this frame...
                    if images_nogo.status == STARTED:
                        # update params
                        pass
                    
                    # if images_nogo is stopping this frame...
                    if images_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > images_nogo.tStartRefresh + 0.8-frameTolerance:
                            # keep track of stop time/frame for later
                            images_nogo.tStop = t  # not accounting for scr refresh
                            images_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'images_nogo.stopped')
                            # update status
                            images_nogo.status = FINISHED
                            images_nogo.setAutoDraw(False)
                    
                    # *trial_key_nogo* updates
                    waitOnFlip = False
                    
                    # if trial_key_nogo is starting this frame...
                    if trial_key_nogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        trial_key_nogo.frameNStart = frameN  # exact frame index
                        trial_key_nogo.tStart = t  # local t and not account for scr refresh
                        trial_key_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trial_key_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trial_key_nogo.started')
                        # update status
                        trial_key_nogo.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trial_key_nogo.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trial_key_nogo.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if trial_key_nogo is stopping this frame...
                    if trial_key_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > trial_key_nogo.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            trial_key_nogo.tStop = t  # not accounting for scr refresh
                            trial_key_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_key_nogo.stopped')
                            # update status
                            trial_key_nogo.status = FINISHED
                            trial_key_nogo.status = FINISHED
                    if trial_key_nogo.status == STARTED and not waitOnFlip:
                        theseKeys = trial_key_nogo.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _trial_key_nogo_allKeys.extend(theseKeys)
                        if len(_trial_key_nogo_allKeys):
                            trial_key_nogo.keys = _trial_key_nogo_allKeys[0].name  # just the first key pressed
                            trial_key_nogo.rt = _trial_key_nogo_allKeys[0].rt
                            trial_key_nogo.duration = _trial_key_nogo_allKeys[0].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Go_NogoComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Go_Nogo" ---
                for thisComponent in Go_NogoComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Go_Nogo.stopped', globalClock.getTime())
                # Run 'End Routine' code from code_nogo
                print(trial_key_nogo.time,istarget)
                
                if len(trial_key_nogo.keys)>0:
                    key_name = "space"
                
                if (key_name == "nan" and istarget == 1) or (key_name == "space" and istarget == 0):
                    correct = 1
                else:
                    correct = 0
                
                correct_counter += correct
                
                thisExp.addData("correct", correct)
                # check responses
                if trial_key_nogo.keys in ['', [], None]:  # No response was made
                    trial_key_nogo.keys = None
                trials_nogo_2.addData('trial_key_nogo.keys',trial_key_nogo.keys)
                if trial_key_nogo.keys != None:  # we had a response
                    trials_nogo_2.addData('trial_key_nogo.rt', trial_key_nogo.rt)
                    trials_nogo_2.addData('trial_key_nogo.duration', trial_key_nogo.duration)
                # Run 'End Routine' code from ET_nogo
                tracker.send_message('_'.join(['offset', f"{str(file_name)}"]))
                # the Routine "Go_Nogo" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'trials_nogo_2'
            
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'go_gonogo_2'
        
        
        # set up handler to look after randomisation of conditions etc
        go_gonogo_3 = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='go_gonogo_3')
        thisExp.addLoop(go_gonogo_3)  # add the loop to the experiment
        thisGo_gonogo_3 = go_gonogo_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisGo_gonogo_3.rgb)
        if thisGo_gonogo_3 != None:
            for paramName in thisGo_gonogo_3:
                globals()[paramName] = thisGo_gonogo_3[paramName]
        
        for thisGo_gonogo_3 in go_gonogo_3:
            currentLoop = go_gonogo_3
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisGo_gonogo_3.rgb)
            if thisGo_gonogo_3 != None:
                for paramName in thisGo_gonogo_3:
                    globals()[paramName] = thisGo_gonogo_3[paramName]
            
            # --- Prepare to start Routine "intro_go_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_go_3.started', globalClock.getTime())
            introLoop_key_go_3.keys = []
            introLoop_key_go_3.rt = []
            _introLoop_key_go_3_allKeys = []
            # keep track of which components have finished
            intro_go_3Components = [intro_text_go_3, introLoop_key_go_3]
            for thisComponent in intro_go_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "intro_go_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *intro_text_go_3* updates
                
                # if intro_text_go_3 is starting this frame...
                if intro_text_go_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_text_go_3.frameNStart = frameN  # exact frame index
                    intro_text_go_3.tStart = t  # local t and not account for scr refresh
                    intro_text_go_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_text_go_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_text_go_3.started')
                    # update status
                    intro_text_go_3.status = STARTED
                    intro_text_go_3.setAutoDraw(True)
                
                # if intro_text_go_3 is active this frame...
                if intro_text_go_3.status == STARTED:
                    # update params
                    pass
                
                # *introLoop_key_go_3* updates
                waitOnFlip = False
                
                # if introLoop_key_go_3 is starting this frame...
                if introLoop_key_go_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    introLoop_key_go_3.frameNStart = frameN  # exact frame index
                    introLoop_key_go_3.tStart = t  # local t and not account for scr refresh
                    introLoop_key_go_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(introLoop_key_go_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'introLoop_key_go_3.started')
                    # update status
                    introLoop_key_go_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(introLoop_key_go_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(introLoop_key_go_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if introLoop_key_go_3.status == STARTED and not waitOnFlip:
                    theseKeys = introLoop_key_go_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _introLoop_key_go_3_allKeys.extend(theseKeys)
                    if len(_introLoop_key_go_3_allKeys):
                        introLoop_key_go_3.keys = _introLoop_key_go_3_allKeys[0].name  # just the first key pressed
                        introLoop_key_go_3.rt = _introLoop_key_go_3_allKeys[0].rt
                        introLoop_key_go_3.duration = _introLoop_key_go_3_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_go_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "intro_go_3" ---
            for thisComponent in intro_go_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('intro_go_3.stopped', globalClock.getTime())
            # check responses
            if introLoop_key_go_3.keys in ['', [], None]:  # No response was made
                introLoop_key_go_3.keys = None
            go_gonogo_3.addData('introLoop_key_go_3.keys',introLoop_key_go_3.keys)
            if introLoop_key_go_3.keys != None:  # we had a response
                go_gonogo_3.addData('introLoop_key_go_3.rt', introLoop_key_go_3.rt)
                go_gonogo_3.addData('introLoop_key_go_3.duration', introLoop_key_go_3.duration)
            # the Routine "intro_go_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_go_3 = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/dummy_block_3.csv"),
                seed=None, name='trials_go_3')
            thisExp.addLoop(trials_go_3)  # add the loop to the experiment
            thisTrials_go_3 = trials_go_3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_go_3.rgb)
            if thisTrials_go_3 != None:
                for paramName in thisTrials_go_3:
                    globals()[paramName] = thisTrials_go_3[paramName]
            
            for thisTrials_go_3 in trials_go_3:
                currentLoop = trials_go_3
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_go_3.rgb)
                if thisTrials_go_3 != None:
                    for paramName in thisTrials_go_3:
                        globals()[paramName] = thisTrials_go_3[paramName]
                
                # --- Prepare to start Routine "Go" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Go.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_go
                key_name = "nan"
                # covet study said 1+-0.03s is fixation-cross time
                randDuration = np.random.normal(10, 0.3) / 10
                randDuration = randDuration + 1.00
                images_go.setImage(image)
                trial_key_go.keys = []
                trial_key_go.rt = []
                _trial_key_go_allKeys = []
                # Run 'Begin Routine' code from ET_go
                # tracker.send_message('_'.join(['onset', Name.jpg_Counter"]))
                
                file_name = os.path.basename(image)
                tracker.send_message('_'.join(['onset', f"{str(file_name)}"]))
                # keep track of which components have finished
                GoComponents = [fixation_cross_trial_go, images_go, trial_key_go]
                for thisComponent in GoComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Go" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_trial_go* updates
                    
                    # if fixation_cross_trial_go is starting this frame...
                    if fixation_cross_trial_go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_trial_go.frameNStart = frameN  # exact frame index
                        fixation_cross_trial_go.tStart = t  # local t and not account for scr refresh
                        fixation_cross_trial_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_trial_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_trial_go.started')
                        # update status
                        fixation_cross_trial_go.status = STARTED
                        fixation_cross_trial_go.setAutoDraw(True)
                    
                    # if fixation_cross_trial_go is active this frame...
                    if fixation_cross_trial_go.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_trial_go is stopping this frame...
                    if fixation_cross_trial_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_trial_go.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_trial_go.tStop = t  # not accounting for scr refresh
                            fixation_cross_trial_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_trial_go.stopped')
                            # update status
                            fixation_cross_trial_go.status = FINISHED
                            fixation_cross_trial_go.setAutoDraw(False)
                    
                    # *images_go* updates
                    
                    # if images_go is starting this frame...
                    if images_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        images_go.frameNStart = frameN  # exact frame index
                        images_go.tStart = t  # local t and not account for scr refresh
                        images_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(images_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'images_go.started')
                        # update status
                        images_go.status = STARTED
                        images_go.setAutoDraw(True)
                    
                    # if images_go is active this frame...
                    if images_go.status == STARTED:
                        # update params
                        pass
                    
                    # if images_go is stopping this frame...
                    if images_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > images_go.tStartRefresh + 0.8-frameTolerance:
                            # keep track of stop time/frame for later
                            images_go.tStop = t  # not accounting for scr refresh
                            images_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'images_go.stopped')
                            # update status
                            images_go.status = FINISHED
                            images_go.setAutoDraw(False)
                    
                    # *trial_key_go* updates
                    waitOnFlip = False
                    
                    # if trial_key_go is starting this frame...
                    if trial_key_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        trial_key_go.frameNStart = frameN  # exact frame index
                        trial_key_go.tStart = t  # local t and not account for scr refresh
                        trial_key_go.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trial_key_go, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trial_key_go.started')
                        # update status
                        trial_key_go.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trial_key_go.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trial_key_go.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if trial_key_go is stopping this frame...
                    if trial_key_go.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > trial_key_go.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            trial_key_go.tStop = t  # not accounting for scr refresh
                            trial_key_go.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_key_go.stopped')
                            # update status
                            trial_key_go.status = FINISHED
                            trial_key_go.status = FINISHED
                    if trial_key_go.status == STARTED and not waitOnFlip:
                        theseKeys = trial_key_go.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _trial_key_go_allKeys.extend(theseKeys)
                        if len(_trial_key_go_allKeys):
                            trial_key_go.keys = _trial_key_go_allKeys[0].name  # just the first key pressed
                            trial_key_go.rt = _trial_key_go_allKeys[0].rt
                            trial_key_go.duration = _trial_key_go_allKeys[0].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in GoComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Go" ---
                for thisComponent in GoComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Go.stopped', globalClock.getTime())
                # Run 'End Routine' code from code_go
                print(trial_key_go.time,istarget)
                
                if len(trial_key_go.keys)>0:
                    key_name = "space"
                
                if key_name =="space":
                    correct = 1
                else:
                    correct = 0
                
                correct_counter += correct
                
                thisExp.addData("correct", correct)
                # check responses
                if trial_key_go.keys in ['', [], None]:  # No response was made
                    trial_key_go.keys = None
                trials_go_3.addData('trial_key_go.keys',trial_key_go.keys)
                if trial_key_go.keys != None:  # we had a response
                    trials_go_3.addData('trial_key_go.rt', trial_key_go.rt)
                    trials_go_3.addData('trial_key_go.duration', trial_key_go.duration)
                # Run 'End Routine' code from ET_go
                tracker.send_message('_'.join(['offset', f"{str(file_name)}"]))
                # the Routine "Go" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'trials_go_3'
            
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # --- Prepare to start Routine "intro_gonogo_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_gonogo_3.started', globalClock.getTime())
            introLoop_key_nogo_3.keys = []
            introLoop_key_nogo_3.rt = []
            _introLoop_key_nogo_3_allKeys = []
            intro_tagetimg_nogo_3.setImage(targetimg3)
            # keep track of which components have finished
            intro_gonogo_3Components = [intro_text_nogo_3, introLoop_key_nogo_3, intro_tagetimg_nogo_3]
            for thisComponent in intro_gonogo_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "intro_gonogo_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *intro_text_nogo_3* updates
                
                # if intro_text_nogo_3 is starting this frame...
                if intro_text_nogo_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_text_nogo_3.frameNStart = frameN  # exact frame index
                    intro_text_nogo_3.tStart = t  # local t and not account for scr refresh
                    intro_text_nogo_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_text_nogo_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_text_nogo_3.started')
                    # update status
                    intro_text_nogo_3.status = STARTED
                    intro_text_nogo_3.setAutoDraw(True)
                
                # if intro_text_nogo_3 is active this frame...
                if intro_text_nogo_3.status == STARTED:
                    # update params
                    pass
                
                # *introLoop_key_nogo_3* updates
                waitOnFlip = False
                
                # if introLoop_key_nogo_3 is starting this frame...
                if introLoop_key_nogo_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    introLoop_key_nogo_3.frameNStart = frameN  # exact frame index
                    introLoop_key_nogo_3.tStart = t  # local t and not account for scr refresh
                    introLoop_key_nogo_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(introLoop_key_nogo_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'introLoop_key_nogo_3.started')
                    # update status
                    introLoop_key_nogo_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(introLoop_key_nogo_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(introLoop_key_nogo_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if introLoop_key_nogo_3.status == STARTED and not waitOnFlip:
                    theseKeys = introLoop_key_nogo_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _introLoop_key_nogo_3_allKeys.extend(theseKeys)
                    if len(_introLoop_key_nogo_3_allKeys):
                        introLoop_key_nogo_3.keys = _introLoop_key_nogo_3_allKeys[0].name  # just the first key pressed
                        introLoop_key_nogo_3.rt = _introLoop_key_nogo_3_allKeys[0].rt
                        introLoop_key_nogo_3.duration = _introLoop_key_nogo_3_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *intro_tagetimg_nogo_3* updates
                
                # if intro_tagetimg_nogo_3 is starting this frame...
                if intro_tagetimg_nogo_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    intro_tagetimg_nogo_3.frameNStart = frameN  # exact frame index
                    intro_tagetimg_nogo_3.tStart = t  # local t and not account for scr refresh
                    intro_tagetimg_nogo_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(intro_tagetimg_nogo_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'intro_tagetimg_nogo_3.started')
                    # update status
                    intro_tagetimg_nogo_3.status = STARTED
                    intro_tagetimg_nogo_3.setAutoDraw(True)
                
                # if intro_tagetimg_nogo_3 is active this frame...
                if intro_tagetimg_nogo_3.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in intro_gonogo_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "intro_gonogo_3" ---
            for thisComponent in intro_gonogo_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('intro_gonogo_3.stopped', globalClock.getTime())
            # check responses
            if introLoop_key_nogo_3.keys in ['', [], None]:  # No response was made
                introLoop_key_nogo_3.keys = None
            go_gonogo_3.addData('introLoop_key_nogo_3.keys',introLoop_key_nogo_3.keys)
            if introLoop_key_nogo_3.keys != None:  # we had a response
                go_gonogo_3.addData('introLoop_key_nogo_3.rt', introLoop_key_nogo_3.rt)
                go_gonogo_3.addData('introLoop_key_nogo_3.duration', introLoop_key_nogo_3.duration)
            # the Routine "intro_gonogo_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_nogo_3 = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions("settings/result/participant_"+expInfo["participant"]+"/target_block_3.csv"),
                seed=None, name='trials_nogo_3')
            thisExp.addLoop(trials_nogo_3)  # add the loop to the experiment
            thisTrials_nogo_3 = trials_nogo_3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_nogo_3.rgb)
            if thisTrials_nogo_3 != None:
                for paramName in thisTrials_nogo_3:
                    globals()[paramName] = thisTrials_nogo_3[paramName]
            
            for thisTrials_nogo_3 in trials_nogo_3:
                currentLoop = trials_nogo_3
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_nogo_3.rgb)
                if thisTrials_nogo_3 != None:
                    for paramName in thisTrials_nogo_3:
                        globals()[paramName] = thisTrials_nogo_3[paramName]
                
                # --- Prepare to start Routine "Go_Nogo" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Go_Nogo.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_nogo
                key_name = "nan"
                # covet study said 1+-0.03s is fixation-cross time
                randDuration = np.random.normal(10, 0.3) / 10
                randDuration = randDuration + 1.00
                images_nogo.setImage(image)
                trial_key_nogo.keys = []
                trial_key_nogo.rt = []
                _trial_key_nogo_allKeys = []
                # Run 'Begin Routine' code from ET_nogo
                # tracker.send_message('_'.join(['onset', Name.jpg_Counter"]))
                
                file_name = os.path.basename(image)
                tracker.send_message('_'.join(['onset', f"{str(file_name)}"]))
                # keep track of which components have finished
                Go_NogoComponents = [fixation_cross_trial_nogo, images_nogo, trial_key_nogo]
                for thisComponent in Go_NogoComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Go_Nogo" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_trial_nogo* updates
                    
                    # if fixation_cross_trial_nogo is starting this frame...
                    if fixation_cross_trial_nogo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_trial_nogo.frameNStart = frameN  # exact frame index
                        fixation_cross_trial_nogo.tStart = t  # local t and not account for scr refresh
                        fixation_cross_trial_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_trial_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_trial_nogo.started')
                        # update status
                        fixation_cross_trial_nogo.status = STARTED
                        fixation_cross_trial_nogo.setAutoDraw(True)
                    
                    # if fixation_cross_trial_nogo is active this frame...
                    if fixation_cross_trial_nogo.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_trial_nogo is stopping this frame...
                    if fixation_cross_trial_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_trial_nogo.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_trial_nogo.tStop = t  # not accounting for scr refresh
                            fixation_cross_trial_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_trial_nogo.stopped')
                            # update status
                            fixation_cross_trial_nogo.status = FINISHED
                            fixation_cross_trial_nogo.setAutoDraw(False)
                    
                    # *images_nogo* updates
                    
                    # if images_nogo is starting this frame...
                    if images_nogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        images_nogo.frameNStart = frameN  # exact frame index
                        images_nogo.tStart = t  # local t and not account for scr refresh
                        images_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(images_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'images_nogo.started')
                        # update status
                        images_nogo.status = STARTED
                        images_nogo.setAutoDraw(True)
                    
                    # if images_nogo is active this frame...
                    if images_nogo.status == STARTED:
                        # update params
                        pass
                    
                    # if images_nogo is stopping this frame...
                    if images_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > images_nogo.tStartRefresh + 0.8-frameTolerance:
                            # keep track of stop time/frame for later
                            images_nogo.tStop = t  # not accounting for scr refresh
                            images_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'images_nogo.stopped')
                            # update status
                            images_nogo.status = FINISHED
                            images_nogo.setAutoDraw(False)
                    
                    # *trial_key_nogo* updates
                    waitOnFlip = False
                    
                    # if trial_key_nogo is starting this frame...
                    if trial_key_nogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        trial_key_nogo.frameNStart = frameN  # exact frame index
                        trial_key_nogo.tStart = t  # local t and not account for scr refresh
                        trial_key_nogo.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trial_key_nogo, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trial_key_nogo.started')
                        # update status
                        trial_key_nogo.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trial_key_nogo.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trial_key_nogo.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if trial_key_nogo is stopping this frame...
                    if trial_key_nogo.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > trial_key_nogo.tStartRefresh + randDuration-frameTolerance:
                            # keep track of stop time/frame for later
                            trial_key_nogo.tStop = t  # not accounting for scr refresh
                            trial_key_nogo.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_key_nogo.stopped')
                            # update status
                            trial_key_nogo.status = FINISHED
                            trial_key_nogo.status = FINISHED
                    if trial_key_nogo.status == STARTED and not waitOnFlip:
                        theseKeys = trial_key_nogo.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _trial_key_nogo_allKeys.extend(theseKeys)
                        if len(_trial_key_nogo_allKeys):
                            trial_key_nogo.keys = _trial_key_nogo_allKeys[0].name  # just the first key pressed
                            trial_key_nogo.rt = _trial_key_nogo_allKeys[0].rt
                            trial_key_nogo.duration = _trial_key_nogo_allKeys[0].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Go_NogoComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Go_Nogo" ---
                for thisComponent in Go_NogoComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Go_Nogo.stopped', globalClock.getTime())
                # Run 'End Routine' code from code_nogo
                print(trial_key_nogo.time,istarget)
                
                if len(trial_key_nogo.keys)>0:
                    key_name = "space"
                
                if (key_name == "nan" and istarget == 1) or (key_name == "space" and istarget == 0):
                    correct = 1
                else:
                    correct = 0
                
                correct_counter += correct
                
                thisExp.addData("correct", correct)
                # check responses
                if trial_key_nogo.keys in ['', [], None]:  # No response was made
                    trial_key_nogo.keys = None
                trials_nogo_3.addData('trial_key_nogo.keys',trial_key_nogo.keys)
                if trial_key_nogo.keys != None:  # we had a response
                    trials_nogo_3.addData('trial_key_nogo.rt', trial_key_nogo.rt)
                    trials_nogo_3.addData('trial_key_nogo.duration', trial_key_nogo.duration)
                # Run 'End Routine' code from ET_nogo
                tracker.send_message('_'.join(['offset', f"{str(file_name)}"]))
                # the Routine "Go_Nogo" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'trials_nogo_3'
            
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('rest.started', globalClock.getTime())
            # keep track of which components have finished
            restComponents = [fixation_cross]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross* updates
                
                # if fixation_cross is starting this frame...
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.started')
                    # update status
                    fixation_cross.status = STARTED
                    fixation_cross.setAutoDraw(True)
                
                # if fixation_cross is active this frame...
                if fixation_cross.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross is stopping this frame...
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                        # update status
                        fixation_cross.status = FINISHED
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'go_gonogo_3'
        
    # completed 1.0 repeats of 'exp_trails'
    
    
    # --- Prepare to start Routine "finished" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('finished.started', globalClock.getTime())
    # keep track of which components have finished
    finishedComponents = [text]
    for thisComponent in finishedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "finished" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finishedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "finished" ---
    for thisComponent in finishedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('finished.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    # Run 'End Experiment' code from Calibration
    tracker.stop_recording(gaze=True)
    if not expInfo['dummymode']:
        tracker.save_data()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)

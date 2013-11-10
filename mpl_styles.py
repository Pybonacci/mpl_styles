# -*- coding: utf-8 -*-
"""
mpl_styles
Version 0.1

Library to easily provide styles to your matplotlib plots

@author: kikocorreoso

"""

import matplotlib as mpl

# Adapted from https://github.com/daler/matplotlibrc
def gg_style(func):
    def apply_style():
        params = {'lines.linewidth': 1.0, 'lines.color': 'purple',
                  'lines.antialiased': True, 'patch.linewidth': 0.5,
                  'patch.facecolor': 'FF0000', 'patch.edgecolor': 'eeeeee',
                  'patch.antialiased': True, 'font.family': 'Arial',
                  'font.size': 10.0, 
                  'font.monospace': ['DejaVu Sans Mono', 'Andale Mono', 
                                     'Nimbus Mono L', 'Courier New', 
                                     'Courier', 'Fixed', 'Terminal', 
                                     'monospace'],
                  'axes.facecolor': 'eeeeee', 'axes.edgecolor': 'bcbcbc',
                  'axes.linewidth': 1.0, 'axes.grid': True,
                  'axes.titlesize': 'x-large', 'axes.labelsize': 'large',
                  'axes.labelcolor': '555555', 'axes.axisbelow': True,
                  'axes.color_cycle': ['348ABD', '7A68A6', 'A60628', 
                                       '467821', 'CF4457', '188487', 
                                       'E24A33'],
                  'xtick.major.size': 0.0, 'xtick.minor.size': 0.0,
                  'xtick.major.pad': 6.0, 'xtick.minor.pad': 6.0,
                  'xtick.color': '555555', 'xtick.direction': 'in',
                  'ytick.major.size': 0.0, 'ytick.minor.size': 0.0,
                  'ytick.major.pad': 6.0, 'ytick.minor.pad': 6.0,
                  'ytick.color': '555555', 'ytick.direction': 'in', 
                  'legend.fancybox': True, 'legend.numpoints': 1.0, 
                  'figure.figsize': (11, 8), 'figure.facecolor': '1.0', 
                  'figure.edgecolor': '0.5', 'figure.subplot.hspace': 0.5}
        orig_params = {}
        for key in params.keys():
            orig_params[key] = mpl.rcParams[key]
            mpl.rcParams[key] = params[key]
                
        func()

        for key in orig_params.keys():
            mpl.rcParams[key] = orig_params[key]
            
    return apply_style

# Adapted from https://gist.github.com/huyng/816622
def gg2_style(func):
    def apply_style():
        params = {'lines.linewidth': 1.0, 'lines.antialiased': True, 
                  'patch.linewidth': 0.5, 'patch.facecolor': '348ABD', 
                  'patch.edgecolor': 'eeeeee', 'patch.antialiased': True, 
                  'font.family': 'monospace', 'font.size': 10.0, 
                  'font.monospace': ['DAndale Mono', 'Nimbus Mono L', 
                                     'Courier New,' 'Courier', 'Fixed', 
                                     'Terminal', 'monospace'],
                  'axes.facecolor': 'eeeeee', 'axes.edgecolor': 'bcbcbc',
                  'axes.linewidth': 1.0, 'axes.grid': True,
                  'axes.titlesize': 'x-large', 'axes.labelsize': 'large',
                  'axes.labelcolor': '555555', 'axes.axisbelow': True,
                  'axes.color_cycle': ['348ABD', '7A68A6', 'A60628', '467821', 
                                       'CF4457', '188487', 'E24A33'],
                  'xtick.major.size': 0.0, 'xtick.minor.size': 0.0,
                  'xtick.major.pad': 6.0, 'xtick.minor.pad': 6.0,
                  'xtick.color': '555555', 'xtick.direction': 'in',
                  'ytick.major.size': 0.0, 'ytick.minor.size': 0.0,
                  'ytick.major.pad': 6.0, 'ytick.minor.pad': 6.0,
                  'ytick.color': '555555', 'ytick.direction': 'in', 
                  'legend.fancybox': True, 'figure.figsize': (11, 8), 
                  'figure.facecolor': '0.85', 'figure.edgecolor': '0.5', 
                  'figure.subplot.hspace': 0.5}
        orig_params = {}
        for key in params.keys():
            orig_params[key] = mpl.rcParams[key]
            mpl.rcParams[key] = params[key]
                
        func()

        for key in orig_params.keys():
            mpl.rcParams[key] = orig_params[key]
            
    return apply_style    

# Adapted from https://github.com/daler/matplotlibrc
def probpro_style(func):
    def apply_style():
        params = {'lines.linewidth': 2.0, 'patch.linewidth': 0.5,
                  'patch.facecolor': 'blue', 'patch.edgecolor': 'eeeeee',
                  'patch.antialiased': True, 'text.hinting_factor': 8,
                  'mathtext.fontset': 'cm', 'axes.facecolor': 'eeeeee', 
                  'axes.edgecolor': 'bcbcbc', 'axes.grid': True,
                  'axes.titlesize': 'x-large', 'axes.labelsize': 'large',
                  'axes.labelcolor': '555555', 
                  'axes.color_cycle': ['348ABD', 'A60628', '7A68A6', '467821',
                                       'D55E00', 'CC79A7', '56B4E9', '009E73', 
                                       'F0E442', '0072B2'],
                  'legend.fancybox': True, 'figure.figsize': (11, 8)}
        orig_params = {}
        for key in params.keys():
            orig_params[key] = mpl.rcParams[key]
            mpl.rcParams[key] = params[key]
                
        func()

        for key in orig_params.keys():
            mpl.rcParams[key] = orig_params[key]
            
    return apply_style

def pybo_style(func):
    def apply_style():
        params = {'lines.linewidth': 1.0, 'lines.color': '5390C1',
                  'lines.antialiased': True, 'patch.linewidth': 0.5,
                  'patch.facecolor': 'FFD333', 'patch.edgecolor': 'FFE771',
                  'patch.antialiased': True, 'font.family': 'Arial',
                  'font.size': 10.0, 
                  'font.monospace': ['DejaVu Sans Mono', 'Andale Mono', 
                                     'Nimbus Mono L', 'Courier New', 
                                     'Courier', 'Fixed', 'Terminal', 
                                     'monospace'],
                  'axes.facecolor': 'eeeeee', 'axes.edgecolor': 'bcbcbc',
                  'axes.linewidth': 1.0, 'axes.grid': True,
                  'axes.titlesize': 'x-large', 'axes.labelsize': 'large',
                  'axes.labelcolor': '555555', 'axes.axisbelow': True,
                  'axes.color_cycle': ['5390C1', 'FFD333', 'FFE771', 
                                       '70A4CB', '4385BB', '3D79AA', 
                                       '39719E'],
                  'xtick.major.size': 0.0, 'xtick.minor.size': 0.0,
                  'xtick.major.pad': 6.0, 'xtick.minor.pad': 6.0,
                  'xtick.color': '555555', 'xtick.direction': 'in',
                  'ytick.major.size': 0.0, 'ytick.minor.size': 0.0,
                  'ytick.major.pad': 6.0, 'ytick.minor.pad': 6.0,
                  'ytick.color': '555555', 'ytick.direction': 'in', 
                  'legend.fancybox': True, 'legend.numpoints': 1.0, 
                  'figure.figsize': (11, 8), 'figure.facecolor': '1.0', 
                  'figure.edgecolor': '0.5', 'figure.subplot.hspace': 0.5}
        orig_params = {}
        for key in params.keys():
            orig_params[key] = mpl.rcParams[key]
            mpl.rcParams[key] = params[key]
                
        func()

        for key in orig_params.keys():
            mpl.rcParams[key] = orig_params[key]
            
    return apply_style

# Adapted from https://github.com/daler/matplotlibrc
def r_style(func):
    def apply_style():
        params = {'patch.facecolor': '0.5', 'font.family': 'Arial',
                  'text.hinting_factor': 8, 
                   'axes.color_cycle': ['0.5', '4b6983', '990000', '267726', 
                                        'df421e', '887fa3'],
                   'xtick.major.size': 4.0, 'xtick.direction': 'out',
                   'ytick.major.size': 4.0, 'ytick.direction': 'out', 
                   'legend.fancybox': True, 'legend.fontsize': 'medium',
                   'figure.figsize': (8, 8), 'figure.facecolor': 'white',
                   'image.cmap': 'Spectral'}
        orig_params = {}
        for key in params.keys():
            orig_params[key] = mpl.rcParams[key]
            mpl.rcParams[key] = params[key]
                
        func()

        for key in orig_params.keys():
            mpl.rcParams[key] = orig_params[key]
            
    return apply_style

def my_style(params):
    def decorator(func):
        def apply_style():
            orig_params = {}
            for key in params.keys():
                orig_params[key] = mpl.rcParams[key]
                mpl.rcParams[key] = params[key]
                
            func()

            for key in orig_params.keys():
                mpl.rcParams[key] = orig_params[key]
            
        return apply_style
    return decorator

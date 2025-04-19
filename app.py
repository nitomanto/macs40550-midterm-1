import solara
from model import SchellingModel
from mesa.visualization import (  
    SolaraViz,
    make_space_component,
    make_plot_component,
)
import numpy as np
from scipy.spatial.distance import cosine

## EDIT!!!: defined two different functions for two dimensions
def agent_portrayal_1(agent):
    return {
        "color": 'red' if agent.type[0] == 0 else 'blue',
        "marker": "s",
        "size": 40,
    }

def agent_portrayal_2(agent):
    return {
        "color": 'green' if agent.type[1] == 0 else 'purple',
        "marker": "s",
        "size": 40,
    }

## Enumerate variable parameters in model: seed, grid dimensions, population density, agent preferences, vision, and relative size of groups.
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 50,
        "label": "Width",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 50,
        "label": "Height",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "density": {
        "type": "SliderFloat",
        "value": 0.7,
        "label": "Population Density",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "desired_share_alike": {
        "type": "SliderFloat",
        "value": 0.5,
        "label": "Desired Share Alike",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "dim_one_share": {
        "type": "SliderFloat",
        "value": 0.7,
        "label": "Split on Dimension 1",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "dim_two_share": {
        "type": "SliderFloat",
        "value": 0.0,
        "label": "Split on Dimension 2",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "radius": {
        "type": "SliderInt",
        "value": 1,
        "label": "Vision Radius",
        "min": 1,
        "max": 5,
        "step": 1,
    },
}

## Instantiate model
schelling_model = SchellingModel()

## Define happiness over time plot
HappyPlot = make_plot_component({"share_happy": "tab:green"})

space_components = [make_space_component(agent_portrayal_1, draw_grid=False),
                    make_space_component(agent_portrayal_2, draw_grid=False)]

## Instantiate page inclusing all components
page = SolaraViz(
    schelling_model,
    components=space_components+[HappyPlot],
    model_params=model_params,
    name="Schelling Segregation Model",
)
## Return page
page
    

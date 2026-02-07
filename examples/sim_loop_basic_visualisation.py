"""
Minimal SyMBac simulation example with live visualisation.

Identical to sim_loop_basic.py, but opens a pygame window so you can watch
the colony grow in real time.  Close the window or press ESC to stop.
"""

import numpy as np
from pymunk import Vec2d

from symbac.simulation import Simulator
from symbac.simulation.config import CellConfig, PhysicsConfig, SimViewerConfig
from symbac.simulation.visualisation.live.live_visualisation import LiveVisualisation

np.random.seed(42)

# --- Physics configuration ---------------------------------------------------
physics_config = PhysicsConfig(
    ITERATIONS=100,
)

# --- Cell configuration -------------------------------------------------------
initial_cell_config = CellConfig(
    GRANULARITY=4,
    SEGMENT_RADIUS=10,
    SEGMENT_MASS=1.0,
    GROWTH_RATE=5,
    BASE_MAX_LENGTH=130,
    MAX_LENGTH_VARIATION=0,
    MIN_LENGTH_AFTER_DIVISION=4,
    NOISE_STRENGTH=0.05,
    SEED_CELL_SEGMENTS=30,
    ROTARY_LIMIT_JOINT=True,
    MAX_BEND_ANGLE=0.005,
    START_POS=Vec2d(0, 100),
    START_ANGLE=np.pi / 2,
    STIFFNESS=300_000,
    PIVOT_JOINT_STIFFNESS=5000,
    SIMPLE_LENGTH=False,
)

# --- Create the simulator -----------------------------------------------------
simulator = Simulator(physics_config, initial_cell_config)

# --- Set up live visualisation ------------------------------------------------
sim_viewer_config = SimViewerConfig(SIM_STEPS_PER_DRAW=10)
live_visualisation = LiveVisualisation(sim_viewer_config)
simulator.add_post_step_hook(live_visualisation.draw)

# --- Run until the window is closed ------------------------------------------
while live_visualisation.running:
    simulator.step()

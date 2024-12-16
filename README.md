# Multi-Agent-Envy-Free-Traffic-Management-System

This code was written for the A Novel Multi-Agent Envy-Free Traffic Management System.
In this implementation, it is assumed that no unexpected events will occur, and each agent moves according to its optimal path. There is no need for calculations at each intersection.
In this implementation, a directed weighted graph with 5 edges and 6 agents is considered. Each agent travels from a starting point to a destination. Among the possible paths, based on the modeling explained in the paper, the optimal subsequence of the selected states is chosen, and the agents move accordingly.

To make the agents' movement more realistic, their speed is adjusted based on a safety distance between them. This safety distance is set to the length of the agents themselves, meaning that if the distance between two agents is less than this value, the agent will apply deceleration. Otherwise, the agent will increase acceleration to reach the maximum allowable speed for that edge.

After covering 85% of the path, the agent will initiate deceleration for a smoother stop.

At the end of the simulation, the optimal time and travel time for each agent will be printed.
In this implementation, it is assumed that no unexpected events will occur, and each agent moves according to its optimal path. There is no need for calculations at each intersection.

## How to Run

To run the simulation, simply execute the Python file `animation.py` to view the animation. You can modify the agents and graphs according to your preferences in this file.

### Required Modules
Make sure you have Python installed on your system. The required modules are:

- `networkx`
- `matplotlib`

You can install them using `pip`:

```bash
pip install networkx matplotlib





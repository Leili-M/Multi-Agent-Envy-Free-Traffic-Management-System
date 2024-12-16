# Multi-Agent-Envy-Free-Traffic-Management-System

This code was written for the A Novel Multi-Agent Envy-Free Traffic Management System.

In this implementation, a directed weighted graph with 5 edges and 6 agents is considered. Each agent travels from a starting point to a destination. Among the possible paths, based on the modeling explained in the paper, the optimal subsequence of the selected states is chosen, and the agents move accordingly.

To make the agents' movement more realistic, their speed is adjusted based on a safety distance between them. This safety distance is set to the length of the agents themselves, meaning that if the distance between two agents is less than this value, the agent will apply deceleration. Otherwise, the agent will increase acceleration to reach the maximum allowable speed for that edge.

After covering 85% of the path, the agent will initiate deceleration for a smoother stop.

At the end of the simulation, the optimal time and travel time for each agent will be printed.


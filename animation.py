import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
from Agent import Agent
from Network import Network
from Road import Road




G = nx.DiGraph()
edges = [ 
    ("A", "B", {"length": 6000, "v_max": 100}),
    ("B", "C", {"length": 15000, "v_max": 25}),
    ("C", "D", {"length": 20000, "v_max": 40}),
    ("A", "C", {"length": 31000, "v_max": 80}),
    ("B", "D", {"length": 20000, "v_max": 50}),
]

network_roads = []
index = 0
for u, v, attr in edges:
    L = attr["length"]
    v_max = attr["v_max"]  
    road = Road(edges[index], u, v, L, v_max)
    network_roads.append(road)
    index += 1
    G.add_edge(u, v, **attr)

network_agents = [
    Agent(0, 'A', 'D', 0),
    Agent(1, 'A', 'C', 0),
    Agent(2, 'B', 'D', 0),
    Agent(3, 'A', 'B', 0),
    Agent(4, 'A', 'C', 0),
    Agent(5, 'A', 'C', 0),
]
network = Network(network_agents , network_roads , len(network_agents))
network.roads = network_roads
network.graph = G
network.build_states()



cars = []
for agent in network.agents: 
    info = agent.get_info()
    cars.append(agent.get_info())


for car , agent in zip(cars , network.agents):
    car["reached_time"] = None  
    car["optimal"] = agent.optimal_time
    




time_step = 1  
total_time = 1000 
time_points = int(total_time / time_step)
positions_history = []

for t in range(time_points):
    current_positions = []
    for i, car in enumerate(cars):
        if car["reached_time"] is not None:
            current_positions.append((car["current_edge"], car["position"], car["velocity"]))
            continue

        if t * time_step < car["start_time"]:
            current_positions.append((car["current_edge"], car["position"], car["velocity"]))
            continue

        edge = car["current_edge"]
        edge_data = G.edges[edge]
        remaining_distance = edge_data["length"] - car["position"]

        cars_in_same_edge = [
            c for c in cars
            if c["current_edge"] == car["current_edge"]
            and c["position"] > car["position"]
            and c["start_time"] <= t * time_step
        ]

        velocity_m_per_s = car["velocity"] / 3.6  
        max_velocity_m_per_s = edge_data["v_max"] / 3.6  

        if cars_in_same_edge:
            front_car = min(cars_in_same_edge, key=lambda c: c["position"]) 
            delta_x = front_car["position"] - car["position"]  

            if delta_x > Agent.length:  
                acceleration = min((delta_x / edge_data["length"]) * max_velocity_m_per_s, max_velocity_m_per_s - velocity_m_per_s)
                
            else:
                acceleration = 0  
        else:
            remaining_distance = (edge_data["length"] - car["position"])  
            if edge_data['length']*0.01<=remaining_distance <= edge_data['length'] * 0.15:  
                acceleration = -(max_velocity_m_per_s**2) / (2 * remaining_distance)  
            else:
                if velocity_m_per_s == 0:  
                    acceleration = max_velocity_m_per_s 
                else:
                    acceleration = min(max_velocity_m_per_s - velocity_m_per_s, 1) 
        acceleration *= 3.6  
        car["velocity"] += acceleration * time_step
        car["velocity"] = max(0, min(car["velocity"], edge_data["v_max"]))
        car["position"] += car["velocity"] * time_step

        if car["position"] >= edge_data["length"]:  
            car["position"] -= edge_data["length"]
            path = car["path"]
            current_index = path.index(edge[1])

            if current_index < len(path) - 1:
                car["current_edge"] = (path[current_index], path[current_index + 1])
                car["velocity"] = 0
            else:
                car["velocity"] = 0
                car["reached_time"] = t * time_step  

        current_positions.append((car["current_edge"], car["position"], car["velocity"]))
    positions_history.append(current_positions)


for i, car in enumerate(cars):
    print(f"Car {i + 1} real_cost: {car['reached_time'] - car['start_time']} seconds\noptimal {car['optimal']}")
    





fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G)

def draw_graph():
    nx.draw(G, pos, with_labels=True, node_size=400, node_color="lightblue", ax=ax)
    edge_labels = {edge: f"L={data['length']} v_max={data['v_max']}" for edge, data in G.edges.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

def update(frame):
    ax.clear()
    draw_graph()
    
    
    current_time = frame  
    time_text = f"Time: {current_time}s"
    ax.text(0.05, 0.95, time_text, transform=ax.transAxes, fontsize=12, color="black", verticalalignment="bottom", horizontalalignment='left')

    for car_index, (edge, position, velocity) in enumerate(positions_history[frame]):
        u, v = edge
        ux, uy = pos[u]
        vx, vy = pos[v]
        x = ux + (vx - ux) * (position / G.edges[edge]["length"])
        y = uy + (vy - uy) * (position / G.edges[edge]["length"])

        ax.plot(x, y, "o", label=f"Car {car_index + 1}")
        ax.text(x, y + 0.02, f"v={velocity:.2f} km/h", fontsize=9, color="blue")

    ax.legend()


ani = FuncAnimation(fig, update, frames=len(positions_history), interval=280, repeat=False)
plt.show()

from Agent import Agent
import networkx as nx
from helpers import get_matrices_in_range , sum_matrices_pure , find_changed_roads

class Network : 
    def __init__(self , agents:list[Agent] , roads , n) -> None:
        self.agents = agents
        self.roads = roads
        self.current_state = [(0, float('inf')) , [[0]*n for i in range(len(roads))]]
        self.states = []
    
    def build_graph(self , nodes):
        for node in nodes.values() :
         node_info = node.get_node_info()
         self.graph.add_node(
                node_info['name'],
                pos=(node_info['x_pos'], node_info['y_pos'])
            )
  

    def build_states(self) :
        all_agents_seq = []
        for i, agent in enumerate(self.agents) : 
            paths = list(nx.all_simple_paths(self.graph , agent.start , agent.end))
            agent_seq = agent.choose_path(paths = paths  , roads=self.roads , n = len(self.agents))
            all_agents_seq.append(agent_seq[0])

        self.merge_states(all_agents_seq)
    def merge_states(self , agents_seq) :
        merged_states = [] 
        intervals = {}
        for seq in agents_seq :
            intervals[seq['seq'][0][0]] = []
        for seq in agents_seq :
            intervals[seq['seq'][0][0]].append(seq['seq'][0][1] )


        def find_all_sub_intervals(ranges ):
            points = set()
            for start, end in ranges:
                points.add(start)
                points.add(end)
            sorted_points = sorted(points)
            sub_intervals = []
            for i in range(len(sorted_points) - 1):
                sub_start = sorted_points[i]
                sub_end = sorted_points[i + 1]
                sub_intervals.append((sub_start, sub_end))

            intersections = []
            for interval in sub_intervals:
                covered = [r for r in ranges if r[0] <= interval[0] and r[1] >= interval[1]]
                if covered:
                    intersections.append(interval)
            
            return intersections

        ranges = list(intervals.keys())
        result = find_all_sub_intervals(ranges)
        sub_states= {}
        for sub_interval in result :
            for interval in intervals :
             if interval[0]<= sub_interval[0] <=sub_interval[1] <= interval[1] :
                 if sub_interval in sub_states : 
                     sub_states[sub_interval].append(intervals[interval])
                 else:
                     sub_states.setdefault(sub_interval, [intervals[interval]])

        merged_states = sum_matrices_pure(sub_states)
        for agent in self.agents : 
           subsequence = get_matrices_in_range( merged_states, agent.start_time  , agent.optimal_time)
           sub_states  = []
           for interval in subsequence : 
            sub_states.append(subsequence[interval])
            agent.subsequence = sub_states
           agent.subsequence = find_changed_roads(agent.subsequence , agent.id)


    
                

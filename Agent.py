class Agent : 
    length = 5
    def __init__(self , id, start , end  , start_time:float) -> None:
        self.id =id
        self.subsequence = None
        self.start = start
        self.end = end
        self.speed = 0
        self.start_time = start_time
        self.path = None
        self.cost = 0
        self.real_cost = 0
        self.current_edge = None
        self.optimal_time = 0
        self.expected_cost = 0
        self.optimal_sequence = None

    def get_info(self) : 
       return {'path' : self.path, 'position' : 0 , 'current_edge' : self.current_edge , 'velocity' : self.speed , 'start_time' : self.start_time }
    def choose_path(self , roads, paths , n) :
        all_seq = []
        for i , path in enumerate(paths) :
            sequence = []
            time = self.start_time 
            for j in range(len(path)-1):
              startT = time
              for road in roads : 
                if road.start == path[j] and road.end == path[j+1] : 
                    time_to_pass = road.length / road.max_speed 
                    endT = time + time_to_pass 
                    state = [[0]*n for i in range(len(roads))]
                    current_road = state[roads.index(road)]
                    current_road[self.id] = 1
                    state [roads.index(road)] = current_road
                    sequence.append([(round(startT , 5),round(endT , 5)),state])
                    time += time_to_pass
                    break
            all_seq.append({tuple(path) : {"seq": sequence , "time" : sequence[-1][0][1]}})
        optimal_time = float('inf')
        optimal_seq = None
        for seq  in all_seq : 
           for path in seq : 
            if seq[path]['time'] < optimal_time :
                optimal_time = seq[path]['time']
                optimal_seq = seq[path]
                optimal_path = list(seq.keys())[0]
            self.optimal_time = optimal_time - self.start_time
            self.path = optimal_path
            self.current_edge = optimal_path[0] , optimal_path[1]
            self.optimal_sequence = optimal_seq

        return [optimal_seq , optimal_path , optimal_time]
    
    
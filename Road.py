class Road :
    n = 4
    def __init__(self , id ,start , end, length:float , max_speed : int) -> None:
        self.id = id
        self.start = start
        self.end = end
        self.length = length 
        self.max_speed = max_speed 
        self.status = [0]*4
        self.density = 0
        self.current_velocity = max_speed

    def get_info(self) : 
        return self.start , self.end , {'length' : self.length , 'v_max' : self.max_speed}
    
    




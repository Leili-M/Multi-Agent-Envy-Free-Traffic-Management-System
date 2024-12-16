def flatten_matrices(nested_matrices):
    flat_list = []
    for sublist in nested_matrices:
        for matrix in sublist:
            flat_list.append(matrix)
    return flat_list

def sum_matrices_pure(intervals):
    summed_intervals = {}

    for interval, nested_matrices in intervals.items():
        matrices = flatten_matrices(nested_matrices)
        
        if not matrices:
            summed_intervals[interval] = []
            continue
        num_rows = len(matrices[0])
        num_cols = len(matrices[0][0])
        summed_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        for matrix in matrices:
            if len(matrix) != num_rows or any(len(row) != num_cols for row in matrix):
                raise ValueError(f"Inconsistent matrix dimensions in interval {interval}.")

            for i in range(num_rows):
                for j in range(num_cols):
                    summed_matrix[i][j] += matrix[i][j]

        summed_intervals[interval] = summed_matrix

    return summed_intervals



def get_matrices_in_range(data, start, end):
    result = {}
    for interval, matrix in data.items():
        interval_start, interval_end = interval
        if interval_start >= start and interval_end <= end:
            result[interval] = matrix

    return result
def find_changed_roads(states, index_to_check):
    changed_roads = []  
    current_road = states[0]
    index = [current_road.index(road) for road in current_road if road[index_to_check] == 1][0]
    changed_roads = [current_road] 
    for state in states[1:]:
        for road in state:
            if road[index_to_check] == 1 and road != current_road and state.index(road)!=index:
                changed_roads.append(state)
                current_road = road
                index = state.index(current_road)
                break 
    return changed_roads



class SlowdownHandler():
    def __init__(self):
        self.slowdown_index = [0]
        self.throttle_index = [0]
        self.has_iterated = [False]
        self.current_throttle = [0.8, 0.03]
        #Read list of positions
        turn_txt_file = open("slowdown_points.txt", "r")
        thr_txt_file = open("speedup_points.txt", "r")
        turn_array = turn_txt_file.read().split("\n")
        thr_array = thr_txt_file.read().split("\n")
        self.turn_points = []
        self.thr_points = []
        #Split both position lists into separate arrays, then convert position values into float
        for i in range(len(turn_array)):
                item = turn_array[i]
                items = item.split(",")                
                for j in range(len(items)):
                    item_new = items[j].replace('[', '').replace(']', '').replace(' ', '')                              
                    items[j] = float(item_new)
                self.turn_points.append(items)
        #Repeat for speed increasing points
        for i in range(len(thr_array)):
                item = thr_array[i]
                items = item.split(",")                
                for j in range(len(items)):
                    item_new = items[j].replace('[', '').replace(']', '').replace(' ', '')                              
                    items[j] = float(item_new)
                self.thr_points.append(items)

    def check_pos(self, current_pos):
        print(self.slowdown_index[0])
        print(self.throttle_index[0])
        print(self.has_iterated[0])        
        if (current_pos[0] >= self.turn_points[self.slowdown_index[0]][0] - 7.5 and current_pos[0] <= self.turn_points[self.slowdown_index[0]][0] + 7.5):
            if (current_pos[2] >= self.turn_points[self.slowdown_index[0]][2] - 7.5 and current_pos[2] <= self.turn_points[self.slowdown_index[0]][2] + 7.5):
                if (self.has_iterated[0] == False):
                    self.slowdown_index[0] += 1
                    self.has_iterated[0] == True
                print("in slowdown region range")
                self.current_throttle[0] = 0.4
                self.current_throttle[1] = 0.02
        if (current_pos[0] >= self.thr_points[self.throttle_index[0]][0] - 7.5 and current_pos[0] <= self.thr_points[self.throttle_index[0]][0] + 7.5):
            if (current_pos[2] >= self.thr_points[self.throttle_index[0]][2] - 7.5 and current_pos[2] <= self.thr_points[self.throttle_index[0]][2] + 7.5):
                if (self.has_iterated[0] == False):
                    self.throttle_index[0] += 1
                    self.has_iterated[0] == False
                print("in throttle region range")
                self.current_throttle[0] = 0.8
                self.current_throttle[1] = 0.03
        return self.current_throttle[0], self.current_throttle[1]   
                  


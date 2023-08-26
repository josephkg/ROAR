class SlowdownHandler():
    def __init__(self):
        self.slowdown_index = [0]
        self.throttle_index = [0]
        self.has_iterated = [False]
        self.rg_iterated = [False]
        self.current_throttle = [0.8, 0.03]
        self.throttle_in_region = [0.8, 0.4]
        #Read list of positions
        turn_txt_file = open("slowdown_points.txt", "r")
        thr_txt_file = open("speedup_points.txt", "r")
        turn_array = turn_txt_file.read().split("\n")
        thr_array = thr_txt_file.read().split("\n")
        self.turn_points = []
        self.thr_points = []
        self.rg_points = [2433.98168945, 116.29998779, 3732.32983398]
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
        if (current_pos[0] >= self.turn_points[self.slowdown_index[0]][0] - 30 and current_pos[0] <= self.turn_points[self.slowdown_index[0]][0] + 30):
            if (current_pos[2] >= self.turn_points[self.slowdown_index[0]][2] - 30 and current_pos[2] <= self.turn_points[self.slowdown_index[0]][2] + 30):
                if (self.has_iterated[0] == False):
                    self.slowdown_index[0] += 1
                    self.has_iterated[0] == True
                print("in slowdown region range")
                self.current_throttle[0] = self.throttle_in_region[1]
                self.current_throttle[1] = 0.03
        if (current_pos[0] >= self.thr_points[self.throttle_index[0]][0] - 30 and current_pos[0] <= self.thr_points[self.throttle_index[0]][0] + 30):
            if (current_pos[2] >= self.thr_points[self.throttle_index[0]][2] - 30 and current_pos[2] <= self.thr_points[self.throttle_index[0]][2] + 30):
                if (self.has_iterated[0] == False):
                    self.throttle_index[0] += 1
                    self.has_iterated[0] == False
                print("in throttle region range")
                self.current_throttle[0] = self.throttle_in_region[0]
                self.current_throttle[1] = 0.04
        if (current_pos[0] >= self.rg_points[0] - 30 and current_pos[0] <= self.rg_points[0] + 30):
            if (current_pos[2] >= self.rg_points[2] - 30 and current_pos[2] <= self.rg_points[2] + 30):
                    if (self.rg_iterated[0] == False):
                        print("region 2 reached, throttle values changing")
                        self.throttle_in_region[0] = 0.8
                        self.throttle_in_region[1] = 0.6
                        self.rg_iterated[0] == True
        return self.current_throttle[0], self.current_throttle[1]   
                  


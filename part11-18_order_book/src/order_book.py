class Task:
    counter = 1
    def __init__(self, description: str, programmer:str, workload: int) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.counter
        Task.counter += 1
    def mark_finished(self):
        self.finished = True
    def is_finished(self):
        return True if self.finished == True else False

    def __repr__(self) -> str:
        fin = f"{"NOT FINISHED" if self.finished == False else "FINISHED"}"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {fin}"

class OrderBook:
    namelist = []
    def __init__(self) -> None:
        self.tasklist = []
        self.names = OrderBook.namelist
    def add_order(self, description, programmer, workload):
        self.task = Task(description, programmer, workload)
        self.tasklist.append(self.task)
    def all_orders(self):
        return self.tasklist
    def programmers(self):
        for p in self.tasklist:
            self.names.append(p.programmer)
        return list(set(self.names))
    def mark_finished(self, task_id: int):
        for order in self.tasklist:
            if order.id == task_id:
                order.finished = True
                return
        raise ValueError (f"No task found with id {task_id}")
    def finished_orders(self):
        return [order for order in self.tasklist if order.finished == True]
    def unfinished_orders(self):
        return [order for order in self.tasklist if order.finished != True]
    
    def  status_of_programmer(self, programmer: str):
        finished = 0
        workload_finished = 0
        unfinished = 0
        workload_unfinished = 0
        for order in self.tasklist:
            if order.programmer == programmer:
                if order.finished == True:
                    finished +=1
                    workload_finished += order.workload
                elif order.finished == False:
                    unfinished +=1
                    workload_unfinished += order.workload
        if finished == 0 and unfinished == 0:
            raise ValueError
        
        return finished, unfinished, workload_finished, workload_unfinished
        
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)
    orders.mark_finished(1)
    orders.mark_finished(2)
    status = orders.status_of_programmer("Adele")
    print(status)
    
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[e, p, i] for i, (e, p) in enumerate(tasks)]  # add the index to tasks to compare two tasks with similar processing time
        tasks.sort(key=lambda x: x[0])  # sort by enquiry time
        res = []  # order in which the CPU will process the tasks
        heap = []  # available task sorted by processing time (and by index if equality)
        i = 0  # index of task for enquiry time
        time = tasks[0][0]  # init time directly at minimum time
        nb_tasks = len(tasks)

        while heap or (i < nb_tasks):
            # add the new available tasks
            while (i < nb_tasks) and (time >= tasks[i][0]):
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if heap:  # process a task
                t = heapq.heappop(heap)
                res.append(t[1])
                time += t[0]
            else:  # no available task, CPU remains idle until the next one
                time = tasks[i][0]
        return res

    # TLE ...
    """
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 1  # init time
        tasks = [[e, p, i] for i, (e, p) in enumerate(tasks)]  # add the index to tasks to compare two tasks with similar processing time
        d_enqueue = deque(sorted(tasks))  # sort by enqueue time first
        d_process = deque([])  # available task sorted by processing time
        res = []  # order in which the CPU will process the tasks
        
        # to add a process to the available tasks and sort by processing time and then by index
        def add_d_process(task: list) -> None:
            nonlocal d_process
            d_process.append(task)
            j = len(d_process) - 1
            while (j > 0) and ((d_process[j][1] < d_process[j-1][1]) or ((d_process[j][1] == d_process[j-1][1]) and (d_process[j][2] < d_process[j-1][2]))):
                d_process[j], d_process[j-1] = d_process[j-1], d_process[j]
                j -= 1
        
        while d_enqueue:
            while d_enqueue and (d_enqueue[0][0] <= time):  # add all the new available tasks
                add_d_process(d_enqueue.popleft())
            if d_process:  # if we can process a tasks, process it
                task = d_process.popleft()
                res.append(task[2])
                time += task[1]
            else:  # else, CPU remains idle
                time += 1
        res.extend([task[2] for task in d_process])  # add the remaining available tasks in order
        return res
    """

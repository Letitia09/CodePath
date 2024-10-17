def find_task_pair(task_times, available_time):
    res = False
    for i in range(len(task_times)):
        for j in range(i+1,len(task_times)):
            if task_times[i]+task_times[j]==available_time:
                res=True
                break
    return res        
              
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

#METHOD 2
def find_task_pair(task_times, available_time):
    res = False
    for i in range(len(task_times)):
        if available_time-task_times[i] in task_times[:i]+task_times[i+1:]:
            res=True
            break
    return res        
              
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))



#METHOD 3
def find_task_pair(task_times, available_time):
    task_set = set()

    for time in task_times:
        complement = available_time - time
        #print(complement)
        if complement in task_set:
            return True
        task_set.add(time)
        #print(task_set)
    return False
              
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

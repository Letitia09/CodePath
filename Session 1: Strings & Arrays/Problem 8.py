def print_todo_list(task):
    print("Pooh's To Dos:")
    if len(task) > 1:
        sum = 1
        for i in range(len(task)):
            print(f"{sum}. {task[i]}")
            sum += 1
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

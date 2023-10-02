def calculate_metrics(processes):
    n = len(processes)
    
    # Initialize variables for metrics
    total_turnaround_time = 0
    total_waiting_time = 0
    
    for i in range(n):
        if i == 0:
            processes[i]['CompletionTime'] = processes[i]['ArrivalTime'] + processes[i]['BurstTime']
        else:
            processes[i]['CompletionTime'] = max(processes[i]['ArrivalTime'], processes[i - 1]['CompletionTime']) + processes[i]['BurstTime']
        
        processes[i]['TurnaroundTime'] = processes[i]['CompletionTime'] - processes[i]['ArrivalTime']
        processes[i]['WaitingTime'] = processes[i]['TurnaroundTime'] - processes[i]['BurstTime']
        
        total_turnaround_time += processes[i]['TurnaroundTime']
        total_waiting_time += processes[i]['WaitingTime']
    
    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n
    
    return processes, average_turnaround_time, average_waiting_time

if __name__ == "__main__":
    # Example input: ID, ArrivalTime, BurstTime
    processes = [
        {'ID': 1, 'ArrivalTime': 0, 'BurstTime': 7},
        {'ID': 2, 'ArrivalTime': 2, 'BurstTime': 4},
        {'ID': 3, 'ArrivalTime': 4, 'BurstTime': 1},
        {'ID': 4, 'ArrivalTime': 5, 'BurstTime': 4},
    ]

    # Sort processes by arrival time (if unsorted)
    processes.sort(key=lambda x: x['ArrivalTime'])

    processed_processes, avg_turnaround_time, avg_waiting_time = calculate_metrics(processes)

    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processed_processes:
        print(f"{process['ID']}\t{process['ArrivalTime']}\t\t{process['BurstTime']}\t\t{process['CompletionTime']}\t\t{process['TurnaroundTime']}\t\t{process['WaitingTime']}")

    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")
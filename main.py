import psutil

def list_process_information():
    # List of desired attributes
    attributes = [
        'cmdline', 
       # 'connections',
        'cpu_affinity', 
        'cpu_num', 
        'cpu_percent', 
        'cpu_times', 
        'create_time', 
        'cwd', 
        'environ', 
        'exe', 
        'gids', 
        'io_counters', 
        'ionice', 
        'memory_full_info', 
        'memory_info', 
        # 'memory_maps', 
        'memory_percent', 
        'name', 
        'nice', 
        'num_ctx_switches', 
        'num_fds', 
        'num_threads', 
        'open_files', 
        'pid', 
        'ppid', 
        'status', 
        'terminal', 
        'threads', 
        'uids', 
        'username'
    ]

    # Iterate over all processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.as_dict(attrs=attributes)
            print('\n---------------------------------------------------------------------------------------\n')

            print(f"\nPID: {process_info['pid']} - Name: {process_info['name']}")
            print("Information:")
            for attr, value in process_info.items():
                if attr not in ['pid', 'name']:
                    print(f"  {attr}: {value}")

            print('\n---------------------------------------------------------------------------------------\n')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that no longer exist or are inaccessible
            pass

if __name__ == "__main__":
    list_process_information()

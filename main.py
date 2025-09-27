import psutil
import datetime

def listar_informacoes_processos():
    # Lista de itens desejados
    itens = [
        'cmdline', 
        #'connections',
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

    with open("/app/process_log.txt", "a") as f:  
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process_info = proc.as_dict(attrs=itens)

                f.write("\n" + "-" * 90 + "\n")
                f.write(f"\n{datetime.datetime.now()} - PID: {process_info['pid']} - Nome: {process_info['name']}\n")
                f.write("Informações:\n")
                for item, value in process_info.items():
                    if item not in ['pid', 'name']:
                        f.write(f"  {item}: {value}\n")
                f.write("\n" + "-" * 90 + "\n\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


if __name__ == "__main__":
    listar_informacoes_processos()



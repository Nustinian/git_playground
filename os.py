import os

def get_warnings_total():
    cmd = "sudo cat -n /var/log/awslogs.log" | grep "WARNING" | wc -n"
    total = int(os.popen(cmd).read())
    return total

def search_and_add(thread_number):
    thread_name = f(Thread-{thread_number})
    cmd = f'sudo cat -n /var/log/awslogs.log | grep "WARNING" | grep "{thread_name}" | wc -l'
    warnings_num = int(os.popen(cmd).read())
    remaining_warnings -= warnings_num
    threads_dict[thread_name] = warnings_num

    

threads_dict = {}

myCmd = 'ls -la > output.txt'
os.system(myCmd)

warnings_total = get_warnings_total()
remaining_warnings = warnings_total


import os

def get_warnings_total():
    cmd = "sudo cat -n /var/log/awslogs.log | grep 'WARNING' | wc -l"
    total = int(os.popen(cmd).read())
    return total

def search_and_add(thread_number):
    thread_name = "Thread-{thread_number}".format(thread_number=thread_number)
    cmd = 'sudo cat -n /var/log/awslogs.log | grep "WARNING" | grep "{thread_name}" | wc -l'.format(thread_name=thread_name)
    warnings_num = int(os.popen(cmd).read())
    remaining_warnings -= warnings_num
    threads_dict[thread_name] = warnings_num

    

threads_dict = {}

warnings_total = get_warnings_total()
remaining_warnings = warnings_total

print("There are " + str(warnings_total) + " warnings in the awslogs.log.")
search_and_add(1)
import os

def get_warnings_total():
    cmd = "sudo cat -n /var/log/awslogs.log | grep 'WARNING' | wc -l"
    total = int(os.popen(cmd).read())
    return total

def search_and_add(thread_number):
    thread_name = "Thread-{thread_number}".format(thread_number=thread_number)
    cmd = 'sudo cat -n /var/log/awslogs.log | grep "WARNING" | grep "{thread_name}" | wc -l'.format(thread_name=thread_name)
    warnings_num = int(os.popen(cmd).read())
    threads_dict[thread_name] = warnings_num
    return warnings_num

def report_minimum(minimum=0):
    report_dict = {}
    for key, value in threads_dict.items():
        if value > minimum:
            report_dict[key] = value
    if len(report_dict) > 0:
        print("The following threads produced more than {0} warning(s):").format(minimum)
        for key, value in report_dict.items():
            print("{key}: {value} warning(s)").format(key=key, value=value)

threads_dict = {}
warnings_total = get_warnings_total()
remaining_warnings = warnings_total

print("There are " + str(warnings_total) + " warnings in the awslogs.log.")

i = 1
while remaining_warnings > 0:
    warnings_num = search_and_add(i)
    if warnings_num != 0:
        print("There were " + str(warnings_num) + " warnings under Thread-" + str(i) + ".")
    remaining_warnings -= warnings_num
    i += 1

report_minimum(10)


def generate_report(name, date,  finished_tasks=None, to_do_tasks=None):
    report = f"Name: {name}\n"
    report += f"Date: {date}\n"
    report += "Report on Completed Tasks\n"


    if finished_tasks:
        report += "Finished Tasks\n"
        report += f"{finished_tasks}\n"

    if to_do_tasks:
        report += "Tasks yet to do\n"
        report += f"{to_do_tasks}\n"

    return report

print(generate_report("Anush", "27/07/2024", finished_tasks="problems 1 to 5", to_do_tasks = "problems 6,7,8" ))
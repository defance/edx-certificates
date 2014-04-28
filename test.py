from weasyprint import HTML

import globals
import student
import html_academy_certificate


def perform_task(input_file='', logfile='', do_compile=True):
    lst = student.get_student_list(input_file)
    with open(logfile, "w") as f:
        for (i, s) in enumerate(lst, start=1):
            print("Processing student %i/%i" % (i, len(lst)))
            c = html_academy_certificate.HTMLAcademyCertificate(
                s,
                base_path=globals.RESOURCE_PATH,
                output_prefix=globals.OUTPUT_DIR
            )
            if do_compile:
                c.compile()
            f.write(globals.REPORT_STRING.format(
                user_id=s.id,
                course_id=c._COURSE_ID,
                grade=s.grade,
                download_url='/static/files/certificates/'+c.output_file
            ))
            f.write('\n')


def main():
    do_compile = False
    perform_task(globals.LIST_WITH_HONOURS, globals.OUTPUT_DIR + 'report_with_honours.txt', do_compile=do_compile)
    perform_task(globals.LIST_WITHOUT_HONOURS, globals.OUTPUT_DIR + 'report_without_honours.txt', do_compile=do_compile)
    perform_task(globals.LIST_TEST, globals.OUTPUT_DIR + 'report_test.txt', do_compile=do_compile)
    print("All done")

# Main program
if __name__ == "__main__":
    main()

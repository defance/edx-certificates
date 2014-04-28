RESOURCE_PATH = './resources/fancy_cert/'
CERTIFICATE = RESOURCE_PATH + 'certificate.html'
OUTPUT = 'certificate.pdf'

INPUT_DIR = './input/'

OUTPUT_DIR = './output/'
OUTPUT_DIR_CERTIFICATES = OUTPUT_DIR + 'certificates/'

LIST_WITH_HONOURS = INPUT_DIR + 'x004-00_complete_2014_04_28_with_dist.csv'
LIST_WITHOUT_HONOURS = INPUT_DIR + 'x004-00_complete_2014_04_28_no_dist.csv'
LIST_TEST = INPUT_DIR + 'test_myself.csv'

SECRET = '5Zp6KcWkYJhQ9nXzcAarXvgj'

REPORT_STRING = "GeneratedCertificate(user=User.objects.get(id={user_id}), course_id='{course_id}', grade='{grade}', download_url='{download_url}', status='downloadable').save()"  # noqa

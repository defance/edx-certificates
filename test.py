from weasyprint import HTML

RESOURCE_PATH = './fancy_cert/'
CERTIFICATE = RESOURCE_PATH + 'certificate.html'
OUTPUT = 'certificate.pdf'

def get_file_contents(filename):
    with open (filename, "r") as f:
        return f.read()

def main():
    HTML(
      string=get_file_contents(CERTIFICATE),
      base_url=RESOURCE_PATH
    ).write_pdf(OUTPUT)

# Main program
if __name__=="__main__":
    main()

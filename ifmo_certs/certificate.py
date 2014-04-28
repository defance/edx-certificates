# -*- coding: utf-8 -*-

import hashlib
import utils
import weasyprint


class Certificate(object):

    def __init__(self, student_obj, source, course_id, course_name, secret='', base_path='./', output_prefix='./'):
        self.course_id = course_id
        self.student = student_obj
        self.course_name = course_name
        self._source = source
        self._secret = secret
        self._base_path = base_path
        self._output_prefix = output_prefix

    def compile(self):
        utils.ensure_dir(self._output_prefix + self.output_path)
        string = utils.get_file_contents(self._source).format(
            student_name=self.student.printed_name,
            title='{student_name} - {course_name}'.format(
                student_name=self.student.printed_name,
                course_name=self.course_name
            )
        )
        weasyprint.HTML(
            string=string,
            base_url=self._base_path
        ).write_pdf(self._output_prefix + self.output_file)

    @property
    def output_path(self):
        digest = lambda x: hashlib.sha1(x + self._secret).hexdigest()
        return "{course_hash}/{student_hash}/".format(
            course_hash=digest(self.course_id),
            student_hash=digest(self.student.id)
        )

    @property
    def output_file(self):
        return self.output_path + "certificate.pdf".format(
            student_name=self.student.printed_name,
            course_name=self.course_name
        )
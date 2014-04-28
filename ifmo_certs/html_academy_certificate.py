# -*- coding: utf-8 -*-

from ifmo_certs import globals, certificate


class HTMLAcademyCertificate(certificate.Certificate):

    _COURSE_ID = 'ITMO/x0002.00/2014_02'
    _COURSE_NAME = 'Создание веб-интерфейсов с помощью HTML и CSS'
    _SOURCE = globals.CERTIFICATE

    def __init__(self, student_obj, secret=globals.SECRET, base_path='./', output_prefix='./'):
        super(HTMLAcademyCertificate, self).__init__(
            student_obj,
            self._SOURCE,
            self._COURSE_ID,
            self._COURSE_NAME,
            secret=secret,
            base_path=base_path,
            output_prefix=output_prefix
        )
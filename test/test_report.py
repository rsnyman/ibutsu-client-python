# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ibutsu_client
from ibutsu_client.models.report import Report  # noqa: E501
from ibutsu_client.rest import ApiException

class TestReport(unittest.TestCase):
    """Report unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Report
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.report.Report()  # noqa: E501
        if include_optional :
            return Report(
                id = 'c6188b3fa767f0c9baf3', 
                filename = 'myreport.zip', 
                mimetype = 'application/zip', 
                url = 'http://ibutsu/reports/download/myreport.zip', 
                download_url = 'http://ibutsu/reports/download/myreport.zip', 
                view_url = 'http://ibutsu/reports/view/myreport.html', 
                parameters = {"type":"dashboard","filter":"test_navigation","source":"iqe-jenkins"}, 
                status = 'done'
            )
        else :
            return Report(
        )

    def testReport(self):
        """Test Report"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
"""Module for unittesting dmidecode methods"""

import os
import unittest
from hwinfo.host.dmidecode import *


class DmidecodeParserTests(unittest.TestCase):

    pwd = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE = os.path.join(pwd, 'data', 'dmidecode')

    DATA_REC = {
        'bios_vendor_name': 'Dell Inc.',
        'bios_version': '1.0.0',
        'bios_release_date': '02/11/2010',
        'system_manufacturer': 'Dell Inc.',
        'system_product_name': 'PowerEdge R310',
        'system_serial_number': 'GZ7BS4J',
        'system_uuid': '4C4C4544-005A-3710-8042-C7C04F53344A',
        'chassis_type': 'Rack Mount Chassis',
        'socket_designation': 'CPU1, CPU2',
    }


    def setUp(self):
        fh = open(self.DATA_FILE)
        data = fh.read()
        fh.close()
        self.parser = DmidecodeParser(data)

    def _assert_equal(self, key):
        rec = self.parser.parse()
        return self.assertEqual(rec[key], self.DATA_REC[key])

    def test_dmidecode_bios_vendor_name(self):
        return self._assert_equal('bios_vendor_name')

    def test_dmidecode_bios_version(self):
        return self._assert_equal('bios_version')

    def test_dmidecode_bios_release_date(self):
        return self._assert_equal('bios_release_date')

    def test_dmidecode_system_manufacturer(self):
        return self._assert_equal('system_manufacturer')

    def test_dmidecode_system_product_name(self):
        return self._assert_equal('system_product_name')

    def test_dmidecode_system_serial_number(self):
        return self._assert_equal('system_serial_number')

    def test_dmidecode_system_uuid(self):
        return self._assert_equal('system_uuid')

    def test_dmidecode_chassis_type(self):
        return self._assert_equal('chassis_type')

    def test_dmidecode_socket_designation_type(self):
        return self._assert_equal('socket_designation')

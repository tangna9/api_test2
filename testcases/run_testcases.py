#!/usr/bin/env python
#encoding:utf8

from testcases.test_scene_live import MyTestCaseSceneLive
from testcases.test_scene_mobile import MyTestCaseSceneMobile
from testcases.test_scene_short_vedio import MyTestCaseSceneShortVedio
import unittest

if __name__ == "__main__":

    suite_list = []
    test_class_list = [MyTestCaseSceneLive,
                       MyTestCaseSceneMobile,
                       MyTestCaseSceneShortVedio]
    for test_class in test_class_list:
        print test_class
        suite_list.append(unittest.TestLoader().loadTestsFromTestCase(test_class))
    suite = unittest.TestSuite(suite_list)
    unittest.TextTestRunner(verbosity=2).run(suite)

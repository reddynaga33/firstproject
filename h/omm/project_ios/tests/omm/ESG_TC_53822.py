#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This test case is for installation with verification of only screen names 
    (need to be used for BVT testing)

    :copyright: (c) 2016 by Nithya_V for Dell.
"""
from libs.product.omm import omm_step_functions
from libs.product.omm.omm_step_functions import Steps
from libs.product.omm.standard.base_class import TestBase

obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)


class ESG_TC_53822(TestBase):

    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        self.driver_start_status = False
        self.uninstall_app = False

    def setUp(self):
        print "Inside the set up function"
        self.uninstall_app,  msg = obj_common.step_uninstall_app()
        if self.uninstall_app:
            self.driver_start_status, msg = obj_common.step_start_driver()
        else:
            self.fail("Failed to un-install the app")


    def test_200(self):
        """
        @testcase: 1000.1
        """

        
        #step_1 = obj_omm.step_verify_license_agreement_screenname
        step_2 = obj_omm.step_verify_end_user_license_agreement_text
        step_3 = obj_omm.step_accept_license
        step_4 = obj_omm.step_verify_Diagnostics_and_usage_screenname 
        step_5 = obj_omm.step_verify_Diagnostics_and_usage_text
        step_6 = obj_omm.step_accept_diagnostics_and_usage
        #step_7 = obj_omm.step_verify_createPassword_screenname
        step_8 = obj_omm.step_create_login_password
        step_9 = obj_omm.step_verify_try_demomode_screenname
        step_10 = obj_omm.step_verify_try_demomode_page_text
        'Verify demo mode screen and continue to try demo mode'
        step_11 = obj_omm.step_demo_mode_try_now
        step_12 = obj_omm.demomode_exit_from_all_pages
        #step_13 = obj_omm.step_verify_all_idrac_devices_text
        step_13= obj_omm.step_vrify_first_ome_devices_txt           
        #step_14 = obj_omm.step_vrify_first_ome_devices_txt
        step_14 = obj_omm.step_verify_first_idrac_devices_text
     
        step_15= obj_omm.step_verify_enable_demomode_option_from_settings
        'Verify eixt demo mode option from demo mode all pages'
        #step_15 = obj_omm.demomode_exit_from_all_pages

        if self.uninstall_app and self.driver_start_status:
            self.run_steps(step_2,step_3,step_4, step_5,step_6,step_8,step_9,step_10,step_11,step_12,step_13,step_14,step_15,
                           step_args=[self], continue_on_fail=True)
        else:
            self.fail("Failed to start driver")

    def tearDown(self):
        print "Inside the tear down function"
        if self.uninstall_app and self.driver_start_status:
            driver_stop_status, msg = obj_common.step_quit_driver()
            if not driver_stop_status:
                self.fail("Failed to stop driver")

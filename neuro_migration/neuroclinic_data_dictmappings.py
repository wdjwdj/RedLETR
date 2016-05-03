__author__ = 'dagutman'
"""This module simply contains all of the data dictionaries/mappings that I refer to in the base
neuro converter module--- this was split out to make the other code ... readable"""

Summary_sheet_data_dict = {'summary_cerad_tot_z_scr': 'I30', 'summary_veg_fl_dcd': 'M18',
                           'summary_wl_ret_z_scr': 'I24', 'summary_w_ir_t2_pcnt': 'K21',
                           'summary_veg_fl_rw_scr': 'C18', 'summary_cprx_dr_rw_scr': 'C29',
                           'summary_wmsr_ds_dcd': 'M31', 'summary_trails_a_dcd': 'M10', 'summary_ani_fl_rw_scr': 'C17',
                           'summary_w_ir_t1_z_scr': 'I20', 'summary_ex_wl_sc_scr': 'G36', 'summary_w_ir_t2_rw_scr': 'C21',
                           'summary_cerad_tscr_dcd': 'M30',
                           'summary_moca_z_scr': 'I9',
                           'summary_moca_rw_scr': 'C9',
                           'summary_tscr_fwd_dcd': 'M32', 'summary_bwd_dcd': 'M35',
                           'summary_bnt_dcd': 'M19',
                           'summary_clk_z_scr': 'I14', 'summary_trails_a_t_scr': 'E10',
                           'summary_trails_b_pcnt': 'K12',
                           'summary_trails_a_sc_scr': 'G10',
                           'summary_w_ir_t3_rw_scr': 'C22', 'summary_w_ir_t2_dcd': 'M21',
                           'summary_w_dr_pcnt': 'K23',
                           'summary_w_ir_t1_dcd': 'M20',  'summary_reyo_ir_rw_scr': 'C40',
                           'summary_w_ir_t1_pcnt': 'K20',
                           'summary_cprx_dr_dcd': 'M29', 'summary_cerad_tscr_pcnt': 'K30', 'summary_ex_wl_z_scr': 'I36',
                           'summary_trails_b_dcd': 'M12',
                           'summary_ani_fl_pcnt': 'K17', 'summary_trails_a_z_scr': 'I10', 'summary_moca_dcd': 'M9',
                           'summary_trails_b_rw_scr': 'C12',
                           'summary_reyo_ir_dcd': 'M40',
                           'summary_w_ir_t3_z_scr': 'I22',
                           'summary_reyo_cp_rw_scr': 'C39',
                           'summary_w_ir_t3_pcnt': 'K22',
                           'summary_fas_dcd': 'M15', 'summary_fas_z_scr': 'I15',
                           'summary_w_dr_dcd': 'M23',
                           'summary_ex_wl_rw_scr': 'C36',
                           'summary_trails_b_t_scr': 'E12',
                           'summary_cprx_ir_pcnt': 'K28',
                           'summary_cerad_tscr_rw_scr': 'C30',
                           'summary_reyo_dr_rw_scr': 'C41',
                           'summary_cprx_ir_rw_scr': 'C28',
                           'summary_trails_b_sc_scr': 'G12',
                           'summary_cor_y_pcnt': 'K25',
                           'summary_reyo_dr_dcd': 'M41', 'summary_gds_rw_scr': 'C37',
                           'summary_cprx_ir_z_scr': 'I28', 'summary_cor_y_z_scr': 'I25',
                           'summary_wmsr_ds_rw_scr': 'C31',
                           'summary_tscr_fwd_rw_scr': 'C32', 'summary_ex_wl_dcd': 'M36', 'summary_trails_a_pcnt': 'K10',
                           'summary_fas_pcnt': 'K15',
                           'summary_cor_no_dcd': 'M26',
                           'summary_w_prc_ret_rw_scr': 'C24', 'summary_dscrm_dcd': 'M27',
                           'summary_moca_pcnt': 'K9',
                           'summary_cor_no_z_scr': 'I26', 'summary_gds_dcd': 'M37',
                           'summary_bnt_rw_scr': 'C19',
                           'summary_ani_fl_dcd': 'M17',
                           'summary_w_ir_t2_z_scr': 'I21', 'summary_ani_fl_z_scr': 'I17',
                           'summary_clk_rw_scr': 'C14',
                           'summary_cor_y_rw_scr': 'C25',
                           'summary_clk_pcnt': 'K14',
                           'summary_fwd_dcd': 'M33',
                           'summary_trails_a_rw_scr': 'C10', 'summary_w_prc_ret_pcnt': 'K24',
                            'summary_trails_b_z_scr': 'I12',
                           'summary_fwd_rw_scr': 'C33', 'summary_w_prc_ret_dcd': 'M24', 'summary_bwd_rw_scr': 'C35',
                           'summary_dscrm_rw_scr': 'C27',
                           'summary_w_dr_rw_scr': 'C23',
                           'summary_tscr_bwkd_rw_scr': 'C34', 'summary_fas_t_scr': 'E15',
                           'summary_bnt_pcnt': 'K19', 'summary_w_ir_t3_dcd': 'M22',
                           'summary_ex_wl_pcnt': 'K36', 'summary_fas_rw_scr': 'C15',
                           'summary_ex_wl_t_scr': 'E36',
                           'summary_w_ir_t1_rw_scr': 'C20',
                           'summary_reyo_cp_dcd': 'M39',
                           'summary_tscr_bkwd_dcd': 'M34',
                           'summary_clk_dcd': 'M14', 'summary_cor_no_pcnt': 'K26',
                           'summary_cor_y_dcd': 'M25',
                           'summary_w_dr_z_scr': 'I23', 'summary_cor_no_rw_scr': 'C26',
                           'summary_bnt_z_scr': 'I19',
                           'summary_cprx_ir_dcd': 'M28'}

Summary_sheet_vars = {'MOCA Raw Score': 'C9', 'MOCA T-Score': 'E9', 'MOCA Scaled Score': 'G9', 'MOCA Z-Score': 'I9',
                      'MOCA %ile': 'K9', 'MOCA Did not Administer/Discontinued': 'M9',
                      'Trails A Raw Score': 'C10', 'Trails A T-Score': 'E10', 'Trails A Scaled Score': 'G10',
                      'Trails A Z-Score': 'I10',
                      'Trails A %ile': 'K10', 'Trails A Did not Administer/Discontinued': 'M10',
                      'Trails B Raw Score': 'C12', 'Trails B T-Score': 'E12', 'Trails B Scaled Score': 'G12',
                      'Trails B Z-Score': 'I12',
                      'Trails B %ile': 'K12', 'Trails B Did not Administer/Discontinued': 'M12',
                      'Clock Raw Score': 'C14', 'Clock T-Score': 'E14', 'Clock Scaled Score': 'G14',
                      'Clock Z-Score': 'I14',
                      'Clock %ile': 'K14', 'Clock Did not Administer/Discontinued': 'M14',
                      'FAS Raw Score': 'C15', 'FAS T-Score': 'E15', 'FAS Scaled Score': 'G15', 'FAS Z-Score': 'I15',
                      'FAS %ile': 'K15', 'FAS Did not Administer/Discontinued': 'M15',
                      'CERAD Raw Score': 'C16', 'CERAD T-Score': 'E16', 'CERAD Scaled Score': 'G16',
                      'CERAD Z-Score': 'I16',
                      'CERAD %ile': 'K16', 'CERAD Did not Administer/Discontinued': 'M16',
                      'Animal Fluency Raw Score': 'C17', 'Animal Fluency T-Score': 'E17',
                      'Animal Fluency Scaled Score': 'G17', 'Animal Fluency Z-Score': 'I17',
                      'Animal Fluency %ile': 'K17', 'Animal Fluency Did not Administer/Discontinued': 'M17',
                      'Vegetable Fluency Raw Score': 'C18', 'Vegetable Fluency T-Score': 'E18',
                      'Vegetable Fluency Scaled Score': 'G18', 'Vegetable Fluency Z-Score': 'I18',
                      'Vegetable Fluency %ile': 'K18', 'Vegetable Fluency Did not Administer/Discontinued': 'M18',
                      'BNT (15 item) Raw Score': 'C19', 'BNT (15 item) T-Score': 'E19',
                      'BNT (15 item) Scaled Score': 'G19', 'BNT (15 item) Z-Score': 'I19',
                      'BNT (15 item) %ile': 'K19', 'BNT (15 item) Did not Administer/Discontinued': 'M19',
                      'World List IR (Trial 1) Raw Score': 'C20', 'World List IR (Trial 1) T-Score': 'E20',
                      'World List IR (Trial 1) Scaled Score': 'G20', 'World List IR (Trial 1) Z-Score': 'I20',
                      'World List IR (Trial 1) %ile': 'K20',
                      'World List IR (Trial 1) Did not Administer/Discontinued': 'M20',
                      'World List IR (Trial 2) Raw Score': 'C21', 'World List IR (Trial 2) T-Score': 'E21',
                      'World List IR (Trial 2) Scaled Score': 'G21', 'World List IR (Trial 2) Z-Score': 'I21',
                      'World List IR (Trial 2) %ile': 'K21',
                      'World List IR (Trial 2) Did not Administer/Discontinued': 'M21',
                      'World List IR (Trial 3) Raw Score': 'C22', 'World List IR (Trial 3) T-Score': 'E22',
                      'World List IR (Trial 3) Scaled Score': 'G22', 'World List IR (Trial 3) Z-Score': 'I22',
                      'World List IR (Trial 3) %ile': 'K22',
                      'World List IR (Trial 3) Did not Administer/Discontinued': 'M22',
                      'World List DR Raw Score': 'C23', 'World List DR T-Score': 'E23',
                      'World List DR Scaled Score': 'G23', 'World List DR Z-Score': 'I23',
                      'World List DR %ile': 'K23', 'World List DR Did not Administer/Discontinued': 'M23',
                      'World List % Retention Raw Score': 'C24', 'World List % Retention T-Score': 'E24',
                      'World List % Retention Scaled Score': 'G24', 'World List % Retention Z-Score': 'I24',
                      'World List % Retention %ile': 'K24',
                      'World List % Retention Did not Administer/Discontinued': 'M24',
                      'Correct Yes Raw Score': 'C25', 'Correct Yes T-Score': 'E25', 'Correct Yes Scaled Score': 'G25',
                      'Correct Yes Z-Score': 'I25',
                      'Correct Yes %ile': 'K25', 'Correct Yes Did not Administer/Discontinued': 'M25',
                      'Correct No Raw Score': 'C26', 'Correct No T-Score': 'E26', 'Correct No Scaled Score': 'G26',
                      'Correct No Z-Score': 'I26',
                      'Correct No %ile': 'K26', 'Correct No Did not Administer/Discontinued': 'M26',
                      'Discrimination Raw Score': 'C27', 'Discrimination T-Score': 'E27',
                      'Discrimination Scaled Score': 'G27', 'Discrimination Z-Score': 'I27',
                      'Discrimination %ile': 'K27', 'Discrimination Did not Administer/Discontinued': 'M27',
                      'Const. Praxis IR Raw Score': 'C28', 'Const. Praxis IR T-Score': 'E28',
                      'Const. Praxis IR Scaled Score': 'G28', 'Const. Praxis IR Z-Score': 'I28',
                      'Const. Praxis IR %ile': 'K28', 'Const. Praxis IR Did not Administer/Discontinued': 'M28',
                      'Const. Praxis DR Raw Score': 'C29', 'Const. Praxis DR T-Score': 'E29',
                      'Const. Praxis DR Scaled Score': 'G29', 'Const. Praxis DR Z-Score': 'I29',
                      'Const. Praxis DR %ile': 'K29', 'Const. Praxis DR Did not Administer/Discontinued': 'M29',
                      'CERAD Total Score Raw Score': 'C30', 'CERAD Total Score T-Score': 'E30',
                      'CERAD Total Score Scaled Score': 'G30', 'CERAD Total Score Z-Score': 'I30',
                      'CERAD Total Score %ile': 'K30', 'CERAD Total Score Did not Administer/Discontinued': 'M30',
                      'WMS-R DS (Total Score) Raw Score': 'C31', 'WMS-R DS (Total Score) Raw T-Score': 'E31',
                      'WMS-R DS (Total Score) Raw Scaled Score': 'G31', 'WMS-R DS (Total Score) Raw Z-Score': 'I31',
                      'WMS-R DS (Total Score) Raw %ile': 'K31',
                      'WMS-R DS (Total Score) Raw Did not Administer/Discontinued': 'M31',
                      'Total Score Forward Raw Score': 'C32', 'Total Score Forward T-Score': 'E32',
                      'Total Score Forward Scaled Score': 'G32', 'Total Score Forward Z-Score': 'I32',
                      'Total Score Forward %ile': 'K32', 'Total Score Forward Did not Administer/Discontinued': 'M32',
                      'FWD Raw Score': 'C12', 'FWD T-Score': 'E12', 'FWD Scaled Score': 'G12', 'FWD Z-Score': 'I12',
                      'FWD %ile': 'K12', 'FWD Did not Administer/Discontinued': 'M12',
                      'Total Score Backward Raw Score': 'C12', 'Total Score Backward T-Score': 'E12',
                      'Total Score Backward Scaled Score': 'G12', 'Total Score Backward Z-Score': 'I12',
                      'Total Score Backward %ile': 'K12', 'Total Score Backward Did not Administer/Discontinued': 'M12',
                      'BWD Raw Score': 'C12', 'BWD T-Score': 'E12', 'BWD Scaled Score': 'G12', 'BWD Z-Score': 'I12',
                      'BWD %ile': 'K12', 'BWD Did not Administer/Discontinued': 'M12',
                      'Exception World List Raw Score': 'C12', 'Exception World List T-Score': 'E12',
                      'Exception World List Scaled Score': 'G12', 'Exception World List Z-Score': 'I12',
                      'Exception World List %ile': 'K12', 'Exception World List Did not Administer/Discontinued': 'M12',
                      'GDS (Short Form) Raw Score': 'C12', 'GDS (Short Form) T-Score': 'E12',
                      'GDS (Short Form) Scaled Score': 'G12', 'GDS (Short Form) Z-Score': 'I12',
                      'GDS (Short Form) %ile': 'K12', 'GDS (Short Form) Did not Administer/Discontinued': 'M12',
                      'Rey-O Raw Score': 'C12', 'Rey-O T-Score': 'E12', 'Rey-O Scaled Score': 'G12',
                      'Rey-O Z-Score': 'I12',
                      'Rey-O %ile': 'K12', 'Rey-O Did not Administer/Discontinued': 'M12',
                      'Rey-O Copy Raw Score': 'C12', 'Rey-O Copy T-Score': 'E12', 'Rey-O Copy Scaled Score': 'G12',
                      'Rey-O Copy Z-Score': 'I12',
                      'Rey-O Copy %ile': 'K12', 'Rey-O Copy Did not Administer/Discontinued': 'M12',
                      'Rey-O IR Raw Score': 'C12', 'Rey-O IR T-Score': 'E12', 'Rey-O IR Scaled Score': 'G12',
                      'Rey-O IR Z-Score': 'I12',
                      'Rey-O IR %ile': 'K12', 'Rey-O IR Did not Administer/Discontinued': 'M12',
                      'Rey-O DR Raw Score': 'C12', 'Rey-O DR T-Score': 'E12', 'Rey-O DR Scaled Score': 'G12',
                      'Rey-O DR Z-Score': 'I12',
                      'Rey-O DR %ile': 'K12', 'Rey-O DR Did not Administer/Discontinued': 'M12',
}


MOCA_test_form_data_dict = {'Alternating Trail Making Score': 'B18', 'Visuoconstructional Skills (Cube)': 'B32',
                            'Visuoconstructional Skills (Clock) Contour': 'D50',
                            'Visuoconstructional Skills (Clock) Numbers': 'D51',
                            'Visuoconstructional Skills (Clock) Hands': 'D52',
                            'Visuoconstructional Skills (Clock) Total points': 'D53', 'Naming Lion Score': 'D66',
                            'Naming Lion Intrusions': 'E66',
                            'Naming Rhino Score': 'D67', 'Naming Rhino Intrusion': 'E67', 'Naming Camel Score': 'D68',
                            'Naming Camel Intrusion': 'E68',
                            'Naming Total Points': 'D50'}

MOCA_vars = {'moca_trail_scr': 'B18', 'moca_cube_scr': 'B32', 'moca_clock_contour': 'D50',
                       'moca_clock_numbers': 'D51', 'moca_clock_hands': 'D52',
                       'moca_clock_tot': 'D53', 'moca_naming_lion_scr': 'D66', 'moca_naming_lion_int': 'E66',
                       'moca_naming_rhino_scr': 'D67', 'moca_naming_rhino_int': 'E67', 'moca_naming_camel_scr': 'D68',
                       'moca_naming_camel_int': 'E68',
                       'moca_naming_tot': 'D50'}


""" The DIGIT SPAN TEST"""


Digit_span_vars = {'ds_fd_t1_1_resp': 'B17', 'ds_fd_t1_1_scr': 'C17', 'ds_fd_t1_2_resp': 'B18',
                   'ds_fd_t1_2_scr': 'C18',
                   'ds_fd_t1_3_resp': 'B19', 'ds_fd_t1_3_scr': 'C19', 'ds_fd_t1_4_resp': 'B20',
                   'ds_fd_t1_4_scr': 'C20', 'ds_fd_t1_5_resp': 'B21',
                   'ds_fd_t1_5_scr': 'C21', 'ds_fd_t1_6_resp': 'B22', 'ds_fd_t1_6_scr': 'C22',
                   'ds_fd_t2_1_resp': 'E17',
                   'ds_fd_t2_1_scr': 'F17', 'ds_fd_t2_2_resp': 'E18', 'ds_fd_t2_2_scr': 'F18',
                   'ds_fd_t2_3_resp': 'E19', 'ds_fd_t2_3_scr': 'F19',
                   'ds_fd_t2_4_resp': 'E20', 'ds_fd_t2_4_scr': 'F20', 'ds_fd_t2_5_resp': 'E21',
                   'ds_fd_t2_5_scr': 'F21', 'ds_fd_t2_6_resp': 'E22',
                   'ds_fd_t2_6_scr': 'F22', 'ds_rd_t1_1_resp': 'B27', 'ds_rd_t1_1_scr': 'C27',
                   'ds_rd_t1_2_resp': 'B28', 'ds_rd_t1_2_scr': 'C28',
                   'ds_rd_t1_3_resp': 'B29', 'ds_rd_t1_3_scr': 'C29', 'ds_rd_t1_4_resp': 'B30',
                   'ds_rd_t1_4_scr': 'C30', 'ds_rd_t1_5_resp': 'B31',
                   'ds_rd_t1_5_scr': 'C31', 'ds_rd_t1_6_resp': 'B32', 'ds_rd_t1_6_scr': 'C32',
                   'ds_rd_t2_1_resp': 'E27', 'ds_rd_t2_1_scr': 'F27',
                   'ds_rd_t2_2_resp': 'E28', 'ds_rd_t2_2_scr': 'F28', 'ds_rd_t2_3_resp': 'E29',
                   'ds_rd_t2_3_scr': 'F29', 'ds_rd_t2_4_resp': 'E30',
                   'ds_rd_t2_4_scr': 'F30', 'ds_rd_t2_5_resp': 'E31', 'ds_rd_t2_5_scr': 'F31',
                   'ds_rd_t2_6_resp': 'E32', 'ds_rd_t2_6_scr': 'F32',
                   'ds_fd_total': 'I21', 'ds_fd_span': 'I22', 'ds_rd_total': 'I31', 'ds_rd_span': 'I32'
}



Clock_vars = {'np_clock_rpt_time': 'B6', 'np_clock_q1': 'B10', 'np_clock_arabnum_q2': 'B11', 'np_clock_ordnum_q3': 'B12',
              'np_clock_norot_q4': 'B13',
              'np_clock_numpos_q5': 'B14', 'np_clock_numcirc_q6': 'B15', 'np_clock_twohands_q7': 'B19', 'np_clock_hourtarg_q8': 'B20',
              'np_clock_minute_q9': 'B21',
              'np_clock_center_q10': 'B22', 'np_clock_noextra_q11': 'B24', 'np_clock_joinhand_q12': 'B25', 'np_clock_center_q13': 'B29',
              'np_clock_total': 'C31'
}

"""This one is written differently... and requires a bit more finessing as it is a data dictionary which has a list
as its input... so there's a umber of arguably confusing transformations I had to do in order to actually use the data
but I still think this was the cleanest way to do it as this is a one-to-many example"""

FAS_vars = {
    'fas_f_1': ['B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18'],
    'fas_f_2': ['B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25'],
    'fas_f_3': ['B26', 'B27', 'B28', 'B29', 'B30', 'B31', 'B32', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32'],
    'fas_f_4': ['B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39'],
    'fas_f_tot': ['B40'],
    'fas_a_1': ['F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18'],
    'fas_a_2': ['F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25'],
    'fas_a_3': ['F26', 'F27', 'F28', 'F29', 'F30', 'F31', 'F32', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
    'fas_a_4': ['F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F39', 'G33', 'G34', 'G35', 'G36', 'G37', 'G38', 'G39'],
    'fas_a_tot': ['F40'],
    'fas_s_1': ['J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18'],
    'fas_s_2': ['J19', 'J20', 'J21', 'J22', 'J23', 'J24', 'J25', 'K19', 'K20', 'K21', 'K22', 'K23', 'K24', 'K25'],
    'fas_s_3': ['J26', 'J27', 'J28', 'J29', 'J30', 'J31', 'J32', 'K26', 'K27', 'K28', 'K29', 'K30', 'K31', 'K32'],
    'fas_s_4': ['J33', 'J34', 'J35', 'J36', 'J37', 'J38', 'J39', 'K33', 'K34', 'K35', 'K36', 'K37', 'K38', 'K39'],
    'fas_s_tot': ['J40'],
    'fas_tot': ['C44']
}



CERAD_animal_veg_fluency_vars = {
    'avf_anm1': ['F41', 'F42', 'F43', 'F44', 'F45', 'F46', 'F47', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47'],
    'avf_anm2': ['F48', 'F49', 'F50', 'F51', 'F52', 'F53', 'F54', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54'],
    'avf_anm3': ['F55', 'F56', 'F57', 'F58', 'F59', 'F60', 'F61', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'G61'],
    'avf_anm4': ['F62', 'F63', 'F64', 'F65', 'F66', 'F67', 'F68', 'G62', 'G63', 'G64', 'G65', 'G66', 'G67', 'G68'],
    'avf_anm_tot': 'F73',
    'avf_veg1': ['J41', 'J42', 'J43', 'J44', 'J45', 'J46', 'J47', 'K41', 'K42', 'K43', 'K44', 'K45', 'K46', 'K47'],
    'avf_veg2': ['J48', 'J49', 'J50', 'J51', 'J52', 'J53', 'J54', 'K48', 'K49', 'K50', 'K51', 'K52', 'K53', 'K54'],
    'avf_veg3': ['J55', 'J56', 'J57', 'J58', 'J59', 'J60', 'J61', 'K55', 'K56', 'K57', 'K58', 'K59', 'K60', 'K61'],
    'avf_veg4': ['J62', 'J63', 'J64', 'J65', 'J66', 'J67', 'J68', 'K62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68'],
    'avf_veg_tot': 'K73'
}

CERAD_15_Item_BNT_vars = {
    'cerad15bnt_tree_resp': 'B26', 'cerad15bnt_tree_scr': 'E26', 'cerad15bnt_bed_resp': 'B27', 'cerad15bnt_bed_scr': 'E27',
    'cerad15bnt_whistle_resp': 'B28', 'cerad15bnt_whistle_scr': 'E28', 'cerad15bnt_flower_resp': 'B29',
    'cerad15bnt_flower_scr': 'E29',
    'cerad15bnt_house_resp': 'B30', 'cerad15bnt_house_scr': 'E30', 'cerad15bnt_canoe_resp': 'B32',
    'cerad15bnt_canoe_scr': 'E32',
    'cerad15bnt_tooth_resp': 'B33', 'cerad15bnt_tooth_scr': 'E33', 'cerad15bnt_volcano_resp': 'B34',
    'cerad15bnt_volcano_scr': 'E34',
    'cerad15bnt_mask_resp': 'B35', 'cerad15bnt_mask_scr': 'E35', 'cerad15bnt_camel_resp': 'B36',
    'cerad15bnt_camel_scr': 'E36',
    'cerad15bnt_harm_resp': 'B38', 'cerad15bnt_harm_scr': 'E38', 'cerad15bnt_tongs_resp': 'B39',
    'cerad15bnt_tongs_scr': 'E39',
    'cerad15bnt_hamm_resp': 'B40', 'cerad15bnt_hamm_scr': 'E40', 'cerad15bnt_funnel_resp': 'B41',
    'cerad15bnt_funnel_scr': 'E241',
    'cerad15bnt_domin_resp': 'B42', 'cerad15bnt_domin_scr': 'E42', 'cerad15bnt_tot': 'B44'
}


"""
This is a confusing aspect of REDCap--- when you use a datamatrix it prepends either a __1 or a __2 or __3 etc.. depending on what column the variable represents
in the data matrix... doing this mapping really has to be done by looking at the UI itself
"""

CERAD_Constructional_Praxis_vars = {
    'ccp_circle_1___1': 'H22', 'ccp_circle_1___2': 'I22', 'ccp_circle_2___1': 'H23', 'ccp_circle_2___2': 'I23', 'ccp_diamond_1___1': 'H26', 'ccp_diamond_1___2': 'I26',
    'ccp_diamond_2___1': 'H27', 'ccp_diamond_2___2': 'I27', 'ccp_diamond_3___1': 'H28', 'ccp_diamond_3___2': 'I28', 'ccp_rectangles_1___1': 'H31', 'ccp_rectangles_1___2': 'I31',
    'ccp_rectangles_2___1': 'H32', 'ccp_rectangles_2___2': 'I32', 'ccp_cube_1___1': 'H35', 'ccp_cube_1___2': 'I35', 'ccp_cube_2___1': 'H36', 'ccp_cube_2___2': 'I36',
    'ccp_cube_3___1': 'H37', 'ccp_cube_3___2': 'I37', 'ccp_cube_4___1': 'H38', 'ccp_cube_4___2': 'I38', 'ccp_ir_total': 'H40',
    'ccp_dr_total': 'I40'
}

CERAD_Word_List_datadict = {
    'cwl_wlr_chur': 'B51', 'cwl_wlr_coff': 'B52', 'cwl_wlr_butt': 'B53', 'cwl_wlr_doll': 'B54', 'cwl_wlr_arm': 'B55',
    'cwl_wlr_shor': 'B56',
    'cwl_wlr_five': 'B57', 'cwl_wlr_lett': 'B58', 'cwl_wlr_hote': 'B59', 'cwl_wlr_moun': 'B60', 'cwl_wlr_quee': 'B61',
    'cwl_wlr_cabi': 'B62',
    'cwl_wlr_slip': 'B63', 'cwl_wlr_pole': 'B64', 'cwl_wlr_vill': 'B65', 'cwl_wlr_stri': 'B66', 'cwl_wlr_tick': 'B67',
    'cwl_wlr_troo': 'B68',
    'cwl_wlr_gras': 'B69', 'cwl_wlr_engi': 'B70', 'cwl_wlr_yes': 'B72', 'cwl_wlr_no': 'B73', 'cwl_wlr_falspos': 'B74'
}

## Geriatric depression scale
GDS_datadict = {
    'gdss_1': 'B9', 'gdss_2': 'B10', 'gdss_3': 'B11', 'gdss_4': 'B12', 'gdss_5': 'B13', 'gdss_6': 'B14',
    'gdss_7': 'B15', 'gdss_8': 'B16', 'gdss_9': 'B17', 'gdss_10': 'B18', 'gdss_11': 'B19', 'gdss_12': 'B20',
    'gdss_13': 'B21', 'gdss_14': 'B22', 'gdss_15': 'B23'
}

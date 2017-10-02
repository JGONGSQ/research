#!/usr/bin/python

INPUT_DIR_PATH = '../Data/input_files'

COMPULSORY_FIELDS = ['id', 'uno', 'sero', 'NUMSTOP', 'PATH']
STATE_LISTS = ['NSW', 'VIC', 'QLD', 'SA', 'TAS', 'NT']
STATE_CODES = ['1', '2', '3', '4', '6', '8']
DISTANCE_DESTINATION_LIST = ['DISTANCE_TO_NSW', 'DISTANCE_TO_VIC', 'DISTANCE_TO_QLD', 'DISTANCE_TO_SA', 'DISTANCE_TO_TAS', 'DISTANCE_TO_NT']


RESULTS_PATH = '../Data/results/ivs'


PARTYPE_LIST = ['PARTYPE_UNACCOMPANIED', 'PARTYPE_ADULT_COUPLE', 'PARTYPE_FAMILY_GROUP', 'PARTYPE_FREIEND_RELATIVES', 'PARTYPE_BUSINESS_ASSOCIATES', 'PARTYPE_SCHOOL_TOUR']
PARTYPE_CODE = [['1'], ['2'], ['3'], ['4'], ['5'], ['6']]


GROUPTYPE_LIST = ['GROUPTYPE_SPORTING', 'GROUPTYPE_SPECIAL_INTEREST', 'GROUPTYPE_GUIDED_HOLIDAY', 'GROUPTYPE_BUSINESS_OR_CONVENTION', 'GROUPTYPE_OTHER', 'PARTYPE_SCHOOL_EXCURSION']
GROUPTYPE_CODE = [['1'], ['2'], ['3'], ['4'], ['5', '8'], ['6']]

TRIP_PURPOSE_LIST = ['TRIP_PURPOSE_HOLIDAY', 'TRIP_PURPOSE_VISITING_FR', 'TRIP_PURPOSE_BUSINESS', 'TRIP_PURPOSE_EMPLOYMENT', 'TRIP_PURPOSE_EDUCATION', 'TRIP_PURPOSE_OTHER']
TRIP_PURPOSE_CODE = [['1'], ['2'], ['3', '4'], ['5'], ['6'], [str(x) for x in range(7, 99)]]

CUSTOMS_LIST = ['CUSTOMS_ENTRY_NSW', 'CUSTOMS_ENTRY_VIC', 'CUSTOMS_ENTRY_QLD', 'CUSTOMS_ENTRY_SA', 'CUSTOMS_ENTRY_TAS', 'CUSTOMS_ENTRY_NT', 'CUSTOMS_ENTRY_OTHER']
CUSTOMS_CODE = [['1'], ['2'], ['3', '7', '8', '11'], ['5'], ['9'], ['6'], ['4', '10', '98']]

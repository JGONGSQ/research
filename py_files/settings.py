# Path
# DEFAULT_PATH = '/Users/James/Desktop/master_project'

# File
### csv ###
# INPUT_DATA_FILE = '../Data/NVS2007.csv'
INPUT_DIR_PATH = '../Data/input_files'
TEST_INPUT_FILE_PATH = '../r_resources/Model_Estimation/az_hhld_vfc_cleaned_final.csv'

# NEW ADDED DATA FILE
TEST_INPUT_DATA_PATH = '../Data/NVS2007unit.csv'
TEST_OUTPUT_DATA_PATH = '../Data/test_output_file.csv'

RESULTS_PATH = '../Data/results'

### R scripts ###
TEST_R_SCRIPT_FILE = 'r_files/runner.r'
R_MDCEV_SCRIPT = 'r_files/MDCEV.r'

RUNNER_MDCEV = 'r_files/runner_mdcev_nooutside.r'

# Constants
# NUMBER_OF_DATA_NEEDED = 200
NUMBER_OF_DATA_NEEDED = 40000
NUMBER_OF_OUTSIDE_GOODS = 1

# Fields list
PREFIX = ['REGN', 'NITES']

COMPULSORY_FIELDS = ['id', 'uno', 'sero', 'NUMSTOP']

CITY_LISTS = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Hobart', 'Darwin']
CITY_CODES = ['104', '201', '302', '404', '601', '801']

STATE_LISTS = ['NSW', 'VIC', 'QLD', 'SA', 'TAS', 'NT']
STATE_CODES = ['1', '2', '3', '4', '6', '8']


ALL_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'PARENT', 'YOUNGEST',
                 'AGEGROUP', 'CH15TO24', 'GENDER', 'MARITAL', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE']

UTILITY_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE', 'OVER15']
# 'GENDER']
# 'CH15TO24'  'YOUNGEST' PARENT
Removed_list = ['PARENT', 'GENDER']


EXECLUDE_VARIABLE_1 = []
EXECLUDE_VARIABLE_4 = ['YOUNGEST', 'PARENT', 'HOMESUPP', 'HOMESLA', 'HOMEREGN']
EXECLUDE_VARIABLE_7 = []

# ORIGIN GROUP
ORIGIN_LIST = ['ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'ORIGIN_NT', 'ORIGIN_ACT']
ORIGIN_CODE = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10'], ['11'], ['12'], ['13']]

PARENT_LIST = ['PARENT_YES', 'PARENT_NO', 'PARENT_DONT_KNOW']
PARENT_CODE = [['1'], ['0', '2'], ['9']]

YOUNGEST_LIST = ['YOUNGEST_ZERO_TO_FIVE', 'YOUNGEST_SIZX_TO_TEN', 'YOUNGEST_ELEVEN_TO_FOURTEEN', 'YOUNGEST_DONT_KNOW']
YOUNGEST_CODE = [['1'], ['3'], ['4'], ['9']]

CH15TO24_LIST = ['CH15TO24_YES', 'CH15TO24_NO', 'CH15TO24_DONT_KNOW']
CH15TO24_CODE = [['1'], ['0', '2'], ['9']]

GENDER_LIST = ['GENDER_MALE', 'GENDER_FEMALE']
GENDER_CODE = [['1'], ['2']]

MARITAL_LIST = ['MARITAL_SINGLE', 'MARITAL_COUPLE', 'MARITAL_REFUSED']
MARITAL_CODE = [['1'], ['2'], ['9']]

EMPLOYMENT_LIST = ['EMPLOYMENT_WORKING', 'EMPLOYMENT_NOT_WORKING', 'EMPLOYMENT_RETIRED', 'EMPLOYMENT_STUDYING', 'EMPLOYMENT_DONT_KNOW']
EMPLOYMENT_CODE = [['1', '2', '5'], ['3'], ['4'], ['6'], ['7', '8', '9']]

HOUSINC_LIST = ['HOUSINC_LOW', 'HOUSINC_MEDIUM', 'HOUSINC_HIGH', 'HOUSINC_DONT_KONW']
HOUSINC_CODE = [['1', '2', '3', '4', '5'], ['6', '7', '8', '9'], ['11', '12'], ['10', '13', '99', '25', '28', '29']]

LIFECYCLE_LIST = ['LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'LIFECYCLE_COUPLE_WITH_KIDS', 'LIFECYCLE_DONT_KNOW']
LIFECYCLE_CODE = [['1', '2', '3', '8', '9'], ['4', '10', '11'], ['5', '6', '7'], ['0']]

AGEGROUP_LIST = ['AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69', 'AGEGROUP_70+']
AGEGROUP_CODE = [['1', '2', '3'], ['4', '5'], ['6', '7'], ['8', '9'], ['10', '11'], ['12']]



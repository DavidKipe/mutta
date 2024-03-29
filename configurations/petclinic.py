
config_name = "SpringBoot PetClinic"

# -- configuration -- #

# Application (SUT) config #
app_root_dir = '/home/david/IdeaProjects/spring-petclinic-mutation'    # root directory of the application (all paths of app are relative to this)

backup_ext = '.bak'						# this string will be appended to the original filename
orig_line_tag = ' // original line'		# this string will be appended to the original commented line
mutate_line_tag = ' // mutated line'    # this string will be appended to the mutated line
indentation_format = '\t'				# could be either '\t' (tab) or ' ' (*one* space)

source_paths = ['src/main/java']    # directories of the source code in the app root dir

mutants_dir = 'mutants'             # directory name where the mutated files will be saved inside the app root dir

command_path_run = ''    # path relative for the run command (optional)
command_app_run = 'mvn spring-javaformat:apply spring-boot:run -B'  # command to run application
app_ready_stdout_signal = "Started PetClinicApplication in"         # what the application write on stdout when is ready
app_shutdown_stdout_signal = "Shutdown completed"                   # what the application write on shutdown completed

command_app_reset = ''     # this command will be run to reset the app to the initial state (optional)
#  #

# Mutation info # (path relative to root of this tool)
input_pit_xml_report_filename = 'resources/mutations_petclinic.xml'     # input file from PIT
output_mut_infos_json_filename = 'resources/mutations_petclinic.json'    # generated file by this tool

mutants_to_skip = [13, 33, 34, 49, 51, 55, 59, 73, 76, 88, 104, 105, 106]    # list of ids of the mutants to be skipped

#  #

# Information about test suites #
# all fields are mandatory
# name: full name of the test suite
# tag: short name of the test suite
# root_dir: root directory of the test suite project
# mvn_opts: options to insert in the Maven command
#   command = 'mvn {mvn_opts} surefire-report:report test -B'
test_suites = [
	{
		'name': 'Selenium assertions',
		'tag': 'assertions',
		'root_dir': '/home/david/IdeaProjects/petclinic-test-suite',
		'mvn_opts': '-Dtest="assertions.**" -Djava.awt.headless=true'
	},
	{
		'name': 'ReTest Recheck explicit check',
		'tag': 'retest_explicit',
		'root_dir': '/home/david/IdeaProjects/petclinic-test-suite',
		'mvn_opts': '-Dtest="recheck.explicit.**" -Djava.awt.headless=true'
	},
	{
		'name': 'ReTest Recheck implicit check',
		'tag': 'retest_implicit',
		'root_dir': '/home/david/IdeaProjects/petclinic-test-suite',
		'mvn_opts': '-Dtest="recheck.implicit.**" -Djava.awt.headless=true'
	}
]

surefire_reports_subdir = 'target/surefire-reports'     # relative location of surefire reports
#  #

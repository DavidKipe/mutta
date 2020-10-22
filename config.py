
## configurations ##

pit_xml_report_filename = 'resources/mutations.xml'
mut_infos_json_filename = 'resources/mutations.json'

app_rootdir = '/home/david/IdeaProjects/spring-petclinic-mutation/'    # root directory of the application
testsuite_assertions_rootdir = '/home/david/IdeaProjects/petclinic-test-suite/'
testsuite_retest_expl_rootdir = '/home/david/IdeaProjects/petclinic-test-suite/'
testsuite_retest_impl_rootdir = '/home/david/IdeaProjects/petclinic-test-suite/'

backup_ext = '.bak'						# this string will be appened to the original filename
orig_line_tag = ' // original line'		# this string will be appened to the original commented line
mutate_line_tag = ' // mutated line'    # this string will be appened to the mutated line
indentation_format = '\t'				# could be either '\t' (tab) or ' ' (*one* space)

# derived
source_rootdir = app_rootdir + 'src/main/java/' # root directory of the source code
target_dir = app_rootdir + 'target/'            # target directory of the project
mutants_dir = app_rootdir + 'mutants/'          # directory of the mutant files inside the root app dir
#

run_app_command = 'mvn spring-javaformat:apply spring-boot:run -B'
app_ready_stdout_signal = "Started PetClinicApplication in"

# must be only Maven commands
run_testsuite_assertions_command = 'mvn -Dtest="assertions.**" -Djava.awt.headless=true test -B'
run_testsuite_retest_expl_command = 'mvn -Dtest="recheck.explicit.**" -Djava.awt.headless=true test -B'
run_testsuite_retest_impl_command = 'mvn -Dtest="recheck.implicit.**" -Djava.awt.headless=true test -B'

##  ##

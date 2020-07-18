from behave import __main__ as runner_as_options
import sys
import os

if __name__ == '__main__':
    sys.stdout.flush()
    featureFilePath = 'FeaturesFiles'
    tagList = ' --tags=all' # it will run only regression scenarios
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o reporting_folder_json'
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    featureFileFolder = 'reporting_folder_json'
    reportdir = os.getcwd() + '\\' + "reporting_folder_json"
    singleline = featureFilePath+tagList+reportingRelated+commonRunnerOptions
    runner_as_options.main(singleline)

    os.system('cmd /c "allure serve "'+reportdir)

# jko-auto-test
for jko login API auto test

# Project Set up
run
`git clone https://github.com/remember-improvement/jko-auto-test.git`

# Env Set up
run
`cd jko-auto-test/jkoproject`
`pip install -r requirements`
    * for MacOs 
    run
    `brew install allure`
    * for windows
    Download allure-commandline from https://github.com/allure-framework/allure2/releases and set {your_path}/allure-{download-version}\allure-{download-version}\bin to System Environment PATH

# Start Django Login Server
run
`cd jko-auto-test/jkoproject`
`python manage.py runserver`

# Execute pytest test case and generate report
run
`pytest --clean-alluredir --alluredir=./report test_login.py`

# Display allure test report
run
`allure serve ./report`

    
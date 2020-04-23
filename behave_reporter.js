var reporter = require('cucumber-html-reporter');

var options = {
        theme: 'bootstrap',
        jsonFile: 'reports/behave/cucumber.json',
        output: 'reports/behave/test_report.html',
        reportSuiteAsScenarios: true,
        launchReport: false,
        metadata: {
            "Version": "0.0.1",
            "Test Environment": "TEST"
        }
    };

    reporter.generate(options);

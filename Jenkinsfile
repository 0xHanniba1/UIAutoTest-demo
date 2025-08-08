pipeline {
    agent any

    stages {
        stage('运行测试') {
            steps {
                echo '执行自动化测试...'
                sh 'python3 -m pytest --alluredir=reports/allure-results --clean-alluredir'
            }
        }
    }

    post {
        always {
            echo '发布测试报告'
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'reports/allure-results']]
            ])
        }
    }
}
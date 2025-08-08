pipeline {
    agent any

    stages {
        stage('运行测试') {
            steps {
                echo '清理旧报告并执行测试...'
                sh '''
                    cd ${WORKSPACE}
                    rm -rf reports/allure-results
                    source venv/bin/activate
                    python -m pytest --alluredir=reports/allure-results
                '''
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
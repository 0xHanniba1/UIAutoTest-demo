pipeline {
    agent any

    stages {
        stage('运行测试') {
            steps {
                echo '激活虚拟环境并执行测试...'
                sh '''
                    cd ${WORKSPACE}
                    source venv/bin/activate
                    python -m pytest --alluredir=allure-results --clean-alluredir
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
                results: [[path: 'allure-results']]
            ])
        }
    }
}
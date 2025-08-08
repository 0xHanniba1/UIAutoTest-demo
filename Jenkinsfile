pipeline {
    agent any

    stages {
        stage('环境准备') {
            steps {
                echo '开始准备测试环境...'
                // 安装依赖
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('运行测试') {
            steps {
                echo '开始执行自动化测试...'
                sh 'python3 -m pytest --alluredir=reports/allure-results'
            }
        }
    }

    post {
        always {
            echo '测试执行完成'
            // 发布 Allure 报告
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
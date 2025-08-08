pipeline {
    agent any

    stages {
        stage('环境准备') {
            steps {
                echo '检查并安装依赖...'
                script {
                    // 检查是否已存在虚拟环境
                    if (!fileExists('venv')) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
                        '''
                    } else {
                        echo '虚拟环境已存在，跳过安装'
                    }
                }
            }
        }

        stage('运行测试') {
            steps {
                echo '执行自动化测试...'
                sh '''
                    . venv/bin/activate
                    python -m pytest --alluredir=reports/allure-results --clean-alluredir
                '''
            }
        }
    }

    post {
        always {
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
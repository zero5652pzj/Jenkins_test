pipeline {
   agent any
   parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        string(name: 'PYTHON', defaultValue: 'Mr Eric', description: 'How can i output?')
    }
   stages {
        stage('构建') {
           steps {
                echo 'Ready to ping baidu...'
                bat 'ping baidu.com'
               timeout(time: 1,unit:'MINUTES') {
                   bat 'E:/pause.bat'
               }
               }
        }
        stage('部署') {
            steps {
                echo 'Step two'
                echo '%BUILD_NUMBER%'
            }
        }
        stage('测试') {
            steps {
                bat 'java -version'
            }
        }
        stage('Example') {
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
                }
            }
            steps {
                echo "Hello, ${PERSON}, nice to meet you."
            }
        }
    }
    
    post {
        always {
            echo 'This is always run'
        }
        success {
            echo 'This is success run'
        }
        failure {
            echo 'This is failure run'
        }
        unstable {
            echo 'This is unstable run'
        }
        changed {
            echo 'This is changed run'
        }
    }
}
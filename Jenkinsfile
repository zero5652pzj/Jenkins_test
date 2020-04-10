pipeline {
   agent any
   parameters {
   	    choice(
   	    	    name: "deploy_env",
   	    	    choices: "dev\nmaster"
   	    	    descriptions: "This is github&Jenkinfile"
   	    	)
        string(name: 'version', defaultValue: '1.0.0', description: 'Choose the version:')
    }
   stages {
        stage('Build') {
           steps {
                echo 'Ready to ping baidu...'
                bat 'ping baidu.com'
                timeout(time: 1,unit:'MINUTES') {
                bat 'E:/pause.bat'
               }
            steps {
            	echo '%env.WORKSPACE%'
            }
            }
            }
        }
        stage('CD') {
            steps {
                echo 'Step two'
                echo '%BUILD_NUMBER%'
            }
        }
        stage('Testing') {
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
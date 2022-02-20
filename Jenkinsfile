pipeline {
    agent any

    stages {
        stage('build python') {
            steps {
              sh 'python app.py'
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
     
    }
} 

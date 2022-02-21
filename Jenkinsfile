pipeline {
  agent {
    docker { image 'python:latest' }
  }
  stages {
    stage('Test python version') {
      steps {
        sh 'python3 --version'
      }
    }
    
    stage('Compile Application') {
            steps {
                sh "python app.py"
            }
        }
    
    stage('deploy application') {
            steps {
                echo "aplicacion lanzada"
            }
        }
  }
}

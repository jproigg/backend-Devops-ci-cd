pipeline {
  agent {
    label "Linux"
  }
  environment {
      registry = "jproigg/backend-devops-ci-cd"
      registryCredential = 'dockerhub'
      dockerImage = ''
  }

  stages {
    stage('docker version') {
      steps {
        sh 'docker ps'
      }
    }

    stage('compile application and install dependencies') {
      agent { dockerfile true }
      steps {
        echo 'success'
      }
    }

     stage('build docker image') {
        agent any
        steps {
            script {
                dockerImage = docker.build registry
            }
        }
    }

     stage('push to docker hub') {
        agent any
        steps{    
            script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
            }
        }
     }
  }
}

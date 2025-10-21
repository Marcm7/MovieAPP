pipeline {
  agent any

  triggers {
    pollSCM('H/2 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        git branch: 'main', url: 'https://github.com/Marcm7/MovieAPP.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        sh '''
          eval $(minikube docker-env)
          docker build -t videostore:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml
          kubectl rollout status deployment/videostore-deployment
        '''
      }
    }
  }
}

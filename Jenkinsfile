pipeline {
  agent any

  // Make Homebrew + default bins visible to Jenkins
  environment {
    PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
  }

  // Optional: auto-build every 2 minutes on new commits
  triggers { pollSCM('H/2 * * * *') }

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
          # Point Docker CLI at Minikube’s dockerd
          eval "$(minikube docker-env)"

          # Sanity prints (visible in Console Output)
          which docker && docker version --format '{{.Server.Version}}'
          which kubectl && kubectl version --client=true --output=yaml
          which minikube && minikube version

          # Build image inside Minikube
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

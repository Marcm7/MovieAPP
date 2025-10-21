pipeline {
  agent any

  // Make sure Jenkins can find brew-installed tools on macOS
  environment {
    PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
  }

  // Auto-check GitHub every 2 minutes
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
          set -euo pipefail

          echo ">> Pointing Docker CLI to Minikube dockerd"
          eval "$(minikube docker-env)"

          echo ">> Tool versions"
          which docker && docker version --format '{{.Server.Version}}' || true
          which kubectl && kubectl version --client --output=yaml || true
          which minikube && minikube version || true

          echo ">> Compute image tag (short Git SHA)"
          GIT_SHA="$(git rev-parse --short HEAD)"
          echo "$GIT_SHA" > .gitsha
          echo "TAG=$GIT_SHA"

          echo ">> Build image videostore:${GIT_SHA}"
          docker build -t videostore:${GIT_SHA} .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
          set -euo pipefail

          GIT_SHA="$(cat .gitsha)"
          echo ">> Using tag videostore:${GIT_SHA}"

          echo ">> Ensure manifests exist in cluster (idempotent)"
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml

          echo ">> Determine container name from deployment"
          DEPLOY="videostore-deployment"
          CONTAINER="$(kubectl get deploy ${DEPLOY} -o jsonpath='{.spec.template.spec.containers[0].name}')"
          echo "Container=${CONTAINER}"

          echo ">> Update deployment to new image"
          kubectl set image deployment/${DEPLOY} ${CONTAINER}=videostore:${GIT_SHA}

          echo ">> Wait for rollout"
          kubectl rollout status deployment/${DEPLOY}
        '''
      }
    }
  }
}

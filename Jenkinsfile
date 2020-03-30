#!groovy
import groovy.json.JsonBuilder

def attachmentPayload = [[
    fallback: "execution #${env.BUILD_NUMBER}",
    color: "#2eb886",
    pretext: "${env.JOB_NAME}",
    text: "TEST DONE #${env.BUILD_NUMBER}",
]]

pipeline {
    agent {
        docker { image 'cutem/python-build' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }
    post {
        always {
            echo 'TEST DONE'
            script {// ここだけscripted pipeline のsyntaxを適用する
                slackSend(channel: '#sugaya_github_bot', color: "#2eb886", attachments: new JsonBuilder(attachmentPayload).toString())
            }
        }
    }
}

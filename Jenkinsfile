#!groovy
import groovy.json.JsonBuilder

def successPayload = [[
    fallback: "${env.JOB_NAME} #${env.BUILD_NUMBER}",
    text: "TEST SUCCESS #${env.BUILD_NUMBER} ${env.BUILD_URL}",
]]

def failedPayload = [[
    fallback: "${env.JOB_NAME} #${env.BUILD_NUMBER}",
    text: "TEST FAILED #${env.BUILD_NUMBER} ${env.BUILD_URL}",
]]

pipeline {
    agent none
    stages {
        stage('SetUp') {
            agent {
                label 'master'
            }
            steps {
                sh 'docker build -t cutem/python-build .'
            }
        }
        stage('Test') {
            agent {
                docker { image 'cutem/python-build' }
            }
            steps {
                script {
                    try {
                        sh 'python3 discover.py'
                        currentBuild.result = 'FAILURE'
                    } catch (err) {
                        echo "Failed: ${err}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
    post {
        success {
            script {// ここだけscripted pipeline のsyntaxを適用する
                slackSend(channel: '#sugaya_github_bot', color: "#2eb886", attachments: new JsonBuilder(successPayload).toString())
            }
        }
        failure {
            script {// ここだけscripted pipeline のsyntaxを適用する
                slackSend(channel: '#sugaya_github_bot', color: "#FF0000", attachments: new JsonBuilder(failedPayload).toString())
            }
        }
    }
}

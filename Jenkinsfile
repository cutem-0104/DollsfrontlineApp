#!groovy
import groovy.json.JsonBuilder

def attachmentPayload = [[
    fallback: "execution #${env.BUILD_NUMBER}",
    color: "#2eb886",
    pretext: "${env.JOB_NAME}",
    text: "TEST DONE #${env.BUILD_NUMBER}",
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
        always {
            echo 'TEST DONE'
            script {// ここだけscripted pipeline のsyntaxを適用する
                slackSend(channel: '#sugaya_github_bot', color: "#2eb886", attachments: new JsonBuilder(attachmentPayload).toString())
            }
        }
    }
}

#!groovy
import groovy.json.JsonBuilder

def successPayload = [[
    fallback: "${env.JOB_NAME} #${env.BUILD_NUMBER}",
    color: "good",
    text: "TEST SUCCESS #${env.BUILD_NUMBER} ${env.BUILD_URL}",
]]

def failedPayload = [[
    fallback: "${env.JOB_NAME} #${env.BUILD_NUMBER}",
    color: "danger",
    text: "TEST FAILED #${env.BUILD_NUMBER} ${env.BUILD_URL}",
]]

pipeline {
    agent {
        label 'master'
    }
    environment {
        mysqlserver = sh(returnStdout: true, script: 'echo $MYSQL_SERVER')
        mysqlpassword = sh(returnStdout: true, script: 'echo $MYSQL_PASSWORD')
    }
    stages {
        stage('SetUp') {
            agent {
                label 'master'
            }
            steps {
                sh 'echo ${testtext}'
                sh 'docker build -t cutem/python-build .'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'cutem/python-build'
                    args '-e MYSQL_SERVER=${mysqlserver} -e MYSQL_PASSWORD=${mysqlpassword}'
                }
            }
            steps {
                script {
                    try {
                        sh 'flake8 .'
                        sh 'python3 -m unittest discover test "test_*.py"'
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
                slackSend(channel: '#sugaya_github_bot', attachments: new JsonBuilder(successPayload).toString())
            }
        }
        failure {
            script {// ここだけscripted pipeline のsyntaxを適用する
                slackSend(channel: '#sugaya_github_bot', attachments: new JsonBuilder(failedPayload).toString())
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Generating Configuration') {
            steps {
		sh 'sudo python3 /home/netman/Downloads/lab11-createTemp.py'
                sh 'sudo ansible-playbook /etc/ansible/site.yaml'
		sh 'sudo python3 /home/netman/Downloads/lab11-ospfConfig.py'
		sh 'sudo python3 /home/netman/Downloads/lab11-confBGP.py'
		echo "Triggered"
            }
        }
        stage('Stage 2') {
            steps {
                echo "Stage2"
            }
        }
 	stage('Stage 3') {
            steps {
                echo "Stage 3"
            }
        }
        stage('Stage 4') {
            steps {
                echo "Stage 4"
            }
        }
    }
}

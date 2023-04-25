pipeline {
    agent any

    stages {
        stage('Stage 1') {
            steps {
		sh 'sudo python3 /home/netman/Downloads/lab11-createTemp.py'
                sh 'sudo ansible-playbook /etc/ansible/site.yaml'
		echo "Triggered"
            }
        }
        stage('Stage 2') {
            steps {
                echo "Stage2"
		sh 'sudo python3 /home/netman/Downloads/lab11-ospfConfig.py'
            }
        }
 	stage('Stage 3') {
            steps {
                echo "Stage 3"
		sh 'sudo python3 /home/netman/Downloads/lab11-confBGP.py'
            }
        }
        stage('Stage 4') {
            steps {
                echo "Stage 4"
		sh 'sudo python3 -m pip install easysnmp'
		sh 'sudo python3 -m pip install matplotlib'
		sh 'sudo python3 /home/netman/Downloads/lab11-CPUgraph.py'
            }
        }
    }
}

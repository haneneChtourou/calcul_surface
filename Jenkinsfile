pipeline {
    agent any
	environment{
	    //NB: credential_dockerhub_didierdefrance69 is ID of credential
		//prepared in "Admin Jenkins / Credentials / system /global"
		dockerhub_credential_id='mon_token'
		
		//default/empty dockerRegistry is dockerhub
		docker_registry= 'https://registry.hub.docker.com'
		
		docker_image_name='hanenechtourou/calcul_surface:1'
	}
    stages {
        stage('build') {
            steps {
                sh 'python -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt'
                echo 'build'
            }
        }
		stage('tests') {
            steps {
                sh '. .venv/bin/activate && pytest test_gemotry.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('build_docker_image') {
		 steps {
            //sh 'docker build -t my_rest_api:1 .'
            //with Pipeline docker plugin:
			script{
				    echo "docker_image_name=" + docker_image_name
					dockerImage = docker.build(docker_image_name)
				  }
			   }
        }
		stage('push_docker_image') {
            steps {
			  script{
					echo "docker_registry=" + docker_registry
					echo "dockerhub_credential_id=" +dockerhub_credential_id
					docker.withRegistry( docker_registry, dockerhub_credential_id ) { 
					     dockerImage.push() 
						 }
					  }
				  }
		}
        
    }
}

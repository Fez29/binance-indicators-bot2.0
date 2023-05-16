.PHONY: rebuild_docker_image

rebuild_docker_image:
	docker stop binanceindicatorbot && docker rm binanceindicatorbot && docker rmi binanceindicatorbot:v1 && docker build -t binanceindicatorbot:v1 .
	docker run -d --restart unless-stopped --name binanceindicatorbot binanceindicatorbot:v1

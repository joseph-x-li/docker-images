default:
	docker run -v /home/joseph/Github/compilers-dev:/data \
	-td dockercat9000/jst-compilers

buildmac:
	 docker buildx build --platform linux/amd64  --push -t dockercat9000/jst-compilers .

build:
	docker build -t dockercat9000/jst-compilers .

push:
	docker push dockercat9000/jst-compilers
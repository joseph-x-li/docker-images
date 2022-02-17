default:
	docker run -v ~/Github/compilers-dev:/cdev \
	-td dockercat9000/jst-compilers

build:
	 docker buildx build --platform linux/amd64  --push -t dockercat9000/jst-compilers .
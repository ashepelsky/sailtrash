if [ "$1" = "--build" ]
  then docker build -t sailtrash .
fi

docker run -v "$PWD:/workspace"  \
    --rm \
    --privileged \
    -e DISPLAY=$IP:0 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v ~/.Xauthority:/.Xauthority \
    -e XAUTHORITY=/.Xauthority \
    -w /workspace \
    -ti sailtrash

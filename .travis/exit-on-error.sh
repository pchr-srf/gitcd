exitOnError() {
    if [ $? != 0 ]; then
        exit 1
    fi
}
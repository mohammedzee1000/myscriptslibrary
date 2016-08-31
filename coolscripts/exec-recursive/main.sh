#!/usr/bin/env bash

dir=$1
shift
cmd=$@

function runcmd(){

    current=$1

    pushd ${current} &> /dev/null

    echo "Getting into ${PWD}...."

    for item in `ls ${current}`; do

        if [ -d ${item} ]; then

            runcmd ${item}

        fi

    done

    echo "Executing command ${cmd} on ${PWD}"

    exec ${cmd}

    popd &> /dev/null
}

function main(){

    runcmd ${dir}

}

main
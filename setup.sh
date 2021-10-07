#!/usr/bin/env bash
set -u
set -o pipefail
set -e
#set -x
# v0.5

###################
# setup
#################
h1(){
  echo "***[ $1 ]***"
}

help(){
  h1 "help"
  cat << EOF
  bash ${0} tag
  ex
  bash ${0} 0.1
EOF
}

get_code(){
  h1 "params $1"
  ZEROto100=safari-books-0to100
  TAG="${1}"
  DIR_TARGET="."

  mkdir -p "${DIR_TARGET}"  || true
  cd "${DIR_TARGET}"

  wget https://raw.githubusercontent.com/obar1/${ZEROto100}/master/${ZEROto100}/tests/resources/map.yaml
  sed -i '' -e "s|./books|$DIR_TARGET|g" map.yaml
  wget -qO- https://github.com/obar1/${ZEROto100}/archive/refs/tags/${TAG}.tar.gz | tar -xvf -

  cd -

}

create_runme(){
  h1 "! use this to run"

cat <<EOF >"${DIR_TARGET}/runme.sh"
  export CONFIG_FILE="map.yaml"
  export ZEROto100py="${ZEROto100}-${TAG}/${ZEROto100}/main.py"
  # main at run time
  python \$ZEROto100py "\$@"
EOF

}


help
get_code "$@"
create_runme "$@"

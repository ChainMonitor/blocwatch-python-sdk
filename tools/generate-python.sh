#!/usr/bin/env bash

set -o nounset -o pipefail -o errexit
set -x

readonly script="$(readlink -f $0)"
readonly dir="$(dirname $script)"
readonly tmpdir="$(mktemp -d)"

pushd "${tmpdir}"

cp "${dir}/../api-swagger.json" "${tmpdir}/api-swagger.json"
cp "${dir}/generate-python.pom.xml" "${tmpdir}/pom.xml"
mvn generate-sources
cp -r ${tmpdir}/target/generated-sources/swagger/* "${dir}/../"

popd

rm -rf ${tmpdir}


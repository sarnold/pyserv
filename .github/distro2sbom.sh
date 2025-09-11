#!/usr/bin/env bash
#
# sbom_type is either query or system (the latter takes approx 10 mins)

distro_name=$(cat /etc/os-release | grep ^NAME | cut -d'"' -f2 | cut -d= -f2)
distro_namespace=$(cat /etc/os-release | grep ^VERSION_ID | cut -d'"' -f2 | cut -d= -f2)
distro_host=$(uname -n)
version=$(uname -r)

sbom_type=${1}
input_file=${2:-data/distro-data.txt}
output_file=${3:-data/distro2sbom_${distro_host}_${sbom_type}_cydx.json}

#Get distro type
if which dpkg &>/dev/null; then
    distro_type='deb'
elif which rpm &>/dev/null; then
    distro_type='rpm'
else
    distro_type='auto'
fi

mkdir -p data

echo "Running distro2sbom this might take few minutes"

if [[ $sbom_type == "query" ]]; then
    command="distro2sbom --distro '$distro_type' --name '$distro_name' --distro-namespace '$distro_namespace' --release '$version' --input-file '$input_file' --format json --sbom cyclonedx --output-file '$output_file'"
else
    command="distro2sbom --distro '$distro_type' --name '$distro_name' --release '$version' --system --format json --sbom cyclonedx --output-file '$output_file'"
fi

echo "Using distro2sbom command line: $command"

bash -c "$command"

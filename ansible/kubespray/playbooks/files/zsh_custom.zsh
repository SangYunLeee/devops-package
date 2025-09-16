alias k='kubectl'
source <(kubectl completion zsh)

alias g='git'

alias dc='docker compose'




# kubectl column
kncolumn() {
  local option="$1"
  local optionValue=""
  if [[ $option == "-opt="* ]]; then
      optionValue="${option#*=}"
      shift
  else
      option=""
  fi

  local printFields=""
  for col in "$@"; do
      printFields="${printFields}\$$col, "
  done

  # Remove trailing comma
  printFields=${printFields%, }

  local awkOptions="$optionValue {print $printFields}"
  awk "$awkOptions" | column -t
}


# namespace 설정
kn() {
  if [ -z "$1" ]; then
    echo "Usage: ksetns <namespace>"
  else
    kubectl config set-context --current --namespace="$1"
    echo "Namespace set to '$1'"
  fi
}

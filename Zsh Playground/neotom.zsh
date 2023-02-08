#!/bin/zsh

# Define variables for the various system info
OS=$(uname -sr)
KERNEL=$(uname -r)
UPTIME=$(uptime | awk '{print $3 " " $4}')
SHELL=$(basename $SHELL)
TERM=$(echo $TERM)
DE=${XDG_CURRENT_DESKTOP}

# Print the system info
echo "Operating System: $OS"
echo "Kernel: $KERNEL"
echo "Uptime: $UPTIME"
echo "Shell: $SHELL"
echo "Terminal: $TERM"
echo "Desktop Environment: $DE"

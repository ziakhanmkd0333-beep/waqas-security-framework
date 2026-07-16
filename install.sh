#!/bin/bash

# WAQAS Premium Framework - Installer & Launcher
# Version: 4.0 | Author: WAQAS Security Researcher

BOLD='\033[1m'
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
NC='\033[0m'

echo -e "${RED}${BOLD}"
cat << "EOF"
██╗    ██╗ █████╗  ██████╗  █████╗ ███████╗
██║    ██║██╔══██╗██╔═══╝██╔══██╗██╔════╝
██║ █╗ ██║███████║██║   ██║███████║███████╗
██║███╗██║██╔══██║██║   ██║██╔══██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║  ██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

        ⚡ SOFTWARE ENGINEER • AI • CYBER SECURITY ⚡
               Premium Multi-Platform Framework v4.0
EOF
echo -e "${NC}"

if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}${BOLD}[!] Error: Root privileges required.${NC}"
  echo -e "${YELLOW}[+] Please run as: sudo bash install.sh${NC}"
  exit 1
fi

echo -e "${CYAN}${BOLD}[*] Initializing Premium Setup...${NC}"
echo ""

# Fixed: Safely ask user if they want to run the full installation process
echo -ne "${YELLOW}${BOLD}[?] Do you want to run the full dependency update and installation process? (y/n): ${NC}"
read run_setup

if [[ "$run_setup" != "y" && "$run_setup" != "Y" ]]; then
    echo -e "${YELLOW}${BOLD}[-] Skipping installation process.${NC}"
    echo -e "${CYAN}[*] Verifying Python script exists...${NC}"
    if [ -f "waqas_android_framework.py" ]; then
        chmod +x waqas_android_framework.py
        echo -e "${GREEN}${BOLD}[✓] Launching WAQAS Framework...${NC}\n"
        python3 waqas_android_framework.py
    else
        echo -e "${RED}${BOLD}[!] Error: waqas_android_framework.py not found!${NC}"
    fi
    exit 0
fi

# If user chose 'y', run the full visible installation
echo ""
echo -e "${YELLOW}[1/4] Fixing broken packages (if any)...${NC}"
apt-get install -f -y

echo ""
echo -e "${YELLOW}[2/4] Updating package lists (apt-get update)...${NC}"
apt-get update -y

echo ""
echo -e "${YELLOW}[3/4] Installing System Dependencies...${NC}"
echo -e "${CYAN}    -> metasploit-framework default-jdk apksigner zipalign python3 python3-pip wget${NC}"
DEBIAN_FRONTEND=noninteractive apt-get install -y metasploit-framework default-jdk apksigner zipalign python3 python3-pip wget

echo ""
echo -e "${YELLOW}[4/4] Verifying Apktool (v2.9.3 required for APK injection)...${NC}"
current_version=$(apktool --version 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')

if [ -z "$current_version" ]; then
    echo -e "${RED}    [!] Apktool is missing.${NC}"
    need_apktool=true
elif [ "$current_version" \< "2.9.2" ]; then
    echo -e "${YELLOW}    [!] Apktool is outdated (v$current_version).${NC}"
    need_apktool=true
else
    echo -e "${GREEN}    [✓] Apktool v$current_version is already installed.${NC}"
    need_apktool=false
fi

if [ "$need_apktool" = true ]; then
    echo -e "${CYAN}    -> Downloading Apktool v2.9.3 wrapper and jar...${NC}"
    wget -q https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O /usr/local/bin/apktool
    wget -q https://github.com/iBotPeaches/Apktool/releases/download/v2.9.3/apktool_2.9.3.jar -O /usr/local/bin/apktool.jar
    chmod +x /usr/local/bin/apktool /usr/local/bin/apktool.jar
    echo -e "${GREEN}    [✓] Apktool v2.9.3 installed successfully.${NC}"
fi

export PATH="/usr/local/bin:$PATH"

echo ""
echo -e "${YELLOW}[*] Verifying Python Dependencies (colorama)...${NC}"
if python3 -c "import colorama" &> /dev/null; then
    echo -e "${GREEN}    [✓] Colorama is already installed.${NC}"
else
    echo -e "${CYAN}    -> Installing colorama...${NC}"
    python3 -m pip install colorama || python3 -m pip install colorama --break-system-packages
fi

echo ""
echo -e "${GREEN}${BOLD}========================================================${NC}"
echo -e "${GREEN}${BOLD} [✓] Setup Complete! Launching WAQAS Framework... ${NC}"
echo -e "${GREEN}${BOLD}========================================================${NC}"
echo ""

if [ -f "waqas_android_framework.py" ]; then
    chmod +x waqas_android_framework.py
    python3 waqas_android_framework.py
else
    echo -e "${RED}${BOLD}[!] Critical Error: waqas_android_framework.py not found!${NC}"
    exit 1
fi
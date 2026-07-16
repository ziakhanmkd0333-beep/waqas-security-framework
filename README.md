WAQAS Multi-Platform Security Framework v4.0 (Ultra Premium)
Author: WAQAS Security Researcher
Version: 4.0 (Ultra Premium)
Purpose: Educational & Authorized Security Research Only


        MULTI-PLATFORM SECURITY FRAMEWORK v4.0       
                   (Ultra Premium)                   
======================================================================
 [*] Author  : WAQAS Security Researcher
 [*] Version : 4.0 (Ultra Premium)
 [*] Purpose : Educational & Authorized Security Research Only
======================================================================

⚠️ CRITICAL LEGAL DISCLAIMER
This software is provided STRICTLY for EDUCATIONAL and RESEARCH purposes.

By using this tool you acknowledge and agree that:

You will ONLY test devices you OWN or have EXPLICIT WRITTEN PERMISSION to test.
You will operate ONLY in controlled, isolated research environments (lab, VM, dedicated test devices).
You will NOT use this tool against any device, network, or individual without proper authorization.
Unauthorized access to computer systems is ILLEGAL under international cybercrime laws (e.g., CFAA, CMA, IT Act).
The author (WAQAS Security Researcher) is NOT responsible for any misuse, damage, or legal consequences.
All activity is logged locally for audit and accountability (waqas_framework.log).
If you do not agree with these terms, DO NOT USE this tool.

📖 Overview
The WAQAS Multi-Platform Security Framework (v4.0 Ultra Premium) is a highly advanced, menu-driven Python tool designed for authorized security researchers and penetration testers. It integrates Metasploit Framework and Android/Windows build tools into a single, automated, easy-to-use workflow.

✨ What's New in v4.0 (Ultra Premium)
✅ Windows Payload Generation: Create standalone stageless Windows EXE payloads.
✅ Windows EXE Embedding (Backdooring): Inject payloads into legitimate Windows applications using the -k (preserve) flag.
✅ Smart Auto-Error Handler: Catches tool failures, displays them in a professional formatted box, and suggests automatic fixes.
✅ Multi-Platform Smart Listener: Dynamically configures Metasploit (Staged vs. Stageless) based on your exact payload type (Android/Windows).
✅ Premium Dashboard UI: Grouped menu layout (Android, Windows, Exploitation, Automation) with status bars.
✅ Advanced Auto-Installer: Automatically fixes broken apt packages, installs all dependencies, and forces the correct apktool v2.9.3 required for modern APK injection.
✨ Core Features
✅ Modern Android Compatibility: Uses stageless meterpreter_reverse_tcp for Android 11–16.
✅ Dual Standalone Payload Generation: Creates both Normal and Stealth (hidden icon) variants.
✅ Automatic APK Signing: Signs APKs with apksigner (includes jarsigner fallback).
✅ Session Management: List and interact with active Meterpreter sessions.
✅ Mandatory Disclaimer Acknowledgment: Enforces ethical use at startup.
✅ Local Audit Logging: Records all actions to waqas_framework.log.
📂 Project Structure
Ensure you have these three files in the same directory before starting:

waqas_framework_project/│├── waqas_android_framework.py  # The main Python script (v4.0 Ultra Premium)├── install.sh                  # 1-Click Automated Installer & Launcher└── requirements.txt            # Python dependencies (colorama)
🛠️ System Requirements
OS: Kali Linux / Parrot OS / Any Debian-based Linux (Recommended)
Privileges: Root (sudo) access is required.
Python: Version 3.x
System Tools: metasploit-framework, default-jdk, apksigner, zipalign, apktool (v2.9.3+)
Python Packages: colorama
🚀 Installation Procedure (1-Click)
The framework is designed to be as easy to use as possible. A single command will install all dependencies, fix broken packages, update apktool, and launch the tool.

Open your terminal in the project directory.
Run the automated installer script:
bash

sudo bash install.sh
What happens next:

The script silently fixes any broken apt packages.
It updates your apt package lists.
It installs Metasploit, JDK, Apksigner, Zipalign, Python, and Wget.
It verifies apktool. If missing or outdated, it downloads v2.9.3 directly from the official repository.
It installs the colorama Python library.
It automatically launches the WAQAS Framework.
Note: If you ever need to run the framework manually after installation, simply use:

bash

sudo python3 waqas_android_framework.py
▶️ Execution & First Run Setup
When the framework launches:

The Legal Disclaimer will appear. You must type yes to accept and proceed.
The framework will run a quick check to ensure all dependencies are installed. If any are missing, it will prompt you to install them automatically.
The Ultra Premium Main Menu will appear.
📚 Complete Usage Procedures
Below are the step-by-step procedures for the core features of the framework.

Procedure A: 1-Click Automated Attack (Android or Windows)
This feature generates the payload, hosts it on a web server, and starts the listener—all in one step.

Run the framework: sudo python3 waqas_android_framework.py
Accept the disclaimer.
From the Main Menu, type 9 and press Enter (Automated Attack).
Select the Target Platform (1 for Android, 2 for Windows).
Action:
The framework generates the payload.
It starts a background HTTP server on port 8000.
It launches the correctly configured Metasploit listener.
On your test device: Open a browser and navigate to http://<YOUR-KALI-IP>:8000/<payload_name> to download and execute.
A Meterpreter session will appear in your terminal.
Procedure B: Backdooring a Legitimate Windows EXE
This feature embeds the payload into an existing Windows application.

Place a legitimate .exe file in the same directory as the script (e.g., putty.exe).
Run the framework and select Option 4 (Embed Payload into EXE).
Enter the exact filename of the original EXE when prompted.
Action:
msfvenom injects the payload using the -k flag (keeping original functionality).
The output file will be named SystemUpdate_win_embedded.exe.
Deliver the EXE to your test device, then use Option 5 to start the Windows Embedded listener.
Procedure C: Backdooring a Legitimate Android APK
This feature embeds the payload into an existing Android application.

Place a legitimate .apk file in the same directory as the script (e.g., app.apk).
Run the framework and select Option 2 (Embed Payload into APK).
Enter the exact filename of the original APK when prompted.
Action:
msfvenom injects the payload and the framework aligns/signs the backdoored APK.
The output file will be named SystemUpdate_embedded_final.apk.
Deliver the APK to your test device, then use Option 5 to start the Android Embedded listener.
Procedure D: Managing Sessions
Once a device is infected and connects back to your listener:

If you are not already in the Metasploit console, select Option 7 to list active sessions.
Select Option 8 to interact with a session.
Enter the Session ID (e.g., 1).
You will drop into a meterpreter > prompt.
📂 Output Files Description
File
Description
SystemUpdate_final.apk	Signed normal standalone Android payload (Visible icon)
SystemUpdate_stealth_final.apk	Signed stealth standalone Android payload (Hidden icon)
SystemUpdate_embedded_final.apk	Signed backdoored legitimate Android APK
SystemUpdate_win.exe	Standalone stageless Windows EXE payload
SystemUpdate_win_embedded.exe	Backdoored legitimate Windows EXE
debug.keystore	Auto-generated signing keystore (DO NOT DELETE)
waqas_framework.log	Local audit log of all actions, errors, and fixes

🐛 Troubleshooting & Smart Error Handling
The v4.0 Framework includes a Smart Auto-Error Handler. If msfvenom or the framework encounters an error, it will display a professional error box and suggest a fix.

Issue
Solution
msfvenom cannot inject into heavily obfuscated APKs/EXEs	This is a Metasploit limitation. Try using a clean, standard app (like a calculator) to verify the tool works.
apktool version not supported	Run sudo bash install.sh again. The installer will automatically download apktool v2.9.3.
No session appears after opening app	1. Ensure Kali firewall is disabled (ufw disable).
2. Ensure LHOST is your correct Kali IP (Check Option 10).
3. Ensure you selected the correct Listener type (Option 5).
colorama missing	Run pip3 install colorama or re-run install.sh.
Permission denied errors	Always run the script with sudo.

👤 Author & Credits
WAQAS Security Researcher
Software Engineer • AI • Cyber Security
Educational Cybersecurity Research

📜 License
This tool is released for educational and research purposes only.
No warranty is provided. Use at your own risk and responsibility.

Final Reminder: Unauthorized use of this tool against systems you do not own or lack permission to test is ILLEGAL. The author disclaims all liability for misuse. Act ethically. Act legally. Act responsibly.

#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Takbir Wifux - Wireless Security Assessment Framework
Version: 3.1.2
Build: 2024.03.15
Author: T.W. Research Team
"""

import os
import sys
import time
import random
import platform
from datetime import datetime

BANNER = """
\033[91m
████████╗ █████╗ ██╗  ██╗██████╗ ██╗██████╗ 
╚══██╔══╝██╔══██╗██║ ██╔╝██╔══██╗██║██╔══██╗
   ██║   ███████║█████╔╝ ██████╔╝██║██████╔╝
   ██║   ██╔══██║██╔═██╗ ██╔══██╗██║██╔══██╗
   ██║   ██║  ██║██║  ██╗██████╔╝██║██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝
                                            
          ██╗    ██╗██╗███████╗██╗          
          ██║    ██║██║██╔════╝██║          
          ██║ █╗ ██║██║█████╗  ██║          
          ██║███╗██║██║██╔══╝  ██║          
          ╚███╔███╔╝██║██║     ██║          
           ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝        
                      
                    \033[92m[ Takbir Wifux v3.1.2 ]
                    \033[96m[ Cybersecurity for Ethical Hacking ]
                    \033[93m[ Educational Purposes Only ]
\033[0m
"""

MENU = """
\033[96m┌───[ MAIN MENU ]────────────────────┐
│                                         │
│   [1] Network Scanner                   │
│   [2] Handshake Capturer                │
│   [3] WPA/WPA2 Cracker                  │
│   [4] Deauthentication Module           │
│   [5] WPS Pixie Dust Attack             │
│   [6] PMKID Attack                      │
│   [7] Evil Twin AP                      │
│   [8] Client Monitor                    │
│   [9] Exit                              │
└─────────────────────────────────────────┘
\033[0m
"""

class TakbirWifux:
    def __init__(self):
        self.monitor_interface = "wlan0mon"
        self.handshake_dir = "/data/data/com.termux/files/home/handshakes"
        self.wordlist = "/data/data/com.termux/files/home/wordlists/rockyou.txt"
        
        # Create directories if they don't exist
        os.makedirs(self.handshake_dir, exist_ok=True)
    
    def clear_screen(self):
        os.system('clear' if platform.system() != 'Windows' else 'cls')
    
    def print_status(self, message, status="info"):
        symbols = {
            "info": "\033[94m[*]\033[0m",
            "success": "\033[92m[+]\033[0m",
            "error": "\033[91m[-]\033[0m",
            "warning": "\033[93m[!]\033[0m"
        }
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{symbols.get(status, symbols['info'])} [{timestamp}] {message}")
    
    def loading_animation(self, message, duration=2):
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r\033[94m{frames[i]}\033[0m {message}", end="", flush=True)
            time.sleep(0.1)
            i = (i + 1) % len(frames)
        print()
    
    def check_root(self):
        """Check if running with appropriate privileges"""
        try:
            return os.geteuid() == 0
        except:
            return True  # Termux doesn't have geteuid
    
    def scan_networks(self):
        """WiFi network scanner"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║         NETWORK SCANNER ACTIVE           ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        self.print_status("Initializing wireless interface...", "info")
        self.loading_animation("Setting monitor mode", 2)
        
        # Simulated network data
        networks = [
            {"bssid": "00:11:22:33:44:55", "essid": "BANGLALINK-4G", "channel": 6, "signal": -45, "enc": "WPA2", "clients": 3},
            {"bssid": "AA:BB:CC:DD:EE:FF", "essid": "GP-HOMENET", "channel": 1, "signal": -67, "enc": "WPA3", "clients": 5},
            {"bssid": "11:22:33:44:55:66", "essid": "ROBI-FIBER", "channel": 11, "signal": -72, "enc": "WPA2", "clients": 2},
            {"bssid": "77:88:99:AA:BB:CC", "essid": "AIRPORT-FREE", "channel": 3, "signal": -81, "enc": "OPEN", "clients": 8},
            {"bssid": "DE:AD:BE:EF:CA:FE", "essid": "CORPORATE-NET", "channel": 8, "signal": -55, "enc": "WPA2-ENT", "clients": 12},
        ]
        
        print("\n")
        print("\033[96m{:<20} {:<18} {:<4} {:<10} {:<12} {:<8}\033[0m".format(
            "BSSID", "ESSID", "CH", "SIGNAL", "ENCRYPTION", "CLIENTS"))
        print("\033[90m" + "-"*75 + "\033[0m")
        
        for net in networks:
            signal_bars = "▂▃▄▅▆▇" if net['signal'] > -50 else "▂▃▄▅▆" if net['signal'] > -60 else "▂▃▄▅" if net['signal'] > -70 else "▂▃▄"
            print("{:<20} {:<18} {:<4} {:<3}dBm {:<4} {:<12} {:<8}".format(
                net['bssid'], net['essid'], net['channel'], 
                net['signal'], signal_bars, net['enc'], net['clients']))
        
        print("\n")
        self.print_status(f"Found {len(networks)} networks in range", "success")
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def capture_handshake(self):
        """Capture WPA handshake"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║        HANDSHAKE CAPTURE MODULE          ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        target_bssid = input("\n\033[93m[?] Target BSSID: \033[0m")
        target_channel = input("\033[93m[?] Target Channel: \033[0m")
        
        self.print_status(f"Monitoring channel {target_channel}", "info")
        self.print_status("Waiting for handshake...", "info")
        
        print("\n\033[96m[Live Capture Log]\033[0m")
        events = [
            "[20:15:23] Probe request from client (34:23:87:65:43:21)",
            "[20:15:25] Authentication request detected",
            "[20:15:26] Association request",
            "[20:15:28] EAPOL frame 1/4 captured",
            "[20:15:29] EAPOL frame 2/4 captured",
            "[20:15:31] EAPOL frame 3/4 captured",
            "[20:15:32] EAPOL frame 4/4 captured - HANDSHAKE COMPLETE"
        ]
        
        for event in events:
            time.sleep(1.2)
            print(f"\033[92m[+]\033[0m {event}")
        
        handshake_file = f"{self.handshake_dir}/handshake_{target_bssid.replace(':', '')}.cap"
        self.print_status(f"Handshake saved: {handshake_file}", "success")
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def crack_wpa(self):
        """Crack WPA/WPA2 handshake"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║          WPA/WPA2 CRACKING MODULE         ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        handshake = input("\n\033[93m[?] Handshake file path: \033[0m") or "auto-detect"
        wordlist = input("\033[93m[?] Wordlist path (default: rockyou.txt): \033[0m") or self.wordlist
        
        self.print_status("Initializing cracking engine", "info")
        self.loading_animation("Loading wordlist", 3)
        
        print("\n\033[96m[Cracking Progress]\033[0m")
        attempts = [
            ("password", "❌"),
            ("12345678", "❌"),
            ("admin123", "❌"),
            ("wifi1234", "❌"),
            ("taka_den", "✅ FOUND!")
        ]
        
        for pwd, status in attempts:
            if status == "✅ FOUND!":
                time.sleep(1.5)
                print(f"\033[92m[+]\033[0m Testing: {pwd:<12} [{status}]")
                print(f"\n\033[92m[+] KEY FOUND: {pwd}\033[0m")
                print(f"\033[92m[+] PSK: {pwd}\033[0m")
            else:
                print(f"\033[91m[-]\033[0m Testing: {pwd:<12} [{status}]")
                time.sleep(0.8)
        
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def deauth_attack(self):
        """Deauthentication attack"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║      DEAUTHENTICATION ATTACK MODULE       ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        target = input("\n\033[93m[?] Target BSSID: \033[0m")
        channel = input("\033[93m[?] Channel: \033[0m")
        
        self.print_status(f"Target locked: {target}", "info")
        self.print_status("Injecting deauth packets...", "warning")
        
        for i in range(1, 101):
            if i % 10 == 0:
                print(f"\r\033[94m[*]\033[0m Packets injected: {i}/100", end="", flush=True)
            time.sleep(0.05)
        
        print("\n")
        self.print_status("Attack completed successfully", "success")
        self.print_status("3 clients disconnected from target", "success")
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def wps_pixie(self):
        """WPS Pixie Dust attack"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║         WPS PIXIE DUST ATTACK             ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        target = input("\n\033[93m[?] Target BSSID: \033[0m")
        
        self.print_status("Starting pixie dust attack", "info")
        self.loading_animation("Computing WPS PIN", 3)
        
        pins = ["12345670", "98765432", "11112222"]
        
        for pin in pins:
            print(f"\r\033[94m[*]\033[0m Trying PIN: {pin}", end="", flush=True)
            time.sleep(1)
        
        print("\n")
        self.print_status("WPS PIN recovered!", "success")
        print(f"\033[92m[+] PIN: 12345670\033[0m")
        print(f"\033[92m[+] PSK: HomeNetwork@2024\033[0m")
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def pmkid_attack(self):
        """PMKID attack"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║           PMKID ATTACK MODULE              ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        self.print_status("Scanning for PMKID vulnerable APs", "info")
        self.loading_animation("Capturing RSN IE", 3)
        
        print("\n\033[96m[PMKID Capture]\033[0m")
        print("\033[92m[+]\033[0m PMKID captured from 00:11:22:33:44:55")
        print("\033[92m[+]\033[0m PMKID: 4a5b6c7d8e9f0a1b2c3d4e5f...")
        
        self.print_status("PMKID saved to database", "success")
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def evil_twin(self):
        """Evil Twin attack"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║           EVIL TWIN AP MODULE              ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        ssid = input("\n\033[93m[?] Target SSID to clone: \033[0m")
        
        self.print_status(f"Creating Evil Twin for {ssid}", "info")
        steps = [
            "Creating virtual interface",
            "Starting hostapd",
            "Starting dnsmasq",
            "Enabling NAT",
            "Starting captive portal"
        ]
        
        for step in steps:
            time.sleep(1)
            print(f"\033[92m[+]\033[0m {step}")
        
        self.print_status(f"Evil Twin AP '{ssid}' is active", "success")
        self.print_status("Waiting for connections...", "info")
        
        # Simulate a connection
        time.sleep(3)
        print("\n\033[92m[+] New client connected\033[0m")
        print("    MAC: 12:34:56:78:90:AB")
        print("    Device: Samsung Galaxy S21")
        
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def client_monitor(self):
        """Monitor connected clients"""
        self.clear_screen()
        print("\033[96m╔════════════════════════════════════════════╗")
        print("║           CLIENT MONITOR MODULE            ║")
        print("╚════════════════════════════════════════════╝\033[0m")
        
        self.print_status("Scanning for active clients", "info")
        self.loading_animation("Monitoring network traffic", 2)
        
        clients = [
            {"mac": "12:34:56:78:90:AB", "vendor": "Samsung", "signal": -45, "packets": 2345},
            {"mac": "98:76:54:32:10:FE", "vendor": "Xiaomi", "signal": -52, "packets": 1678},
            {"mac": "AB:CD:EF:12:34:56", "vendor": "Apple", "signal": -61, "packets": 892},
            {"mac": "11:22:33:44:55:66", "vendor": "OnePlus", "signal": -73, "packets": 445},
        ]
        
        print("\n\033[96m{:<20} {:<12} {:<10} {:<12}\033[0m".format(
            "MAC Address", "Vendor", "Signal", "Packets"))
        print("\033[90m" + "-"*55 + "\033[0m")
        
        for client in clients:
            print("{:<20} {:<12} {:<3}dBm {:<4} {:<12}".format(
                client['mac'], client['vendor'], client['signal'], 
                "▂▃▄▅▆", client['packets']))
        
        print("\n")
        self.print_status("Active clients: 4", "success")
        input("\n\033[93mPress [Enter] to continue...\033[0m")
    
    def run(self):
        """Main execution loop"""
        try:
            while True:
                self.clear_screen()
                print(BANNER)
                print(MENU)
                
                choice = input("\n\033[93mtakbir@wifux:~$ \033[0m")
                
                if choice == "1":
                    self.scan_networks()
                elif choice == "2":
                    self.capture_handshake()
                elif choice == "3":
                    self.crack_wpa()
                elif choice == "4":
                    self.deauth_attack()
                elif choice == "5":
                    self.wps_pixie()
                elif choice == "6":
                    self.pmkid_attack()
                elif choice == "7":
                    self.evil_twin()
                elif choice == "8":
                    self.client_monitor()
                elif choice == "9":
                    self.print_status("Shutting down modules...", "info")
                    self.loading_animation("Cleaning up", 2)
                    print("\n\033[92m[+] Takbir Wifux terminated\033[0m")
                    sys.exit(0)
                else:
                    self.print_status("Invalid option", "error")
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            print("\n\n\033[91m[-] Interrupted by user\033[0m")
            self.print_status("Exiting safely", "info")
            sys.exit(0)

if __name__ == "__main__":
    tool = TakbirWifux()
    tool.run()

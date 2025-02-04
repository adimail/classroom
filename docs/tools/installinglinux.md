---
layout: default
title: Installing Linux
parent: Tools
---

# How to install Linux

First of all congratulations! Good to have you here.

> ## TL;DR
> Download a Linux distibution .iso file. Use balenaEtcher to write it to a usb stick. Boot the computer from that usb and follow the on screen instructions.

---

## Common problems while installing Linux

First off, hardware compatibility. I remember when I tried installing Linux on my laptop and the Wi-Fi didn't work out of the box. That was frustrating. Maybe drivers for things like graphics cards, especially Nvidia or AMD, are common issues. Also, newer hardware might not be supported yet, like the latest CPUs or peripherals.

Then partitioning the disk can be tricky. People accidentally wipes off their Windows partition. Understanding UEFI vs. Legacy BIOS is another part of that. Secure Boot might cause problems too. Oh, and dual-booting in general—managing the bootloader, especially GRUB. Sometimes GRUB doesn't detect other OSes, or the Windows bootloader takes over.

Installation media issues: Maybe the USB drive isn't properly created. Using tools like Rufus or Etcher correctly, ensuring the ISO is downloaded properly without corruption. Also, booting from USB might require changing BIOS settings, which some users find confusing.

Driver availability after installation. Like, printers or scanners not working because manufacturers don't provide Linux drivers. Or needing to install proprietary drivers for better performance, which isn't always straightforward.

If someone picks a distro with a heavy DE, it might not run well on older hardware. Or maybe the DE crashes or has bugs. Choosing the right distro for their needs could be a problem too—Ubuntu vs. Arch, for example.

Post-installation configuration. Setting up things like multimedia codecs, which aren't always included by default. Managing software repositories, dealing with dependency issues. System updates breaking things occasionally, especially with rolling release distros.

Secure Boot and TPM modules in newer systems. Some distros handle Secure Boot better than others. TPM 2.0 with Windows 11 compatibility might interfere, though that's more of a dual-boot scenario.

Here's a step-by-step guide to installing Linux properly, followed by a table of popular Linux distributions with their advantages and use cases.

---

### **Steps to Install Linux Properly**
1. **Choose a Linux Distribution**
   - Research distros based on your needs (e.g., Ubuntu for beginners, Arch for customization).
   - Download the ISO file from the official website.

2. **Backup Your Data**
   - Save important files to an external drive or cloud storage.

3. **Create a Bootable USB Drive**
   - Use tools like **Rufus** (Windows), **Balena Etcher** (macOS/Linux), or `dd` (Linux CLI).
   - Ensure the USB is formatted correctly (FAT32 for UEFI).

4. **Configure BIOS/UEFI**
   - Restart your PC and enter BIOS/UEFI (usually via `F2`, `F12`, `Delete`, or `Esc`).
   - Disable **Secure Boot** (if required by the distro).
   - Set boot priority to USB.

5. **Boot into the Live Environment**
   - Select "Try Linux" to test hardware compatibility (Wi-Fi, graphics, etc.).

6. **Start the Installation**
   - Choose language, keyboard layout, and timezone.
   - **Partitioning**:
     - **Automatic**: Let the installer handle partitioning (recommended for beginners).
     - **Manual**:
       - Create a **root** (`/`) partition (min. 20GB).
       - Optional: **Swap** partition (equal to RAM size for hibernation).
       - Optional: **Home** (`/home`) partition (for personal files).
     - Ensure the bootloader (GRUB) is installed on the correct drive (e.g., `/dev/sda`).

7. **Complete Installation**
   - Remove the USB when prompted and reboot.

---

Below is the updated post-installation guide that includes sections for **tmux**, **Neovim**, and **fzf** along with relevant links for all the tools mentioned. You can use or modify this markdown as needed:

---

## Post-Installation Setup

After setting up a fresh Linux installation, follow this guide to install essential development tools, improve your workflow, and enhance your system.

---

#### 1. Desktop Customization
- **Change Themes & Icons**:
  - **GNOME** (Ubuntu/Fedora):
    ```bash
    sudo apt install gnome-tweaks  # Ubuntu/Debian
    sudo dnf install gnome-tweaks  # Fedora
    ```
    - Use the **GNOME Extensions** app for add-ons like [Dash to Panel](https://extensions.gnome.org/).
  - **KDE Plasma** (Kubuntu/KDE Neon):
    - Install themes via *System Settings > Appearance*.
  - **XFCE** (Xubuntu):
    - Customize via *Settings Manager > Appearance*.

- **Dock & Panels**:
  - Install **Plank** (lightweight dock):
    ```bash
    sudo apt install plank  # Debian/Ubuntu
    sudo dnf install plank  # Fedora
    ```
    - [Plank on GitHub](https://github.com/ricotz/plank)

---

#### 2. Essential Software Installation
- **Web Browsers**:
  ```bash
  sudo apt install firefox chromium  # Debian/Ubuntu
  sudo dnf install firefox chromium  # Fedora
  ```
  - For Google Chrome:
    ```bash
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install ./google-chrome-stable_current_amd64.deb  # Debian/Ubuntu
    ```
    - [Google Chrome](https://www.google.com/chrome/)

- **Office Suite**:
  ```bash
  sudo apt install libreoffice  # Debian/Ubuntu
  sudo dnf install libreoffice  # Fedora
  ```
  - [LibreOffice](https://www.libreoffice.org/)

- **Media Players**:
  ```bash
  sudo apt install vlc  # Debian/Ubuntu
  sudo dnf install vlc  # Fedora
  ```
  - [VLC Media Player](https://www.videolan.org/vlc/)

---

#### 3. Multimedia Codecs
- **Debian/Ubuntu**:
  ```bash
  sudo apt install ubuntu-restricted-extras libavcodec-extra
  ```
- **Fedora**:
  ```bash
  sudo dnf install gstreamer1-plugins-{bad-free,good,base} gstreamer1-plugin-openh264 gstreamer1-libav
  ```

---

#### 4. Driver Management
- **Graphics Drivers**:
  - **NVIDIA** (Debian/Ubuntu):
    ```bash
    sudo ubuntu-drivers autoinstall  # Auto-detect and install
    sudo apt install nvidia-driver-535  # Specific version
    ```
  - **AMD/Intel**: Usually open-source and pre-installed.

- **Wi-Fi/Bluetooth**:
  - For Broadcom (Debian/Ubuntu):
    ```bash
    sudo apt install bcmwl-kernel-source
    ```
  - Use `lspci` or `lsusb` to identify hardware.

- **Printers**:
  - Install **CUPS**:
    ```bash
    sudo apt install cups  # Debian/Ubuntu
    sudo dnf install cups  # Fedora
    ```
  - Open `http://localhost:631` in a browser to configure.

---

#### 5. Security Hardening
- **Firewall**:
  - **UFW** (Debian/Ubuntu):
    ```bash
    sudo ufw enable
    sudo ufw allow ssh  # Allow SSH
    ```
  - **Firewalld** (Fedora/RHEL):
    ```bash
    sudo firewall-cmd --permanent --add-service=ssh
    sudo firewall-cmd --reload
    ```

- **Automatic Updates**:
  - **Debian/Ubuntu** (Unattended Upgrades):
    ```bash
    sudo apt install unattended-upgrades
    sudo dpkg-reconfigure unattended-upgrades
    ```
  - **Fedora** (DNF Automatic):
    ```bash
    sudo dnf install dnf-automatic
    sudo systemctl enable --now dnf-automatic.timer
    ```

---

#### 6. Development Tools
- **Compilers & IDEs**:
  ```bash
  sudo apt install build-essential gcc g++ python3 python3-pip nodejs npm  # Debian/Ubuntu
  sudo dnf groupinstall "Development Tools"  # Fedora
  ```

  - **Visual Studio Code**:
    ```bash
    sudo snap install code --classic  # Snap
    ```
    - [Visual Studio Code](https://code.visualstudio.com/)

- **Terminal Utilities**:
  - **tmux** - Terminal Multiplexer:
    ```bash
    sudo apt install tmux  # Debian/Ubuntu
    sudo dnf install tmux  # Fedora
    ```
    - [tmux on GitHub](https://github.com/tmux/tmux)

  - **Neovim** - Modern Vim-based Editor:
    ```bash
    sudo apt install neovim  # Debian/Ubuntu
    sudo dnf install neovim  # Fedora
    ```
    - [Neovim](https://neovim.io/)

  - **fzf** - Fuzzy Finder:
    ```bash
    sudo apt install fzf  # Debian/Ubuntu
    sudo dnf install fzf  # Fedora
    ```
    - [fzf on GitHub](https://github.com/junegunn/fzf)

- **Docker**:
  ```bash
  sudo apt install docker.io  # Debian/Ubuntu
  sudo dnf install docker  # Fedora (if available)
  sudo systemctl enable --now docker
  sudo usermod -aG docker $USER  # Add user to docker group
  ```
  - [Docker](https://www.docker.com/)

---

#### 7. Backup Solutions
- **System Snapshots**:
  - **Timeshift** (Debian/Ubuntu):
    ```bash
    sudo apt install timeshift
    ```
    - [Timeshift](https://github.com/teejee2008/timeshift)

- **File Backups**:
  - **Deja Dup** (GUI):
    ```bash
    sudo apt install deja-dup  # Debian/Ubuntu
    ```
    - [Deja Dup](https://wiki.gnome.org/Apps/DejaDup)
  - **rsync** (CLI):
    ```bash
    rsync -avh --progress /source/folder /backup/folder
    ```

---

#### 8. Gaming Setup
- **Steam**:
  ```bash
  sudo apt install steam  # Debian/Ubuntu
  sudo dnf install steam  # Fedora
  ```
  - [Steam](https://store.steampowered.com/about/)

- **Proton & Lutris**:
  ```bash
  sudo apt install lutris  # Debian/Ubuntu
  ```
  - [Lutris](https://lutris.net/)

- **Game Controllers**:
  - Install **SDL2** for better compatibility:
    ```bash
    sudo apt install libsdl2-2.0-0
    ```
    - [SDL2](https://www.libsdl.org/)

---

#### 9. Network Tools
- **SSH Server**:
  ```bash
  sudo apt install openssh-server  # Debian/Ubuntu
  sudo systemctl enable --now sshd
  ```
  - [OpenSSH](https://www.openssh.com/)

- **VPN Clients**:
  - **OpenVPN**:
    ```bash
    sudo apt install openvpn network-manager-openvpn  # Debian/Ubuntu
    ```
    - [OpenVPN](https://openvpn.net/)

---

#### 10. Cloud Integration
- **Nextcloud Client**:
  ```bash
  sudo apt install nextcloud-desktop  # Debian/Ubuntu
  ```
  - [Nextcloud](https://nextcloud.com/)

- **rclone** (CLI):
  ```bash
  sudo apt install rclone  # Debian/Ubuntu
  rclone config  # Follow prompts to link cloud storage
  ```
  - [rclone](https://rclone.org/)

---

#### 11. Flatpak/Flathub Setup
- Enable Flatpak:
  ```bash
  sudo apt install flatpak  # Debian/Ubuntu
  flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
  ```
  - [Flatpak](https://flatpak.org/)

- Install apps:
  ```bash
  flatpak install flathub com.spotify.Client
  ```
  - [Spotify on Flathub](https://flathub.org/apps/details/com.spotify.Client)

---

#### 12. Shell Customization
- **Zsh + Oh My Zsh**:
  ```bash
  sudo apt install zsh  # Debian/Ubuntu
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```
  - [Oh My Zsh](https://ohmyz.sh/)

- **Powerline Themes**:
  ```bash
  sudo apt install powerline fonts-powerline  # Debian/Ubuntu
  ```
  - [Powerline](https://github.com/powerline/powerline)

---

#### 13. Power Management (Laptops)
- **TLP** (Battery Saving):
  ```bash
  sudo apt install tlp tlp-rdw  # Debian/Ubuntu
  sudo systemctl enable tlp
  ```
  - [TLP](https://linrunner.de/tlp/)

---

#### 14. Troubleshooting Tools
- **Diagnose Audio Issues**:
  ```bash
  sudo apt install pavucontrol  # PulseAudio Volume Control
  alsamixer  # CLI audio mixer
  ```
  - [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/)

- **Check Hardware**:
  ```bash
  inxi -F  # System summary
  lspci -v  # PCI devices
  ```
  - [inxi](https://github.com/smxi/inxi)

---

#### 15. Virtualization
- **VirtualBox**:
  ```bash
  sudo apt install virtualbox virtualbox-ext-pack  # Debian/Ubuntu
  ```
  - [VirtualBox](https://www.virtualbox.org/)

- **KVM/QEMU** (Advanced):
  ```bash
  sudo apt install qemu-kvm libvirt-daemon-system virt-manager  # Debian/Ubuntu
  ```
  - [KVM](https://www.linux-kvm.org/page/Main_Page)
  - [QEMU](https://www.qemu.org/)

---

### Final Tips
- Join forums like [Ask Ubuntu](https://askubuntu.com/) or [Reddit’s r/linuxquestions](https://www.reddit.com/r/linuxquestions/).
- Use `man [command]` for built-in documentation (e.g., `man apt`).

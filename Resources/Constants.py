# pylint: disable=multiple-statements
# Define Files
# Copyright (C) 2020-2021, Dhinak G, Mykola Grymalyuk

from __future__ import print_function

from pathlib import Path


class Constants:
    def __init__(self):
        self.patcher_version = "0.0.20"
        self.opencore_commit = "a57d8df - 2021-03-27"
        self.opencore_version = "0.6.8"
        self.lilu_version = "1.5.1"
        self.whatevergreen_version = "1.4.8"
        self.airportbcrmfixup_version = "2.1.2"
        self.bcm570_version = "1.0.1"
        self.marvel_version = "1.0.0"
        self.nforce_version = "1.0.0"
        self.mce_version = "1.0.0"
        self.mousse_version = "0.93"
        self.telemetrap_version = "1.0.0"
        self.io80211high_sierra_version = "1.0.0"
        self.io80211mojave_version = "1.0.0"
        self.voodoohda_version = "296"
        self.restrictevents_version = "1.0.1"
        self.piixata_version = "1.0.0"
        self.backlight_version = "1.0.0"
        self.cpufriend_version = "1.2.3"
        self.nightshift_version = "1.1.0"
        self.smcspoof_version = "1.0.0"

        # Get resource path
        self.current_path = Path(__file__).parent.parent.resolve()
        self.payload_path = self.current_path / Path("payloads")

        self.custom_model: str = None
        self.custom_mxm_gpu: str = None
        self.current_gpuv: str = None
        self.current_gpud: str = None

        # Patcher Settings
        self.opencore_debug = False
        self.opencore_build = "RELEASE"
        self.kext_debug = False
        self.verbose_debug = False
        self.os_support = 11.0
        self.min_os_support = 11.0
        self.max_os_support = 11.0
        self.metal_build = False
        self.imac_vendor = "None"
        self.wifi_build = False
        self.gui_mode = False
        self.serial_settings = "Minimal"
        self.showpicker = True
        self.vault = False
        self.sip_status = True
        self.secure_status = True
        self.detected_os = 0

        # OS Versions
        self.tiger = 8
        self.leopard = 9
        self.snow_leopard = 10
        self.lion = 11
        self.mountain_lion = 12
        self.mavericks = 13
        self.yosemite = 14
        self.el_capitan = 15
        self.sierra = 16
        self.high_sierra = 17
        self.mojave = 18
        self.catalina = 19
        self.big_sur = 20

    # Payload Location
    # OpenCore
    @property
    def opencore_zip_source(self): return self.payload_path / Path(f"OpenCore/OpenCore-{self.opencore_build}-v{self.opencore_version}.zip")
    @property
    def plist_template(self): return self.payload_path / Path(f"Config/v{self.opencore_version}/config.plist")

    # ACPI
    @property
    def pci_ssdt_path(self): return self.payload_path / Path("ACPI/SSDT-CPBG.aml")

    # Drivers
    @property
    def nvme_driver_path(self): return self.payload_path / Path("Drivers/NvmExpressDxe.efi")

    # Kexts
    @property
    def payload_kexts_path(self): return self.payload_path / Path("Kexts")
    @property
    def lilu_path(self): return self.payload_kexts_path / Path(f"Acidanthera/Lilu-v{self.lilu_version}.zip")
    @property
    def whatevergreen_path(self): return self.payload_kexts_path / Path(f"Acidanthera/WhateverGreen-v{self.whatevergreen_version}.zip")
    @property
    def airportbcrmfixup_path(self): return self.payload_kexts_path / Path(f"Acidanthera/AirportBrcmFixup-v{self.airportbcrmfixup_version}.zip")
    @property
    def restrictevents_path(self): return self.payload_kexts_path / Path(f"Acidanthera/RestrictEvents-v{self.restrictevents_version}.zip")
    @property
    def bcm570_path(self): return self.payload_kexts_path / Path(f"Ethernet/CatalinaBCM5701Ethernet-v{self.bcm570_version}.zip")
    @property
    def marvel_path(self): return self.payload_kexts_path / Path(f"Ethernet/MarvelYukonEthernet-v{self.marvel_version}.zip")
    @property
    def nforce_path(self): return self.payload_kexts_path / Path(f"Ethernet/nForceEthernet-v{self.nforce_version}.zip")
    @property
    def mce_path(self): return self.payload_kexts_path / Path(f"Misc/AppleMCEReporterDisabler-v{self.mce_version}.zip")
    @property
    def mousse_path(self): return self.payload_kexts_path / Path(f"SSE/AAAMouSSE-v{self.mousse_version}.zip")
    @property
    def telemetrap_path(self): return self.payload_kexts_path / Path(f"SSE/telemetrap-v{self.telemetrap_version}.zip")
    @property
    def io80211high_sierra_path(self): return self.payload_kexts_path / Path(f"Wifi/IO80211HighSierra-v{self.io80211high_sierra_version}.zip")
    @property
    def io80211mojave_path(self): return self.payload_kexts_path / Path(f"Wifi/IO80211Mojave-v{self.io80211mojave_version}.zip")
    @property
    def voodoohda_path(self): return self.payload_kexts_path / Path(f"Audio/VoodooHDA-v{self.voodoohda_version}.zip")
    @property
    def piixata_path(self): return self.payload_kexts_path / Path(f"Misc/AppleIntelPIIXATA-v{self.piixata_version}.zip")
    @property
    def backlight_path(self): return self.payload_kexts_path / Path(f"Misc/AppleBacklightFixup-v{self.backlight_version}.zip")
    @property
    def cpufriend_path(self): return self.payload_kexts_path / Path(f"Acidanthera/CPUFriend-v{self.cpufriend_version}.zip")
    @property
    def nightshift_path(self): return self.payload_kexts_path / Path(f"Misc/NightShiftEnabler-v{self.nightshift_version}.zip")
    @property
    def smcspoof_path(self): return self.payload_kexts_path / Path(f"Misc/SMC-Spoof-v{self.smcspoof_version}.zip")

    # Build Location
    @property
    def build_path(self): return self.current_path / Path("Build-Folder/")
    @property
    def opencore_release_folder(self): return self.build_path / Path(f"OpenCore-{self.opencore_build}-v{self.opencore_version}")
    @property
    def opencore_zip_copied(self): return self.build_path / Path(f"OpenCore-{self.opencore_build}-v{self.opencore_version}.zip")

    @property
    def oc_folder(self): return self.opencore_release_folder / Path("EFI/OC/")
    @property
    def plist_path(self): return self.oc_folder / Path("config.plist")
    @property
    def acpi_path(self): return self.oc_folder / Path("ACPI")
    @property
    def drivers_path(self): return self.oc_folder / Path("Drivers")
    @property
    def kexts_path(self): return self.oc_folder / Path("Kexts")
    @property
    def resources_path(self): return self.oc_folder / Path("Resources")
    @property
    def map_kext_folder(self): return self.kexts_path / Path("USB-Map.kext")
    @property
    def map_contents_folder(self): return self.map_kext_folder / Path("Contents")
    @property
    def pp_kext_folder(self): return self.kexts_path / Path("CPUFriendDataProvider.kext")
    @property
    def pp_contents_folder(self): return self.pp_kext_folder / Path("Contents")
    @property
    def agdp_kext_folder(self): return self.kexts_path / Path("AGDP-Override.kext")
    @property
    def agdp_contents_folder(self): return self.agdp_kext_folder / Path("Contents")
    @property
    def agpm_kext_folder(self): return self.kexts_path / Path("AGPM-Override.kext")
    @property
    def agpm_contents_folder(self): return self.agpm_kext_folder / Path("Contents")
    @property
    def amc_kext_folder(self): return self.kexts_path / Path("AMC-Override.kext")
    @property
    def amc_contents_folder(self): return self.amc_kext_folder / Path("Contents")

    # Tools
    @property
    def macserial_path(self): return self.payload_path / Path("Tools/macserial")
    @property
    def vault_path(self): return self.payload_path / Path("Tools/CreateVault/sign.command")

    # Icons
    @property
    def app_icon_path(self): return self.current_path / Path("OC-Patcher.icns")
    @property
    def icon_path_external(self): return self.payload_path / Path("Icon/External/.VolumeIcon.icns")
    @property
    def icon_path_internal(self): return self.payload_path / Path("Icon/Internal/.VolumeIcon.icns")
    @property
    def icon_path_sd(self): return self.payload_path / Path("Icon/SD-Card/.VolumeIcon.icns")
    @property
    def icon_path_ssd(self): return self.payload_path / Path("Icon/SSD/.VolumeIcon.icns")
    @property
    def gui_path(self): return self.payload_path / Path("Icon/Resources.zip")

    # Apple Paylods Paths
    @property
    def payload_apple_root_path(self): return self.payload_path / Path("Apple")
    @property
    def payload_apple_kexts_path(self): return self.payload_apple_root_path / Path("Extensions")
    @property
    def payload_apple_frameworks_path(self): return self.payload_apple_root_path / Path("Frameworks")
    @property
    def payload_apple_lauchd_path(self): return self.payload_apple_root_path / Path("LaunchDaemons")
    @property
    def payload_apple_private_frameworks_path(self): return self.payload_apple_root_path / Path("PrivateFrameworks")

    # Apple Extensions
    @property
    def applebcm_path(self): return self.payload_apple_kexts_path / Path("misc-kexts/AppleBCM5701Ethernet.kext")
    @property
    def applehda_path(self): return self.payload_apple_kexts_path / Path("misc-kexts/AppleHDA.kext")
    @property
    def iosurface_path(self): return self.payload_apple_kexts_path / Path("misc-kexts/IOSurface.kext")


    # GPU Kexts and Bundles
    @property
    def legacy_nvidia_path(self): return self.payload_apple_kexts_path / Path("legacy-nvidia")
    @property
    def legacy_amd_path(self): return self.payload_apple_kexts_path / Path("legacy-amd")
    @property
    def legacy_intel_gen1_path(self): return self.payload_apple_kexts_path / Path("intel-gen1")
    @property
    def legacy_intel_gen2_path(self): return self.payload_apple_kexts_path / Path("intel-gen2")

    # Apple Frameworks
    @property
    def coredisplay_path(self): return self.payload_apple_frameworks_path / Path("CoreDisplay.framework")
    @property
    def iosurface_f_path(self): return self.payload_apple_frameworks_path / Path("IOSurface.framework")
    @property
    def opengl_path(self): return self.payload_apple_frameworks_path / Path("OpenGL.framework")

    # Apple LaunchDaemons
    @property
    def hiddhack_path(self): return self.payload_apple_lauchd_path / Path("HiddHack.plist")

    # Apple PrivateFrameworks
    @property
    def gpusupport_path(self): return self.payload_apple_private_frameworks_path / Path("GPUSupport.framework")
    @property
    def skylight_path(self): return self.payload_apple_private_frameworks_path / Path("SkyLight.framework")

    csr_values = [
        "CSR_ALLOW_UNTRUSTED_KEXTS           ",# 0x1   - Introduced in El Capitan
        "CSR_ALLOW_UNRESTRICTED_FS           ",# 0x2   - Introduced in El Capitan
        "CSR_ALLOW_TASK_FOR_PID              ",# 0x4   - Introduced in El Capitan
        "CSR_ALLOW_KERNEL_DEBUGGER           ",# 0x8   - Introduced in El Capitan
        "CSR_ALLOW_APPLE_INTERNAL            ",# 0x10  - Introduced in El Capitan
        "CSR_ALLOW_UNRESTRICTED_DTRACE       ",# 0x20  - Introduced in El Capitan
        "CSR_ALLOW_UNRESTRICTED_NVRAM        ",# 0x40  - Introduced in El Capitan
        "CSR_ALLOW_DEVICE_CONFIGURATION      ",# 0x80  - Introduced in El Capitan
        "CSR_ALLOW_ANY_RECOVERY_OS           ",# 0x100 - Introduced in Sierra
        "CSR_ALLOW_UNAPPROVED_KEXTS          ",# 0x200 - Introduced in High Sierra
        "CSR_ALLOW_EXECUTABLE_POLICY_OVERRIDE",# 0x400 - Introduced in Mojave
        "CSR_ALLOW_UNAUTHENTICATED_ROOT      ",# 0x800 - Introduced in Big Sur
    ]
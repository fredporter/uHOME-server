"""uHOME hardware preflight checker migrated from uDOS Sonic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class UHOMEHardwareProfile:
    min_cpu_cores: int = 4
    min_ram_gb: float = 8.0
    min_storage_gb: float = 256.0
    min_media_storage_gb: float = 2000.0
    min_tuner_count: int = 1
    rec_cpu_cores: int = 6
    rec_ram_gb: float = 16.0
    rec_storage_gb: float = 512.0
    rec_media_storage_gb: float = 4000.0
    rec_tuner_count: int = 2
    require_hdmi: bool = True
    require_gigabit: bool = True
    min_usb_ports: int = 2


DEFAULT_PROFILE = UHOMEHardwareProfile()


@dataclass
class UHOMEPreflightResult:
    passed: bool
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    probe: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "issues": self.issues,
            "warnings": self.warnings,
            "probe": self.probe,
        }


def preflight_check(
    probe: dict[str, Any],
    profile: UHOMEHardwareProfile = DEFAULT_PROFILE,
) -> UHOMEPreflightResult:
    issues: list[str] = []
    warnings: list[str] = []
    cpu = probe.get("cpu_cores")
    if cpu is not None:
        if cpu < profile.min_cpu_cores:
            issues.append(f"CPU: {cpu} cores < minimum {profile.min_cpu_cores}.")
        elif cpu < profile.rec_cpu_cores:
            warnings.append(f"CPU: {cpu} cores meets minimum but {profile.rec_cpu_cores}+ recommended.")
    ram = probe.get("ram_gb")
    if ram is not None:
        if ram < profile.min_ram_gb:
            issues.append(f"RAM: {ram:.1f} GB < minimum {profile.min_ram_gb:.0f} GB.")
        elif ram < profile.rec_ram_gb:
            warnings.append(f"RAM: {ram:.1f} GB meets minimum but {profile.rec_ram_gb:.0f} GB recommended.")
    storage = probe.get("storage_gb")
    if storage is not None and storage < profile.min_storage_gb:
        issues.append(f"OS storage: {storage:.0f} GB < minimum {profile.min_storage_gb:.0f} GB.")
    media = probe.get("media_storage_gb")
    if media is not None:
        if media < profile.min_media_storage_gb:
            issues.append(f"Media storage: {media:.0f} GB < minimum {profile.min_media_storage_gb:.0f} GB.")
        elif media < profile.rec_media_storage_gb:
            warnings.append(
                f"Media storage: {media:.0f} GB, {profile.rec_media_storage_gb:.0f} GB recommended."
            )
    gigabit = probe.get("has_gigabit")
    if gigabit is not None and profile.require_gigabit and not gigabit:
        issues.append("Network: Gigabit Ethernet required.")
    hdmi = probe.get("has_hdmi")
    if hdmi is not None and profile.require_hdmi and not hdmi:
        issues.append("Display: HDMI output required for uHOME console mode.")
    tuners = probe.get("tuner_count")
    if tuners is not None:
        if tuners < profile.min_tuner_count:
            issues.append(f"Tuner: {tuners} found, at least {profile.min_tuner_count} required.")
        elif tuners < profile.rec_tuner_count:
            warnings.append(f"Tuner: {tuners} found, {profile.rec_tuner_count}+ recommended.")
    usb = probe.get("has_usb_ports")
    if usb is not None and usb < profile.min_usb_ports:
        warnings.append(f"USB: {usb} port(s), {profile.min_usb_ports}+ recommended.")
    bluetooth = probe.get("has_bluetooth")
    if bluetooth is not None and not bluetooth:
        warnings.append("Bluetooth: not detected.")
    return UHOMEPreflightResult(passed=not issues, issues=issues, warnings=warnings, probe=probe)

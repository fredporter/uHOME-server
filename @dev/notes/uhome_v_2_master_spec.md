# uHOME v2 Master Architecture Specification

(Upgraded from v1.5.3 Kiosk + Local Network Server Spec)

---

# Purpose

uHOME v2 defines the **local-first household server platform** for the uDOS ecosystem.

It provides:

- local infrastructure host
- kiosk UI environment
- home automation integration
- local vault and service hosting
- media and game services
- automation extension runtime
- controller‑first household interface

uHOME is designed to operate **independently of cloud services**, while still supporting optional integration through the Empire extension.

The system is composed of:

- uHOME-server (core)
- uHOME-matter extension
- uHOME-empire extension
- optional Android / iOS / tablet kiosk and portal clients

---

# Upgrade from v1.5.3

The original **Android kiosk + LAN server concept** remains valid and is expanded into a full modular platform.

Key upgrades:

- kiosk concept generalized beyond Android
- controller-first design standardized
- streaming and device casting surfaces added
- automation and cloud sync modularized
- Home Assistant + Matter integrated as extension
- Jellyfin media server integrated into core
- Steam/game launcher capabilities formalized

---

# Repository Boundaries

uHOME remains **separate from the main uDOS repo**.

Repositories:

- uHOME-server
- uHOME-matter
- uHOME-empire
- uHOME-app-android
- uHOME-app-ios

Clients consume contracts exposed by uHOME-server.

---

# Topology

## Server

- always-on machine on local network
- hybrid Linux / Windows deployment supported

Preferred architecture:

Linux side hosts:

- uHOME-server
- Wizard
- Sonic
- Empire
- Jellyfin
- Matter subsystem

Windows "toybox" side may host:

- Steam
- auxiliary software
- gaming tools

Windows is **never the orchestration authority**.

Linux host remains the primary system controller.

---

# Core System: uHOME-server

uHOME-server is the **always-on household infrastructure node**.

Responsibilities:

- kiosk GUI host
- local service routing
- media services
- vault exposure
- network bridge
- streaming/casting surfaces
- decentralized library map

## Included Services

### Jellyfin

Jellyfin is the primary media server.

Responsibilities:

- media library hosting
- local streaming
- playback metadata
- household media management

Jellyfin integrates directly into kiosk UI surfaces.

### Steam / Game Services

uHOME-server supports Steam presence and gaming launch surfaces.

Capabilities:

- Steam library access
- remote play support
- game launcher integration
- controller‑first navigation

---

# Kiosk Environment

uHOME provides a **Steam‑console‑style launcher interface**.

This UI is designed primarily for:

- TVs
- tablets
- living room displays

Primary design principle:

Controller‑first navigation.

Input support:

- Xbox controllers
- PlayStation controllers
- Bluetooth HID gamepads
- keyboard
- mouse
- touch

Gamepad is the **primary interaction model**.

---

# Main UX Surfaces

## Living‑Room Launcher

Features:

- tile-based launcher
- big-screen friendly
- controller-first navigation
- access to household services

Launch targets include:

- media
- games
- automation
- vault content
- dashboards

## Thin‑GUI Kiosk Mode

Thin‑GUI surfaces can be pushed or streamed to:

- tablets
- TVs
- secondary displays

These surfaces display:

- job status
- dashboards
- playback status
- automation panels

## Media Panel

Provides:

- Jellyfin library browsing
- playback controls
- queue management

## Jobs / Scheduling Panel

Displays:

- scheduled jobs
- automation status
- retries / failures

Jobs may originate from:

- Empire
- Wizard
- local automation scripts

---

# Device Streaming

uHOME-server can push kiosk or UI surfaces to devices on the LAN.

Supported content types:

- Thin-GUI menus
- video streams
- image displays
- rendered HTML

Target devices include:

- tablets
- TVs
- browsers
- secondary kiosk clients

---

# Local Network Infrastructure

uHOME-server includes a **network infrastructure map**.

It tracks:

- connected servers
- vault libraries
- media libraries
- connected clients
- extensions

This allows the kiosk to visualize the household infrastructure.

---

# uHOME Networking Modes

## Default Mode

Standard home networking.

Supports:

- WiFi
- Ethernet
- existing routers

No Wizard required.

## Advanced Mode (Wizard Managed)

Wizard may define advanced networking profiles.

Profiles include:

### Beacon

- public/open network
- visible
- local vault access only
- no internet sharing

### Crypt

- visible network
- password protected
- local vault access
- no internet sharing

### Tomb

- hidden network
- discovery-based access
- no public internet access

### Home

- private household network
- password protected
- may be hidden or visible

Wizard defines policies but **uHOME-server hosts the runtime services**.

---

# uHOME-matter Extension

The uHOME-matter extension provides:

- Home Assistant integration
- Matter device support
- device graph
- room/zone logic
- scenes and automations

Responsibilities:

- device pairing
- device state tracking
- automation triggers
- kiosk control panels

This extension integrates a cloned Home Assistant + Matter backend.

Device automation remains separate from Empire.

---

# uHOME-empire Extension

Empire provides **server automation and cloud sync**.

Responsibilities:

- vault mirroring
- Google API integration
- HubSpot API integration
- webhook listeners
- scheduled jobs
- binder-aware routing

Empire acts as a **low-cost Zapier-style automation engine**.

Script containers support:

- Python
- uCode

Empire runs:

- webhook triggers
- cron jobs
- event-based scripts

---

# Android Kiosk Client

Android tablets remain a supported client lane.

Features:

- multi-app kiosk mode
- controller-friendly UI
- Thin‑GUI overlays
- remote server control

Tablet role:

- control surface
- launcher client
- household dashboard

---

# LAN Discovery

Discovery options:

- manual server entry
- hostname connection

Future:

- mDNS
- Zeroconf

Trusted servers may be remembered.

---

# Session Model

Two modes:

Passive mode

- read-only
- dashboard viewing

Control mode

- authenticated
- job execution

Local-only operation is preferred.

---

# Deployment Modes

uHOME clients may operate in three modes:

Dedicated kiosk

- always-on launcher

Launcher mode

- entry point to services

Companion device

- secondary controller

---

# Acceptance Criteria

## MVP

- connect kiosk to local uHOME-server
- launcher UI functional
- controller navigation operational
- Thin‑GUI overlays visible
- job status visible

## Phase 2

- media browsing stable
- Jellyfin integration
- Steam launcher integration
- profile/session management

## Phase 3

- advanced controller remapping
- household roles
- infrastructure visualization

---

# Design Principles

- local-first
- controller-first UX
- modular extensions
- no mandatory cloud dependency
- server-hosted automation

uHOME acts as the **household digital infrastructure hub** for the uDOS ecosystem.

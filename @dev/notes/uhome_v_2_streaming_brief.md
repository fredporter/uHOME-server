uHOME-server — Local Rewind Channel Delivery Brief

Purpose

uHOME-server should be able to ingest, normalise, and locally redistribute lightweight “always-on” media channels to:
	•	uHOME-client on kiosk / TV / lounge devices
	•	uHOME Android app
	•	uHOME iOS app

For this use case, the initial target channels are:
	•	MTV Rewind — an always-on music video channel experience, positioned as ad-free, no-login, and backed by YouTube-hosted video embeds.  
	•	Cartoon Rewind — an always-on classic cartoon channel experience, also positioned as free and embedded from YouTube rather than self-hosted media.  

uHOME-server does not need to become a public CDN or a pirate media host. Its job is to act as a local network relay, controller, cache coordinator, and playback abstraction layer for approved household devices.

⸻

Core Principle

uHOME-server owns local delivery orchestration, not channel ownership.

That means:
	•	the upstream channel remains the source of truth
	•	uHOME-server handles household-safe distribution
	•	clients connect to uHOME-server first, not directly to the public site in normal use
	•	the system preserves a “TV channel” feel across the local network

The goal is to make these web-native channels feel like native uHOME broadcast surfaces.

⸻

Target Experience

A user should be able to:
	•	open uHOME-client
	•	see Music TV and Cartoon TV as local channels
	•	start playback instantly on the current device
	•	hand off the same channel to another room or device
	•	keep a shared household channel state where appropriate
	•	optionally run one channel as ambient background audio/video across the home

This should feel closer to a home media tuner than a web browser bookmark.

⸻

Delivery Model

uHOME-server should support two delivery channels for each source:

1. Video Channel

Full video + audio stream for:
	•	kiosks
	•	wall tablets
	•	lounge displays
	•	mobile/tablet apps when foregrounded

2. Audio-First Channel

Audio-priority stream or low-bandwidth mode for:
	•	phones in background mode
	•	passive listening devices
	•	low-power clients
	•	whole-home “radio style” playback

For MTV-style sources this is especially useful, since users may want the music feed without needing full video on every device.

⸻

Architectural Role of uHOME-server

uHOME-server should provide five responsibilities.

A. Source Adapter Layer

A source adapter wraps each upstream channel and translates it into uHOME-native playback metadata.

For these first two channels, the adapter should capture:
	•	source identity
	•	title
	•	artwork / icon
	•	current playback state
	•	upstream player URL
	•	media mode: video, audio-video, or audio-first
	•	policy flags
	•	local compatibility notes

Example logical adapters:
	•	channel.rewind.mtv
	•	channel.rewind.cartoons

B. Session Controller

The server maintains local playback sessions such as:
	•	living room session
	•	kitchen session
	•	bedroom session
	•	personal mobile session

This allows:
	•	join current session
	•	create isolated session
	•	sync playback
	•	resume recent channel
	•	move playback between devices

C. Local Stream Gateway

uHOME-server should expose a local network playback endpoint that clients consume instead of loading the raw site directly every time.

This gateway may operate in three modes:
	•	web passthrough mode
embedded local wrapper around the upstream player
	•	proxy-assisted mode
local reverse proxy and sanitised embed shell
	•	transcoded relay mode
optional future mode for converting source playback into a more TV-like LAN stream where technically and legally appropriate

For v2, the recommended baseline is web passthrough + proxy-assisted mode, not full restreaming by default.

D. Metadata + EPG Layer

uHOME-server should present these channels like proper TV entries:
	•	channel number
	•	channel name
	•	description
	•	current now-playing
	•	source badge
	•	content type
	•	age/profile flags
	•	available actions

This enables the same channels to appear consistently in:
	•	uHOME-client channel guide
	•	Android app
	•	iOS app
	•	remote controls / gamepad navigation
	•	future uHOME voice or automation surfaces

E. Policy / Safety Layer

Because both sources rely on third-party hosted video, uHOME-server must apply a household policy layer before exposure to clients.

This includes:
	•	admin enable/disable per channel
	•	profile restrictions
	•	child-safe visibility rules
	•	device-level access rules
	•	local-only access enforcement
	•	upstream health checks
	•	fallback messaging when upstream fails

⸻

Recommended v2 Channel Object

Each delivered channel should be normalised into a shared object model.

channel_id: channel.rewind.mtv
title: MTV Rewind
kind: linear-stream
delivery_modes:
  - video
  - audio_first
source:
  type: web-embedded
  upstream_url: https://wantmymtv.xyz/player.html
  upstream_provider: Rewind Me TV
network_scope: local
session_modes:
  - shared-house
  - personal
controls:
  - play
  - pause
  - mute
  - volume
  - next
  - previous
  - move-to-device
policy:
  admin_enabled: true
  profile_gate: optional
  recordable: false
  offline_cache: metadata-only
ui:
  hero_art: local
  icon: local
  guide_label: Music TV

Equivalent object:

channel_id: channel.rewind.cartoons
title: Cartoon Rewind
kind: linear-stream
delivery_modes:
  - video
  - audio_first
source:
  type: web-embedded
  upstream_url: https://cartoonrewind.tv/player.html
  upstream_provider: Rewind Me TV
network_scope: local
session_modes:
  - shared-house
  - personal
controls:
  - play
  - pause
  - mute
  - volume
  - move-to-device
policy:
  admin_enabled: true
  profile_gate: optional
  recordable: false
  offline_cache: metadata-only
ui:
  hero_art: local
  icon: local
  guide_label: Cartoon TV


⸻

Client Delivery Expectations

uHOME-client

uHOME-client should be the strongest “TV surface”.

It should support:
	•	full-screen 10-foot UI
	•	remote/gamepad navigation
	•	instant channel switching
	•	now-playing overlay
	•	ambient playback mode
	•	household shared session mode

This is the primary destination for these channels.

Android App

The Android app should support:
	•	local discovery of uHOME-server
	•	direct playback from server session endpoint
	•	cast / handoff to kiosk or TV client
	•	picture-in-picture where supported
	•	audio-background mode for music channels
	•	quick launch widgets for favourite channels

iOS App

The iOS app should support:
	•	local discovery of uHOME-server
	•	direct playback from server session endpoint
	•	handoff to active household session
	•	audio-first playback mode
	•	simple remote-control mode for shared screens

⸻

UX Positioning

These channels should not appear as “open website”.
They should appear as:
	•	Music TV
	•	Cartoon TV

with optional detail showing source attribution.

That keeps uHOME coherent and avoids dumping users into raw browser UX.

Recommended guide presentation:
	•	Channel 21 — Music TV
	•	Channel 22 — Cartoon TV

Optional subtitle:
	•	“Powered by Rewind channel adapter”

⸻

Networking Model

uHOME-server should treat this as a LAN-first service.

Required
	•	mDNS / local discovery
	•	local HTTP(S) service
	•	authenticated household pairing
	•	per-device capability negotiation

Preferred
	•	local websocket state sync
	•	adaptive bandwidth mode
	•	session persistence
	•	low-latency control relay

Avoid by default
	•	public internet exposure of the home relay
	•	unrestricted WAN rebroadcast
	•	permanent restreaming copies of third-party media

⸻

Legal / Platform Boundary

Both referenced services explicitly describe themselves as non-commercial archival projects and state that content is embedded from YouTube rather than hosted directly by them.  

So the uHOME-server brief should assume:
	•	no claim of ownership over source media
	•	no bulk downloading as default behaviour
	•	no permanent media mirroring
	•	no public redistribution layer
	•	metadata caching is acceptable
	•	playback should remain tied to lawful, household-local access patterns

For v2, the safest architecture is:
	•	local wrapper
	•	local control plane
	•	local session sync
	•	no default archival ingest of the actual media files

⸻

Recommended v2 Implementation Stages

Stage 1 — Wrapped Local Playback

Deliver quickly with:
	•	channel registry
	•	local guide entries
	•	embedded local playback shell
	•	session state sync
	•	Android/iOS/client playback handoff

Stage 2 — Smart Relay Layer

Add:
	•	local reverse proxy
	•	sanitised embed handling
	•	bandwidth mode switching
	•	audio-first mode
	•	health/failure monitoring

Stage 3 — Full Home Broadcast UX

Add:
	•	shared “currently on” household channel mode
	•	favourites and presets
	•	scheduled autoplay
	•	automation hooks
	•	room-based session routing
	•	local channel guide / pseudo-EPG

⸻

Recommended v2 Boundary Statement

uHOME-server is a local media orchestration layer for household-approved web-native channels.
It does not replace the upstream service, and it does not act as a public rebroadcaster.
Its purpose is to convert approved internet channels into stable, controllable, room-aware uHOME playback surfaces for uHOME-client and mobile apps.

⸻

Final Recommendation

For uDOS v2 / uHOME:
	•	treat these two sources as adapter-backed local channels
	•	deliver them through uHOME-server
	•	expose them as LAN-native TV services
	•	support both video mode and audio-first mode
	•	keep the initial implementation wrapper/proxy based, not full media restreaming
	•	make uHOME-client the premium TV surface, with Android/iOS as companion and personal playback surfaces

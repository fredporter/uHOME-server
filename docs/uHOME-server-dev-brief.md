uHOME-server repo — @dev workspace and #binder workflow note

This note defines how the uHOME-server repo should align with the same @dev workspace and development workflow used by the uDOS core repo, while maintaining a disciplined separation between local development activity and the distributable server repo.

The uHOME-server project should operate as a governed development stream within the uDOS ecosystem, using #binders to track milestones, objectives, and pending development work, and using the @dev workspace as the primary active development surface.

⸻

Purpose

The uHOME-server repo should:
	•	follow the same @dev workspace conventions as the uDOS core repo
	•	track development milestones and objectives using #binders
	•	allow local development scaffolding and experimental work within a local extension layer
	•	prevent dev-mode artifacts from leaking into the distributable repo
	•	restrict public repo contributions to approved contributors only

The uHOME-server repo therefore represents a curated output surface, while active development occurs in the @dev workspace and local extension environment.

⸻

Core alignment with uDOS core

uHOME-server development should mirror the same high-level workflow used by uDOS core.

Shared development model
	•	@dev workspace = active development environment
	•	#binder = mission, milestone, or objective container
	•	local extension supports development scaffolding and background advancement
	•	compiled binder outcomes are reviewed before repo promotion
	•	repo commits are milestone-driven and contributor-governed

This ensures the uHOME-server repo remains clean, stable, and distributable, while allowing flexible development locally.

⸻

Shared lifecycle

All uHOME-server development should follow the same binder lifecycle used in uDOS core.

Open
Hand off
Advance
Review
Commit
Complete
Compile
Promote

Meaning

Open
Define a new objective or development mission.

Hand off
Prepare the binder so it can be progressed locally.

Advance
Perform bounded development progress inside the @dev workspace.

Review
Evaluate results, identify risks, and check milestone alignment.

Commit
Checkpoint progress locally.

Complete
Objective outcome has been achieved.

Compile
Clean development artifacts and prepare a final binder outcome.

Promote
Approved contributors selectively move outputs into the distributable repo.

Important rule:

local completion does not imply repo contribution.

⸻

uHOME-server inside @dev

The uHOME-server project should have a defined space inside the shared development workspace.

Example conceptual structure:

@dev/
  uhome-server/
    workspace/
    binders/
    local-extension/
    review/
    compost/

This allows uHOME-server development to remain consistent with uDOS core workflow patterns.

⸻

Recommended @dev sections

workspace/

Active development notes, scratch work, experiments, and temporary tasks.

binders/

All development missions, milestones, fixes, and feature streams.

local-extension/

Local tools, automation helpers, prototypes, dev utilities, adapters, and unpublished scaffolding.

review/

Artifacts awaiting review or approval before repo promotion.

compost/

Deprecated experiments, stale drafts, or abandoned exploratory work.

⸻

#binder usage for uHOME-server

All meaningful development work should be tracked using #binders.

Binders represent:
	•	milestones
	•	feature work
	•	infrastructure updates
	•	server configuration improvements
	•	integration work
	•	migration tasks
	•	documentation revisions
	•	packaging and release preparation

Example binders

#binder/uhome-server-local-network-runtime
#binder/uhome-server-auth-layer
#binder/uhome-server-api-routing
#binder/uhome-server-device-integration
#binder/uhome-server-installation-flow
#binder/uhome-server-release-prep-v1


⸻

Binder role in server development

Each binder should document:
	•	the mission objective
	•	associated milestone
	•	current state
	•	development tasks
	•	blockers or dependencies
	•	areas of the codebase affected
	•	local development artifacts
	•	potential promotion candidates
	•	compile and completion criteria

This ensures server development progress is structured and inspectable.

⸻

Advancing pending development tasks

Pending uHOME-server development should be progressed within the @dev workspace.

Advancement should:
	•	occur locally first
	•	follow binder mission boundaries
	•	advance incrementally
	•	maintain milestone alignment
	•	avoid uncontrolled mutation of the public repo
	•	produce reviewable outcomes

Development should therefore follow this flow:

@dev workspace
    ↓
binder advancement
    ↓
review
    ↓
compile
    ↓
promotion
    ↓
public repo


⸻

Milestones and objectives

uHOME-server development should organize work into milestones and objectives.

Milestones

Major development checkpoints such as:
	•	server runtime stabilization
	•	local network service architecture
	•	device integration support
	•	authentication layer
	•	API routing normalization
	•	installer and deployment tooling
	•	release preparation

Objectives

Specific outcomes that contribute to a milestone.

Examples:
	•	configure local network service layer
	•	implement device discovery
	•	normalize API endpoint routing
	•	add configuration loader
	•	implement authentication gateway
	•	finalize installation documentation

Binders

Execution containers for objectives.

Hierarchy example:

Milestone
  -> Objective
    -> #binder

or

Milestone
  -> #binder

for larger development streams.

⸻

Local extension model

uHOME-server development requires a local extension layer that supports experimentation and development tooling.

This layer should remain outside the distributable repo.

Purpose of local extension

Local extension may contain:
	•	experimental server modules
	•	local configuration scaffolds
	•	development utilities
	•	automation helpers
	•	binder runtime state
	•	test harnesses
	•	temporary scripts
	•	review staging artifacts
	•	experimental integrations

Principle:

local extension is flexible and experimental; the distributable repo is curated and stable.

⸻

Contribution boundary

The uHOME-server repo must enforce a clear contribution boundary.

Rule

Only approved contributors may promote changes into the distributable repo.

This ensures:
	•	development scaffolding remains local
	•	experimental code does not pollute the repo
	•	architectural stability is preserved
	•	release surfaces remain clean

⸻

Promotion workflow

Promotion should follow a structured process.

local @dev workspace
    ↓
binder compile
    ↓
review
    ↓
approval
    ↓
contributor promotion
    ↓
distributable repo

This ensures that the repo reflects intentional, curated development outcomes.

⸻

Gitignore scaffold for local development

The uHOME-server repo should include gitignore patterns that exclude local development artifacts.

Example categories

# uDOS dev workspace
.dev/
@dev/
binders/
.local-extension/
.local/
.compost/
review-staging/
workspace-state/

# Local notes and drafts
*.local.md
*.draft.md
*.scratch.md
*.temp.md

# Machine-specific configuration
.env.local
.env.dev.local
*.machine.json
*.local.json
*.cache.json

# Binder runtime state
binder-state/
binder-cache/
binder-runs/
workflow-state/
workflow-cache/

# Review and compile staging
compile-staging/
promotion-staging/
approval-staging/

# Editor/system files
.DS_Store
Thumbs.db
.vscode/
.idea/

This prevents development artifacts from entering the repo unintentionally.

⸻

Recommended uHOME-server workflow

1. Open a binder

Create a binder representing the development objective.

Example:

#binder/uhome-server-api-routing
#binder/uhome-server-device-discovery
#binder/uhome-server-installation-flow


⸻

2. Work inside @dev

All experimentation, notes, and development should occur within the uHOME-server area of the @dev workspace.

⸻

3. Advance development

Progress binders incrementally while maintaining milestone alignment.

⸻

4. Review candidate outcomes

Inspect which outputs should remain local and which may be promotable.

⸻

5. Compile the binder

Compile should:
	•	remove development clutter
	•	normalize documentation and scripts
	•	isolate promotable outputs
	•	archive stale materials

⸻

6. Promote approved outputs

An approved contributor moves selected outcomes into the distributable repo.

⸻

Binder metadata for uHOME-server

Example binder metadata:

binder: uhome-server-device-discovery
project: uhome-server
milestone: device-integration-v1
objective: implement local device discovery service
status: active
priority: high
mode: slow-and-low
repo_target: uhome-server
local_only: true
promotion_candidate: partial
approved_contributor_required: true
compile_target: review-ready

Additional optional fields:

files_touched:
repo_paths:
local_paths:
blockers:
review_required: true
promotion_notes:
completion_criteria:


⸻

Compile and promotion behavior

For uHOME-server, compile prepares a binder outcome for review and possible promotion.

Compile should:
	•	clean dev artifacts
	•	consolidate documentation
	•	isolate repo-ready outputs
	•	archive exploratory material
	•	produce a promotion summary

Promotion then moves approved artifacts only into the repo.

⸻

Governance rule

uHOME-server should follow the same governance philosophy as uDOS core.

The @dev workspace is the active mission development surface, #binders track development progress and objectives, local extension supports experimental work, and the distributable repo remains a curated output surface governed by approved contributors.

⸻

Short policy block for repo documentation

You may include the following summary directly in the repo documentation.

uHOME-server development follows the same @dev workspace and binder-driven workflow used by the uDOS core repo. Development objectives, milestones, and pending work are tracked as #binders within the uHOME-server area of the @dev workspace. Local extension scaffolding supports active development while remaining excluded from the distributable repo through gitignore and workspace separation. Contribution to the public uHOME-server repo is restricted to approved contributors, with changes promoted only after binder compile, review, and approval.

⸻

Suggested command pattern

Example command workflow:

binder open #uhome-server-device-discovery
binder handoff #uhome-server-device-discovery
binder advance #uhome-server-device-discovery
binder review #uhome-server-device-discovery
binder compile #uhome-server-device-discovery
binder promote #uhome-server-device-discovery


⸻

Final intent

The uHOME-server repo should remain:
	•	developed locally within @dev
	•	organized through #binders
	•	structured by milestones and objectives
	•	supported by a flexible local extension layer
	•	promoted into the distributable repo only through approved contributor governance

This keeps uHOME-server aligned with the uDOS development model while maintaining a clean and stable public repo.
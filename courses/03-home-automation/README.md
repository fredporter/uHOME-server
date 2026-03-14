# Course 03 - Home Automation

Purpose:

- explain local automation flows and bridge patterns
- connect schedules, triggers, and household devices

Topics:

- event automation
- scheduling
- smart device control
- bridge boundaries
- local-first automation distinct from `uHOME-empire` online webhooks

Repo anchors:

- `modules/home-assistant-bridge/`
- `services/bridge/`
- `services/scheduling/`
- `src/uhome_server/routes/home_assistant.py`

First project:

- implement a simple automation workflow over the sample vault

Boundary note:

- Home Assistant, Matter, and local device automation stay in `uHOME-server`
- custom online APIs and webhook jobs belong in `uHOME-empire`

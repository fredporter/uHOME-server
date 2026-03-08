# Bridge

Purpose:

- connect `uHOME` runtime services to local automation systems
- expose bridge status, discovery, and commands
- isolate external-home-system integration from core server flows

Current runtime anchors:

- `src/uhome_server/services/home_assistant/`
- `src/uhome_server/services/home_assistant_service.py`
- `src/uhome_server/routes/home_assistant.py`

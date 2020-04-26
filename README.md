# Project Planner
Creates Project Outlines and Hardware Planning For IT Installations
- Checklist to ensure cabling, switch ports, drive space, etc... prior to quoting
- Creates base project outline

### Architecture
- Backend: Python w/ JSON component files
- Frontend: Flask (python)

### Development Phases
1: Base backend logic with hardcoded components and text-only output

2: Move components options to JSON file

3: Move frontend to web-based deployment

4: Option to import previous project configs/save work between sessions

5: User profiles/logins

### To-Do List
- Update base logic for remaining components
- Phases 2-5

### Notes
- Considering components with database, JSON files seem more "portable"
- Considering Django depending on complexity, starting with Flask for simplicity
- After phase 5, looking at login options like SAML/OAuth

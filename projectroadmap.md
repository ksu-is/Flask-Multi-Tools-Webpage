## SPRINT 1

- [x] Create Github Account, Github Desktop, VS Code
- [x] Join ksu-is Github organization
- [x] State project idea in Project Spreadsheet in Teams
- [x] Create project repository on ksu-is with README.md and projectroadmap.md
- [x] Search related existing repositories on Github and clone it to my github account:
  - First found: flask-tool-page (https://github.com/ksu-is/flask-tool-page.git):
    - [x] Fork and Clone to local laptop
    - [x] Read through, attempt to run it, evaluate, any issues occur should be documented in "Sprint 1" section:
      - issue found : Grade Tracker tab appears to be "404 Not Found"
        - This is intentional: not having code line @app.route("/grades"), but do have @app.errorhandler(404)
      - issue found : Temperature Converter tab appears "400 Bad Request: The browser (or proxy) sent a request that this server could not understand. KeyError: 'tem_value'
        - Solution: correct the variable name from 'tem_value' to 'temp_value'
      - issue found: duplicate content in calculator.html and converter.html due to lack of general structure template "layout.html"
        - solution: - create layout.html with {%block content%} {& end block%}
                    - In other templates, {% extends 'layout.html' %}

## SPRINT 2
- [x] Learn Flask tutorial in Youtube
- [x] Coding and using git to manage code
- [x] Make updates and add commit messages in KSU-IS repository
- [x] Commit at least 6 code changes of significant size

## Sprint 3
- [x] More coding, refining, testing
- [x] Explore more capabilities for the web
- [x] Restyle the website appearance
- [x] Add comments where are appropriate
- [x] Updating README.md and projectroadmap.md
- [x] Create ppt slide showing team members, title, purpose of project, and a copy to Github repository
- [x] Schedule presentation meeting on Teams
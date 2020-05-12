A Shiny-based, Reproducible Lab Notebook Gateway
================================================

The purpose of this project is to develop a Shiny-based, reproducible lab notebook. 


Minimum set of features for launch:
-----------------------------------------------

1. Web browser support
1. Homepage with calendar and todo list
1. Synchronization of calendar and todo list with your favorite service (start with Google, Outlook, and Todoist?)
1. One-touch creation of reproducible lab notebook "page" consisting of an RMarkdown file titled by the date
1. Reproducibility managed by mandatory inclusion of `workflowr` and `renv` (or equivalent)

Dependencies:
-------------

- `shiny`: powers the interactivity
- `workflowr`: enforces the reproducibility
- `renv`: streamlines the reproducibility
- `blogdown`: hosts the site (?)
- [packages for the integration of calendar and other services]
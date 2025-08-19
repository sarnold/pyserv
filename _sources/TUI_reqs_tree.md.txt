# 1.0 TUI Requirements {#TUI_006}

TUI Requirements

The `daemontui` script provides a convenient way to run any of the existing
daemon scripts with default (but adjustable) values. The TUI interface can
support both keyboard and mouse input (as long as the underlying console
also supports mouse input) for both option selection and navigation. The
Debug option will increase verbosity both in the daemon log output and the
TUI parameters (on exit).


## 1.1 TUI_001 {#TUI_001}

The server TUI **Shall** run any of the pyserv daemons.

*Child links: SDD_003*

| Attribute | Value |
| --------- | ----- |
| normative | True |


## 1.2 TUI_002 {#TUI_002}

The server TUI **Shall** set default values for required daemon options.

*Child links: SDD_002, TST_002*

| Attribute | Value |
| --------- | ----- |
| normative | True |


## 1.3 TUI_003 {#TUI_003}

The server TUI **Shall** provide user controls to edit/modify default values.

*Child links: SDD_002*

| Attribute | Value |
| --------- | ----- |
| normative | True |


## 1.4 TUI_004 {#TUI_004}

The server TUI **Shall** provide individual UI elements to control the
selected daemon.

*Child links: SDD_004*

| Attribute | Value |
| --------- | ----- |
| normative | True |


## 1.5 TUI_005 {#TUI_005}

The server TUI **Shall** display log output from the currently
running daemon.

*Child links: SDD_003, TST_003*

| Attribute | Value |
| --------- | ----- |
| normative | True |



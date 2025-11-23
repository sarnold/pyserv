Changelog
=========


1.9.0 (2025-11-23)
------------------

Changes
~~~~~~~
- Cleanup doc bits, tool configs, and some lint. [Stephen L Arnold]


1.8.11 (2025-11-22)
-------------------

Changes
~~~~~~~
- Use transitional rpm deps in workflow, review doorstop bits. [Stephen
  L Arnold]

  * update changelog file for release
- Revert diagram markup to (re)generate dep graph. [Stephen L Arnold]

  * add checkout workaround for pull request action
- Update doorstop doc items, restore comment markers. [Stephen L Arnold]
- Replace pygtail with logwatcher, update log handling and deps.
  [Stephen L Arnold]


1.8.10 (2025-11-03)
-------------------

Changes
~~~~~~~
- Bump daemonizer to latest release in setup.cfg and reqs files.
  [Stephen L Arnold]


1.8.9 (2025-11-03)
------------------

Changes
~~~~~~~
- Bump daemonizer to latest in all reqs files and setup.cfg. [Stephen L
  Arnold]

  * bump all the deps in requirements-rpm.txt to latest

Fixes
~~~~~
- Restore missing async argparser defaults, cleanup logging. [Stephen L
  Arnold]

  * fix lpname string split in daemontui script
  * fix missing arg defaults in async argparser, cleanup help strings
  * cleanup logging configuration, set daemon class logging to INFO only
  * align server logging with parent cfg, move asyncio setup out of try block


1.8.8 (2025-09-11)
------------------

New
~~~
- Add rpm sbom dependency workflow, mv ci scripts to .github dir.
  [Stephen L Arnold]

Changes
~~~~~~~
- Remove experimental daemontui script from installed files. [Stephen L
  Arnold]

  * update readme and project files, cleanup pylint and version bits


1.8.7 (2025-08-19)
------------------

Fixes
~~~~~
- Remove deprecated version attribute from package metadata. [Stephen L
  Arnold]

  * bump github deps to latest versions with the same fix


1.8.6 (2025-08-15)
------------------

Changes
~~~~~~~
- Bump picotui to latest version, use tags in pip URLs. [Stephen L
  Arnold]


1.8.5 (2025-08-10)
------------------

Changes
~~~~~~~
- Add readme admonition about change in previous behavior. [Stephen L
  Arnold]

Fixes
~~~~~
- Add fallback values for empty environment settings. [Stephen L Arnold]

  * provide the same default values for each setting var if set but empty
  * add another test using monkeypatched empty values
  * update requirements file and coverage config

  this closes issue #62


1.8.4 (2025-07-21)
------------------

Changes
~~~~~~~
- Update changelog for packaging release. [Stephen L Arnold]
- Backport metadata from pyproject.toml to setup.cfg, relax versions.
  [Stephen L Arnold]

  * makes things compatible with ancient el9 setuptools


1.8.3 (2025-07-21)
------------------

New
~~~
- Add requirements file of wheel URLs for flatpak-generator. [Stephen L
  Arnold]

  * use a different dep format for all the git+https urls
  * update project files to match wheel deps

Changes
~~~~~~~
- Update dependency versions, add GH cli workflow. [Stephen L Arnold]

  * downloading specific rpm assets from specified tags
- Remove psutil, along with related get_iface funcs and tests. [Stephen
  L Arnold]
- Add flatpak generator tool and cleanup docs review and config.
  [Stephen L Arnold]

Fixes
~~~~~
- Cleanup and update dependencies and imports, update tox and readme.
  [Stephen L Arnold]

  * ignore one spurious flake8 warning in daemontui.py


1.8.2 (2025-06-15)
------------------

New
~~~
- Make sphinx config use git to get last non-dev versions. [Stephen L
  Arnold]

  * this should work as long as at least 2 tags exist

Changes
~~~~~~~
- Disable fallback version logic, go through release workflow as-is.
  [Stephen L Arnold]
- Disable link-checker command in CI to workaround extension error.
  [Stephen L Arnold]

  * upstream issue: https://github.com/danirus/sphinx-nefertiti/issues/66
- Add sphinx_nefertiti and mermaid extensions, cleanup conf.py. [Stephen
  L Arnold]
- Update and pin git-based dependencies. [Stephen L Arnold]

Fixes
~~~~~
- Add another pytest ignore, update container workflow. [Stephen L
  Arnold]

  * bare github container plus rawhide equals broken workflows
  * force py3.13 on rawhide to avoid building platform wheels from source


1.8.1 (2025-06-03)
------------------

Changes
~~~~~~~
- Update, review, and regenerate doorstop doc bits. [Stephen L Arnold]

Fixes
~~~~~
- Use string for license expression, cleanup deps. [Stephen L Arnold]

  * cleanup crufty picotui dev branch, use master#hash


1.8.0 (2025-06-01)
------------------

New
~~~
- Add doorstop TST document with test items, links, and references.
  [Stephen L Arnold]

  * add test keywords and move some tests, update design doc
  * add test doc to sphinx build
  * note: the reference file test_extras.py causes a doorstop error
    but with the same tests and keyword moved to a new file it works
    just fine (using tests/test_timer.py as reference file)
- Add post-process script for munging markdown diagrams in CI. [Stephen
  L Arnold]

  * works with render-md-mermaid action to convert image URLs required
    by action into myst-parser captions
  * remove extra diagram clutter
- Add small template func to munge markdown after render. [Stephen L
  Arnold]

  * diagrams workflow needs a helper to replace the simple image
    syntax with a myst diagram directive
  * add some extra (temporary) image URLs to goose multiple files in CI
- Add new doorstop doc for sw design bits, link to parent reqs. [Stephen
  L Arnold]
- Replace refresh button with a separate thread. [Stephen L Arnold]

  * call the refresh func with its own daemon thread on a smallish interval
  * update packaging and deps for daemontui script, cleanup imports and typos
- Add pid check and kill on exit, use DEBUG for console output. [Stephen
  L Arnold]
- Add IDEV environment var to settings. [Stephen L Arnold]

  * flake8 config file to replace what was in setup.cfg, update tox file
- Testing doorstop for collecting TUI requirements. [Stephen L Arnold]

Changes
~~~~~~~
- Update changelog for release. [Stephen L Arnold]
- Update changelog cfg, coverage paths, change deps. [Stephen L Arnold]

  * improve changelog cleanliness, use setuptools_scm to get version
- Sync up documented minimum supported python version. [Stephen L
  Arnold]
- Remove support for older python versions. [Stephen L Arnold]

  * rmove old importlib and http handler checks
  * ignore thread deprectation warnings from pytracer in pytest cfg
- Add implementation references to SDD bits, update workflows. [Stephen
  L Arnold]

  * limit container workflow to available redhat-ish and deb containers
  * allow for github container emptyness and set version via env
- Update doorstop doc sources, move thread timer class to module.
  [Stephen L Arnold]
- Cleanup python requirements. [Stephen L Arnold]
- Refactor workflow helper to remove external python deps. [Stephen L
  Arnold]
- Revert to original render-md-mermaid, add svg target. [Stephen L
  Arnold]

  * make sure bogus image link only exists in doorstop item
  * allow contents and pull-requests perms for cpr action
- Cleanup initial reqs experiment, add header item for docs. [Stephen L
  Arnold]

  * include the generated doorstop doc in sphinx build, update conf
  * cleanup readme, add animated gif generated from desktop recording
  * add doorstop to dev environment and docs cmd
- Add server status indicator to run console, update screenshot.
  [Stephen L Arnold]
- Add ui note about mouse support, update docs. [Stephen L Arnold]

  * add some console screenshots and a brief daemontui description
- Flesh out daemontui controls, update doorstop dep to fork. [Stephen L
  Arnold]
- Revert to sphinx contrib apidoc, apply type hints, reformatting.
  [Stephen L Arnold]

  * update project files, ignore mypy errors in tui script
- Add more type annotations, update tests and conf.py. [Stephen L
  Arnold]
- Add basic tests for tui_helpers, check for empty lines. [Stephen L
  Arnold]

  * make sure we check for an empty line in the list from pygtail
  * allow line-shortening by splitting on space char, ie, using
    shorten=3 drops leading date chars (depending on format)
- Add more (optional) deps for tui experiments. [Stephen L Arnold]

  * update daemontui log display, split out helper funcs from tui source
  * update project, tox, and reqs files
- Update server logging configs, misc cleanup, update daemontui.
  [Stephen L Arnold]

  * allow env override for log file path instead of console
- Update doorstop doc config, edit some reqs, create a new one. [Stephen
  L Arnold]
- Update picotui example, add workarounds for doorstop deps. [Stephen L
  Arnold]
- Skip 2 tests on windows and file a bug in psutils repo. [Stephen L
  Arnold]
- Refactor get_iface funcs to only return strings, update tests.
  [Stephen L Arnold]

  * split original into 3 separate functions that should always return
    a (possibly empty) string and not raise an exception
- Add more settings widgets and update environment. [Stephen L Arnold]

  * populate default port number when daemon selection changes
- Make sure current widgets can update env state, cleanup lint. [Stephen
  L Arnold]
- Update reqs file and tox lint cmd, cleanup some lint. [Stephen L
  Arnold]
- Add a different get_useriface using psutil. [Stephen L Arnold]
- Update project files with picotui and doorstop deps. [Stephen L
  Arnold]

  * use .venv for dev environment or doorstop cries
- Reduce workflow permissions. [Stephen L Arnold]
- Still more corrections, rewrites, and updates for the readme. [Stephen
  L Arnold]

Fixes
~~~~~
- Cleanup imports and mypy errors, add more type hints. [Stephen L
  Arnold]

  * update tests, mypy cfg, and project files
- Use push event for current release status. [Stephen L Arnold]

  * somehow adding workflow_dispatch made github look away and
    start displaying the wrong status (where push event is now
    correct)


1.7.3 (2025-03-21)
------------------

New
~~~
- Add extended container workflow for other Linux environments. [Stephen
  L Arnold]

  * no setup-python or git commands, disable until we have more time

Changes
~~~~~~~
- Update readme with reuse compliance and sbom snippet. [Stephen L
  Arnold]
- Testing license-as-string in CI matrix. [Stephen L Arnold]


1.7.2 (2025-03-20)
------------------

Changes
~~~~~~~
- Update changelog file for next release. [Stephen L Arnold]
- Make sure included workflows get the workflow_call trigger. [Stephen L
  Arnold]

  * cleanup old runner versions, sync up artifact names
- Make sure included workflows get the workflow_call trigger. [Stephen L
  Arnold]

  * cleanup old runner versions
- Test local workflow file includes. [Stephen L Arnold]
- Simplify packaging files, remove PYTHONPATH from default env. [Stephen
  L Arnold]

  * default values *do* get inherited by named envs who do not use setenv


1.7.1 (2025-03-18)
------------------

Changes
~~~~~~~
- Update to latest bandit action for testing. [Stephen L Arnold]


1.7.0 (2025-03-18)
------------------

Changes
~~~~~~~
- Add changelog and include it as docs appendix. [Stephen L Arnold]

  * remove deprecated apidoc contrib module, use built-in instead
  * bump python version in sphinx workflow
- Really fix license badge. [Stephen L Arnold]
- Make license badge static since GH cannot recognize reuse path.
  [Stephen L Arnold]

Fixes
~~~~~
- Give release.yml a newer python version to match sphinx. [Stephen L
  Arnold]
- Migrate to non-deprecated package metadata in pyproject.toml. [Stephen
  L Arnold]

  * remove setup.cfg metadata and update tox
- Fix package metadata nit and cleanup release workflow. [Stephen L
  Arnold]

  * update .pre-commit-config.yaml and apply new formatting


1.6.3 (2024-12-24)
------------------

New
~~~
- Refactor module for async instead of importing it directly. [Stephen L
  Arnold]

  * add attribution to REUSE.toml config
  * cleanup daemon scripts

Changes
~~~~~~~
- Integrate args and env vars, try and except, update docs. [Stephen L
  Arnold]

  * mainly async daemon and tox/readme updates
- Async integration and cleanup commit that broke something. [Stephen L
  Arnold]
- Cleanup tftpd logging, add async dep for testing. [Stephen L Arnold]

Fixes
~~~~~
- Make sure tftpdaemon gets an absolute path for DOCROOT. [Stephen L
  Arnold]
- Convert syntax for gh-pages deploy workflow action. [Stephen L Arnold]


1.6.1 (2024-12-16)
------------------

New
~~~
- Add reuse tool to lint environment, use reuse cfg and LICENSES dir.
  [Stephen Arnold]

Changes
~~~~~~~
- Refactor test, remove pytest skip, show test output in ci workflow.
  [Stephen L Arnold]
- Fefactor platform_check, remove a branch, adjust test assert. [Stephen
  L Arnold]

Fixes
~~~~~
- Let Daemon class set the working directory, not GetServer. [Stephen L
  Arnold]

  * this only applies to the httpdaemon script
- Add daemon fallback path for XDG runtime dir. [Stephen L Arnold]

  * XDG runtime path may not exist in a console environment
  * fixes issue #23


1.6.0 (2024-10-13)
------------------

Changes
~~~~~~~
- Remove old py version from coverage workflow and tox config. [Stephen
  L Arnold]
- Restore py36 in CI coverage and tox file and bump pip req. [Stephen L
  Arnold]
- Update version handling to use setuptools_scm. [Stephen L Arnold]

  * update __init__ plus consumers, including packaging
  * some minor nit cleanup
- Still more version updates in tox workflows. [Stephen L Arnold]
- Update all workflow action vertsions, bump macos to latest. [Stephen L
  Arnold]
- Still more setup cleanup, use gh release tarballs for deps. [Stephen L
  Arnold]
- Bump repolite dep to latest release, cleanup setup.cfg. [Stephen L
  Arnold]

Fixes
~~~~~
- Add missing action version updates to ci workfolw file. [Stephen L
  Arnold]

Other
~~~~~
- Cleanup old release bits. [Stephen L Arnold]


1.5.0 (2023-09-20)
------------------

Changes
~~~~~~~
- Belated readme updates for new user paths, default tftp port. [Stephen
  L Arnold]
- Refactor/update dependencies, cleanup tests and tox. [Stephen L
  Arnold]

  * appdirs => platformdirs, minor refactor, daemonizer => 0.4.0
- Update dcos build and docs, add git info. [Stephen L Arnold]
- Move to src layout for packaging. [Stephen L Arnold]
- Add pip show command to tox package check. [Stephen L Arnold]
- Cleanup package metadata and version imports. [Stephen L Arnold]


1.4.2 (2023-08-28)
------------------

Fixes
~~~~~
- Add missing env override for tftpdaemon script. [Stephen L Arnold]

  * this is mostly a workflow fix to set the correct logging name


1.4.1 (2023-08-28)
------------------
- Fix tftpy port handling, set defaults in tftpd and daemon script.
  [Stephen L Arnold]

  * update tftpy dep to VCT-hosted patch release
  * cleanup test workflow cmd


1.4.0 (2023-08-27)
------------------

New
~~~
- Add experimental tftpdaemon script, configure via settings. [Stephen L
  Arnold]

Changes
~~~~~~~
- Just a bit more readme clarity. [Stephen L Arnold]
- Update readme with latest examples, cleanup some lint. [Stephen L
  Arnold]
- Revert previous module, adjust for alternate tftpy module. [Stephen L
  Arnold]

  * tftp server needs upstream master, add repolite cfg file
  * update tox tftp cmd with daemon/curl client test using 40Mb bin file
  * make fork release on github for somewhat more permanent pkging URL
- Update reqs file, ignore duplicate code in daemon scripts. [Stephen L
  Arnold]

  * add get_timeouts to test_extras

Fixes
~~~~~
- Cleanup new tftpy deps, docstrings, and lint, add small test. [Stephen
  L Arnold]


1.3.0 (2023-08-17)
------------------

New
~~~
- Add wsgi support, eg simple wsgi server and check script. [Stephen L
  Arnold]

  * cleanup deprecated tox directives, update pre-commit config

Changes
~~~~~~~
- Cleanup manifest warnings. [Stephen L Arnold]
- Make sure we have py36 for split tests. [Stephen L Arnold]
- Cleanup some docstrings and update a test. [Stephen L Arnold]
- Cleanup tox/test nits, update wsgi module and black formatting.
  [Stephen L Arnold]

Fixes
~~~~~
- Post-rebase cleanup, remove unused import from daemon script. [Stephen
  L Arnold]

Other
~~~~~
- Revert covdefault changes, go back to 3.6 in split coverage ci.
  [Stephen L Arnold]
- Update workflow action versions, cleanup interfaces, bump py vers.
  [Stephen L Arnold]

  * fix another test nit


1.2.5 (2022-10-18)
------------------

Changes
~~~~~~~
- Move old directory support to serv_run, update daemon script. [Stephen
  L Arnold]
- Spread matrix workflows across more python/platform versions. [Stephen
  L Arnold]

  * make GetHandler compatible with py36, update mypy config
  * update project and tox files to match workflow versions

Fixes
~~~~~
- Handle nonexistent DOCROOT in serv_init, update readme. [Stephen L
  Arnold]

  * remove superflous daemon check, it will raise FileNotFound error
    if home_dir (ie, doc root) does not exist
  * include honcho proc/env files in sdist
- Make things work on py36, add tests, skip one test on py36. [Stephen L
  Arnold]

  * use GetHandler without the directory arg on py36, change to docroot
    in run method instead
- Refactor GetServer to be compatible with older python pre-3.7.
  [Stephen L Arnold]

  * make log/pid file names a user-settable environment var (default: httpd)
  * update pip install URLs and docstrings, update readme/tox files

Other
~~~~~
- Cgh: dev: try combining python version coverage in current workflow.
  [Stephen L Arnold]

  * split coverage in tox file from testenv


1.2.4 (2022-08-24)
------------------

Changes
~~~~~~~
- Update serv example command in readme file. [Stephen L Arnold]
- Remove environment marker from daemonizer dep, use PEP440 url.
  [Stephen L Arnold]

  * sadly this is required for "stock" Ubuntu focal since it does not
    appear to understand PEP345 markers
  * this means we have to rely on readme blurb about posix daemon
    not compaitble with Windows


1.2.3 (2022-08-22)
------------------

Changes
~~~~~~~
- Add post-release docs build job to release workflow. [Stephen L
  Arnold]

  * make sure we have matching docs version on release
- Update setup metadata => author info and python versions. [Stephen L
  Arnold]
- Improve iface settings display, cleanup/disable logging_tree. [Stephen
  L Arnold]

  * make reqs spec compatible with py38

Fixes
~~~~~
- Ripple cmd changes to all affected workflows. [Stephen L Arnold]
- Make sure tox cmds match the release workflow. [Stephen L Arnold]
- Remove one picky pylint warning. [Stephen L Arnold]


1.2.2 (2022-07-15)
------------------

New
~~~
- Add minimal argparse, mainly for help and version. [Stephen L Arnold]

  * daemon class does not like having its args handled, so
  * use settings defaults or ENV variables for daemon config

Changes
~~~~~~~
- Fix doc string formatting in settings. [Stephen L Arnold]
- Fix set log level, add test assert, cleanup test imports. [Stephen L
  Arnold]
- Add DEBUG var for serv cmd logging, update readme. [Stephen L Arnold]
- (un)refactor moving to argarse, go back to env vars. [Stephen L
  Arnold]

  * argparse with daemonizer is not a great mix
- Refactor with argparse instead of env vars. [Stephen L Arnold]

Fixes
~~~~~
- Tox file and lint cleanup, daemon not runnable on windows. [Stephen L
  Arnold]

  * mark test_platform_check with @pytest.mark.skipif

Other
~~~~~
- Fx: dev: cleanup thread deprecation warnings. [Stephen L Arnold]

  * lower required coverage to 85 percent, <sigh> Windows skip
- Update issue templates. [Steve Arnold]


1.2.1 (2022-07-09)
------------------

New
~~~
- Add coverage workflow and fix_pkg_name coverage script. [Stephen L
  Arnold]
- Add httpdaemon script, cleanup logging, update tox file. [Stephen L
  Arnold]

Changes
~~~~~~~
- Update minimum daemon requirement to latest release. [Stephen L
  Arnold]
- Add post-install check for daemon script, cleanup setup.cfg. [Stephen
  L Arnold]

  * add coverage/status badges to readme file
- Flesh out sdist using MANIFEST.in file. [Stephen L Arnold]
- Add more tests and coverage controls, mark main/serv_run no cover.
  [Stephen L Arnold]
- Remove superfluous check, fix test name, add more tests. [Stephen L
  Arnold]
- Refactor some bits, add some tests, update reqs and tox files.
  [Stephen L Arnold]
- More docstring cleanup, add debug logging for thread info. [Stephen L
  Arnold]
- Switch desc back to docstring, remove unused imports. [Stephen L
  Arnold]
- Add missing arg check, simplify platform error. [Stephen L Arnold]
- Add platform check and change dir to doc root. [Stephen L Arnold]
- Revert optional deps, allow broken daemon script on windows. [Stephen
  L Arnold]
- Update readme, cleanup packaging, add devenv file. [Stephen L Arnold]

  * make daemonizer deps optional => [dev] and add to readme
  * add conda devenv file with conda deps (use pip for daemonizer)
- Move script to no-extension, add symlink for py. [Stephen L Arnold]
- Package daemon script, update cfgs, apply cleanup. [Stephen L Arnold]
- Switch to threaded http.server class, update docstrings. [Stephen L
  Arnold]
- More refactoring, allow iface arg, update readme. [Stephen L Arnold]
- Refactor stand-alone run() interface for daemon script. [Stephen L
  Arnold]

  * add settings file with env overrides for user defaults
  * split run() into init and foreground runner
  * update tox file with default env and deps
  * add appdirs dep to setup.cfg

Fixes
~~~~~
- Use tuple of names and add platform check for logdir. [Stephen L
  Arnold]
- Handle thread shutdown cleanly, cleanup readme and docstrings.
  [Stephen L Arnold]
- Pylint needs egg_info in clean ci environment. [Stephen L Arnold]
- Packaging and lint cleanup, add damonizer deps. [Stephen L Arnold]

  * cleanup pylint and flake8 warnings, update setup.cfg and tox files
  * add daemon script dependencies to install_requires
  * install stand-alone httpdaemon script to venv bin dir
  * show both default paths and env values in settings display


1.2.0 (2022-06-27)
------------------

New
~~~
- Use versioningit to maintain package versioning. [Stephen L Arnold]

  * convert pkg from py_module to package
  * add module init for version/description metadata
  * add config to project files, update tox and .gitignore
  * add base tag for last upstream version
- Add pre-commit and pep8speaks configs, apply cleanup. [Stephen L
  Arnold]
- Add the usual github workflows for python. [Stephen L Arnold]
- Add docs build, cleanup doc strings, update readme/tox files. [Stephen
  L Arnold]

Changes
~~~~~~~
- Add pre-commit section to readme. [Stephen L Arnold]
- Still-another-readme-update. [Stephen L Arnold]
- Yet-another-readme-update. [Stephen L Arnold]
- Add honcho dependency, plus basic env and Procfile. [Stephen L Arnold]
- Update (minimal) readme. [Stephen L Arnold]
- Remove clutter, try SimpleHTTPRequestHandler instead. [Stephen L
  Arnold]

Fixes
~~~~~
- Use the right branch name for pylint badge. [Stephen L Arnold]
- Cleanup some lint in server and tox files. [Stephen L Arnold]
- Flesh out get wrapper and logging, rewrite get path ftw. [Stephen L
  Arnold]

  * this now works with the dialog ota_update console cmds
- Give it a proper main() and modern packaging. [Stephen Arnold]


1.1.0 (2019-12-18)
------------------
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- File change. [Dheeraj M Pai]
- Initial commit. [dheerajmpai]

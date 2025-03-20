Changelog
=========


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

Other
~~~~~
- Merge pull request #33 from sarnold/reusable-workflows. [Steve Arnold]

  cleanup linked workflows
- Merge pull request #32 from sarnold/reusable-workflows. [Steve Arnold]

  Reusable workflows
- Merge pull request #31 from sarnold/packaging-fixes. [Steve Arnold]

  Packaging fixes


1.7.1 (2025-03-18)
------------------

Changes
~~~~~~~
- Update to latest bandit action for testing. [Stephen L Arnold]

Other
~~~~~
- Merge pull request #30 from sarnold/action-tests. [Steve Arnold]

  Action tests


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

Other
~~~~~
- Merge pull request #29 from sarnold/workflow-cleanup. [Steve Arnold]

  fix release docs
- Merge pull request #28 from sarnold/package-up. [Steve Arnold]

  migrate packaging to toml
- Merge pull request #27 from sarnold/workflow-cleanup. [Steve Arnold]

  Workflow cleanup


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

Other
~~~~~
- Merge pull request #26 from sarnold/more-tftp. [Steve Arnold]

  Integrate new async daemon script


1.6.2 (2024-12-18)
------------------
- Merge pull request #25 from sarnold/tftpdaemon-srv-root. [Steve
  Arnold]

  tftpdaemon server root fixes


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

Other
~~~~~
- Merge pull request #24 from sarnold/server-root. [Steve Arnold]

  server root hot-fix
- Merge pull request #22 from sarnold/add-reuse. [Steve Arnold]

  Add reuse config and cleanup; includes bug fix for #23


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
- Merge pull request #21 from sarnold/dep-updates. [Steve Arnold]

  Dep updates and cleanup


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

Other
~~~~~
- Merge pull request #20 from sarnold/pkg-metadata. [Steve Arnold]

  update package metadata and dependencies


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

Other
~~~~~
- Merge pull request #19 from sarnold/tftpy-ref. [Steve Arnold]

  tftpy refactor


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
- Merge pull request #17 from sarnold/docstrings. [Steve Arnold]

  docstring and test fixes
- Merge pull request #16 from sarnold/lint-cleanup. [Steve Arnold]

  Lint cleanup
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
- Merge pull request #15 from sarnold/test-dirs. [Steve Arnold]

  handle nonexistent DOCROOT in serv_init, update readme
- Merge pull request #14 from sarnold/older-than-37. [Steve Arnold]

  Older than py37
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

Other
~~~~~
- Merge pull request #13 from sarnold/plat-fixes. [Steve Arnold]

  make install compatible with ubuntu LTS


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

Other
~~~~~
- Merge pull request #11 from sarnold/doc-cleanup. [Steve Arnold]

  apidoc cleanup


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
- Merge pull request #10 from sarnold/doc-updates. [Steve Arnold]

  doc updates plus cleanup
- Merge pull request #9 from sarnold/defs-refactor. [Steve Arnold]

  refactor with argparse instead of env vars
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

Other
~~~~~
- Merge pull request #7 from sarnold/tests-test. [Steve Arnold]

  Add tests
- Merge pull request #6 from sarnold/serv-refactor. [Steve Arnold]

  refactor server code, cleanup threaded shutdown and docs
- Merge pull request #5 from sarnold/daemonizer. [Steve Arnold]

  refactor for daemonizer


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

Other
~~~~~
- Merge pull request #4 from sarnold/pre-commit. [Steve Arnold]

  add pre-commit and pep8speaks
- Merge pull request #3 from sarnold/workflows. [Steve Arnold]

  Docs and workflows
- Merge pull request #2 from sarnold/simple-handler. [Steve Arnold]

  Simple request handler plus path rewrite


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

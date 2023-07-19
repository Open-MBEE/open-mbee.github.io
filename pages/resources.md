---
layout: default
title: Participate
permalink: participate.html
---

The Open MBEE Community utilizes a variety of resources available to open source projects. See how you can participate!

<div class="row link-grid">
  <div class="col-xl-2 col-lg-4 col-md-6">
    <a target="_blank" href="https://groups.google.com/forum/#!forum/openmbee">
      <img src="images/vendor-logos/google-groups.png">Google Group
    </a>
  </div>
  <div class="col-xl-2 col-lg-4 col-md-6">
    <a target="_blank" href="https://join.slack.com/t/openmbee/shared_invite/zt-ec86jsqc-3VJNYM4a5Drx0v1n70~C8A">
      <img src="images/vendor-logos/slack.png">Slack
    </a>
  </div>
</div>

<h2>OpenMBEE Resources</h2>
  <div class="row link-grid">
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://search.maven.org/search?q=OpenMBEE" target="_blank">
        <img src="images/vendor-logos/maven_central.png">Maven Central
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://github.com/Open-MBEE" target="_blank">
        <img src="images/vendor-logos/github.png">Github
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://hub.docker.com/u/openmbee" target="_blank">
        <img src="images/vendor-logos/docker.png">Docker Hub
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://github.com/Open-MBEE/open-mbee.github.io/wiki/OpenMBEE-public-server-information" target="_blank">
        <img src="images/vendor-logos/eng-hub.png">EngHub
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://drive.google.com/drive/folders/1-0gZYOUMf-ht56co9OumzvWxhS2C90rC" target="_blank">
        <img src="images/vendor-logos/drive.png">Google Drive
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="http://jira.openmbee.org" target="_blank">
        <img src="images/vendor-logos/jira.png">Issues
      </a>
    </div>
  </div>
  <div class="row link-grid mb-5">
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://github.com/Open-MBEE/open-mbee.github.io/wiki/OpenMBEE-documentation" target="_blank">
        <img src="images/vendor-logos/user-guide.png">User Guides
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://mms.openmbee.org" target="_blank">
        <img src="images/vendor-logos/ve.png">View Editor
      </a>
    </div>
    <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://www.youtube.com/channel/UCC4Ucy6P86ozz3pT01H7fmA" target="_blank">
        <img src="images/vendor-logos/youtube.png">YouTube
      </a>
  </div>
  <div class="col-xl-2 col-lg-4 col-md-6">
      <a href="https://openmbee.atlassian.net/wiki/spaces/OPENMBEE/overview" target="_blank">
        <img src="images/vendor-logos/user-guide.png">Confluence
      </a>
    </div>
</div>


<h2>OpenMBEE Pipeline</h2>

<img class="img-fluid" src="images/process-diagram.png" alt="diagram showing overall process (Change Package - Traceable, Auditable, Repeatable) using JIRA and circleci. The phases include design (using magicdraw, maplembse, cameo systems modeler, jupyter, and View Editor), development (using GitHub), testing (using Postman and JUnit), and operation (using jfrog bintray, python package index, jcenter, and anaconda cloud)">

## How to Contribute?

OpenMBEE is a community of engineers who believe in the power of open tools and standards for education, research, and modeling. We welcome contributions and contributors of all kinds - whether they come as contributions to code, participation in the community, opening issues and pointing out bugs, or simply sharing your work with your colleagues and friends.

## Contributing to OpenMBEE

Each project may have its own more detailed contributor guidelines, but the following general guidelines 
apply to all OpenMBEE projects.

### Reporting Bugs
To report any bugs found in a project, please create a new ticket in the appropriate repository.
The following information will be expected in all bug reports:

- A detailed description of the issue
- Project version and dependency versions

Any additional information which may be useful in reproducing the bug would be
greatly appreciated, such as details from the running configuration or the stack
trace of the error.

### Pull Requests
As open-sourced projects, we are open to contributions from community members
who wish to enhance or fix portions of the software. Below are some guidelines
to follow which will help your pull request be approved and ultimately keep the
code base clean, readable, and maintainable.

#### Branch and PR Naming
If a PR is to address a particular issue, please reference it. For 
new features, prefix the branch with `feature/` and for bugfixes `bugfix/`.

#### Code Formatting and Linting
Each project may have its own set of code formatting guidelines, for example, in 
the form of `.editorconfig` files, IntelliJ formatter, ESLint config, etc. depending on
the project's language. Please follow these guidelines to ensure the project codebase remain
readable and maintainable.

#### Tests
As with code formatting, please add appropriate tests when contributing code for a
project. Depending on the language/framework of the project, This can range from JUnit
tests for Java code, Postman collection tests for API testing, or Mocha/Chai for Javascript,
etc.

#### Commenting
Please add comments if code being contributed is not self evident in what it does or needs
other assumptions/context information. Add comments to functions that are to be used as API
so API docs can be generated by tools like JavaDoc or JSDoc.

[OpenMBEE's GitHub](https://github.com/Open-MBEE/){:target="_blank"}

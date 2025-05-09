<!-- ---
layout: default
title: Contribute
permalink: contribute.html
--- -->

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
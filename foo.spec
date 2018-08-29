%global package_name hello
%global spec_release 4
%global commit 581ad942510cde4f09734e3e22e74d0052666634

Name:     hello
Version:  2.10
Release:  1
Summary:  The "Hello World" program from GNU
License:  GPLv3+
URL:      https://www.gnu.org/software/hello/
Source0:  https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%changelog
* Tue Aug 28 2018 Johnny Dev <awesome_dev@example.com>
- We did things
- Some things were awesome
- Some we should have considered more

* Thu Jul 07 2018 The Coon of Ty <Ty@coon.org> - 2.10-1
- Initial version of the package

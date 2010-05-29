%define		plugin	git
%include	/usr/lib/rpm/macros.java
Summary:	JIRA git plugin
Name:		jira-plugin-%{plugin}
Version:	0.5.1
Release:	1
License:	BSD + EPL
Group:		Libraries/Java
Source0:	http://github.com/pawelz/jira4-git-plugin/tarball/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c5c6c67d75e809956f795be9d400eee1
URL:		http://github.com/pawelz/jira4-git-plugin
BuildRequires:	ant
BuildRequires:	java(servlet)
BuildRequires:	java-jgit
BuildRequires:	java-jsch
BuildRequires:	jira >= 4.0
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-jgit
Requires:	java-jsch
Requires:	jira >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pluginsdir	%{_datadir}/jira/plugins
%define		pluginsdeploydir	%{_datadir}/jira/WEB-INF/lib

%description
A plugin to integrate JIRA with Git. This plugin displays Git commit
info in a tab on the associated JIRA issue. To link a commit to a JIRA
issue, the commit's text must contain the issue key (eg. "This commit
fixes TST-123").

%prep
%setup -qc
mv pawelz-jira4-git-plugin-*/* .

%build
%ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{pluginsdeploydir},%{pluginsdir}}
cp jira-plugin-git-%{version}.jar $RPM_BUILD_ROOT%{pluginsdir}/plugin-%{plugin}-%{version}.jar
ln -s %{pluginsdir}/plugin-%{plugin}-%{version}.jar $RPM_BUILD_ROOT%{pluginsdeploydir}/plugin-%{plugin}-%{version}.jar

JGIT_JAR=$(find-jar jgit)
JSCH_JAR=$(find-jar jsch)

ln -s $JGIT_JAR $RPM_BUILD_ROOT%{pluginsdeploydir}/jgit.jar
ln -s $JSCH_JAR $RPM_BUILD_ROOT%{pluginsdeploydir}/jsch.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{pluginsdir}/plugin-%{plugin}-%{version}.jar
%{pluginsdeploydir}/plugin-%{plugin}-%{version}.jar
%{pluginsdeploydir}/jgit.jar
%{pluginsdeploydir}/jsch.jar

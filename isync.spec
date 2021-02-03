# NOTE
# - new name will be probably mbsync, but project name still stays isync
Summary:	Tool to synchronize IMAP4 and Maildir mailboxes
Name:		isync
Version:	1.3.4
Release:	1
License:	GPL v2+
Group:		Applications/Networking
URL:		http://isync.sourceforge.net/
Source0:	http://downloads.sourceforge.net/isync/%{name}-%{version}.tar.gz
# Source0-md5:	022e83a9d795a8f2b3e8561f5f4e13fe
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4.2
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
isync is a command line application which synchronizes mailboxes;
currently Maildir and IMAP4 mailboxes are supported. New messages,
message deletions and flag changes can be propagated both ways. isync
is suitable for use in IMAP-disconnected mode.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/doc/isync

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog src/mbsyncrc.sample src/compat/isyncrc.sample
%attr(755,root,root) %{_bindir}/isync
%attr(755,root,root) %{_bindir}/mbsync
%attr(755,root,root) %{_bindir}/mdconvert
%attr(755,root,root) %{_bindir}/mbsync-get-cert
%{_mandir}/man1/*

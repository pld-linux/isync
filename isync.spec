# NOTE
# - new name will be probably mbsync, but project name still stays isync
Summary:	Tool to synchronize IMAP4 and Maildir mailboxes
Name:		isync
Version:	1.4.1
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	https://downloads.sourceforge.net/isync/%{name}-%{version}.tar.gz
# Source0-md5:	c0c9899c2ff629e4e6de429c394b2613
URL:		https://isync.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel >= 4.2
BuildRequires:	openssl-devel
BuildRequires:	perl-base >= 1:5.14
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	zlib-devel
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

rm -r $RPM_BUILD_ROOT%{_docdir}/isync

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog src/mbsyncrc.sample
%attr(755,root,root) %{_bindir}/mbsync
%attr(755,root,root) %{_bindir}/mdconvert
%attr(755,root,root) %{_bindir}/mbsync-get-cert
%{_mandir}/man1/*

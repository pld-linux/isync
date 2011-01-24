# NOTE
# - new name will be probably mbsync, but project name still stays isync
Summary:	Tool to synchronize IMAP4 and Maildir mailboxes
Name:		isync
Version:	1.0.4
Release:	1
License:	GPL v2+
Group:		Applications/Networking
URL:		http://isync.sourceforge.net/
Source0:	http://downloads.sourceforge.net/isync/%{name}-%{version}.tar.gz
# Source0-md5:	8a836a6f4b43cd38a8b8153048417616
Patch0:		recursive_imap_ubuntu.patch
BuildRequires:	db-devel
BuildRequires:	iconv
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
%patch0 -p1

# Convert to utf-8
for file in ChangeLog; do
	mv $file timestamp
	iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
	touch -r timestamp $file
done

%build
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
%attr(755,root,root) %{_bindir}/get-cert
%{_mandir}/man1/*

Summary:	Set various flags to control the behaviour of CD-ROM device
Summary(pl):	Narz�dzie do kontroli zachowania nap�du CD-ROM
Name:		setcd
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/dists/potato/main/source/utils/%{name}_%{version}-1.tar.gz
# Source0-md5:	e7162b8db950eb04d418f4e1f226c081
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setcd is a program that allows you to control the behaviour of your
Linux cdrom device. There are a number of ways you can control the
behaviour of your cdrom drive: should it try to close the tray upon
mounting a cdrom when your happened to have left the tray open, or
should it eject the tray upon unmounting the cdrom? Should it lock the
door when some process uses the cdrom or not? Should the kernel try to
ensure that there actually is a CD in the drive, and that it is of the
right type (i.e., a data CD in case of a mount, or an audio CD in case
of a play operation)?

%description -l pl
setcd pozwala na kontrol� zachowania nap�du CD-ROM. Mo�e ustawia�, czy
szufladka powinna by� automatycznie zamykana przy montowaniu, czy
powinna by� automatycznie wysuwana po odmontowaniu, czy powinna by�
zablokowana podczas gdy p�yta jest podmontowana, czy j�dro ma pr�bowa�
upewni� si�, �e p�yta jest w nap�dzie oraz czy jest w�a�ciwego typu
(tzn. p�yta z danymi przy montowaniu lub p�yta audio przy
odtwarzaniu).

%prep
%setup -q

%build
%{__make} setcd \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install setcd $RPM_BUILD_ROOT%{_bindir}
install setcd.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

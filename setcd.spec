Summary:	Set various flags to control the behaviour of CD-ROM device
Summary(pl.UTF-8):	Narzędzie do kontroli zachowania napędu CD-ROM
Name:		setcd
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/s/setcd/%{name}_%{version}-2.tar.gz
# Source0-md5:	8041ed319600281de2bfce0c4a27f7a2
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

%description -l pl.UTF-8
setcd pozwala na kontrolę zachowania napędu CD-ROM. Może ustawiać, czy
szufladka powinna być automatycznie zamykana przy montowaniu, czy
powinna być automatycznie wysuwana po odmontowaniu, czy powinna być
zablokowana podczas gdy płyta jest podmontowana, czy jądro ma próbować
upewnić się, że płyta jest w napędzie oraz czy jest właściwego typu
(tzn. płyta z danymi przy montowaniu lub płyta audio przy
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

Name:           secure-delete
Version:        3.1
Release:        1%{?dist}
Summary:        Secure Delete
License:        GPL
URL:            https://www.thc.org/

Source0:        http://http.debian.net/debian/pool/main/s/secure-delete/secure-delete_%{version}.orig.tar.gz#/%{name}_%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/keachi/secure-delete-rpm/master/SOURCES/secure-delete_%{version}-1.diff

BuildRequires:  gcc

%description
This is the best secure data deletion toolkit! If you overwrite a file for 10+
times, it can still be recovered. Read why and use the programs included
(w/src!). These tools can wipe files, free disk space, swap and memory!
Changes: Linux LKM for secure file deletion included, small bufixes.

%prep
%setup -q -n %{name}-%{version}.orig
%patch -P 0 -p 1

%build
%make_build

%install
%make_install

%files
%{_bindir}/srm
%{_bindir}/sfill
%{_bindir}/sswap
%{_bindir}/smem
%{_mandir}/man1/srm.1.gz
%{_mandir}/man1/sfill.1.gz
%{_mandir}/man1/sswap.1.gz
%{_mandir}/man1/smem.1.gz
%{_datadir}/doc/%{name}/CHANGES
%{_datadir}/doc/%{name}/FILES
%{_datadir}/doc/%{name}/README
%{_datadir}/doc/%{name}/secure_delete.doc
%{_datadir}/doc/%{name}/usenix6-gutmann.doc

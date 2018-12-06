# http://github.com/prometheus/common

%global goipath         github.com/prometheus/common
%global commit          38c53a9f4bfcd932d1b00bfc65e256a7fba6b37a


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        Go libraries shared across Prometheus components and libraries
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock
Patch0:         change-import-path.patch
Patch1:         Fix-formatting-errors.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/sirupsen/logrus)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/julienschmidt/httprouter)
BuildRequires: golang(github.com/matttproud/golang_protobuf_extensions/pbutil)
# Cyclic dep on the client_golang
#BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/client_model/go)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(gopkg.in/alecthomas/kingpin.v2)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(bitbucket.org/ww/goautoneg)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch0 -p1
%patch1 -p1

%install
rm -rf promlog
%goinstall glide.lock glide.yaml
#rm -f log/eventlog_formatter.go

%check
%gochecks -d config  -d version

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc *.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git38c53a9
- Temporarily remove the promlog due to missing github.com/go-kit/kit dependency
  resolves: #1599386

* Wed Jun 27 2018 Paul Gier <pgier@redhat.com> - 0-0.14.git38c53a9
- Update to newer snapshot version
- Enable checks for config and log dirs

* Tue Jun 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git49fee29
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git49fee29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git49fee29
- add missing dependency
  related: #1315096

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git49fee29
- Bump to upstream 49fee292b27bfff7f354ee0f64e1bc4850462edf
  related: #1315096

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git195bde7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git195bde7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git195bde7
- Bump to upstream 195bde7883f7c39ea62b0d92ab7359b5327065cb
  related: #1315096

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git4fdc91a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git4fdc91a
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.4.git4fdc91a
- Bump to upstream 4fdc91a58c9d3696b982e8a680f4997403132d44
  resolves: #1315096

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitffe929a
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitffe929a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitffe929a
- First package for Fedora
  resolves: #1272465

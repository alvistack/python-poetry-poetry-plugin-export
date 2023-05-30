# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-poetry-plugin-export
Epoch: 100
Version: 1.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Poetry plugin to export the dependencies to various formats
License: MIT
URL: https://github.com/python-poetry/poetry-plugin-export/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package is a plugin that allows the export of locked packages to
various formats.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-poetry-plugin-export
Summary: Poetry plugin to export the dependencies to various formats
Requires: python3
Requires: python3-poetry >= 1.3.0
Requires: python3-poetry-core >= 1.3.0
Provides: python3-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-poetry-plugin-export
This package is a plugin that allows the export of locked packages to
various formats.

%files -n python%{python3_version_nodots}-poetry-plugin-export
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-poetry-plugin-export
Summary: Poetry plugin to export the dependencies to various formats
Requires: python3
Requires: python3-poetry >= 1.3.0
Requires: python3-poetry-core >= 1.3.0
Provides: python3-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}

%description -n python3-poetry-plugin-export
This package is a plugin that allows the export of locked packages to
various formats.

%files -n python3-poetry-plugin-export
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-poetry-plugin-export
Summary: Poetry plugin to export the dependencies to various formats
Requires: python3
Requires: python3-poetry >= 1.3.0
Requires: python3-poetry-core >= 1.3.0
Provides: python3-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry-plugin-export = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry-plugin-export) = %{epoch}:%{version}-%{release}

%description -n python3-poetry-plugin-export
This package is a plugin that allows the export of locked packages to
various formats.

%files -n python3-poetry-plugin-export
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog

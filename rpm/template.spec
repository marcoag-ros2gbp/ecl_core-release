Name:           ros-indigo-ecl-threads
Version:        0.61.3
Release:        0%{?dist}
Summary:        ROS ecl_threads package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_threads
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-build
Requires:       ros-indigo-ecl-concepts
Requires:       ros-indigo-ecl-config
Requires:       ros-indigo-ecl-errors
Requires:       ros-indigo-ecl-exceptions
Requires:       ros-indigo-ecl-license
Requires:       ros-indigo-ecl-time
Requires:       ros-indigo-ecl-utilities
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-build
BuildRequires:  ros-indigo-ecl-concepts
BuildRequires:  ros-indigo-ecl-config
BuildRequires:  ros-indigo-ecl-errors
BuildRequires:  ros-indigo-ecl-exceptions
BuildRequires:  ros-indigo-ecl-license
BuildRequires:  ros-indigo-ecl-time
BuildRequires:  ros-indigo-ecl-utilities

%description
This package provides the c++ extensions for a variety of threaded programming
tools. These are usually different on different platforms, so the architecture
for a cross-platform framework is also implemented.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Sep 05 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.3-0
- Autogenerated by Bloom

* Wed Aug 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.2-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

* Fri Sep 12 2014 Daniel Stonier <d.stonier@gmail.com> - 0.61.0-0
- Autogenerated by Bloom


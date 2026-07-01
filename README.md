# jadens-printer-driver
[![Copr build status](https://copr.fedorainfracloud.org/coprs/srp/jadens-printer-driver/package/jadens-printer-driver/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/srp/jadens-printer-driver/package/jadens-printer-driver/)

A rebuild of JADENS' Debian package to properly work on other distros.

This repo also modifies the behavior that would come with the original Debian package to avoid redundant files, since the original package would otherwise install a filter binary for every architecture it's been built for regardless of the system's architecture.

Source extraction and re-organization is done via GitHub Actions, builds are done with the respective distro's build methods.

JADENS provides their Debian package through a non-static link, meaning updates to the ensemble have to be done manually.

## Installation

### Fedora

```sh
sudo dnf copr enable srp/jadens-printer-driver
sudo dnf install jadens-printer-driver
```

### Arch
<small>will have on AUR as soon as registrations are available</small>

```sh
git clone https://github.com/RdrSeraphim/jadens-printer-driver
cd jadens-printer-driver
makepkg -si
```

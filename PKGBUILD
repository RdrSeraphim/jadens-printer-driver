# Maintainer: RdrSeraphim <me@srp.life>
pkgname=jadens-printer-driver
pkgver=3.3.5.497
pkgrel=1
pkgdesc='CUPS support for JADENS thermal printing devices'
arch=('x86_64' 'aarch64')
url='https://github.com/RdrSeraphim/jadens-printer-driver-rpm'
license=('LicenseRef-Proprietary')
depends=('cups')
source=("${pkgname}-${pkgver}-x86_64.tar.gz::https://raw.githubusercontent.com/RdrSeraphim/jadens-printer-driver-rpm/sources/${pkgname}-${pkgver}-x86_64.tar.gz"
        "${pkgname}-${pkgver}-aarch64.tar.gz::https://raw.githubusercontent.com/RdrSeraphim/jadens-printer-driver-rpm/sources/${pkgname}-${pkgver}-aarch64.tar.gz")
sha512sums=('SKIP'
            'SKIP')
noextract=("${pkgname}-${pkgver}-x86_64.tar.gz"
           "${pkgname}-${pkgver}-aarch64.tar.gz")

prepare() {
  cd "${srcdir}"

  if [[ "${CARCH}" == "x86_64" ]]; then
    tar xzf "${pkgname}-${pkgver}-x86_64.tar.gz"
  elif [[ "${CARCH}" == "aarch64" ]]; then
    tar xzf "${pkgname}-${pkgver}-aarch64.tar.gz"
  fi
}

package() {
  install -Dm755 "${srcdir}/usr/lib/cups/filter/jadens_printer_filter" \
    "${pkgdir}/usr/lib/cups/filter/jadens_printer_filter"

  install -dm755 "${pkgdir}/usr/share/cups/model/Jadens"
  install -Dm644 "${srcdir}"/usr/share/cups/model/Jadens/*.ppd \
    -t "${pkgdir}/usr/share/cups/model/Jadens/"
}

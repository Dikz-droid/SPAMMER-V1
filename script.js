// Proteksi akses
if (sessionStorage.getItem('isLoggedIn') !== 'true') {
  alert("Akses ditolak! Silakan login dulu.");
  window.location.href = "index.html";
}

// Telegram bot config (ganti sesuai milikmu)
const BOT_TOKEN = '7356107042:AAE_RPBh9t06sOqc6tJg5yVML2-6XbgEmR4';
const ADMIN_ID = '6759909494';

// Toggle form report
function toggleReport() {
  const form = document.getElementById('reportForm');
  form.style.display = (form.style.display === 'none' || form.style.display === '') ? 'block' : 'none';
}

// Kirim report ke Telegram
function sendReport() {
  const text = document.getElementById('reportText').value.trim();
  const status = document.getElementById('reportStatus');

  if (text === '') {
    status.style.color = "var(--danger-color)";
    status.textContent = "Pesan tidak boleh kosong!";
    return;
  }

  const message = encodeURIComponent("Laporan dari user:\n\n" + text);
  const url = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage?chat_id=${ADMIN_ID}&text=${message}`;

  fetch(url)
    .then(res => {
      if (res.ok) {
        status.style.color = "var(--accent-color)";
        status.textContent = "Laporan berhasil dikirim!";
        document.getElementById('reportText').value = '';
      } else {
        throw new Error();
      }
    })
    .catch(() => {
      status.style.color = "var(--danger-color)";
      status.textContent = "Gagal mengirim laporan.";
    });
}

from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    model = BukuModel()
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)
    assert hasil is True
    mock_cursor.execute.assert_called_once()
    model.conn.commit.assert_called_once()

def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Mocking koneksi dan kursor database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menyiapkan dummy data hasil fetchall
    mock_cursor.fetchall.return_value = [
        (1, "Buku A", "Penulis A", 2023),
        (2, "Buku B", "Penulis B", 2024)
    ]

    # Eksekusi fungsi
    hasil = model.get_all_buku()

    # Verifikasi hasil dan pemanggilan kursor
    assert len(hasil) == 2
    mock_cursor.execute.assert_called_once()
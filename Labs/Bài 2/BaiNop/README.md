# Bài nộp Lab 2

Mua Mí Sính — DTC235180159 — KTPM K22C.

Đọc `BaoCao_Lab2.md` để xem lời giải Automation, Lean, sơ đồ công cụ và tự đánh giá CALMS.

Mở PowerShell trong thư mục này và chạy:

```powershell
./devops-check.ps1
./setup-dev-env.ps1
docker build -t devops-lab2-app .
docker run -d -p 3000:3000 --name lab2-app devops-lab2-app
curl.exe http://localhost:3000
```

Nếu tên `lab2-app` đã tồn tại, kiểm tra bằng `docker ps -a` trước. Nếu đó là container của bài này thì dùng `docker start lab2-app` để chạy lại.

`dev-env/` là kết quả chạy automation. `logs/` lưu bằng chứng thực thi. `screenshots/` chứa các ảnh dựng từ log thật, sơ đồ và bảng đánh giá; không phải ảnh chụp màn hình. Chạy `python TaoMinhChung.py` để tạo lại ảnh (cần Pillow).

Sau khi chấm, dừng và xóa container của bài bằng `docker stop lab2-app` rồi `docker rm lab2-app`.
